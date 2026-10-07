#!/usr/bin/env python3
"""2023-24 as the outlier: each Detroit forward's EH even-strength defense percentile vs 5v5 finishing."""
import json, csv, pathlib, unicodedata
HERE = pathlib.Path(__file__).parent
PL = json.load(open(HERE / "eh_players.json"))
def norm(s): return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
out = {}
for y in (2023, 2024, 2025):
    SK = {norm(r["name"]): r for r in csv.DictReader(open(HERE / f"mp/skaters_{y}.csv")) if r["situation"] == "5on5"}
    fs = [p for p in PL if p["season"] == y and p["F"]]; q = [p for p in fs if p["toi"] >= 400]
    def pct(p, k): v = p[k] / p["toi"]; return round(100 * sum((x[k] / x["toi"]) < v for x in q) / len(q))
    rows = []
    for p in fs:
        if p["team"] != "DET" or p["toi"] < 300: continue
        m = SK[norm(p["player"])]
        rows.append(dict(player=m["name"], toi=p["toi"], def_pct=pct(p, "xevd"), off_pct=pct(p, "evo"), xevd=p["xevd"],
                         g5=float(m["I_F_goals"]), xg5=float(m["I_F_xGoals"]),
                         onice_ga60=float(m["OnIce_A_goals"]) / float(m["icetime"]) * 3600))
    out[y] = rows
json.dump(out, open(HERE / "outlier.json", "w"), indent=1)
for y, rows in out.items():
    tw = sum(r["def_pct"] * r["toi"] for r in rows) / sum(r["toi"] for r in rows)
    print(y, "TOI-weighted defense percentile of the forward group", round(tw, 1), "| forwards above 60th pct:", sum(r["def_pct"] >= 60 for r in rows), "of", len(rows))
