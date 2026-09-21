#!/usr/bin/env python3
"""Generate inline-ready SVG charts for 'Do the Red Wings have a type?'
Dependency-free. Palette validated with the dataviz skill against the site's
paper surface (#d7d6d3): Copp #ce1126, Finnie #2a78d6, Kasper #c98500.
Every chart carries a legend + direct labels (amber contrast relief)."""
import json, math, csv, pathlib, random
from itertools import combinations

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
OUT = ROOT / "charts"

# ---- site tokens ----
PAPER = "#d7d6d3"; PANEL = "#e7e6e3"; RULE = "#c4c3bf"; INK = "#141414"; SOFT = "#575653"; MUTED = "#8a8781"
COL = {"Copp": "#ce1126", "Finnie": "#2a78d6", "Kasper": "#c98500"}
GRAY = "#b3b1ad"
SANS = "'Space Grotesk', ui-sans-serif, system-ui, sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, monospace"
W = 760

feat = json.load(open(RAW / "forward_features_2025.json"))
sim = json.load(open(RAW / "similarity_2025.json"))
shots = json.load(open(RAW / "shots_three.json"))
IDS = {"8477429": "Copp", "8484471": "Finnie", "8483464": "Kasper"}
ORDER = ["Copp", "Finnie", "Kasper"]


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_open(h, title, sub=None):
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{esc(title)}" font-family="{SANS}" style="max-width:100%;height:auto;background:{PAPER}">',
             f'<rect width="{W}" height="{h}" fill="{PAPER}"/>',
             f'<text x="0" y="20" font-size="17" font-weight="600" fill="{INK}">{esc(title)}</text>']
    if sub:
        parts.append(f'<text x="0" y="38" font-size="12" fill="{SOFT}">{esc(sub)}</text>')
    return parts


def legend(parts, x, y, names=ORDER):
    cx = x
    for n in names:
        parts.append(f'<circle cx="{cx+5}" cy="{y-4}" r="5" fill="{COL[n]}"/>')
        parts.append(f'<text x="{cx+15}" y="{y}" font-size="12" fill="{INK}">{n}</text>')
        cx += 15 + 8 * len(n) + 22


def source(parts, h, text):
    parts.append(f'<text x="0" y="{h-8}" font-size="10.5" font-family="{MONO}" fill="{MUTED}">{esc(text)}</text>')


def close(parts, name):
    parts.append("</svg>")
    (OUT / name).write_text("\n".join(parts))
    print("wrote", name)


# ---------- percentile helpers ----------
P = list(feat)


def pct(k, v):
    vals = [feat[p][k] for p in P if not math.isnan(feat[p][k])]
    return 100 * sum(1 for x in vals if x < v) / len(vals)


# =====================================================================
# C1  Profile strip: league percentiles (forwards, 41+ GP, 500+ 5v5 min)
# =====================================================================
rows = [
    ("Deployment", None),
    ("Time on ice / game", "toi_gm", ""),
    ("Faceoffs taken / game", "fo_share", ""),
    ("Off-zone start share (5v5)", "ozs_pct", ""),
    ("Shot profile", None),
    ("Individual xG / 60 (5v5)", "ixg60_5v5", ""),
    ("High-danger share of attempts", "hd_share", ""),
    ("Shot attempts / 60 (5v5)", "attempts60_5v5", ""),
    ("Rebounds created / 60 (5v5)", "rebounds60", ""),
    ("Finishing", None),
    ("Shooting %", "sh_pct", ""),
    ("Goals minus xG", "gax", ""),
    ("Away from the puck", None),
    ("Hits / 60", "hits60", ""),
    ("Blocked shots / 60", "blocks60", ""),
    ("Takeaways / 60", "takeaways60", ""),
    ("Penalties drawn / 60", "pen_drawn60", ""),
    ("Penalties taken / 60 (low = good)", "pen_taken60", ""),
    ("On-ice results (5v5)", None),
    ("xG share", "xgf_pct_5v5", ""),
    ("xG against / 60 (low = good)", "xga60_on", ""),
    ("Points / 60", "pts60_5v5", ""),
]
row_h = 22; head_h = 26
h = 70 + sum(head_h if r[1] is None else row_h for r in rows) + 40
parts = svg_open(h, "Where the three sit among NHL forwards, 2025-26",
                 "League percentile among 384 forwards (41+ GP, 500+ 5v5 minutes). Dots are direct-labeled with the raw value.")
legend(parts, 0, 58)
x0, x1 = 240, 585
y = 78
parts.append(f'<text x="{x0}" y="{y-6}" font-size="10" font-family="{MONO}" fill="{MUTED}">0</text>')
parts.append(f'<text x="{(x0+x1)/2}" y="{y-6}" font-size="10" font-family="{MONO}" fill="{MUTED}" text-anchor="middle">50th pct</text>')
parts.append(f'<text x="{x1}" y="{y-6}" font-size="10" font-family="{MONO}" fill="{MUTED}" text-anchor="end">100</text>')
fmt = {"toi_gm": lambda v: f"{int(v)}:{int(round((v%1)*60)):02d}", "fo_share": lambda v: f"{v:.1f}", "ozs_pct": lambda v: f"{100*v:.0f}%",
       "hd_share": lambda v: f"{100*v:.0f}%", "sh_pct": lambda v: f"{100*v:.1f}%", "gax": lambda v: f"{v:+.1f}",
       "xgf_pct_5v5": lambda v: f"{100*v:.0f}%"}
for r in rows:
    if r[1] is None:
        y += head_h
        parts.append(f'<text x="0" y="{y-8}" font-size="11" font-family="{MONO}" font-weight="600" fill="{SOFT}" letter-spacing="0.08em">{esc(r[0].upper())}</text>')
        parts.append(f'<line x1="0" y1="{y-2}" x2="{W}" y2="{y-2}" stroke="{RULE}" stroke-width="1"/>')
        continue
    label, k, _ = r
    parts.append(f'<text x="0" y="{y+4}" font-size="12" fill="{INK}">{esc(label)}</text>')
    parts.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{RULE}" stroke-width="1"/>')
    parts.append(f'<line x1="{(x0+x1)/2}" y1="{y-5}" x2="{(x0+x1)/2}" y2="{y+5}" stroke="{RULE}" stroke-width="1"/>')
    pts = []
    for n in ORDER:
        pid = [i for i, nm in IDS.items() if nm == n][0]
        v = feat[pid][k]; p = pct(k, v)
        pts.append((p, n, v))
    pts.sort()
    # jitter overlapping dots vertically so all three stay visible
    placed = []
    for p, n, v in pts:
        cx = x0 + (x1 - x0) * p / 100
        dy = 0
        for (pcx, pdy) in placed:
            if abs(pcx - cx) < 12 and pdy == dy:
                dy = -7 if dy == 0 else (7 if dy == -7 else dy)
        placed.append((cx, dy))
        f = fmt.get(k, lambda v: f"{v:.2f}")
        parts.append(f'<circle cx="{cx:.1f}" cy="{y+dy}" r="6" fill="{COL[n]}" stroke="{PAPER}" stroke-width="2"/>')
    # value labels to the right, in text ink, keyed by order
    lbl = "  ".join(f"{n[0]} {fmt.get(k, lambda v: f'{v:.2f}')(v)}" for p, n, v in sorted(pts, key=lambda t: ORDER.index(t[1])))
    parts.append(f'<text x="{x1+14}" y="{y+4}" font-size="9" font-family="{MONO}" fill="{SOFT}">{esc(lbl)}</text>')
    y += row_h
source(parts, h, "Sources: MoneyPuck 2025-26 regular season; NHL stats API. C/F/K = Copp/Finnie/Kasper values.")
close(parts, "c1-profile-strip.svg")

# =====================================================================
# C2  Shot maps: half rink, dot size = xG, goals filled
# =====================================================================
pw = 236; ph = 268; gap = 18
h = 70 + ph + 70
parts = svg_open(h, "Where they shoot from, 2025-26 (all situations)",
                 "Every unblocked attempt. Dot area = expected-goal value; filled dots are goals. Attacking upward, goal line at the top.")
sx = pw / 85.0  # rink width 85ft across panel
def rink(ox, oy):
    g = [f'<rect x="{ox}" y="{oy}" width="{pw}" height="{ph}" rx="8" fill="{PANEL}" stroke="{RULE}"/>']
    # y-mapping: rink x from 25 (blue line) to 100 (end boards) mapped to panel bottom->top
    def m(x, y):  # x along ice (25..100), y across (-42.5..42.5)
        return ox + (y + 42.5) * sx, oy + ph - (x - 25) * (ph / 75.0)
    # blue line at x=25 (bottom edge), goal line at 89
    gl = m(89, 0)[1]
    g.append(f'<line x1="{ox}" y1="{gl:.1f}" x2="{ox+pw}" y2="{gl:.1f}" stroke="{RULE}" stroke-width="1.5"/>')
    # crease
    cx, cy = m(89, 0)
    g.append(f'<path d="M{cx-6*sx:.1f},{cy:.1f} A{6*sx:.1f},{6*sx:.1f} 0 0 1 {cx+6*sx:.1f},{cy:.1f}" fill="none" stroke="{RULE}" stroke-width="1.5"/>')
    # net
    g.append(f'<rect x="{cx-3*sx:.1f}" y="{cy-4*(ph/75):.1f}" width="{6*sx:.1f}" height="{4*(ph/75):.1f}" fill="none" stroke="{SOFT}" stroke-width="1.5"/>')
    # faceoff circles
    for yy in (-22, 22):
        fx, fy = m(69, yy)
        g.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="{15*sx:.1f}" fill="none" stroke="{RULE}" stroke-width="1"/>')
        g.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="2" fill="{RULE}"/>')
    # blue line
    g.append(f'<line x1="{ox}" y1="{oy+ph-1}" x2="{ox+pw}" y2="{oy+ph-1}" stroke="{RULE}" stroke-width="3"/>')
    return g, m
for i, n in enumerate(ORDER):
    ox = i * (pw + gap); oy = 56
    g, m = rink(ox, oy)
    parts += g
    rows_ = [s for s in shots[n] if s["x"] >= 25]
    for s in sorted(rows_, key=lambda s: s["goal"]):
        px, py = m(s["x"], s["y"])
        r = max(2.2, 2.2 + 12 * math.sqrt(s["xg"]))
        if s["goal"]:
            parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="{COL[n]}" stroke="{PAPER}" stroke-width="1.5"/>')
        else:
            parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="{COL[n]}" fill-opacity="0.22" stroke="{COL[n]}" stroke-opacity="0.7" stroke-width="1"/>')
    tot = len(shots[n]); xg = sum(s["xg"] for s in shots[n]); gl = sum(s["goal"] for s in shots[n])
    d = sorted(s["dist"] for s in shots[n]); med = d[len(d) // 2]
    w20 = 100 * sum(1 for s in shots[n] if s["dist"] <= 20) / tot
    parts.append(f'<circle cx="{ox+8}" cy="{oy+ph+16}" r="5" fill="{COL[n]}"/>')
    parts.append(f'<text x="{ox+18}" y="{oy+ph+20}" font-size="12.5" font-weight="600" fill="{INK}">{n}</text>')
    parts.append(f'<text x="{ox}" y="{oy+ph+36}" font-size="10.5" font-family="{MONO}" fill="{SOFT}">{tot} att · {xg:.1f} xG · {gl} G ({gl-xg:+.1f})</text>')
    parts.append(f'<text x="{ox}" y="{oy+ph+50}" font-size="10.5" font-family="{MONO}" fill="{SOFT}">median {med:.0f} ft · {w20:.0f}% inside 20 ft</text>')
parts.append(f'<text x="{W}" y="{h-22}" font-size="10.5" font-family="{MONO}" fill="{MUTED}" text-anchor="end">League forwards: median 25 ft · 40% inside 20 ft</text>')
source(parts, h, "Source: MoneyPuck shot data, 2025-26 regular season (unblocked attempts; xG model is MoneyPuck's).")
close(parts, "c2-shot-maps.svg")

# =====================================================================
# C3  Finishing scatter: ixG vs goals, all forwards, three highlighted
# =====================================================================
mp = {r["playerId"]: r for r in csv.DictReader(open(RAW / "mp_skaters_2025.csv")) if r["situation"] == "all"}
pts = []
for pid in P:
    r = mp[pid]
    pts.append((float(r["I_F_xGoals"]), float(r["I_F_goals"]), IDS.get(pid), r["name"]))
h = 470
parts = svg_open(h, "Chances in, goals out: the three all finished under their xG",
                 "384 NHL forwards, 2025-26, all situations. Diagonal = scored exactly what the chances were worth.")
legend(parts, 0, 58)
mx = 60; my = 70; pwid = W - mx - 20; phgt = 330
xmax = 40; ymax = 55
def X(v): return mx + pwid * v / xmax
def Y(v): return my + phgt - phgt * v / ymax
for t in range(0, 41, 10):
    parts.append(f'<line x1="{X(t):.1f}" y1="{my}" x2="{X(t):.1f}" y2="{my+phgt}" stroke="{RULE}" stroke-width="1"/>')
    parts.append(f'<text x="{X(t):.1f}" y="{my+phgt+16}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="middle">{t}</text>')
for t in range(0, 56, 10):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pwid}" y2="{Y(t):.1f}" stroke="{RULE}" stroke-width="1"/>')
    parts.append(f'<text x="{mx-8}" y="{Y(t)+4:.1f}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="end">{t}</text>')
parts.append(f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(40)}" y2="{Y(40)}" stroke="{SOFT}" stroke-width="1.5" stroke-dasharray="4 4"/>')
parts.append(f'<text x="{X(38)}" y="{Y(38)-8}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="end">goals = xG</text>')
parts.append(f'<text x="{mx+pwid/2}" y="{my+phgt+34}" font-size="11.5" fill="{SOFT}" text-anchor="middle">Individual expected goals</text>')
parts.append(f'<text transform="translate(14,{my+phgt/2}) rotate(-90)" font-size="11.5" fill="{SOFT}" text-anchor="middle">Goals</text>')
for xg, g, who, name in pts:
    if who is None:
        parts.append(f'<circle cx="{X(xg):.1f}" cy="{Y(g):.1f}" r="3.5" fill="{GRAY}" fill-opacity="0.7"/>')
for xg, g, who, name in pts:
    if who:
        parts.append(f'<circle cx="{X(xg):.1f}" cy="{Y(g):.1f}" r="7" fill="{COL[who]}" stroke="{PAPER}" stroke-width="2"/>')
        dx, dy, anchor = {"Finnie": (12, -6, "start"), "Copp": (12, 18, "start"), "Kasper": (-12, 4, "end")}[who]
        parts.append(f'<text x="{X(xg)+dx:.1f}" y="{Y(g)+dy:.1f}" font-size="12" font-weight="600" fill="{INK}" text-anchor="{anchor}">{who} · {xg:.1f} xG, {int(g)} G</text>')
source(parts, h, "Source: MoneyPuck 2025-26 regular season. Copp -10.8 is the largest shortfall of any NHL forward.")
close(parts, "c3-finishing-scatter.svg")

# =====================================================================
# C4  Distance to the trio centroid: DET forwards + league median
# =====================================================================
cent = json.load(open(RAW / "centroid_2025.json"))
det = sorted(cent["det"].items(), key=lambda t: t[1])
h = 90 + 26 * len(det) + 64
parts = svg_open(h, "How close each Red Wings forward plays to the Copp-Finnie-Kasper 'type'",
                 "Style distance to the trio's centroid across 17 rate/usage metrics (z-scored vs. all NHL forwards). Shorter bar = more alike.")
mx = 170; bw = W - mx - 90; vmax = 1.5
y = 62
med = cent["median"]
parts.append(f'<line x1="{mx + bw*med/vmax:.1f}" y1="{y-6}" x2="{mx + bw*med/vmax:.1f}" y2="{y + 26*len(det)}" stroke="{SOFT}" stroke-width="1" stroke-dasharray="3 3"/>')
parts.append(f'<text x="{mx + bw*med/vmax + 4:.1f}" y="{y-8}" font-size="10.5" font-family="{MONO}" fill="{SOFT}">league median</text>')
for name, d in det:
    short = name.split()[-1] if name not in ("James van Riemsdyk",) else "van Riemsdyk"
    c = COL.get(short, GRAY)
    parts.append(f'<text x="{mx-10}" y="{y+15}" font-size="12" fill="{INK}" text-anchor="end">{esc(name)}</text>')
    wpx = bw * d / vmax
    parts.append(f'<path d="M{mx},{y} h{wpx-4:.1f} a4,4 0 0 1 4,4 v14 a4,4 0 0 1 -4,4 h-{wpx-4:.1f} z" fill="{c}"/>')
    parts.append(f'<text x="{mx+wpx+8:.1f}" y="{y+15}" font-size="11" font-family="{MONO}" fill="{SOFT}">{d:.2f}</text>')
    y += 26
legend(parts, 0, y + 22)
parts.append(f'<text x="0" y="{h-22}" font-size="10.5" font-family="{MONO}" fill="{MUTED}">Source: MoneyPuck 2025-26; forwards with 41+ GP. Metrics: TOI, ixG/60, shots and attempts/60, HD share, hits,</text>')
source(parts, h, "takeaways, giveaways, blocks, penalties drawn/taken, OZ starts, faceoffs, A1/60, rebounds, on-ice xGF and xGA per 60.")
close(parts, "c4-centroid-bars.svg")

# =====================================================================
# C5  Distribution of same-team forward trios; DET trio marked
# =====================================================================
style = sim["style_dims"]
mu = {k: sum(feat[p][k] for p in P) / len(P) for k in style}
sd = {k: (sum((feat[p][k] - mu[k]) ** 2 for p in P) / len(P)) ** .5 for k in style}
z = {p: {k: (feat[p][k] - mu[k]) / sd[k] for k in style} for p in P}
def dist(a, b): return math.sqrt(sum((z[a][k] - z[b][k]) ** 2 for k in style) / len(style))
teams = {}
for p in P: teams.setdefault(feat[p]["team"], []).append(p)
tri = ["8477429", "8484471", "8483464"]
tri_d = (dist(tri[0], tri[1]) + dist(tri[0], tri[2]) + dist(tri[1], tri[2])) / 3
vals = []
for t, ps in teams.items():
    for a, b, c in combinations(ps, 3):
        vals.append((dist(a, b) + dist(a, c) + dist(b, c)) / 3)
vals.sort()
rank_pct = 100 * sum(1 for v in vals if v < tri_d) / len(vals)
bins = [0.6 + 0.05 * i for i in range(30)]
counts = [0] * (len(bins) - 1)
for v in vals:
    for i in range(len(bins) - 1):
        if bins[i] <= v < bins[i + 1]: counts[i] += 1; break
h = 360
parts = svg_open(h, "Is a trio this alike unusual? Yes.",
                 f"Average style distance for all {len(vals):,} same-team forward trios in the NHL, 2025-26. The Red Wings trio is at the {rank_pct:.1f}th percentile.")
mx = 50; my = 60; pwid = W - mx - 20; phgt = 230
cmax = max(counts)
bwid = pwid / len(counts)
for i, c in enumerate(counts):
    x = mx + i * bwid; hh = phgt * c / cmax
    lo = bins[i]
    col = GRAY
    parts.append(f'<rect x="{x+1:.1f}" y="{my+phgt-hh:.1f}" width="{bwid-2:.1f}" height="{hh:.1f}" fill="{col}"/>')
for t in (0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0):
    x = mx + pwid * (t - 0.6) / 1.5
    parts.append(f'<text x="{x:.1f}" y="{my+phgt+16}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="middle">{t:.1f}</text>')
xd = mx + pwid * (tri_d - 0.6) / 1.5
parts.append(f'<line x1="{xd:.1f}" y1="{my-4}" x2="{xd:.1f}" y2="{my+phgt}" stroke="{COL["Copp"]}" stroke-width="2"/>')
parts.append(f'<text x="{xd+8:.1f}" y="{my+12}" font-size="12" font-weight="600" fill="{INK}">Copp / Finnie / Kasper: {tri_d:.2f}</text>')
parts.append(f'<text x="{xd+8:.1f}" y="{my+28}" font-size="11" fill="{SOFT}">closer than {100-rank_pct:.0f}% of same-team trios</text>')
medv = vals[len(vals) // 2]; xm = mx + pwid * (medv - 0.6) / 1.5
parts.append(f'<line x1="{xm:.1f}" y1="{my+phgt}" x2="{xm:.1f}" y2="{my+40}" stroke="{SOFT}" stroke-width="1" stroke-dasharray="3 3"/>')
parts.append(f'<text x="{xm+6:.1f}" y="{my+52}" font-size="11" font-family="{MONO}" fill="{SOFT}">median {medv:.2f}</text>')
parts.append(f'<text x="{mx+pwid/2}" y="{my+phgt+36}" font-size="11.5" fill="{SOFT}" text-anchor="middle">Mean pairwise style distance within the trio (z-score RMS, lower = more alike)</text>')
source(parts, h, "Source: MoneyPuck 2025-26; 17 usage/rate metrics; forwards with 41+ GP and 500+ 5v5 minutes.")
close(parts, "c5-trio-distribution.svg")

# =====================================================================
# C6  Kasper 2024-25 -> 2025-26 dumbbell: process vs. finishing
# =====================================================================
rows24 = {r["playerId"]: r for r in csv.DictReader(open(RAW / "mp_skaters_2024.csv")) if r["situation"] == "5on5"}
rows25 = {r["playerId"]: r for r in csv.DictReader(open(RAW / "mp_skaters_2025.csv")) if r["situation"] == "5on5"}
a24 = {r["playerId"]: r for r in csv.DictReader(open(RAW / "mp_skaters_2024.csv")) if r["situation"] == "all"}
a25 = {r["playerId"]: r for r in csv.DictReader(open(RAW / "mp_skaters_2025.csv")) if r["situation"] == "all"}
K = "8483464"
def p60(r, c): return float(r[c]) / float(r["icetime"]) * 3600
metrics = [
    ("Shot attempts / 60 (5v5)", p60(rows24[K], "I_F_shotAttempts"), p60(rows25[K], "I_F_shotAttempts"), "{:.1f}"),
    ("Individual xG / 60 (5v5)", p60(rows24[K], "I_F_xGoals"), p60(rows25[K], "I_F_xGoals"), "{:.2f}"),
    ("Hits / 60", p60(a24[K], "I_F_hits"), p60(a25[K], "I_F_hits"), "{:.1f}"),
    ("On-ice xG share (5v5)", 100 * float(rows24[K]["onIce_xGoalsPercentage"]), 100 * float(rows25[K]["onIce_xGoalsPercentage"]), "{:.0f}%"),
    ("Time on ice / game (min)", float(a24[K]["icetime"]) / float(a24[K]["games_played"]) / 60, float(a25[K]["icetime"]) / float(a25[K]["games_played"]) / 60, "{:.1f}"),
    ("Shooting % (all situations)", 100 * float(a24[K]["I_F_goals"]) / float(a24[K]["I_F_shotsOnGoal"]), 100 * float(a25[K]["I_F_goals"]) / float(a25[K]["I_F_shotsOnGoal"]), "{:.1f}%"),
    ("On-ice shooting % (5v5)", 100 * float(rows24[K]["OnIce_F_goals"]) / float(rows24[K]["OnIce_F_shotsOnGoal"]), 100 * float(rows25[K]["OnIce_F_goals"]) / float(rows25[K]["OnIce_F_shotsOnGoal"]), "{:.1f}%"),
    ("Points", float(a24[K]["I_F_points"]), float(a25[K]["I_F_points"]), "{:.0f}"),
]
h = 80 + 34 * len(metrics) + 40
parts = svg_open(h, "Kasper's slump was finishing, not process",
                 "2024-25 (hollow) to 2025-26 (filled). Each row is on its own scale; the bar shows direction and size of change.")
mx = 210; bw = W - mx - 150
y = 66
for label, v0, v1, f in metrics:
    lo, hi = min(v0, v1), max(v0, v1)
    span = max(hi - lo, 1e-9); pad = span * 0.6
    smin, smax = lo - pad, hi + pad
    def X(v): return mx + bw * (v - smin) / (smax - smin)
    parts.append(f'<text x="{mx-12}" y="{y+4}" font-size="12" fill="{INK}" text-anchor="end">{esc(label)}</text>')
    parts.append(f'<line x1="{X(v0):.1f}" y1="{y}" x2="{X(v1):.1f}" y2="{y}" stroke="{COL["Kasper"]}" stroke-width="3" stroke-linecap="round"/>')
    parts.append(f'<circle cx="{X(v0):.1f}" cy="{y}" r="6" fill="{PAPER}" stroke="{COL["Kasper"]}" stroke-width="2.5"/>')
    parts.append(f'<circle cx="{X(v1):.1f}" cy="{y}" r="6" fill="{COL["Kasper"]}" stroke="{PAPER}" stroke-width="2"/>')
    parts.append(f'<text x="{mx+bw+14}" y="{y+4}" font-size="11" font-family="{MONO}" fill="{SOFT}">{f.format(v0)} → {f.format(v1)}</text>')
    y += 34
parts.append(f'<circle cx="{8}" cy="{y+8}" r="5" fill="{PAPER}" stroke="{COL["Kasper"]}" stroke-width="2"/>')
parts.append(f'<text x="18" y="{y+12}" font-size="11.5" fill="{INK}">2024-25</text>')
parts.append(f'<circle cx="{88}" cy="{y+8}" r="5" fill="{COL["Kasper"]}"/>')
parts.append(f'<text x="98" y="{y+12}" font-size="11.5" fill="{INK}">2025-26</text>')
source(parts, h, "Source: MoneyPuck. 5v5 rates use 5v5 ice time; hits and shooting % are all situations.")
close(parts, "c6-kasper-dumbbell.svg")

# =====================================================================
# C7  Copp career arc: hits/60 and HD share by season, plus xGF%
# =====================================================================
seasons = [2021, 2022, 2023, 2024, 2025]
C = "8477429"
series = {"hd": [], "xgf": [], "toi": []}
for s in seasons:
    rs = list(csv.DictReader(open(RAW / f"mp_skaters_{s}.csv")))
    e = [r for r in rs if r["playerId"] == C and r["situation"] == "5on5"]
    a = [r for r in rs if r["playerId"] == C and r["situation"] == "all"]
    e = e[0]; a = a[0]
    series["hd"].append(float(e["I_F_highDangerShots"]) / max(1, float(e["I_F_shotAttempts"])))
    series["xgf"].append(float(e["onIce_xGoalsPercentage"]))
    series["toi"].append(float(a["icetime"]) / float(a["games_played"]) / 60)
h = 300
parts = svg_open(h, "Copp's last five seasons: usage stayed, the chance profile sharpened",
                 "5v5 on-ice xG share and high-danger share of his own attempts, 2021-22 through 2025-26.")
mx = 60; my = 62; pwid = W - mx - 30; phgt = 170
def Xs(i): return mx + pwid * i / (len(seasons) - 1)
def Yp(v): return my + phgt - phgt * v / 0.6
for t in (0, 0.2, 0.4, 0.6):
    parts.append(f'<line x1="{mx}" y1="{Yp(t):.1f}" x2="{mx+pwid}" y2="{Yp(t):.1f}" stroke="{RULE}" stroke-width="1"/>')
    parts.append(f'<text x="{mx-8}" y="{Yp(t)+4:.1f}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="end">{int(t*100)}%</text>')
for i, s in enumerate(seasons):
    lab = f"{s}-{str(s+1)[2:]}" + (" (NYR/WPG)" if s == 2021 else "")
    parts.append(f'<text x="{Xs(i):.1f}" y="{my+phgt+18}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="middle">{lab}</text>')
for key, col, name in (("xgf", COL["Copp"], "On-ice xG share (5v5)"), ("hd", SOFT, "High-danger share of own attempts")):
    d = " ".join(f"{'M' if i==0 else 'L'}{Xs(i):.1f},{Yp(v):.1f}" for i, v in enumerate(series[key]))
    parts.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    for i, v in enumerate(series[key]):
        parts.append(f'<circle cx="{Xs(i):.1f}" cy="{Yp(v):.1f}" r="4.5" fill="{col}" stroke="{PAPER}" stroke-width="2"/>')
    parts.append(f'<text x="{Xs(len(seasons)-1)+8:.1f}" y="{Yp(series[key][-1])+4:.1f}" font-size="11" font-family="{MONO}" fill="{INK}" text-anchor="start">{int(round(series[key][-1]*100))}%</text>')
    parts.append(f'<text x="{Xs(0)-4:.1f}" y="{Yp(series[key][0])-10:.1f}" font-size="11" font-family="{MONO}" fill="{INK}" text-anchor="start">{int(round(series[key][0]*100))}%</text>')
lx = mx
parts.append(f'<line x1="{lx}" y1="{h-30}" x2="{lx+18}" y2="{h-30}" stroke="{COL["Copp"]}" stroke-width="2"/>')
parts.append(f'<text x="{lx+24}" y="{h-26}" font-size="11.5" fill="{INK}">On-ice xG share (5v5)</text>')
parts.append(f'<line x1="{lx+200}" y1="{h-30}" x2="{lx+218}" y2="{h-30}" stroke="{SOFT}" stroke-width="2"/>')
parts.append(f'<text x="{lx+224}" y="{h-26}" font-size="11.5" fill="{INK}">High-danger share of own attempts</text>')
source(parts, h, "Source: MoneyPuck. 2021-22 split between Winnipeg and the Rangers; 2024-25 was a 56-game season.")
close(parts, "c7-copp-arc.svg")

print("done")

# =====================================================================
# C8  Evolving Hockey RAPM: isolated 5v5/EV xG impact, league cloud
# =====================================================================
EH = ROOT / "raw" / "eh"
rapm = [r for r in csv.DictReader(open(EH / "rapm_ev_rates_2025.csv")) if r["Position"] in ("C", "L", "R") and float(r["GP"]) >= 41]
h = 470
parts = svg_open(h, "Isolated even-strength impact (Evolving Hockey RAPM), 2025-26",
                 "388 NHL forwards, 41+ GP. Teammates, competition, zone starts and score regressed out. Up-right = creates and suppresses.")
legend(parts, 0, 58)
mx = 70; my = 70; pwid = W - mx - 20; phgt = 330
xs = [float(r["xGF/60"]) for r in rapm]; ys = [-float(r["xGA/60"]) for r in rapm]
xmin, xmax = -0.45, 0.45; ymin, ymax = -0.35, 0.35
def X(v): return mx + pwid * (v - xmin) / (xmax - xmin)
def Y(v): return my + phgt - phgt * (v - ymin) / (ymax - ymin)
for t in (-0.4, -0.2, 0, 0.2, 0.4):
    parts.append(f'<line x1="{X(t):.1f}" y1="{my}" x2="{X(t):.1f}" y2="{my+phgt}" stroke="{RULE if t else SOFT}" stroke-width="1"/>')
    parts.append(f'<text x="{X(t):.1f}" y="{my+phgt+16}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="middle">{t:+.1f}</text>')
for t in (-0.3, -0.15, 0, 0.15, 0.3):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pwid}" y2="{Y(t):.1f}" stroke="{RULE if t else SOFT}" stroke-width="1"/>')
    parts.append(f'<text x="{mx-8}" y="{Y(t)+4:.1f}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="end">{t:+.2f}</text>')
parts.append(f'<text x="{mx+pwid/2}" y="{my+phgt+34}" font-size="11.5" fill="{SOFT}" text-anchor="middle">RAPM xGF/60 (offense created, per 60)</text>')
parts.append(f'<text transform="translate(16,{my+phgt/2}) rotate(-90)" font-size="11.5" fill="{SOFT}" text-anchor="middle">RAPM xGA/60, sign flipped (defense, higher = better)</text>')
for r in rapm:
    if r["Player"] not in ("Andrew Copp", "Emmitt Finnie", "Marco Kasper"):
        parts.append(f'<circle cx="{X(float(r["xGF/60"])):.1f}" cy="{Y(-float(r["xGA/60"])):.1f}" r="3.5" fill="{GRAY}" fill-opacity="0.7"/>')
lab = {"Andrew Copp": ("Copp", 12, -8, "start"), "Emmitt Finnie": ("Finnie", 12, 16, "start"), "Marco Kasper": ("Kasper", 12, -8, "start")}
for r in rapm:
    if r["Player"] in lab:
        n, dx, dy, an = lab[r["Player"]]
        x = X(float(r["xGF/60"])); y = Y(-float(r["xGA/60"]))
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{COL[n]}" stroke="{PAPER}" stroke-width="2"/>')
        parts.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" font-size="12" font-weight="600" fill="{INK}" text-anchor="{an}">{n} · {float(r["xGF/60"]):+.2f} / {-float(r["xGA/60"]):+.2f}</text>')
source(parts, h, "Source: Evolving Hockey RAPM skater tables, EV rates, 2025-26 regular season (pulled 2026-09-02).")
close(parts, "c8-eh-rapm.svg")

# =====================================================================
# C9  GAR vs xGAR: what the results said vs what the chances said
# =====================================================================
gar = {r["Player"]: r for r in csv.DictReader(open(EH / "gar_sk_2025.csv"))}
xgar = {r["Player"]: r for r in csv.DictReader(open(EH / "xgar_sk_2025.csv"))}
names = [("Andrew Copp", "Copp"), ("Emmitt Finnie", "Finnie"), ("Marco Kasper", "Kasper")]
comps = [("Even-strength offense", "EVO_GAR", "xEVO_GAR"), ("Even-strength defense", "EVD_GAR", "xEVD_GAR"), ("Power play", "PPO_GAR", "xPPO_GAR"),
         ("Penalty kill", "SHD_GAR", "xSHD_GAR"), ("Penalties, net", "Pens_GAR", "Pens_GAR"), ("Total GAR", "GAR", "xGAR")]
h = 90 + len(comps) * 3 * 18 + len(comps) * 14 + 50
parts = svg_open(h, "Goals above replacement: results (filled) vs. expected (hollow)",
                 "Evolving Hockey GAR and xGAR components, 2025-26. A filled dot far from its hollow twin is finishing luck, good or bad.")
legend(parts, 0, 58)
mx = 250; bw = W - mx - 30; vmin, vmax = -6, 12
def X(v): return mx + bw * (v - vmin) / (vmax - vmin)
y = 74
for t in (-5, 0, 5, 10):
    parts.append(f'<line x1="{X(t):.1f}" y1="{y-6}" x2="{X(t):.1f}" y2="{h-50}" stroke="{RULE if t else SOFT}" stroke-width="1"/>')
    parts.append(f'<text x="{X(t):.1f}" y="{y-10}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="middle">{t:+d}</text>')
for label, gk, xk in comps:
    parts.append(f'<text x="0" y="{y+12}" font-size="12" font-weight="600" fill="{INK}">{esc(label)}</text>')
    yy = y
    for full, n in names:
        g = float(gar[full][gk]); xg = float(xgar[full][xk])
        parts.append(f'<line x1="{X(min(g,xg)):.1f}" y1="{yy+8}" x2="{X(max(g,xg)):.1f}" y2="{yy+8}" stroke="{COL[n]}" stroke-width="2" stroke-opacity="0.6"/>')
        parts.append(f'<circle cx="{X(xg):.1f}" cy="{yy+8}" r="5" fill="{PAPER}" stroke="{COL[n]}" stroke-width="2"/>')
        parts.append(f'<circle cx="{X(g):.1f}" cy="{yy+8}" r="5" fill="{COL[n]}" stroke="{PAPER}" stroke-width="1.5"/>')
        parts.append(f'<text x="{mx-10}" y="{yy+12}" font-size="10.5" font-family="{MONO}" fill="{SOFT}" text-anchor="end">{n} {g:+.1f} / {xg:+.1f}</text>')
        yy += 18
    y = yy + 14
parts.append(f'<circle cx="8" cy="{h-34}" r="5" fill="{INK}"/><text x="18" y="{h-30}" font-size="11.5" fill="{INK}">GAR (actual goals)</text>')
parts.append(f'<circle cx="150" cy="{h-34}" r="5" fill="{PAPER}" stroke="{INK}" stroke-width="2"/><text x="160" y="{h-30}" font-size="11.5" fill="{INK}">xGAR (expected goals)</text>')
source(parts, h, "Source: Evolving Hockey GAR / xGAR skater tables, 2025-26 regular season. Penalty component is identical in both models.")
close(parts, "c9-eh-gar-xgar.svg")
