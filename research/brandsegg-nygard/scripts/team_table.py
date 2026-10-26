"""Per-DET-skater 5v5 on-ice table over each 10-game sample (for ranking MBN among teammates). usage: team_table.py RAW OUT"""
import json, csv, sys, re, html, collections
RAW, OUT = sys.argv[1], sys.argv[2]
DET = 17
sys.argv = [sys.argv[0], RAW, OUT]
import os
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_onice.py")).read().split("games = json.load")[0]
exec(src)  # reuse loaders: mmss, abs_sec, load_shifts_api, load_shifts_html, mp_shots
games = json.load(open(f"{RAW}/games.json"))
tables = {}
for s, gid, dt, opp in games:
    mp_file = f"{RAW}/mp/shots_{'2025' if s=='20252026' else '2026'}.csv"
    p = json.load(open(f"{RAW}/pbp/{gid}.json")); home_id, away_id = p["homeTeam"]["id"], p["awayTeam"]["id"]; opp_id = away_id if home_id == DET else home_id
    roster = {r["playerId"]: r for r in p["rosterSpots"]}
    shifts = load_shifts_api(gid)
    if len(shifts) < 100: shifts = load_shifts_html(gid, roster, home_id, away_id)
    on_toi = collections.defaultdict(set); on_evt = collections.defaultdict(set)
    for pid, tid, per, st, en in shifts:
        a, b = abs_sec(per, st), abs_sec(per, en)
        for x in range(a, b): on_toi[x].add(pid)
        for x in range(a+1, b+1): on_evt[x].add(pid)
    def sk(S, tid): return [x for x in S if roster.get(x, {}).get("teamId") == tid and roster[x]["positionCode"] != "G"]
    def is55(S): return len(sk(S, DET)) == 5 and len(sk(S, opp_id)) == 5
    T = tables.setdefault(s, collections.defaultdict(collections.Counter))
    maxsec = 3600 + (300 if p["periodDescriptor"]["number"] >= 4 else 0)
    for sec in range(maxsec):
        S = on_toi.get(sec, set())
        if is55(S):
            for x in sk(S, DET): T[x]["toi"] += 1
        # all-situation TOI
        for x in sk(S, DET): T[x]["toi_all"] += 1
    for e in p["plays"]:
        tk = e["typeDescKey"]; det = e.get("details", {})
        if tk not in ("shot-on-goal", "missed-shot", "blocked-shot", "goal"): continue
        sec = abs_sec(e["periodDescriptor"]["number"], mmss(e["timeInPeriod"])); S = on_evt.get(sec, set())
        if not is55(S): continue
        shooter = det.get("shootingPlayerId") or det.get("scoringPlayerId"); forus = roster.get(shooter, {}).get("teamId") == DET
        for x in sk(S, DET):
            T[x]["CF" if forus else "CA"] += 1
            if tk == "goal": T[x]["GF" if forus else "GA"] += 1
        if shooter in roster and roster[shooter]["teamId"] == DET: T[shooter]["iCF"] += 1
    for r in mp_shots(mp_file, gid):
        sec = int(r["time"]); S = on_evt.get(sec, set())
        if not is55(S): continue
        forus = r["teamCode"] == "DET"; x = float(r["xGoal"])
        for pid in sk(S, DET): T[pid]["xGF" if forus else "xGA"] += x
        sh = int(r["shooterPlayerId"]) if r["shooterPlayerId"] else None
        if sh in T: T[sh]["ixg"] += x
    for pid in sk(set(roster), DET): T[pid]["gp"] += 1
    for pid in roster:
        if roster[pid]["teamId"] == DET: T[pid]["name"] = f'{roster[pid]["firstName"]["default"]} {roster[pid]["lastName"]["default"]}'; T[pid]["pos"] = roster[pid]["positionCode"]
out = {}
for s, T in tables.items():
    rows = []
    for pid, c in T.items():
        if c["pos"] in ("G",) or c["toi"] < 60*60: continue  # >=60 min 5v5
        rows.append(dict(pid=pid, name=c["name"], pos=c["pos"], gp=c["gp"], toi5=round(c["toi"]/60, 1), toi_all_gp=round(c["toi_all"]/60/c["gp"], 2), cf=c["CF"], ca=c["CA"], cf_pct=round(100*c["CF"]/(c["CF"]+c["CA"]), 1), xgf=round(c["xGF"], 2), xga=round(c["xGA"], 2), xgf_pct=round(100*c["xGF"]/(c["xGF"]+c["xGA"]), 1), xgf60=round(60*c["xGF"]/(c["toi"]/60), 2), xga60=round(60*c["xGA"]/(c["toi"]/60), 2), gf=c["GF"], ga=c["GA"], icf60=round(60*c["iCF"]/(c["toi"]/60), 2), ixg60=round(60*c["ixg"]/(c["toi"]/60), 2)))
    rows.sort(key=lambda r: -r["xgf_pct"]); out[s] = rows
    print("==", s, "DET skaters, 5v5, >=60 min, first 10 games")
    for r in rows: print(f'  {r["name"]:26s}{r["pos"]} GP{r["gp"]:2d} 5v5 {r["toi5"]:6.1f} CF% {r["cf_pct"]:5.1f} xGF% {r["xgf_pct"]:5.1f} xGF60 {r["xgf60"]:4.2f} xGA60 {r["xga60"]:4.2f} GF-GA {r["gf"]}-{r["ga"]} iCF60 {r["icf60"]:5.2f} ixG60 {r["ixg60"]:4.2f}')
json.dump(out, open(f"{OUT}/team_table.json", "w"), indent=1)
