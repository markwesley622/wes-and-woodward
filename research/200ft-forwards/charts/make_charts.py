#!/usr/bin/env python3
"""Inline-ready SVG charts for 'What does a team of 200-ft forwards get you?'
Dependency-free; same kit as the wings-type / Kreider pieces, on the current site paper (#e9e8e5)."""
import json, csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"; OUT = ROOT / "charts"
PAPER = "#e9e8e5"; PANEL = "#dddcd8"; RULE = "#c9c8c4"; INK = "#141414"; SOFT = "#575653"; MUTED = "#6b6a67"
RED = "#ce1126"; BLUE = "#2a78d6"; AMBER = "#c98500"; GRAY = "#a3a29e"
SANS = "'Space Grotesk', ui-sans-serif, system-ui, sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, monospace"
W = 760

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def svg_open(h, title, sub=None):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{esc(title)}" font-family="{SANS}" style="max-width:100%;height:auto;background:{PAPER}">',
         f'<rect width="{W}" height="{h}" fill="{PAPER}"/>',
         f'<text x="0" y="20" font-size="17" font-weight="600" fill="{INK}">{esc(title)}</text>']
    if sub: p.append(f'<text x="0" y="38" font-size="12" fill="{SOFT}">{esc(sub)}</text>')
    return p
def source(p, h, text): p.append(f'<text x="0" y="{h-8}" font-size="10.5" font-family="{MONO}" fill="{MUTED}">{esc(text)}</text>')
def close(p, name):
    p.append("</svg>"); (OUT / name).write_text("\n".join(p)); print("wrote", name)
def txt(p, x, y, s, size=12, fill=INK, anchor="start", weight=None, mono=False):
    w = f' font-weight="{weight}"' if weight else ""; f = f' font-family="{MONO}"' if mono else ""
    p.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}{f}>{esc(s)}</text>')
def legend(p, x, y, items):
    cx = x
    for name, col in items:
        p.append(f'<circle cx="{cx+5}" cy="{y-4}" r="5" fill="{col}"/>'); txt(p, cx+15, y, name); cx += 15 + 7.2*len(name) + 22
def ordn(n): return f"{n}{'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n % 10, 'th')}"

H = json.load(open(RAW / "history.json")); ALL = H["all"]; LOW = H["low"]
DET = {d["season"]: d for d in ALL if d["team"] == "DET"}
DD = json.load(open(RAW / "detroit_detail.json"))
YRS = (2023, 2024, 2025); LAB = {2023: "2023-24", 2024: "2024-25", 2025: "2025-26"}

# ---------- c1: 5v5 goals vs expected ----------
def c1():
    h = 272; p = svg_open(h, "Detroit beat its 5v5 chances by 33 goals, then missed them by 21 and 19",
                          "5v5 goals scored against expected goals, by season, with the league rank of the gap")
    x0, x1 = 120, 600; lo, hi = 130, 185
    def X(v): return x0 + (v - lo) / (hi - lo) * (x1 - x0)
    for v in range(130, 186, 10):
        p.append(f'<line x1="{X(v)}" x2="{X(v)}" y1="62" y2="196" stroke="{RULE}" stroke-width="0.8"/>'); txt(p, X(v), 212, v, 11, SOFT, "middle", mono=True)
    for i, y in enumerate(YRS):
        d = DET[y]; cy = 85 + i * 46
        txt(p, 0, cy + 4, LAB[y], 13, INK, weight=600)
        p.append(f'<line x1="{X(d["xgf5"])}" x2="{X(d["gf5"])}" y1="{cy}" y2="{cy}" stroke="{RED if d["fin5"] < 0 else INK}" stroke-width="3"/>')
        p.append(f'<circle cx="{X(d["xgf5"])}" cy="{cy}" r="6.5" fill="{GRAY}" stroke="{PAPER}" stroke-width="1.5"/>')
        p.append(f'<circle cx="{X(d["gf5"])}" cy="{cy}" r="6.5" fill="{RED if d["fin5"] < 0 else INK}" stroke="{PAPER}" stroke-width="1.5"/>')
        txt(p, X(d["xgf5"]), cy - 12, f'{d["xgf5"]:.0f}', 11, SOFT, "middle", mono=True)
        txt(p, X(d["gf5"]), cy - 12, f'{d["gf5"]:.0f}', 11, INK, "middle", 600, True)
        txt(p, 620, cy + 4, f'{d["fin5"]:+.0f}', 14, RED if d["fin5"] < 0 else INK, weight=600, mono=True)
        txt(p, 668, cy + 4, f'{ordn(d["r_fin5"])} of 32', 11.5, SOFT, mono=True)
    legend(p, x0, h - 30, [("Expected goals", GRAY), ("Goals, above expected", INK), ("Goals, below expected", RED)])
    source(p, h, "MoneyPuck team season summaries, 5v5.")
    close(p, "c1-goals-vs-expected.svg")

def tiles(p, rows, top, col_x, cw=150, rh=44):
    for j, y in enumerate(YRS): txt(p, col_x + j * (cw + 8) + cw / 2, top - 10, LAB[y], 12, SOFT, "middle", mono=True)
    for i, (label, sub, fn) in enumerate(rows):
        cy = top + i * (rh + 6)
        txt(p, 0, cy + 19, label, 13, INK, weight=600); txt(p, 0, cy + 34, sub, 10.5, MUTED, mono=True)
        for j, y in enumerate(YRS):
            rk, val = fn(y); x = col_x + j * (cw + 8)
            bad = rk > 21; good = rk <= 10
            p.append(f'<rect x="{x}" y="{cy}" width="{cw}" height="{rh}" fill="{RED if bad else (INK if good else PANEL)}"/>')
            fg = "#ffffff" if (bad or good) else INK
            txt(p, x + 12, cy + 28, ordn(rk), 19, fg, weight=600); txt(p, x + cw - 10, cy + 27, val, 11, fg, "end", mono=True)

# ---------- c2: the rank card ----------
def c2():
    rows = [("5v5 goals", "per 60", lambda y: (DET[y]["r_gf60"], f'{DET[y]["gf60"]:.2f}')),
            ("5v5 chances created", "xG for per 60", lambda y: (DET[y]["r_xgf60"], f'{DET[y]["xgf60"]:.2f}')),
            ("5v5 finishing", "goals minus xG", lambda y: (DET[y]["r_fin5"], f'{DET[y]["fin5"]:+.0f}')),
            ("5v5 chances allowed", "xG against per 60", lambda y: (DET[y]["r_xga60"], f'{DET[y]["xga60"]:.2f}')),
            ("Forwards' defense", "EH even-strength defense", lambda y: (DET[y]["r_F_xevd"], f'{DET[y]["F_xevd"]:+.1f}')),
            ("Defensemen's defense", "EH even-strength defense", lambda y: (DET[y]["r_D_xevd"], f'{DET[y]["D_xevd"]:+.1f}')),
            ("5v5 goaltending", "goals saved above expected", lambda y: (DET[y]["r_gsax5"], f'{DET[y]["gsax5"]:+.0f}'))]
    h = 78 + len(rows) * 50 + 52; p = svg_open(h, "Bottom five at 5v5 scoring two years running, with average cover behind it",
                          "Detroit's league rank of 32 in each 5v5 dimension. Black is top ten, red is bottom third")
    tiles(p, rows, 78, 262)
    source(p, h, "MoneyPuck (team 5v5); Evolving Hockey xGAR, even-strength defense summed by position.")
    close(p, "c2-rank-card.svg")

# ---------- c3: defense x goaltending grid for low-scoring teams ----------
def c3():
    g = H["summary"]["grid_def_x_goalie"]
    h = 400; p = svg_open(h, "Low-scoring teams make the playoffs when the defense and goalie are both top third",
                          "189 team seasons since 2008-09 in the bottom third of 5v5 goals per 60: playoff teams out of total, by tier")
    x0, y0, cw, ch = 190, 84, 180, 78
    names = ["Top third", "Middle third", "Bottom third"]
    txt(p, x0 + 1.5 * cw + 8, 62, "5v5 GOALTENDING (goals saved above expected)", 10.5, MUTED, "middle", mono=True)
    for b in range(3): txt(p, x0 + b * (cw + 6) + cw / 2, 78, names[b], 12, SOFT, "middle")
    txt(p, 0, y0 - 6, "5v5 DEFENSE", 10.5, MUTED, mono=True); txt(p, 0, y0 + 8, "(xG against per 60)", 10.5, MUTED, mono=True)
    det = {(2, 0): "Detroit 2024-25", (1, 1): "Detroit 2025-26"}
    for a in range(3):
        txt(p, 0, y0 + a * (ch + 6) + ch / 2 + 14, names[a], 12, SOFT)
        for b in range(3):
            c = g[a][b]; rate = c["playoffs"] / c["n"]; x = x0 + b * (cw + 6); y = y0 + a * (ch + 6)
            op = 0.08 + rate * 0.92
            p.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{PANEL}"/>')
            p.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{INK}" opacity="{op:.2f}"/>')
            fg = "#ffffff" if op > 0.45 else INK
            txt(p, x + 12, y + 32, f'{rate*100:.0f}%', 22, fg, weight=600)
            txt(p, x + 12, y + 50, f'{c["playoffs"]} of {c["n"]} made it', 11, fg, mono=True)
            txt(p, x + 12, y + 65, f'{c["won_round"]} won a round', 11, fg, mono=True)
            if (a, b) in det:
                p.append(f'<rect x="{x+1.5}" y="{y+1.5}" width="{cw-3}" height="{ch-3}" fill="none" stroke="{RED}" stroke-width="3"/>')
                txt(p, x + cw - 10, y + 18, det[(a, b)], 11, RED if op <= 0.45 else "#ffffff", "end", 600)
    txt(p, 0, h - 44, "Detroit's 2023-24 team is not on this grid: it finished 6th in 5v5 goals per 60 and missed anyway", 11.5, SOFT)
    txt(p, 0, h - 29, "with the 20th-ranked defense and the 29th-ranked goaltending.", 11.5, SOFT)
    source(p, h, "MoneyPuck team 5v5, 2008-09 to 2025-26 (554 team seasons); NHL playoff brackets.")
    close(p, "c3-defense-goalie-grid.svg")

# ---------- c4: the teams it worked for ----------
def c4():
    win = sorted([d for d in LOW if d["rounds"] >= 1], key=lambda d: (-d["rounds"], d["season"]))
    rows = win + [DET[2024], DET[2025]]
    rh = 21; h = 96 + len(rows) * rh + 60
    p = svg_open(h, "The 18 low-scoring teams that won a round defended or stopped pucks at a top-ten level",
                 "League rank in three areas for every bottom-third 5v5 offense that won a playoff round since 2008-09, then Detroit")
    x0, x1 = 190, 560
    def X(r): return x0 + (r - 1) / 31 * (x1 - x0)
    p.append(f'<rect x="{X(1)-8}" y="74" width="{X(10)-X(1)+16}" height="{len(rows)*rh+14}" fill="{PANEL}"/>')
    txt(p, X(5.5), 68, "top ten", 10.5, MUTED, "middle", mono=True)
    for r in (1, 10, 16, 32): txt(p, X(r), 68 if r != 1 and r != 10 else 0, "", 1)
    txt(p, X(16), 68, "16th", 10.5, MUTED, "middle", mono=True); txt(p, X(32), 68, "32nd", 10.5, MUTED, "middle", mono=True)
    txt(p, 585, 68, "TOP-SCORING FORWARD", 10.5, MUTED, mono=True)
    res = {4: "Cup", 3: "Final", 2: "2 rounds", 1: "1 round"}
    for i, d in enumerate(rows):
        cy = 92 + i * rh; isdet = d["team"] == "DET" and d["season"] >= 2024
        if isdet and d["season"] == 2024: p.append(f'<line x1="0" x2="{W}" y1="{cy-13}" y2="{cy-13}" stroke="{INK}" stroke-width="1"/>')
        txt(p, 0, cy + 4, d["label"], 12, RED if isdet else INK, weight=600)
        txt(p, 96, cy + 4, "missed" if isdet else res[d["rounds"]], 11, RED if isdet else SOFT, mono=True)
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{cy}" y2="{cy}" stroke="{RULE}" stroke-width="0.8"/>')
        for key, col in (("r_F_xevd", AMBER), ("r_gsax5", BLUE), ("r_xga60", INK)):
            p.append(f'<circle cx="{X(d[key]):.1f}" cy="{cy}" r="5" fill="{col}" stroke="{PAPER}" stroke-width="1.2"/>')
        nm = d["top_pts_f"].split(" ", 1)[1]
        txt(p, 585, cy + 4, f'{nm}, {ordn(d["top_pts_rank"])}', 11, RED if isdet else INK, mono=True)
    legend(p, 0, h - 30, [("Chances allowed (xGA/60)", INK), ("5v5 goaltending (GSAx)", BLUE), ("Forwards' defense (EH)", AMBER)])
    source(p, h, "MoneyPuck, Evolving Hockey, NHL. Top-scoring forward = team's leading forward and his rank among NHL forwards in points.")
    close(p, "c4-teams-it-worked-for.svg")

# ---------- c5: forward-by-forward finishing ----------
def c5():
    panels = [(2024, DD["forwards"]["2024"]), (2025, DD["forwards"]["2025"])]
    n = max(len(L) for _, L in panels); rh = 21; h = 92 + n * rh + 46
    p = svg_open(h, "The misses belong to the checking centers. The scorers finished about as usual",
                 "5v5 goals minus expected goals, Detroit forwards with 200+ 5v5 minutes. Number at right is career goals per xG entering the season")
    for k, (y, L) in enumerate(panels):
        ox = k * 390; zx = ox + 215; sc = 9
        txt(p, ox, 66, LAB[y], 13, INK, weight=600)
        p.append(f'<line x1="{zx}" x2="{zx}" y1="74" y2="{80 + n*rh}" stroke="{INK}" stroke-width="1"/>')
        for i, e in enumerate(sorted(L, key=lambda e: e["g"] - e["xg"])):
            cy = 90 + i * rh; v = e["g"] - e["xg"]
            txt(p, ox, cy + 4, e["name"], 11.5, INK)
            wv = abs(v) * sc; x = zx - wv if v < 0 else zx
            p.append(f'<rect x="{x:.1f}" y="{cy-7}" width="{max(wv,1):.1f}" height="14" fill="{RED if v < 0 else INK}"/>')
            txt(p, (zx - wv - 5) if v < 0 else (zx + wv + 5), cy + 4, f'{v:+.1f}', 10.5, SOFT, "end" if v < 0 else "start", mono=True)
            pr = e.get("prior_ratio")
            txt(p, ox + 352, cy + 4, f'{pr:.2f}' if pr else "new", 10.5, MUTED if not pr else (INK if pr >= 1.1 else SOFT), "end", mono=True)
    source(p, h, "MoneyPuck skaters, 5v5. A traded player's row is his whole season (Perron 2025-26 includes Ottawa).")
    close(p, "c5-forward-finishing.svg")

# ---------- c6: where the finishing went, by shot danger ----------
def c6():
    R = {}
    for y in YRS:
        T = [r for r in csv.DictReader(open(RAW / f"mp/teams_{y}.csv")) if r["situation"] == "5on5"]
        for band in ("low", "medium", "high"):
            f = lambda r: float(r[f"{band}DangerGoalsFor"]) - float(r[f"{band}DangerxGoalsFor"])
            s = sorted(T, key=lambda r: -f(r)); det = [r for r in T if r["team"] == "DET"][0]
            R[(y, band)] = ([r["team"] for r in s].index("DET") + 1, f'{f(det):+.0f}')
    rows = [("Low-danger shots", "goals minus xG", lambda y: R[(y, "low")]), ("Medium-danger shots", "goals minus xG", lambda y: R[(y, "medium")]),
            ("High-danger shots", "goals minus xG", lambda y: R[(y, "high")])]
    h = 78 + 3 * 50 + 66; p = svg_open(h, "Detroit led the league at scoring from distance in 2023-24, then finished 31st",
                                       "5v5 finishing by MoneyPuck shot-danger band, league rank of 32. Black is top ten, red is bottom third")
    tiles(p, rows, 78, 262)
    txt(p, 0, h - 30, "Read the ranks, not the raw high-danger gaps: MoneyPuck's high-danger band runs under expected for every team.", 11.5, SOFT)
    source(p, h, "MoneyPuck team season summaries, 5v5.")
    close(p, "c6-finishing-by-danger.svg")

# ---------- c7: 2023-24, the scorers who didn't defend ----------
def c7():
    rows = json.load(open(RAW / "outlier.json"))["2023"]
    h = 412; p = svg_open(h, "Sprong and Fabbri scored 28 goals at 5v5 and defended worse than 94% of NHL forwards",
                          "Detroit forwards, 2023-24. Across: even-strength defense, percentile among NHL forwards. Up: 5v5 goals minus expected")
    x0, x1, y0, y1 = 60, 720, 64, 320; lo, hi = -6, 8
    def X(v): return x0 + v / 100 * (x1 - x0)
    def Y(v): return y1 - (v - lo) / (hi - lo) * (y1 - y0)
    for v in (0, 25, 50, 75, 100):
        p.append(f'<line x1="{X(v)}" x2="{X(v)}" y1="{y0}" y2="{y1}" stroke="{RULE}" stroke-width="{1.5 if v == 50 else 0.8}"/>'); txt(p, X(v), y1 + 16, v, 11, SOFT, "middle", mono=True)
    for v in (-4, 0, 4, 8):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="{INK if v == 0 else RULE}" stroke-width="{1 if v == 0 else 0.8}"/>'); txt(p, x0 - 8, Y(v) + 4, f"{v:+d}" if v else "0", 11, SOFT, "end", mono=True)
    txt(p, x0, y1 + 34, "worse defensively", 11, MUTED); txt(p, x1, y1 + 34, "better defensively", 11, MUTED, "end")
    left = {"Robby Fabbri": (10, 4, "start"), "Daniel Sprong": (10, 4, "start"), "Christian Fischer": (-9, 4, "end"), "Patrick Kane": (-9, -2, "end"), "Dylan Larkin": (-9, 12, "end"),
            "Lucas Raymond": (0, -11, "middle"), "J.T. Compher": (-9, -4, "end"), "Michael Rasmussen": (0, 18, "middle"), "Andrew Copp": (9, -6, "start"), "David Perron": (-8, 15, "end"), "Joe Veleno": (10, 4, "start"), "Alex DeBrincat": (0, -11, "middle")}
    for r in rows:
        gone = r["player"] in ("Robby Fabbri", "Daniel Sprong"); v = r["g5"] - r["xg5"]; cx, cy = X(r["def_pct"]), Y(v)
        p.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{7 if gone else 5.5}" fill="{RED if gone else INK}" stroke="{PAPER}" stroke-width="1.5"/>')
        dx, dy, a = left.get(r["player"], (9, 4, "start"))
        lab = r["player"].split(" ", 1)[1] + (f', {r["g5"]:.0f} goals on {r["xg5"]:.1f} xG' if gone else "")
        txt(p, cx + dx, cy + dy, lab, 11.5, RED if gone else INK, a, 600 if gone else None)
    legend(p, x0, h - 30, [("Gone after the season", RED), ("Other forwards, 300+ minutes", INK)])
    source(p, h, "Evolving Hockey xGAR even-strength defense per minute vs forwards with 400+ min; MoneyPuck 5v5 goals and xG.")
    close(p, "c7-2023-24-outlier.svg")

# ---------- c8: which template team Detroit 2025-26 resembles ----------
def c8():
    import math
    def vec(d):
        n = d["n"]; return [d["r_gf60"]/n, d["r_xgf60"]/n, d["r_fin5"]/n, d["r_xga60"]/n, d["r_gsax5"]/n, d["r_F_xevd"]/n, d["r_D_xevd"]/n, min(d["top_pts_rank"],60)/60, min(d["top_f_rank"],60)/60, min(d["top_d_rank"],40)/40]
    D = DET[2025]
    named = [("TBL",2016),("NYI",2019),("LAK",2011),("MIN",2015),("MIN",2017),("STL",2018),("LAK",2013),("CAR",2023),("MIN",2012),("MIN",2013),("DAL",2019),("CAR",2025),("TBL",2015),("BOS",2010)]
    rows = sorted([d for d in ALL if (d["team"], d["season"]) in named], key=lambda d: math.dist(vec(D), vec(d)))[:10]
    res = {4: "won the Cup", 3: "lost the Final", 2: "two rounds", 1: "one round", 0: "missed the playoffs"}
    rh = 30; h = 84 + len(rows) * rh + 44
    p = svg_open(h, "The closest comps: a Lightning team that missed and an Islanders team that won two rounds",
                 "Distance from Detroit 2025-26 across ten rank dimensions. Shorter bar = more alike")
    x0, x1 = 120, 480; mx = 1.3
    def X(v): return x0 + v / mx * (x1 - x0)
    for i, d in enumerate(rows):
        cy = 80 + i * rh; dist = math.dist(vec(D), vec(d)); top = i < 2
        txt(p, 0, cy + 5, d["label"], 12.5, RED if top else INK, weight=600)
        p.append(f'<rect x="{x0}" y="{cy-9}" width="{X(dist)-x0:.1f}" height="18" fill="{RED if top else INK}"/>')
        txt(p, X(dist) + 8, cy + 4, f"{dist:.2f}", 11, SOFT, mono=True)
        txt(p, 560, cy + 4, res[d["rounds"]], 11.5, SOFT)
    source(p, h, "MoneyPuck, Evolving Hockey, NHL. Candidates = the template teams named in the piece; Euclidean distance over rank percentiles.")
    close(p, "c8-template-distance.svg")

# ---------- c9: Larkin vs Kopitar ----------
def c9():
    rows = [("Points per 82", "76 · 73 · 70", "83 · 70 · 74"), ("Points rank among forwards", "16th · 28th · 16th", "49th · 41st · 50th"),
            ("EH value rank among forwards", "11th · 9th · 6th", "56th · 43rd · 144th"), ("Even-strength offense, percentile", "70 · 76 · 81", "92 · 66 · 44"),
            ("Even-strength defense, percentile", "76 · 80 · 93", "29 · 53 · 31"), ("5v5 xG share, on ice vs off", "57/50 · 60/52 · 62/52", "47/46 · 50/47 · 47/48")]
    rh = 40; h = 92 + len(rows) * rh + 40
    p = svg_open(h, "Same points, different player", "Kopitar 2011-12 to 2013-14 (age 24 to 26) against Larkin 2023-24 to 2025-26 (age 27 to 29), season by season")
    txt(p, 300, 70, "KOPITAR", 11, MUTED, "start", mono=True); txt(p, 530, 70, "LARKIN", 11, RED, "start", mono=True)
    for i, (lab, k, l) in enumerate(rows):
        cy = 84 + i * rh
        p.append(f'<line x1="0" x2="{W}" y1="{cy-8}" y2="{cy-8}" stroke="{RULE}" stroke-width="0.8"/>')
        txt(p, 0, cy + 14, lab, 12.5, INK, weight=600)
        txt(p, 300, cy + 14, k, 12.5, INK, mono=True); txt(p, 530, cy + 14, l, 12.5, RED, mono=True)
    source(p, h, "MoneyPuck (points, on-ice xG), Evolving Hockey (value and even-strength percentiles among forwards with 600+ min).")
    close(p, "c9-larkin-kopitar.svg")

for f in (c1, c2, c3, c4, c5, c6, c7, c8, c9): f()
