#!/usr/bin/env python3
"""Forward-group profile per team-season from Evolving Hockey GAR/xGAR (2007-08 .. 2025-26).
Offense = forwards' even-strength offense xGAR (chance-based), Defense = forwards' even-strength defense xGAR.
Everything scaled to 82 games; z-scored within season."""
import csv, json, pathlib, statistics as st
HERE = pathlib.Path(__file__).parent
EH = HERE / "../../rasmussen/raw/eh"
G = {(r["Player"], r["Season"], r["Team"]): r for r in csv.DictReader(open(EH / "gar_all_seasons.csv"))}
X = list(csv.DictReader(open(EH / "xgar_all_seasons.csv")))
FIX = {"L.A": "LAK", "N.J": "NJD", "S.J": "SJS", "T.B": "TBL"}
teams = {}
players = []
for x in X:
    g = G[(x["Player"], x["Season"], x["Team"])]
    y = 2000 + int(x["Season"][:2]); t = FIX.get(x["Team"], x["Team"])
    isF = x["Position"][0] != "D"
    p = dict(player=x["Player"], season=y, team=t, F=isF, gp=int(x["GP"]), toi=float(x["TOI_All"]),
             xevo=float(x["xEVO_GAR"]), xevd=float(x["xEVD_GAR"]), evo=float(g["EVO_GAR"]), evd=float(g["EVD_GAR"]),
             xgar=float(x["xGAR"]), gar=float(g["GAR"]), ppo=float(g["PPO_GAR"]))
    players.append(p)
    d = teams.setdefault((y, t), dict(season=y, team=t, F_xevo=0, F_xevd=0, F_evo=0, F_evd=0, D_xevo=0, D_xevd=0, D_evo=0, D_evd=0, F_toi=0, F_gar=0, D_gar=0, D_xgar=0, F_xgar=0))
    k = "F" if isF else "D"
    for a in ("xevo", "xevd", "evo", "evd", "gar", "xgar"): d[f"{k}_{a}"] += p[a]
    if isF: d["F_toi"] += p["toi"]
# league ranks of individual forwards by GAR / xGAR each season
for y in sorted({p["season"] for p in players}):
    fs = [p for p in players if p["season"] == y and p["F"]]
    for key in ("gar", "xgar", "evo", "xevo"):
        for i, p in enumerate(sorted(fs, key=lambda p: -p[key])): p["r_" + key] = i + 1
TS = {(d["season"], d["team"]): d for d in json.load(open(HERE / "team_seasons.json"))}
out = []
for (y, t), d in teams.items():
    ts = TS.get((y, t))
    if not ts:
        if y > 2007: print("no MP row", y, t)
        continue
    sc = 82 / ts["gp"]
    for k in list(d):
        if k[:2] in ("F_", "D_") and k != "F_toi": d[k] *= sc
    fs = sorted([p for p in players if p["season"] == y and p["team"] == t and p["F"]], key=lambda p: -p["gar"])
    d["top_f"] = fs[0]["player"]; d["top_f_gar"] = fs[0]["gar"] * sc; d["top_f_rank"] = fs[0]["r_gar"]
    bx = min(fs, key=lambda p: p["r_xgar"]); d["top_f_x"] = bx["player"]; d["top_f_xrank"] = bx["r_xgar"]
    d["F_shoot"] = d["F_evo"] - d["F_xevo"]      # forwards' EV offense: results minus chance-based = finishing
    d.update({k: ts[k] for k in ts if k not in d})
    out.append(d)
for y in sorted({d["season"] for d in out}):
    S = [d for d in out if d["season"] == y]
    for k in ("F_xevo", "F_xevd", "F_evo", "F_evd", "D_xevd", "D_xevo", "D_gar", "F_shoot", "F_gar", "F_xgar"):
        m, s = st.mean(d[k] for d in S), st.pstdev(d[k] for d in S)
        for i, d in enumerate(sorted(S, key=lambda d: -d[k])): d["r_" + k] = i + 1
        for d in S: d["z_" + k] = (d[k] - m) / s
    for d in S:
        d["tilt"] = d["z_F_xevd"] - d["z_F_xevo"]   # defense-leaning forward group
    for i, d in enumerate(sorted(S, key=lambda d: -d["tilt"])): d["r_tilt"] = i + 1
json.dump(out, open(HERE / "fgroup.json", "w"), indent=0)
json.dump(players, open(HERE / "eh_players.json", "w"))
if __name__ == "__main__":
    for d in sorted(out, key=lambda d: d["season"]):
        if d["team"] == "DET" and d["season"] >= 2016:
            print(d["season"], f"F xEVO {d['F_xevo']:+.1f} r{d['r_F_xevo']} | F xEVD {d['F_xevd']:+.1f} r{d['r_F_xevd']} | tilt {d['tilt']:+.2f} r{d['r_tilt']} | F EVO {d['F_evo']:+.1f} r{d['r_F_evo']} shoot {d['F_shoot']:+.1f} r{d['r_F_shoot']} | D xEVD {d['D_xevd']:+.1f} r{d['r_D_xevd']} D gar r{d['r_D_gar']} | top F {d['top_f']} #{d['top_f_rank']} ; x {d['top_f_x']} #{d['top_f_xrank']}")
