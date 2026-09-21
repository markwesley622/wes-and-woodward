#!/usr/bin/env python3
"""Inline-ready SVG charts for the Wes & Woodward Söderblom column.
Dependency-free; regenerates every chart from ../raw/. Tokens and helpers mirror
research/rasmussen/charts/make_charts.py. Palette (validated on paper #d7d6d3):
Detroit stint #ce1126, Pittsburgh stint #c98500, league / median #b3b1ad, third series #2a78d6."""
import json, math, csv, pathlib, statistics as st
ROOT = pathlib.Path(__file__).resolve().parents[1]; RAW = ROOT / "raw"; OUT = ROOT / "charts"
PAPER = "#d7d6d3"; PANEL = "#e7e6e3"; RULE = "#c4c3bf"; INK = "#141414"; SOFT = "#575653"; MUTED = "#8a8781"
RED = "#ce1126"; GRAY = "#b3b1ad"; BLUE = "#2a78d6"; AMBER = "#c98500"
DET = RED; PIT = AMBER
SANS = "'Space Grotesk', ui-sans-serif, system-ui, sans-serif"; MONO = "'IBM Plex Mono', ui-monospace, monospace"; W = 760

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def ordinal(n):
    n = int(round(n)); suf = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"); return f"{n}{suf}"
def guard(text, size, is_mono, x=0):
    est = x + len(text) * size * (0.62 if is_mono else 0.56)
    if est > W: print(f"  WARN width {est:.0f}px > {W}: {text[:60]}...")
def svg_open(h, title, sub=None):
    guard(title, 17, False)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{esc(title)}" font-family="{SANS}" style="max-width:100%;height:auto;background:{PAPER}">',
             f'<rect width="{W}" height="{h}" fill="{PAPER}"/>', f'<text x="0" y="20" font-size="17" font-weight="600" fill="{INK}">{esc(title)}</text>']
    if sub: guard(sub, 12, False); parts.append(f'<text x="0" y="38" font-size="12" fill="{SOFT}">{esc(sub)}</text>')
    return parts
def legend(parts, x, y, items):
    cx = x
    for n, c, stl in items:
        if stl == "dot": parts.append(f'<circle cx="{cx+5}" cy="{y-4}" r="5" fill="{c}"/>')
        elif stl == "hollow": parts.append(f'<circle cx="{cx+5}" cy="{y-4}" r="4.5" fill="{PAPER}" stroke="{c}" stroke-width="2"/>')
        elif stl == "line": parts.append(f'<line x1="{cx-2}" y1="{y-4}" x2="{cx+12}" y2="{y-4}" stroke="{c}" stroke-width="2.5"/>')
        elif stl == "dash": parts.append(f'<line x1="{cx-2}" y1="{y-4}" x2="{cx+12}" y2="{y-4}" stroke="{c}" stroke-width="2" stroke-dasharray="4 3"/>')
        else: parts.append(f'<rect x="{cx}" y="{y-10}" width="11" height="11" rx="2" fill="{c}"/>')
        parts.append(f'<text x="{cx+16}" y="{y}" font-size="12" fill="{INK}">{esc(n)}</text>'); cx += 16 + 7 * len(n) + 22
    return cx
def source(parts, h, text):
    guard(text, 10.5, True); parts.append(f'<text x="0" y="{h-8}" font-size="10.5" font-family="{MONO}" fill="{MUTED}">{esc(text)}</text>')
def close(parts, name): parts.append("</svg>"); (OUT / name).write_text("\n".join(parts)); print("wrote", name)
def mono(parts, x, y, s, size=10.5, fill=SOFT, anchor="start", weight=None, halo=False):
    w = f' font-weight="{weight}"' if weight else ""; hl = f' stroke="{PAPER}" stroke-width="3" paint-order="stroke"' if halo else ""
    parts.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-family="{MONO}" fill="{fill}" text-anchor="{anchor}"{w}{hl}>{esc(s)}</text>')
def sans(parts, x, y, s, size=12, fill=INK, anchor="start", weight=None):
    if anchor == "start": guard(s, size, False, x)
    w = f' font-weight="{weight}"' if weight else ""
    parts.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}>{esc(s)}</text>')

# ---- data ----
S = json.load(open(RAW / "onice_splits.json")); PCT = S["_percentiles_vs_forwards_300min"]; MED = S["_league_medians"]
games = sorted(json.load(open(RAW / "per_game.json")), key=lambda g: g["date"])
luck = json.load(open(RAW / "luck_test.json")); eh = json.load(open(RAW / "eh_soderblom.json"))
EHS = json.load(open(RAW / "eh_standard_2025.json")); comps = json.load(open(RAW / "age_comps.json")); pick = json.load(open(RAW / "draft" / "pick_value_summary.json"))
det_sched = [g for g in json.load(open(RAW / "nhl" / "det_schedule.json"))["games"] if g["gameType"] == 2 and g["gameDate"] <= "2026-03-06"]
pit_sched = [g for g in json.load(open(RAW / "nhl" / "pit_schedule.json"))["games"] if g["gameType"] == 2 and g["gameDate"] >= "2026-03-07"]
K_DET = "2025-26 DET"; K_PIT = "2025-26 PIT"

# =====================================================================
# C1  2025-26 game by game: TOI per team game (scratches as empty slots) + cumulative goals vs ixG
# =====================================================================
h = 470; parts = svg_open(h, "2025-26 game by game: 10 minutes in Detroit, 12 in Pittsburgh",
                          "Bars = ice time in every team game (empty slot = did not dress). Below: cumulative goals vs expected goals.")
slots = [("DET", g["gameDate"]) for g in det_sched] + [("PIT", g["gameDate"]) for g in pit_sched]
played = {g["date"]: g for g in games if g["gtype"] == 2 and g["date"] >= "2025-10-01"}
mx, my, pw, ph = 46, 60, W - 60, 150; n = len(slots); sw = pw / n
ymax = 16
def Y1(v): return my + ph - ph * v / ymax
for v in (0, 4, 8, 12, 16):
    parts.append(f'<line x1="{mx}" y1="{Y1(v):.1f}" x2="{mx+pw}" y2="{Y1(v):.1f}" stroke="{RULE}" stroke-width="{1.2 if v==0 else 0.6}"/>'); mono(parts, mx - 6, Y1(v) + 4, f"{v}", anchor="end")
# injury shading: Nov 23-26 IR, Dec 23 - Jan 8 (8 games)
inj = {"2025-11-24", "2025-11-22", "2025-12-23", "2025-12-28", "2025-12-31", "2026-01-01", "2026-01-03", "2026-01-05", "2026-01-08"}
for i, (tm, d) in enumerate(slots):
    x = mx + i * sw
    if d in played:
        g = played[d]; col = DET if tm == "DET" else PIT
        parts.append(f'<rect x="{x+0.6:.1f}" y="{Y1(g["toi"]):.1f}" width="{sw-1.2:.1f}" height="{Y1(0)-Y1(g["toi"]):.1f}" fill="{col}"/>')
        if g["g"]: 
            for k in range(g["g"]): parts.append(f'<circle cx="{x+sw/2:.1f}" cy="{Y1(g["toi"])-7-8*k:.1f}" r="2.6" fill="{INK}"/>')
    else:
        parts.append(f'<rect x="{x+0.6:.1f}" y="{Y1(0)-3}" width="{sw-1.2:.1f}" height="3" fill="{BLUE if d in inj else MUTED}"/>')
tx = mx + len(det_sched) * sw
parts.append(f'<line x1="{tx:.1f}" y1="{my-4}" x2="{tx:.1f}" y2="{Y1(0)+4}" stroke="{INK}" stroke-width="1.2" stroke-dasharray="4 3"/>')
mono(parts, tx - 5, my + 8, "traded Mar 6", anchor="end", fill=INK, weight="600")
mono(parts, mx, my - 6, "minutes", size=10)
legend(parts, mx + 8, my + 8, [("Detroit", DET, "bar"), ("Pittsburgh", PIT, "bar")])
legend(parts, mx, Y1(0) + 18, [("scratched", MUTED, "bar"), ("injured / IR", BLUE, "bar"), ("goal", INK, "dot")])
mono(parts, mx + pw, Y1(0) + 18, f"DET: 39 of 63 games, 10:41 avg  |  PIT: 20 of 21, 11:57 avg", anchor="end", fill=INK)
# lower: cumulative goals vs ixG over games played
my2 = 270; ph2 = 140; seq = [g for g in games if g["gtype"] == 2 and g["date"] >= "2025-10-01"]
cg = cx = 0; ptsG = []; ptsX = []
for i, g in enumerate(seq):
    cg += g["g"]; cx += g["ixg"]; ptsG.append((i, cg)); ptsX.append((i, cx))
ymax2 = 9; sw2 = pw / len(seq)
def Y2(v): return my2 + ph2 - ph2 * v / ymax2
def X2(i): return mx + (i + 0.5) * sw2
for v in (0, 3, 6, 9):
    parts.append(f'<line x1="{mx}" y1="{Y2(v):.1f}" x2="{mx+pw}" y2="{Y2(v):.1f}" stroke="{RULE}" stroke-width="{1.2 if v==0 else 0.6}"/>'); mono(parts, mx - 6, Y2(v) + 4, f"{v}", anchor="end")
tx2 = mx + 39 * sw2
parts.append(f'<line x1="{tx2:.1f}" y1="{my2-4}" x2="{tx2:.1f}" y2="{Y2(0)}" stroke="{INK}" stroke-width="1.2" stroke-dasharray="4 3"/>')
parts.append('<path d="M' + " L".join(f"{X2(i):.1f},{Y2(v):.1f}" for i, v in ptsX) + f'" fill="none" stroke="{GRAY}" stroke-width="2.5"/>')
parts.append('<path d="M' + " L".join(f"{X2(i):.1f},{Y2(v):.1f}" for i, v in ptsG) + f'" fill="none" stroke="{INK}" stroke-width="2.5"/>')
mono(parts, mx, my2 - 6, "cumulative, games played (regular season)", size=10)
mono(parts, X2(38) - 4, Y2(2) - 6, "DET: 2 goals on 4.7 expected", anchor="end", fill=DET, weight="600", halo=True)
mono(parts, X2(52), Y2(6.6), "PIT: 5 on 3.3", anchor="end", fill=PIT, weight="600", halo=True)
mono(parts, X2(58) + 2, Y2(8.0) - 6, "ixG 7.9", anchor="end", fill=SOFT, halo=True)
legend(parts, mx, Y2(0) + 18, [("goals", INK, "line"), ("expected goals (MoneyPuck)", GRAY, "line")])
mono(parts, mx + pw, Y2(0) + 18, "last 10 Detroit games: 0 points, 0.7 ixG total", anchor="end", fill=INK)
source(parts, h, "NHL API game logs + schedules; MoneyPuck shot file 2025-26. Regular season only.")
close(parts, "c1-season-timeline.svg")

# =====================================================================
# C2  Deployment dumbbells: DET vs PIT with league percentiles
# =====================================================================
rowsD = [("5v5 minutes per game", "toi5_gp", "min", "toi5_gp", MED["toi"]),
         ("Share of team power-play time", "pp_share", "%", None, None),
         ("Offensive-zone faceoff share (5v5)", "ozs_pct", "%", "ozf", 50.0),
         ("Opponent forwards' 5v5 TOI/GP (QoC)", "qoc_f", "min", None, None),
         ("Linemate forwards' 5v5 TOI/GP (QoT)", "qot_f", "min", None, None),
         ("Shifts per game", "shifts_gp", "", None, None)]
h = 60 + 46 * len(rowsD) + 40; parts = svg_open(h, "Deployment: more minutes in Pittsburgh, and the league's hardest zone starts",
                                                 "Detroit (39 GP) vs Pittsburgh (20 GP), 2025-26, 5v5 unless noted. Percentiles vs NHL forwards (EH, 150+ min).")
lx = 300; rx = W - 20; y0 = 70
for i, (lab, key, unit, pk, med) in enumerate(rowsD):
    y = y0 + 46 * i; a = S[K_DET][key]; b = S[K_PIT][key]
    parts.append(f'<line x1="0" y1="{y+20}" x2="{W}" y2="{y+20}" stroke="{RULE}" stroke-width="0.6"/>')
    sans(parts, 0, y + 4, lab, 12, INK, weight="600")
    lo = min(a, b, med if med else a); hi = max(a, b, med if med else b); span = max(hi - lo, 1e-6); pad = span * 0.6 + (0.5 if unit == "min" else 3)
    def X(v): return lx + (rx - lx) * (v - (lo - pad)) / ((hi + pad) - (lo - pad))
    if med is not None:
        parts.append(f'<line x1="{X(med):.1f}" y1="{y-10}" x2="{X(med):.1f}" y2="{y+12}" stroke="{GRAY}" stroke-width="2"/>'); mono(parts, X(med), y - 13, f"league median {med:g}", anchor="middle", size=9.5)
    parts.append(f'<line x1="{X(a):.1f}" y1="{y}" x2="{X(b):.1f}" y2="{y}" stroke="{RULE}" stroke-width="3"/>')
    parts.append(f'<circle cx="{X(a):.1f}" cy="{y}" r="7" fill="{DET}"/><circle cx="{X(b):.1f}" cy="{y}" r="7" fill="{PIT}"/>')
    def P_(team, pk):
        return EHS[team]["OZF_pctile"] if pk == "ozf" else PCT[K_DET if team == "DET" else K_PIT][pk]
    fa = f"{a:g}{unit}" + (f" ({ordinal(P_('DET', pk))})" if pk else ""); fb = f"{b:g}{unit}" + (f" ({ordinal(P_('PIT', pk))})" if pk else "")
    left, right = (a, fa, DET), (b, fb, PIT)
    if X(a) > X(b): left, right = right, left
    mono(parts, X(left[0]) - 11, y + 4, left[1], anchor="end", fill=left[2], weight="600", halo=True)
    mono(parts, X(right[0]) + 11, y + 4, right[1], anchor="start", fill=right[2], weight="600", halo=True)
legend(parts, 0, h - 28, [("Detroit", DET, "dot"), ("Pittsburgh", PIT, "dot"), ("league median", GRAY, "line")])
source(parts, h, "NHL shift charts (own build, matches Evolving Hockey); QoC/QoT = TOI-weighted avg of opponents'/linemates' 5v5 TOI/GP.")
close(parts, "c2-deployment.svg")

# =====================================================================
# C3  On-ice: chances barely moved, goals flipped (PDO)
# =====================================================================
h = 320; parts = svg_open(h, "On-ice: the chance share barely moved, the goal share flipped",
                          "5v5, with him on the ice vs his team without him in the same games. Right: on-ice shooting and save percentage (PDO).")
groups = [("Expected goals (xGF%)", "xgf_pct", "off_xgf_pct", "xGF_pct_pctile"), ("Actual goals (GF%)", "gf_pct", "off_gf_pct", "GF_pct_pctile")]
mx, my, pw, ph = 40, 60, 430, 170; gw = pw / 2; ymin, ymax = 30, 65
def Y(v): return my + ph - ph * (v - ymin) / (ymax - ymin)
for v in (40, 50, 60):
    parts.append(f'<line x1="{mx}" y1="{Y(v):.1f}" x2="{mx+pw}" y2="{Y(v):.1f}" stroke="{RULE if v!=50 else GRAY}" stroke-width="{0.6 if v!=50 else 1.5}"/>'); mono(parts, mx - 6, Y(v) + 4, f"{v}%", anchor="end")
for gi, (lab, on, off, pk) in enumerate(groups):
    gx = mx + gi * gw; bw = 36; xs = [gx + gw * 0.5 - 86, gx + gw * 0.5 - 44, gx + gw * 0.5 + 8, gx + gw * 0.5 + 50]
    vals = [(S[K_DET][on], DET, "on"), (S[K_DET][off], "#e9a3aa", "off"), (S[K_PIT][on], PIT, "on"), (S[K_PIT][off], "#e6cf8f", "off")]
    for (v, c, kind), x in zip(vals, xs):
        parts.append(f'<rect x="{x:.1f}" y="{min(Y(v),Y(50)):.1f}" width="{bw}" height="{abs(Y(v)-Y(50)):.1f}" fill="{c}"/>')
        mono(parts, x + bw / 2, (Y(v) - 5) if v >= 50 else (Y(v) + 12), f"{v:.1f}", anchor="middle", fill=INK, weight="600" if kind == "on" else None, size=10)
    sans(parts, gx + gw / 2, my + ph + 18, lab, 12, INK, anchor="middle", weight="600")
    mono(parts, gx + gw / 2, my + ph + 33, f"pct vs forwards: DET {ordinal(EHS['DET'][pk])}, PIT {ordinal(EHS['PIT'][pk])}", anchor="middle", size=9.5)
legend(parts, mx, my - 8, [("DET on", DET, "bar"), ("DET off", "#e9a3aa", "bar"), ("PIT on", PIT, "bar"), ("PIT off", "#e6cf8f", "bar")])
# PDO panel
px = 520; sans(parts, px, my + 4, "On-ice luck (Evolving Hockey, 5v5)", 12, INK, weight="600")
rowsP = [("shooting %", "onice_sh", "%"), ("save %", "onice_sv", ""), ("PDO", "PDO", ""), ("PDO percentile", "PDO_pctile", "th")]
for i, (lab, k, u) in enumerate(rowsP):
    y = my + 30 + i * 30
    parts.append(f'<line x1="{px}" y1="{y+10}" x2="{W}" y2="{y+10}" stroke="{RULE}" stroke-width="0.6"/>')
    sans(parts, px, y + 4, lab, 11, SOFT)
    a = EHS["DET"][k]; b = EHS["PIT"][k]
    fa = f"{a:.1f}%" if k == "onice_sh" else (f".{int(round(a*10)):03d}" if k == "onice_sv" else (f"{a:.3f}" if k == "PDO" else ordinal(a)))
    fb = f"{b:.1f}%" if k == "onice_sh" else (f".{int(round(b*10)):03d}" if k == "onice_sv" else (f"{b:.3f}" if k == "PDO" else ordinal(b)))
    mono(parts, px + 130, y + 4, fa, fill=DET, weight="600", size=11); mono(parts, px + 195, y + 4, fb, fill=PIT, weight="600", size=11)
mono(parts, px + 130, my + 16, "DET", fill=DET, size=10); mono(parts, px + 195, my + 16, "PIT", fill=PIT, size=10)
sans(parts, px, my + 30 + 4 * 30 + 6, "Detroit: 6 GF, 10 GA on 18.4 / 17.3 xG.", 10.5, SOFT)
sans(parts, px, my + 30 + 4 * 30 + 21, "Pittsburgh: 14 GF, 11 GA on 10.1 / 11.0 xG.", 10.5, SOFT)
source(parts, h, "Bars: NHL play-by-play + shift charts, MoneyPuck xG (own build; goal counts match EH exactly). PDO: Evolving Hockey.")
close(parts, "c3-onice.svg")

# =====================================================================
# C4  Individual rates DET vs PIT with percentiles
# =====================================================================
rowsI = [("5v5 points per 60", "p60_5v5", "p60", "P60_pctile"), ("5v5 individual xG per 60", "ixg60_5v5", "ixg60", "ixG60_pctile"), ("5v5 shot attempts per 60", "icf60_5v5", "icf60", "iCF60_pctile"), ("Hits per 60 (all situations)", "hits60", "hits60", "HF60_pctile")]
h = 60 + 52 * len(rowsI) + 40; parts = svg_open(h, "Individual play: same shooter, same hitter, with a bounce and more space",
                                                 "Detroit 2025-26 vs Pittsburgh 2025-26. Bars = his rate (own build); label = Evolving Hockey percentile vs forwards.")
lx = 250; rx = W - 90
for i, (lab, key, pk, ek) in enumerate(rowsI):
    y = 66 + 52 * i; a = S[K_DET][key]; b = S[K_PIT][key]; med = MED[pk]; top = max(a, b, med) * 1.25
    def X(v): return lx + (rx - lx) * v / top
    sans(parts, 0, y + 12, lab, 12, INK, weight="600")
    parts.append(f'<rect x="{lx}" y="{y}" width="{X(a)-lx:.1f}" height="11" fill="{DET}"/><rect x="{lx}" y="{y+14}" width="{X(b)-lx:.1f}" height="11" fill="{PIT}"/>')
    parts.append(f'<line x1="{X(med):.1f}" y1="{y-3}" x2="{X(med):.1f}" y2="{y+28}" stroke="{GRAY}" stroke-width="2"/>')
    mono(parts, X(a) + 6, y + 9, f"{a:g}  ({ordinal(EHS['DET'][ek])})", fill=DET, weight="600", size=10)
    mono(parts, X(b) + 6, y + 23, f"{b:g}  ({ordinal(EHS['PIT'][ek])})", fill=PIT, weight="600", size=10)
    parts.append(f'<line x1="0" y1="{y+38}" x2="{W}" y2="{y+38}" stroke="{RULE}" stroke-width="0.6"/>')
legend(parts, 0, h - 28, [("Detroit", DET, "bar"), ("Pittsburgh", PIT, "bar"), ("league median", GRAY, "line")])
source(parts, h, "NHL play-by-play + shift charts (own build); MoneyPuck xG. Percentiles: EH 5v5 box-score table, forwards 150+ min.")
close(parts, "c4-individual.svg")

# =====================================================================
# C5  Finishing by stint: goals vs xG + luck test
# =====================================================================
stints = [("2022-23 DET", "DET 2022-23"), ("2024-25 DET", "DET 2024-25"), ("2025-26 DET", "DET 2025-26"), ("2025-26 PIT", "PIT 2025-26")]
h = 300; parts = svg_open(h, "Finishing: neither the Detroit drought nor the Pittsburgh burst beats chance",
                          "Goals vs xG on his own unblocked shots. P = chance of that few (DET) or that many (PIT) goals on those exact shots.")
mx, my, pw, ph = 40, 60, W - 60, 170; gw = pw / 4; ymax = 7
def Y(v): return my + ph - ph * v / ymax
for v in (0, 2, 4, 6):
    parts.append(f'<line x1="{mx}" y1="{Y(v):.1f}" x2="{mx+pw}" y2="{Y(v):.1f}" stroke="{RULE}" stroke-width="{1.2 if v==0 else 0.6}"/>'); mono(parts, mx - 6, Y(v) + 4, f"{v}", anchor="end")
for i, (lab, lk) in enumerate(stints):
    L = luck[lk]; gx = mx + i * gw + gw / 2; c = PIT if "PIT" in lab else DET
    parts.append(f'<rect x="{gx-40}" y="{Y(L["xg"]):.1f}" width="34" height="{Y(0)-Y(L["xg"]):.1f}" fill="{GRAY}"/>')
    parts.append(f'<rect x="{gx+4}" y="{Y(L["goals"]):.1f}" width="34" height="{Y(0)-Y(L["goals"]):.1f}" fill="{c}"/>')
    mono(parts, gx - 23, Y(L["xg"]) - 5, f"{L['xg']:.1f} xG", anchor="middle", size=10)
    mono(parts, gx + 21, Y(L["goals"]) - 5, f"{L['goals']} G", anchor="middle", fill=c, weight="600", size=10)
    sans(parts, gx, my + ph + 18, lab, 12, INK, anchor="middle", weight="600")
    p = L["p_at_most"] if "DET" in lab else L["p_at_least"]
    mono(parts, gx, my + ph + 33, f"{L['unblocked']} shots · P = {p:.2f}", anchor="middle", size=9.5)
legend(parts, mx, my - 8, [("expected goals", GRAY, "bar"), ("goals, Detroit", DET, "bar"), ("goals, Pittsburgh", PIT, "bar")])
source(parts, h, "MoneyPuck shot files 2022-2025; 200k-draw simulation. Career: 16 G on 18.3 xG, P(that few) = 0.33.")
close(parts, "c5-finishing.svg")

# =====================================================================
# C6  Evolving Hockey GAR / xGAR by stint with percentiles
# =====================================================================
rows = [("22-23 DET", "22-23 DET", DET), ("24-25 DET", "24-25 DET", DET), ("25-26 DET", "25-26 DET", DET), ("25-26 PIT", "25-26 PIT", PIT)]
h = 290; parts = svg_open(h, "Evolving Hockey: below replacement in Detroit, top-decile pace in Pittsburgh",
                          "GAR and expected GAR per stint; percentile = GAR/60 vs forwards with 150+ minutes that season.")
mx, my, pw, ph = 40, 60, W - 60, 160; gw = pw / 4; ymin, ymax = -3, 5
def Y(v): return my + ph - ph * (v - ymin) / (ymax - ymin)
for v in (-2, 0, 2, 4):
    parts.append(f'<line x1="{mx}" y1="{Y(v):.1f}" x2="{mx+pw}" y2="{Y(v):.1f}" stroke="{RULE if v else GRAY}" stroke-width="{0.6 if v else 1.5}"/>'); mono(parts, mx - 6, Y(v) + 4, f"{v:+d}" if v else "0", anchor="end")
pcts = {"22-23 DET": eh["gar60_pct_22-23"], "24-25 DET": eh["gar60_pct_24-25"], "25-26 DET": eh["gar60_pct"]["DET"], "25-26 PIT": eh["gar60_pct"]["PIT"]}
for i, (lab, k, c) in enumerate(rows):
    r = eh["rows"][k]; gx = mx + i * gw + gw / 2
    for j, (key, col) in enumerate((("GAR", c), ("xGAR", GRAY))):
        v = r[key]; x = gx - 40 + j * 42
        parts.append(f'<rect x="{x}" y="{min(Y(v),Y(0)):.1f}" width="36" height="{abs(Y(v)-Y(0)):.1f}" fill="{col}"/>')
        mono(parts, x + 18, (Y(v) - 5) if v >= 0 else (Y(v) + 12), f"{v:+.1f}", anchor="middle", fill=INK, weight="600" if key == "GAR" else None, size=10)
    sans(parts, gx, my + ph + 18, f"{lab}  ({r['GP']} GP)", 12, INK, anchor="middle", weight="600")
    mono(parts, gx, my + ph + 33, f"GAR/60 {ordinal(pcts[k])} pct", anchor="middle", size=9.5)
legend(parts, mx, my - 8, [("GAR, Detroit", DET, "bar"), ("GAR, Pittsburgh", PIT, "bar"), ("xGAR", GRAY, "bar")])
source(parts, h, "Evolving Hockey GAR/xGAR, 2025-26 split by team. Noisy: 7 of 71 forward rows under 25 GP reached +3.2.")
close(parts, "c6-eh-gar.svg")

# =====================================================================
# C7  Age comps: what forwards with his 2025-26 profile did the next season
# =====================================================================
nx = [c["n1"] for c in comps["comps"] if c["n1"]]; n = comps["n"]; gone = n - len(nx)
pts = [c["pts"] for c in nx]
bins = [(0, 9), (10, 19), (20, 29), (30, 39), (40, 49), (50, 99)]
h = 300; parts = svg_open(h, "Base rates: forwards with his 2025-26 profile, one season later",
                          f"{n} forward seasons 2010-23: age 23-25, 35+ GP, 9.5-13 5v5 min, 0.8-1.9 P/60, 0.5-1.1 ixG/60. The next year:")
mx, my, pw, ph = 40, 60, W - 60, 150; cats = ["no NHL season"] + [f"{a}-{b}" if b < 99 else f"{a}+" for a, b in bins]
counts = [gone] + [sum(1 for p in pts if a <= p <= b) for a, b in bins]; gw = pw / len(cats); ymax = max(counts) * 1.2
def Y(v): return my + ph - ph * v / ymax
for i, (c, v) in enumerate(zip(cats, counts)):
    x = mx + i * gw + gw * 0.15; col = MUTED if i == 0 else (BLUE if i < 3 else AMBER if i == 3 else RED)
    parts.append(f'<rect x="{x:.1f}" y="{Y(v):.1f}" width="{gw*0.7:.1f}" height="{Y(0)-Y(v):.1f}" fill="{col}"/>')
    mono(parts, x + gw * 0.35, Y(v) - 6, f"{100*v/n:.0f}%", anchor="middle", fill=INK, weight="600")
    sans(parts, x + gw * 0.35, Y(0) + 16, c, 11, INK, anchor="middle")
parts.append(f'<line x1="{mx}" y1="{Y(0)}" x2="{mx+pw}" y2="{Y(0)}" stroke="{RULE}" stroke-width="1.2"/>')
sans(parts, mx + pw / 2, Y(0) + 32, "points the following season", 11, SOFT, anchor="middle")
r1 = comps["next1"]
mono(parts, mx, h - 40, f"median next season: {r1['med_gp']:.0f} GP, {r1['med_toi']} 5v5 min, {r1['med_pts']:.0f} pts | {r1['pct_30pts']}% reach 30 pts | {r1['pct_p60_2']}% reach 2.0 P/60 (PIT pace 2.7)", fill=INK, size=10)
source(parts, h, "MoneyPuck forward seasons 2010-25. Söderblom 2025-26 combined: 59 GP, 10.7 min, 1.23 P/60, 0.75 ixG/60.")
close(parts, "c7-age-comps.svg")

# =====================================================================
# C8  What a third-round pick is worth vs what he is
# =====================================================================
h = 280; parts = svg_open(h, "The return: a pick in the 65-80 range becomes a 100-game NHLer one time in four",
                          "Draft classes 2008-2017, career NHL games to Sept 2026. His own comps: 55% played 60+ games the next season.")
bars = [("Round 2", pick["round2"]), ("Round 3", pick["round3"]), ("Picks 65-80", pick["picks_65_80"]), ("Round 4", pick["round4"]), ("Round 6 (his slot)", pick["round6"])]
mx, my, pw, ph = 40, 60, W - 60, 150; gw = pw / len(bars); ymax = 70
def Y(v): return my + ph - ph * v / ymax
for v in (0, 20, 40, 60):
    parts.append(f'<line x1="{mx}" y1="{Y(v):.1f}" x2="{mx+pw}" y2="{Y(v):.1f}" stroke="{RULE}" stroke-width="{1.2 if v==0 else 0.6}"/>'); mono(parts, mx - 6, Y(v) + 4, f"{v}%", anchor="end")
for i, (lab, r) in enumerate(bars):
    gx = mx + i * gw; hl = lab.startswith("Picks")
    for j, (key, col, nm) in enumerate((("gp100", AMBER if hl else GRAY, "100+ GP"), ("gp400", RED if hl else "#8a8781", "400+ GP"))):
        x = gx + gw * 0.18 + j * gw * 0.34
        parts.append(f'<rect x="{x:.1f}" y="{Y(r[key]):.1f}" width="{gw*0.3:.1f}" height="{Y(0)-Y(r[key]):.1f}" fill="{col}"/>')
        mono(parts, x + gw * 0.15, Y(r[key]) - 5, f"{r[key]:.0f}%", anchor="middle", fill=INK, weight="600" if hl else None, size=10)
    sans(parts, gx + gw / 2, Y(0) + 16, lab, 11.5, INK, anchor="middle", weight="600" if hl else None)
    mono(parts, gx + gw / 2, Y(0) + 30, f"n = {r['n']}", anchor="middle", size=9.5)
legend(parts, mx, my - 8, [("100+ NHL games", GRAY, "bar"), ("400+ NHL games", "#8a8781", "bar"), ("the pick's neighbourhood (No. 73)", AMBER, "bar")])
source(parts, h, "NHL API draft picks + bios. Pick 73 became Zach Olsen (TOR) after Detroit sent it to St. Louis for Faulk.")
close(parts, "c8-pick-value.svg")

# =====================================================================
# C9  Linemates: 5v5 TOI share with top skaters by stint
# =====================================================================
h = 250; parts = svg_open(h, "Linemates: Rasmussen in Detroit, the Acciari-Dewar checking line in Pittsburgh",
                          "Share of his 5v5 minutes spent with each teammate (skaters only), 2025-26.")
cols = [(K_DET, DET, 20), (K_PIT, PIT, W / 2 + 10)]
for k, c, x0 in cols:
    mates = [(n, a, b) for n, a, b in S[k]["top_mates"] if not any(g in n for g in ("Gibson", "Talbot", "Skinner", "Silovs", "Husso"))][:6]
    sans(parts, x0, 62, k.replace("2025-26 ", "") + " 2025-26", 12, c, weight="600")
    for i, (n, a, b) in enumerate(mates):
        y = 80 + i * 24; bw = (W / 2 - 200) * b / 100
        sans(parts, x0, y + 9, n, 11, INK)
        parts.append(f'<rect x="{x0+130}" y="{y}" width="{bw:.1f}" height="12" fill="{c}"/>')
        mono(parts, x0 + 134 + bw, y + 10, f"{b:.0f}%  ({a:.0f} min)", size=10, fill=SOFT)
source(parts, h, "NHL shift charts (own build). Detroit share is of 406 5v5 minutes; Pittsburgh of 223.")
close(parts, "c9-linemates.svg")

# =====================================================================
# C10  WOWY: linemates with vs without him (Evolving Hockey Teammate Tool)
# =====================================================================
wowy = json.load(open(RAW / "eh_wowy_2025.json"))["rows"]
sel = [r for r in wowy if r["mate"] in ("Michael Rasmussen", "Mason Appleton", "James Van Riemsdyk", "Nate Danielson", "Marco Kasper", "Noel Acciari", "Connor Dewar")]
order = ["Michael Rasmussen", "Mason Appleton", "James Van Riemsdyk", "Nate Danielson", "Marco Kasper", "Noel Acciari", "Connor Dewar"]
sel.sort(key=lambda r: order.index(r["mate"]))
h = 60 + 34 * len(sel) + 50; parts = svg_open(h, "With or without him: Detroit's forwards were better with him, Pittsburgh's were not",
                                              "5v5 expected-goals share of each forward linemate with him (dot) vs without him (hollow), 2025-26.")
lx = 220; rx = W - 30; lo, hi = 38, 60
def X(v): return lx + (rx - lx) * (v - lo) / (hi - lo)
for v in (40, 45, 50, 55, 60):
    parts.append(f'<line x1="{X(v):.1f}" y1="{56}" x2="{X(v):.1f}" y2="{h-44}" stroke="{RULE if v!=50 else GRAY}" stroke-width="{0.6 if v!=50 else 1.5}"/>'); mono(parts, X(v), 52, f"{v}%", anchor="middle", size=9.5)
for i, r in enumerate(sel):
    y = 74 + 34 * i; c = DET if r["team"] == "DET" else PIT
    sans(parts, 0, y + 4, r["mate"], 12, INK, weight="600"); mono(parts, 0, y + 17, f"{r['team']} · {r['toi_tog']:.0f} min together", size=9.5)
    a, b = r["xgf_mate_wo"], r["xgf_tog"]
    parts.append(f'<line x1="{X(a):.1f}" y1="{y}" x2="{X(b):.1f}" y2="{y}" stroke="{c}" stroke-width="3" opacity="0.5"/>')
    parts.append(f'<circle cx="{X(a):.1f}" cy="{y}" r="6" fill="{PAPER}" stroke="{c}" stroke-width="2.5"/><circle cx="{X(b):.1f}" cy="{y}" r="7" fill="{c}"/>')
    d = r["delta_mate"]; mono(parts, X(max(a, b)) + 12, y + 4, f"{d:+.1f}", fill=c, weight="600", halo=True)
    parts.append(f'<line x1="0" y1="{y+24}" x2="{W}" y2="{y+24}" stroke="{RULE}" stroke-width="0.5"/>')
legend(parts, 0, h - 26, [("with Söderblom", DET, "dot"), ("without", DET, "hollow"), ("Pittsburgh linemates", PIT, "dot")])
source(parts, h, "Evolving Hockey Teammate Tool, 5v5, no adjustment; 'without' = teammate season total minus minutes together.")
close(parts, "c10-wowy.svg")
