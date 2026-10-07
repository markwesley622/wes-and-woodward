#!/usr/bin/env python3
"""Detroit detail: pooled 3-yr ranks, shot-mix ranks, forward-by-forward 5v5 finishing, roster's prior finishing talent."""
import csv, json, pathlib, statistics as st
HERE = pathlib.Path(__file__).parent
FIX = {"L.A": "LAK", "N.J": "NJD", "S.J": "SJS", "T.B": "TBL"}
M = json.load(open(HERE / "master.json"))
out = {}
# pooled 2023-25
pool = {}
for d in M:
    if d["season"] >= 2023:
        t = "UTA" if d["team"] == "ARI" else d["team"]
        p = pool.setdefault(t, dict(gf5=0, xgf5=0, ga5=0, xga5=0, gp=0, min=0))
        for k in ("gf5", "xgf5", "ga5", "xga5", "gp"): p[k] += d[k]
        p["min"] += d["gf5"] / d["gf60"] * 60
for t, p in pool.items():
    p["gf60"] = p["gf5"] / p["min"] * 60; p["xgf60"] = p["xgf5"] / p["min"] * 60; p["xga60"] = p["xga5"] / p["min"] * 60; p["ga60"] = p["ga5"] / p["min"] * 60
    p["fin"] = p["gf5"] - p["xgf5"]; p["gsax"] = p["xga5"] - p["ga5"]; p["gd5"] = p["gf5"] - p["ga5"]
def rank(key, hi=True):
    s = sorted(pool, key=lambda t: -pool[t][key] if hi else pool[t][key]); return s.index("DET") + 1
out["pooled"] = {k: (round(pool["DET"][k], 2), rank(k, hi)) for k, hi in [("gf5", 1), ("gf60", 1), ("xgf60", 1), ("fin", 1), ("xga60", 0), ("ga60", 0), ("gsax", 1), ("gd5", 1)]}
print("pooled 2023-26 (value, rank of 32):", out["pooled"])
print("bottom 5 GF5:", sorted(((round(p['gf5']),t) for t,p in pool.items()))[:6])
# shot mix by season
for y in (2023, 2024, 2025):
    R = [r for r in csv.DictReader(open(HERE / f"mp/teams_{y}.csv")) if r["situation"] == "5on5"]
    def f(r, k): return float(r[k])
    feats = {
        "xG per unblocked attempt": lambda r: f(r, "xGoalsFor") / f(r, "unblockedShotAttemptsFor"),
        "high-danger share of xG": lambda r: f(r, "highDangerxGoalsFor") / f(r, "xGoalsFor"),
        "low-danger share of xG": lambda r: f(r, "lowDangerxGoalsFor") / f(r, "xGoalsFor"),
        "rebound xG share": lambda r: f(r, "reboundxGoalsFor") / f(r, "xGoalsFor"),
        "unblocked attempts/60": lambda r: f(r, "unblockedShotAttemptsFor") / f(r, "iceTime") * 3600,
        "HD goals - HD xG": lambda r: f(r, "highDangerGoalsFor") - f(r, "highDangerxGoalsFor"),
        "MD goals - MD xG": lambda r: f(r, "mediumDangerGoalsFor") - f(r, "mediumDangerxGoalsFor"),
        "LD goals - LD xG": lambda r: f(r, "lowDangerGoalsFor") - f(r, "lowDangerxGoalsFor"),
        "rebound goals - rebound xG": lambda r: f(r, "reboundGoalsFor") - f(r, "reboundxGoalsFor"),
    }
    print(y)
    for name, fn in feats.items():
        s = sorted(R, key=lambda r: -fn(r)); i = [r["team"] for r in s].index("DET") + 1
        det = [r for r in R if r["team"] == "DET"][0]
        print(f"   {name}: {fn(det):.3f} r{i}")
# skaters
SK = {}
for y in range(2008, 2026):
    for r in csv.DictReader(open(HERE / f"mp/skaters_{y}.csv")):
        if r["situation"] in ("5on5", "all"):
            SK[(y, r["playerId"], r["situation"])] = r
detf = {}
for y in (2023, 2024, 2025):
    rows = [r for (yy, pid, s), r in SK.items() if yy == y and s == "5on5" and r["team"] == "DET"]
    F = [r for r in rows if r["position"] != "D"]; D = [r for r in rows if r["position"] == "D"]
    g = lambda R, k: sum(float(r[k]) for r in R)
    print(f"\n{y}: forwards 5v5 G {g(F,'I_F_goals'):.0f} xG {g(F,'I_F_xGoals'):.1f} diff {g(F,'I_F_goals')-g(F,'I_F_xGoals'):+.1f} | D G {g(D,'I_F_goals'):.0f} xG {g(D,'I_F_xGoals'):.1f} diff {g(D,'I_F_goals')-g(D,'I_F_xGoals'):+.1f}")
    lst = []
    for r in sorted(F, key=lambda r: float(r["I_F_goals"]) - float(r["I_F_xGoals"])):
        if float(r["icetime"]) < 200 * 60: continue
        # prior career 5v5 finishing (all seasons before y)
        pg = px = 0
        for yy in range(2008, y):
            q = SK.get((yy, r["playerId"], "5on5"))
            if q: pg += float(q["I_F_goals"]); px += float(q["I_F_xGoals"])
        e = dict(name=r["name"], season=y, gp=int(r["games_played"]), toi=float(r["icetime"]) / 60, g=float(r["I_F_goals"]), xg=float(r["I_F_xGoals"]),
                 prior_g=pg, prior_xg=px, prior_ratio=(pg / px if px >= 10 else None))
        lst.append(e)
        pr = f"{e['prior_ratio']:.2f} ({pg:.0f}/{px:.0f})" if e["prior_ratio"] else "n/a"
        print(f"   {e['name']:<22} {e['g']:.0f} G on {e['xg']:.1f} xG ({e['g']-e['xg']:+.1f})  prior career G/xG {pr}")
    # expected finishing given prior talent, shrunk: (pg + 30)/(px + 30)
    exp = sum(e["xg"] * ((e["prior_g"] + 30) / (e["prior_xg"] + 30)) for e in lst)
    print(f"   roster xG {sum(e['xg'] for e in lst):.1f}; goals expected from prior shooting talent (shrunk, k=30 xG) {exp:.1f}; actual {sum(e['g'] for e in lst):.0f}")
    detf[y] = lst
out["forwards"] = detf
json.dump(out, open(HERE / "detroit_detail.json", "w"), indent=1)
