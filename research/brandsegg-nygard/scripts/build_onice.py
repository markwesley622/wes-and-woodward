"""On-ice reconstruction for Brandsegg-Nygård's first 10 games of 2025-26 and 2026-27.
usage: python3 -I build_onice.py RAW_DIR OUT_DIR
Shift boundary rule (soderblom lesson): TOI/faceoffs start-inclusive/end-exclusive [s,e);
events (shots, goals, hits) start-exclusive/end-inclusive (s,e]."""
import json, csv, sys, re, html, collections, os
RAW, OUT = sys.argv[1], sys.argv[2]
MBN = 8484794; DET = 17
def mmss(t):
    m, s = t.split(":"); return int(m)*60+int(s)
def abs_sec(period, t):  # t seconds into period
    return (period-1)*1200 + t if period <= 3 else 3600 + (period-4)*300 + t  # reg-season OT = 5 min

def load_shifts_api(gid):
    d = json.load(open(f"{RAW}/shifts/{gid}.json"))["data"]
    out = []
    for s in d:
        if s.get("typeCode") != 517 or s.get("duration") is None: continue
        out.append((s["playerId"], s["teamId"], s["period"], mmss(s["startTime"]), mmss(s["endTime"])))
    return out

def load_shifts_html(gid, roster, home_id, away_id):
    """Parse TH/TV HTML shift reports; map (team, sweater) -> playerId via roster."""
    out = []
    num = str(gid)[4:]
    for side, tid in (("TH", home_id), ("TV", away_id)):
        t = open(f"{RAW}/htmlshift/{side}{num}.HTM", encoding="utf-8", errors="replace").read()
        bysw = {r["sweaterNumber"]: pid for pid, r in roster.items() if r["teamId"] == tid}
        # split by player headings
        parts = re.split(r'<td[^>]*class="playerHeading[^"]*"[^>]*>', t)
        for part in parts[1:]:
            head = re.sub(r"<[^>]+>", " ", part[:200]); head = html.unescape(head).strip()
            m = re.match(r"(\d+)\s", head)
            if not m: continue
            sw = int(m.group(1)); pid = bysw.get(sw)
            if pid is None: print("WARN no roster match", side, head[:40]); continue
            for row in re.finditer(r'<tr[^>]*class="\s*(?:oddColor|evenColor)"[^>]*>(.*?)</tr>', part, flags=re.S):
                cells = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", row.group(1), flags=re.S)]
                if len(cells) < 5 or not cells[0].isdigit(): continue
                per = cells[1]; per = 4 if per == "OT" else int(per)
                st = mmss(cells[2].split("/")[0].strip()); en = mmss(cells[3].split("/")[0].strip())
                out.append((pid, tid, per, st, en))
    return out

def mp_shots(season_file, gid):
    short = str(gid)[4:].lstrip("0"); short = str(int(str(gid)[4:]))
    rows = []
    with open(season_file) as f:
        for r in csv.DictReader(f):
            if r["game_id"] == short: rows.append(r)
    return rows

def analyze(gid, mp_file):
    p = json.load(open(f"{RAW}/pbp/{gid}.json"))
    home_id, away_id = p["homeTeam"]["id"], p["awayTeam"]["id"]
    home_ab, away_ab = p["homeTeam"]["abbrev"], p["awayTeam"]["abbrev"]
    opp_id = away_id if home_id == DET else home_id
    roster = {r["playerId"]: r for r in p["rosterSpots"]}
    shifts = load_shifts_api(gid)
    src = "api"
    if len(shifts) < 100:
        shifts = load_shifts_html(gid, roster, home_id, away_id); src = "html"
    # drop goalies from skater counts
    maxsec = 3600 + (300 if p["periodDescriptor"]["number"] >= 4 else 0)
    on_toi = collections.defaultdict(set)   # sec -> set(pid) [s,e)
    on_evt = collections.defaultdict(set)   # sec -> set(pid) (s,e]
    toi = collections.Counter()
    for pid, tid, per, st, en in shifts:
        a, b = abs_sec(per, st), abs_sec(per, en)
        if b <= a: continue
        toi[pid] += b - a
        for s in range(a, b): on_toi[s].add(pid)
        for s in range(a+1, b+1): on_evt[s].add(pid)
    def skaters(S, tid): return [x for x in S if roster.get(x, {}).get("teamId") == tid and roster[x]["positionCode"] != "G"]
    def strength(S):
        d = len(skaters(S, DET)); o = len(skaters(S, opp_id))
        return d, o
    # score state per second
    goals = []
    for e in p["plays"]:
        if e["typeDescKey"] == "goal":
            per = e["periodDescriptor"]["number"]; t = abs_sec(per, mmss(e["timeInPeriod"]))
            goals.append((t, e["details"]["eventOwnerTeamId"]))
    def score_diff(sec):  # DET minus opp, goals strictly before sec
        d = 0
        for t, tid in goals:
            if t < sec: d += 1 if tid == DET else -1
        return d
    g = dict(gid=gid, date=p["gameDate"], home=home_ab, away=away_ab, opp=(away_ab if home_id == DET else home_ab), shift_src=src)
    # --- TOI by strength (TOI version)
    st_toi = collections.Counter(); mates = collections.Counter(); opps = collections.Counter(); per_toi = collections.Counter(); score_toi = collections.Counter()
    team_5v5 = 0; team_pp = 0; team_pk = 0; mbn_shifts = 0
    close_late = 0
    for sec in range(0, maxsec):
        S = on_toi.get(sec, set())
        d, o = strength(S)
        if d == 0 and o == 0: continue
        state = "5v5" if (d == 5 and o == 5) else ("PP" if d > o else ("PK" if d < o else f"{d}v{o}"))
        if state == "5v5": team_5v5 += 1
        if state == "PP": team_pp += 1
        if state == "PK": team_pk += 1
        if MBN in S:
            st_toi[state] += 1
            per = 1 + sec//1200 if sec < 3600 else 4
            per_toi[per] += 1
            if state == "5v5":
                for x in skaters(S, DET):
                    if x != MBN: mates[x] += 1
                for x in skaters(S, opp_id): opps[x] += 1
                sd = score_diff(sec); score_toi["lead" if sd > 0 else ("tied" if sd == 0 else "trail")] += 1
            if 3300 <= sec < 3600 and abs(score_diff(sec)) <= 1: close_late += 1
    mbn_shifts = sum(1 for s in shifts if s[0] == MBN)
    g.update(toi_all=sum(st_toi.values()), toi_by_state=dict(st_toi), team_5v5=team_5v5, team_pp=team_pp, team_pk=team_pk, shifts=mbn_shifts, per_toi=dict(per_toi), score_toi=dict(score_toi), close_late_toi=close_late)
    # QoC / QoT: rank opp forwards & D by game TOI
    oppF = sorted([x for x in roster if roster[x]["teamId"] == opp_id and roster[x]["positionCode"] in ("C","L","R")], key=lambda x: -toi[x])
    oppD = sorted([x for x in roster if roster[x]["teamId"] == opp_id and roster[x]["positionCode"] == "D"], key=lambda x: -toi[x])
    detF = sorted([x for x in roster if roster[x]["teamId"] == DET and roster[x]["positionCode"] in ("C","L","R") and x != MBN], key=lambda x: -toi[x])
    t5 = st_toi["5v5"] or 1
    g["qoc_top3F_share"] = sum(opps[x] for x in oppF[:3]) / (3*t5)
    g["qoc_top2D_share"] = sum(opps[x] for x in oppD[:2]) / (2*t5)
    g["qoc_bottom3F_share"] = sum(opps[x] for x in oppF[-3:]) / (3*t5)
    g["qot_top3F_share"] = sum(mates[x] for x in detF[:3]) / (2*t5)  # he fills one of 3 F slots; 2 teammate F slots
    g["mates"] = {f'{roster[x]["firstName"]["default"]} {roster[x]["lastName"]["default"]}|{roster[x]["positionCode"]}': v for x, v in mates.most_common(8)}
    g["opps"] = {f'{roster[x]["firstName"]["default"]} {roster[x]["lastName"]["default"]}|{roster[x]["positionCode"]}|rankTOI{(oppF+oppD).index(x) if x in oppF else oppD.index(x)}': v for x, v in opps.most_common(6)}
    # --- events
    ev = collections.Counter(); ind = collections.Counter(); zs = collections.Counter()
    for e in p["plays"]:
        tk = e["typeDescKey"]; det = e.get("details", {})
        per = e["periodDescriptor"]["number"]; sec = abs_sec(per, mmss(e["timeInPeriod"]))
        S = on_evt.get(sec, set()); d, o = strength(S); is55 = (d == 5 and o == 5)
        on = MBN in S
        if tk == "faceoff":
            S2 = on_toi.get(sec, set()); d2, o2 = strength(S2)
            if MBN in S2 and d2 == 5 and o2 == 5:
                x = det["xCoord"]; side = e.get("homeTeamDefendingSide")
                # home defends 'left' => negative x is home's D zone
                home_dz_neg = (side == "left")
                if abs(x) < 25: z = "N"
                else:
                    home_zone = "D" if ((x < 0) == home_dz_neg) else "O"
                    z = home_zone if home_id == DET else ("O" if home_zone == "D" else "D")
                zs[z] += 1
        if tk in ("shot-on-goal", "missed-shot", "blocked-shot", "goal"):
            shooter = det.get("shootingPlayerId") or det.get("scoringPlayerId")
            steam = roster.get(shooter, {}).get("teamId", det.get("eventOwnerTeamId"))
            forus = steam == DET
            if shooter == MBN:
                ind["iCF"] += 1
                if tk != "blocked-shot": ind["iFF"] += 1
                if tk in ("shot-on-goal", "goal"): ind["iSOG"] += 1
                if tk == "goal": ind["iG"] += 1
                if is55: ind["iCF_5v5"] += 1
            if is55:
                key = "F" if forus else "A"
                sdiff = score_diff(sec); sstate = "lead" if sdiff > 0 else ("tied" if sdiff == 0 else "trail")
                if on:
                    ev[sstate+"_C"+key] += 1
                    ev["C"+key] += 1
                    if tk != "blocked-shot": ev["F"+key] += 1
                    if tk in ("shot-on-goal", "goal"): ev["S"+key] += 1
                    if tk == "goal": ev["G"+key] += 1
                else:
                    ev["off_C"+key] += 1
                    if tk != "blocked-shot": ev["off_F"+key] += 1
                    if tk == "goal": ev["off_G"+key] += 1
        if tk == "goal" and MBN in (det.get("assist1PlayerId"), det.get("assist2PlayerId"), det.get("scoringPlayerId")):
            ind["pts"] += 1
            if det.get("assist1PlayerId") == MBN: ind["A1"] += 1
            if det.get("assist2PlayerId") == MBN: ind["A2"] += 1
            ind["pts_5v5" if is55 else "pts_other"] += 1
        if tk == "hit":
            if det.get("hittingPlayerId") == MBN: ind["hits"] += 1
            if det.get("hitteePlayerId") == MBN: ind["hits_taken"] += 1
        if tk == "giveaway" and det.get("playerId") == MBN: ind["giveaways"] += 1; ind["gv_"+det.get("zoneCode","?")] += 1
        if tk == "takeaway" and det.get("playerId") == MBN: ind["takeaways"] += 1
        if tk == "blocked-shot" and det.get("blockingPlayerId") == MBN: ind["blocks"] += 1
        if tk == "penalty":
            if det.get("committedByPlayerId") == MBN: ind["pen_taken"] += 1
            if det.get("drawnByPlayerId") == MBN: ind["pen_drawn"] += 1
    g["ev5v5"] = dict(ev); g["ind"] = dict(ind); g["zs"] = dict(zs)
    # --- MoneyPuck xG join
    xg = collections.Counter(); ishots = []
    for r in mp_shots(mp_file, gid):
        sec = int(r["time"]); tcode = r["teamCode"]; forus = (tcode == "DET")
        S = on_evt.get(sec, set()); d, o = strength(S); is55 = (d == 5 and o == 5)
        mp55 = r["homeSkatersOnIce"] == "5" and r["awaySkatersOnIce"] == "5"
        x = float(r["xGoal"])
        if r["shooterPlayerId"] == str(MBN):
            ishots.append(dict(sec=sec, xg=x, x=float(r["xCordAdjusted"]), y=float(r["yCordAdjusted"]), gid=gid, type=r["shotType"], dist=float(r["shotDistance"]), angle=float(r["shotAngleAdjusted"]), rebound=r["shotRebound"], rush=r["shotRush"], onGoal=r["shotWasOnGoal"], goal=r["goal"], is55=is55, event=r["event"]))
            xg["ixg_all"] += x
            if is55: xg["ixg_5v5"] += x
        if is55 or mp55:
            pass
        if is55:
            sdiff = score_diff(sec); sstate = "lead" if sdiff > 0 else ("tied" if sdiff == 0 else "trail")
            if MBN in S: xg["xGF" if forus else "xGA"] += x; xg[sstate+"_xGF" if forus else sstate+"_xGA"] += x
            else: xg["off_xGF" if forus else "off_xGA"] += x
        if MBN in S and not is55 and forus and d > o: xg["pp_xGF_on"] += x
    g["xg"] = {k: round(v, 3) for k, v in xg.items()}; g["ishots"] = ishots
    return g

games = json.load(open(f"{RAW}/games.json"))
res = {"20252026": [], "20262027": []}
for s, gid, dt, opp in games:
    mp_file = f"{RAW}/mp/shots_{'2025' if s=='20252026' else '2026'}.csv"
    g = analyze(gid, mp_file); res[s].append(g)
    print(s, dt, opp, g["shift_src"], "TOI", round(g["toi_all"]/60,2), g["toi_by_state"], "zs", g["zs"], "ev", g["ev5v5"].get("CF",0), g["ev5v5"].get("CA",0), "xG", g["xg"].get("xGF",0), g["xg"].get("xGA",0), "qoc", round(g["qoc_top3F_share"],2))
json.dump(res, open(f"{OUT}/onice_games.json", "w"), indent=1)
