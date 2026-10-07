#!/usr/bin/env python3
"""Master team-season table: MoneyPuck 5v5 + EH forward-group profile + points + playoff rounds + star flags."""
import csv, json, pathlib
HERE = pathlib.Path(__file__).parent
FIX = {"L.A": "LAK", "N.J": "NJD", "S.J": "SJS", "T.B": "TBL", "PHX": "ARI"}
tri = {t["id"]: FIX.get(t["triCode"], t["triCode"]) for t in json.load(open(HERE / "nhl/teams.json"))["data"]}
pts = {}
for r in json.load(open(HERE / "nhl/team_summary_all.json"))["data"]:
    pts[(int(str(r["seasonId"])[:4]), tri[r["teamId"]])] = r
rounds = {}
for y in range(2008, 2026):
    for s in json.load(open(HERE / f"nhl/bracket_{y+1}.json"))["series"]:
        if s["playoffRound"] < 1 or not s.get("winningTeamId"): continue
        for side in ("topSeedTeam", "bottomSeedTeam"):
            a = FIX.get(s[side]["abbrev"], s[side]["abbrev"])
            rounds.setdefault((y, a), 0)
        w = tri[s["winningTeamId"]]
        rounds[(y, w)] = rounds.get((y, w), 0) + 1
# forward scoring ranks (all situations) from MoneyPuck skaters
star = {}
for y in range(2008, 2026):
    R = [r for r in csv.DictReader(open(HERE / f"mp/skaters_{y}.csv")) if r["situation"] == "all" and r["position"] != "D"]
    R.sort(key=lambda r: -float(r["I_F_points"]))
    for i, r in enumerate(R):
        t = FIX.get(r["team"], r["team"])
        cur = star.get((y, t))
        if cur is None: star[(y, t)] = dict(top_pts_f=r["name"], top_pts=int(float(r["I_F_points"])), top_pts_rank=i + 1, n_top20=0, n_top30=0)
        if i < 20: star[(y, t)]["n_top20"] += 1
        if i < 30: star[(y, t)]["n_top30"] += 1
out = []
for d in json.load(open(HERE / "fgroup.json")):
    k = (d["season"], d["team"])
    p = pts[k]
    d["points"] = p["points"]; d["pt_pct"] = p["pointPct"]; d["pts82"] = p["pointPct"] * 164
    d["playoffs"] = k in rounds; d["rounds"] = rounds.get(k, 0)
    d.update(star[k])
    d["star"] = d["top_pts_rank"] <= 10 or d["top_f_rank"] <= 10   # top-10 forward by points or by EH GAR
    out.append(d)
for y in sorted({d["season"] for d in out}):
    S = [d for d in out if d["season"] == y]
    for i, d in enumerate(sorted(S, key=lambda d: -d["pt_pct"])): d["r_pts"] = i + 1
json.dump(out, open(HERE / "master.json", "w"), indent=0)
print(len(out), "team-seasons", sum(d["playoffs"] for d in out), "playoff teams")
for d in out:
    if d["team"] == "DET" and d["season"] >= 2023: print(d["season"], d["points"], d["r_pts"], d["playoffs"], d["top_pts_f"], d["top_pts"], d["top_pts_rank"], d["star"], d["n_top30"])
for d in out:
    if d["season"]==2019 and d["rounds"]>=2: print(d["team"],d["rounds"])
