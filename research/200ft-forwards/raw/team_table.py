#!/usr/bin/env python3
"""Team-season table 2008-2025 from MoneyPuck: 5v5 offense, finishing, defense, goaltending, with league ranks."""
import csv, json, pathlib
HERE = pathlib.Path(__file__).parent
rows = []
for y in range(2008, 2026):
    R = list(csv.DictReader(open(HERE / "mp" / f"teams_{y}.csv")))
    by = {}
    for r in R:
        r["team"] = {"L.A": "LAK", "N.J": "NJD", "S.J": "SJS", "T.B": "TBL"}.get(r["team"], r["team"])
        by.setdefault(r["team"], {})[r["situation"]] = r
    season = []
    for t, s in by.items():
        f, a = s["5on5"], s["all"]
        m = float(f["iceTime"]) / 60
        d = dict(season=y, team=t, gp=int(a["games_played"]),
                 gf5=float(f["goalsFor"]), xgf5=float(f["xGoalsFor"]), ga5=float(f["goalsAgainst"]), xga5=float(f["xGoalsAgainst"]),
                 gf60=float(f["goalsFor"]) / m * 60, xgf60=float(f["xGoalsFor"]) / m * 60,
                 ga60=float(f["goalsAgainst"]) / m * 60, xga60=float(f["xGoalsAgainst"]) / m * 60,
                 sh5=float(f["goalsFor"]) / float(f["shotsOnGoalFor"]) * 100,
                 sv5=100 - float(f["goalsAgainst"]) / float(f["shotsOnGoalAgainst"]) * 100,
                 xgpct=float(f["xGoalsPercentage"]) * 100,
                 gf_all=float(a["goalsFor"]), ga_all=float(a["goalsAgainst"]), xga_all=float(a["xGoalsAgainst"]), xgf_all=float(a["xGoalsFor"]))
        d["fin5"] = d["gf5"] - d["xgf5"]              # goals above expected, 5v5
        d["fin5_pct"] = d["gf5"] / d["xgf5"] * 100
        d["gsax5"] = d["xga5"] - d["ga5"]             # goals saved above expected, 5v5
        d["gsax_all"] = d["xga_all"] - d["ga_all"]
        d["fin5_82"] = d["fin5"] / d["gp"] * 82; d["gsax5_82"] = d["gsax5"] / d["gp"] * 82
        d["gf5_82"] = d["gf5"] / d["gp"] * 82
        season.append(d)
    n = len(season)
    for key, hi in [("gf60", 1), ("xgf60", 1), ("fin5", 1), ("fin5_pct", 1), ("sh5", 1), ("xga60", 0), ("ga60", 0), ("gsax5", 1), ("gsax_all", 1), ("sv5", 1), ("xgpct", 1), ("gf5", 1)]:
        srt = sorted(season, key=lambda d: -d[key] if hi else d[key])
        for i, d in enumerate(srt): d["r_" + key] = i + 1
    for d in season: d["n"] = n
    rows += season
json.dump(rows, open(HERE / "team_seasons.json", "w"), indent=0)
if __name__ == "__main__":
    for d in rows:
        if d["team"] == "DET" and d["season"] >= 2019:
            print(d["season"], f"GF5 {d['gf5']:.0f} (r{d['r_gf5']}) gf60 {d['gf60']:.2f} r{d['r_gf60']} | xgf60 {d['xgf60']:.2f} r{d['r_xgf60']} | fin {d['fin5']:+.1f} r{d['r_fin5']} sh% {d['sh5']:.2f} r{d['r_sh5']} | xga60 {d['xga60']:.2f} r{d['r_xga60']} | gsax5 {d['gsax5']:+.1f} r{d['r_gsax5']} all {d['gsax_all']:+.1f} r{d['r_gsax_all']} sv5 {d['sv5']:.2f} r{d['r_sv5']} | xg% {d['xgpct']:.1f} r{d['r_xgpct']}")
