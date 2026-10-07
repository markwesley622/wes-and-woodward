#!/usr/bin/env python3
"""Historical test: bottom-third 5v5 scoring teams 2008-09..2025-26. Who won, with what."""
import csv, json, pathlib, statistics as st
HERE = pathlib.Path(__file__).parent
FIX = {"L.A": "LAK", "N.J": "NJD", "S.J": "SJS", "T.B": "TBL"}
M = json.load(open(HERE / "master.json"))
PL = json.load(open(HERE / "eh_players.json"))
# top defenseman by EH GAR rank among D; starter goalie by MoneyPuck GSAx rank
topd = {}
for y in sorted({p["season"] for p in PL}):
    ds = sorted([p for p in PL if p["season"] == y and not p["F"]], key=lambda p: -p["gar"])
    for i, p in enumerate(ds):
        topd.setdefault((y, p["team"]), (p["player"], i + 1))
gl = {}
for y in range(2008, 2026):
    G = [r for r in csv.DictReader(open(HERE / f"mp/goalies_{y}.csv")) if r["situation"] == "all"]
    for r in G: r["gsax"] = float(r["xGoals"]) - float(r["goals"]); r["team"] = FIX.get(r["team"], r["team"])
    Q = sorted([r for r in G if float(r["icetime"]) >= 1200 * 60 * (48/82 if y == 2012 else 56/82 if y == 2020 else 1)], key=lambda r: -r["gsax"])
    for i, r in enumerate(Q): r["rk"] = i + 1
    for r in sorted(G, key=lambda r: -float(r["icetime"])):
        gl.setdefault((y, r["team"]), (r["name"], r.get("rk"), round(r["gsax"], 1), len(Q)))
def t(q): return 0 if q <= 1/3 else (1 if q <= 2/3 else 2)
for d in M:
    n = d["n"]; k = (d["season"], d["team"])
    d["t_off"] = t(d["r_gf60"] / n); d["t_def"] = t(d["r_xga60"] / n); d["t_g"] = t(d["r_gsax5"] / n); d["t_ga"] = t(d["r_ga60"] / n); d["t_fd"] = t(d["r_F_xevd"] / n)
    d["top_d"], d["top_d_rank"] = topd[k]; d["goalie"], d["goalie_rank"], d["goalie_gsax"], d["goalie_n"] = gl[k]
    d["label"] = f"{d['season']}-{str(d['season']+1)[2:]} {d['team']}"
low = [d for d in M if d["t_off"] == 2]
S = dict(n=len(M), low=len(low), low_playoffs=sum(d["playoffs"] for d in low), low_r1=sum(d["rounds"] >= 1 for d in low), low_r2=sum(d["rounds"] >= 2 for d in low),
         low_final=sum(d["rounds"] >= 3 for d in low), low_cup=sum(d["rounds"] >= 4 for d in low),
         rest_playoff_rate=st.mean(d["playoffs"] for d in M if d["t_off"] < 2),
         top_off_cups=sum(d["rounds"] >= 4 for d in M if d["t_off"] == 0), mid_off_cups=sum(d["rounds"] >= 4 for d in M if d["t_off"] == 1))
grid = [[None] * 3 for _ in range(3)]
for a in range(3):
    for b in range(3):
        c = [d for d in low if d["t_def"] == a and d["t_g"] == b]
        grid[a][b] = dict(n=len(c), playoffs=sum(d["playoffs"] for d in c), won_round=sum(d["rounds"] >= 1 for d in c), pts82=round(st.mean(d["pts82"] for d in c), 1))
S["grid_def_x_goalie"] = grid
print(json.dumps(S, indent=1))
win = [d for d in low if d["rounds"] >= 1]
po = [d for d in low if d["playoffs"]]; miss = [d for d in low if not d["playoffs"]]
def med(L, k): return st.median(d[k] for d in L)
for name, L in (("won a round", win), ("made playoffs", po), ("missed", miss)):
    print(name, len(L), {k: med(L, k) for k in ("r_xgf60", "r_xga60", "r_ga60", "r_gsax5", "r_F_xevd", "r_D_xevd", "top_pts_rank", "top_d_rank")},
          "fin82", round(st.mean(d["fin5_82"] for d in L), 1), "top10 xGA", sum(d["r_xga60"] <= 10 for d in L), "top10 GSAx", sum(d["r_gsax5"] <= 10 for d in L),
          "either", sum(d["r_xga60"] <= 10 or d["r_gsax5"] <= 10 for d in L), "both", sum(d["r_xga60"] <= 10 and d["r_gsax5"] <= 10 for d in L),
          "top10 scorer", sum(d["top_pts_rank"] <= 10 for d in L), "top20 scorer", sum(d["top_pts_rank"] <= 20 for d in L), "top10 F GAR", sum(d["top_f_rank"] <= 10 for d in L),
          "top10 D", sum(d["top_d_rank"] <= 10 for d in L), "top F-def 10", sum(d["r_F_xevd"] <= 10 for d in L), "top10 xGF", sum(d["r_xgf60"] <= 10 for d in L))
print()
for d in sorted(win, key=lambda d: (-d["rounds"], d["season"])):
    print(d["label"], "| top D", d["top_d"], f"#{d['top_d_rank']}", "| G", d["goalie"], f"#{d['goalie_rank']}/{d['goalie_n']}", d["goalie_gsax"], "| F-GAR", d["top_f"], f"#{d['top_f_rank']}")
print("\nDetroit")
for d in M:
    if d["team"] == "DET" and d["season"] >= 2023:
        print(d["label"], d["top_d"], d["top_d_rank"], d["goalie"], d["goalie_rank"], d["goalie_n"], d["goalie_gsax"], "F xEVD", d["r_F_xevd"], "D xEVD", d["r_D_xevd"], "cells", d["t_off"], d["t_def"], d["t_g"], "pts", d["points"], d["r_pts"])
# both low-creation AND low-scoring (Detroit's actual profile): bottom-third GF/60 and bottom-third xGF/60
both = [d for d in low if d["r_xgf60"] / d["n"] > 2/3]
print("\nbottom third in BOTH gf60 and xgf60:", len(both), "playoffs", sum(d["playoffs"] for d in both), "won round", [d["label"] for d in both if d["rounds"] >= 1])
lowx = [d for d in low if d["r_xgf60"] / d["n"] > .6]
print("xgf60 bottom 40% and gf60 bottom third:", len(lowx), sum(d["playoffs"] for d in lowx), [(d["label"], d["rounds"], d["r_xga60"], d["r_gsax5"]) for d in lowx if d["playoffs"]])
json.dump(dict(summary=S, low=low, all=M), open(HERE / "history.json", "w"))
