#!/usr/bin/env python3
"""Generate inline-ready SVG charts for
'Is Michael Rasmussen really as bad as Red Wings fans think he is?'
Dependency-free. Regenerates every chart from raw/.
Tokens and helpers mirror research/wings-type/charts/make_charts.py.
Palette: Rasmussen #ce1126, league/median #b3b1ad, 'without'/league forwards #2a78d6, third series #c98500."""
import json, math, csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
OUT = ROOT / "charts"

# ---- site tokens ----
PAPER = "#d7d6d3"; PANEL = "#e7e6e3"; RULE = "#c4c3bf"; INK = "#141414"; SOFT = "#575653"; MUTED = "#8a8781"
RED = "#ce1126"; GRAY = "#b3b1ad"; BLUE = "#2a78d6"; AMBER = "#c98500"
SANS = "'Space Grotesk', ui-sans-serif, system-ui, sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, monospace"
W = 760

SEASONS = ["2018", "2020", "2021", "2022", "2023", "2024", "2025"]  # 2019 = no NHL games
SLOTS = ["2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]  # with the gap slot


def lab(s):
    s = int(s); return f"{str(s)[2:]}-{str(s + 1)[2:]}"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def ordinal(n):
    n = int(round(n))
    suf = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suf}"


def guard(text, size, is_mono, x=0):
    """Warn when a line is likely to run past the 760px frame in the fallback fonts."""
    est = x + len(text) * size * (0.62 if is_mono else 0.56)
    if est > W:
        print(f"  WARN width {est:.0f}px > {W}: {text[:60]}...")


def svg_open(h, title, sub=None):
    guard(title, 17, False)
    if sub:
        guard(sub, 12, False)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="{esc(title)}" font-family="{SANS}" style="max-width:100%;height:auto;background:{PAPER}">',
             f'<rect width="{W}" height="{h}" fill="{PAPER}"/>',
             f'<text x="0" y="20" font-size="17" font-weight="600" fill="{INK}">{esc(title)}</text>']
    if sub:
        parts.append(f'<text x="0" y="38" font-size="12" fill="{SOFT}">{esc(sub)}</text>')
    return parts


def legend(parts, x, y, items):
    """items: list of (label, color, style) where style in {'dot','hollow','line','bar'}"""
    cx = x
    for n, c, st in items:
        if st == "dot":
            parts.append(f'<circle cx="{cx+5}" cy="{y-4}" r="5" fill="{c}"/>')
        elif st == "hollow":
            parts.append(f'<circle cx="{cx+5}" cy="{y-4}" r="4.5" fill="{PAPER}" stroke="{c}" stroke-width="2"/>')
        elif st == "line":
            parts.append(f'<line x1="{cx-2}" y1="{y-4}" x2="{cx+12}" y2="{y-4}" stroke="{c}" stroke-width="2.5"/>')
        else:
            parts.append(f'<rect x="{cx}" y="{y-10}" width="11" height="11" rx="2" fill="{c}"/>')
        parts.append(f'<text x="{cx+16}" y="{y}" font-size="12" fill="{INK}">{esc(n)}</text>')
        cx += 16 + 7 * len(n) + 22
    return cx


def source(parts, h, text):
    guard(text, 10.5, True)
    parts.append(f'<text x="0" y="{h-8}" font-size="10.5" font-family="{MONO}" fill="{MUTED}">{esc(text)}</text>')


def close(parts, name):
    parts.append("</svg>")
    (OUT / name).write_text("\n".join(parts))
    print("wrote", name)


def mono(parts, x, y, s, size=10.5, fill=SOFT, anchor="start", weight=None, halo=False):
    w = f' font-weight="{weight}"' if weight else ""
    hl = f' stroke="{PAPER}" stroke-width="3" paint-order="stroke"' if halo else ""
    parts.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-family="{MONO}" fill="{fill}" text-anchor="{anchor}"{w}{hl}>{esc(s)}</text>')


def sans(parts, x, y, s, size=12, fill=INK, anchor="start", weight=None):
    if anchor == "start":
        guard(s, size, False, x)
    w = f' font-weight="{weight}"' if weight else ""
    parts.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}>{esc(s)}</text>')


# ---- data ----
arc = json.load(open(RAW / "mp_rasmussen_arc.json"))
shots = json.load(open(RAW / "mp_shots_rasmussen.json"))
luck = json.load(open(RAW / "luck_test.json"))
games = sorted(json.load(open(RAW / "per_game.json")), key=lambda g: g["date"])
# rolling20.json's idx keys the un-sorted per_game order (reverse-date within season), so its windows
# straddle season breaks backwards. Recompute a trailing 20-game window from the date-sorted logs.
rolling = []
for i in range(19, len(games)):
    win = games[i - 19:i + 1]; toi = sum(g["toi"] for g in win)
    rolling.append({"idx": i, "date": games[i]["date"], "p60": 60 * sum(g["p"] for g in win) / toi,
                    "ixg60": 60 * sum(g["ixg"] for g in win) / toi, "toi_gm": toi / 20})
eh = json.load(open(RAW / "eh_rasmussen.json"))
EHS = ["18-19", "20-21", "21-22", "22-23", "23-24", "24-25", "25-26"]
EHSLOTS = ["18-19", "19-20", "20-21", "21-22", "22-23", "23-24", "24-25", "25-26"]
lines = json.load(open(RAW / "mp_lines_rasmussen.json"))
age = json.load(open(RAW / "age_curve_comps.json"))
draft = json.load(open(RAW / "draft_2017_r1.json"))
pk = json.load(open(RAW / "pk_rasmussen.json"))
team = json.load(open(RAW / "det_team_context.json"))

# =====================================================================
# C1  Career arc: 5v5 points/60 and ixG/60 with forward percentiles
# =====================================================================
h = 530
parts = svg_open(h, "Rasmussen at 5v5, season by season, and where each year ranked",
                 "5v5 points/60 and individual xG/60. Percentiles are among NHL forwards with 300+ 5v5 minutes that season.")
mx = 58; pw = W - mx - 30
slot_w = pw / len(SLOTS)
def Xs(s): return mx + slot_w * (SLOTS.index(s) + 0.5)
panels = [("pts60", "5v5 points / 60", 2.2, [0, 0.5, 1.0, 1.5, 2.0], 66, 150),
          ("ixG60", "5v5 individual xG / 60", 1.0, [0, 0.25, 0.5, 0.75, 1.0], 264, 150)]
for key, name, ymax, ticks, my, ph in panels:
    def Y(v, my=my, ph=ph, ymax=ymax): return my + ph - ph * v / ymax
    sans(parts, mx, my - 6, name, 12, INK, weight="600")
    for t in ticks:
        parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE}" stroke-width="1"/>')
        mono(parts, mx - 8, Y(t) + 4, f"{t:.2f}".rstrip("0").rstrip(".") if t else "0", 10.5, SOFT, "end")
    # gap band for 2019-20
    gx = mx + slot_w * SLOTS.index("2019")
    parts.append(f'<rect x="{gx:.1f}" y="{my}" width="{slot_w:.1f}" height="{ph}" fill="{PANEL}"/>')
    parts.append(f'<line x1="{Xs("2019"):.1f}" y1="{my}" x2="{Xs("2019"):.1f}" y2="{my+ph}" stroke="{RULE}" stroke-width="1" stroke-dasharray="3 3"/>')
    # line segments (break across the gap)
    segs = [["2018"], ["2020", "2021", "2022", "2023", "2024", "2025"]]
    for seg in segs:
        d = " ".join(f"{'M' if i==0 else 'L'}{Xs(s):.1f},{Y(arc[s]['5on5'][key][0]):.1f}" for i, s in enumerate(seg))
        if len(seg) > 1:
            parts.append(f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="2" stroke-linejoin="round"/>')
    # dashed bridge across the gap
    parts.append(f'<line x1="{Xs("2018"):.1f}" y1="{Y(arc["2018"]["5on5"][key][0]):.1f}" x2="{Xs("2020"):.1f}" y2="{Y(arc["2020"]["5on5"][key][0]):.1f}" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 4" stroke-opacity="0.6"/>')
    for s in SEASONS:
        v, p = arc[s]["5on5"][key]
        parts.append(f'<circle cx="{Xs(s):.1f}" cy="{Y(v):.1f}" r="5" fill="{RED}" stroke="{PAPER}" stroke-width="2"/>')
        mono(parts, Xs(s), Y(v) - 10, f"{v:.2f}", 10.5, INK, "middle")
        mono(parts, Xs(s), my + ph + 14, f"{ordinal(p)} pct", 10, SOFT, "middle")
    sans(parts, Xs("2019"), my + 16, "no NHL games", 10.5, SOFT, "middle")
    sans(parts, Xs("2019"), my + 30, "AHL, back injury", 10.5, SOFT, "middle")
# season axis labels under the bottom panel
ay = 264 + 150 + 34
for s in SLOTS:
    mono(parts, Xs(s), ay, lab(s), 11, INK if s != "2019" else MUTED, "middle")
# injury markers
def inj(s, y, text1, text2):
    x = Xs(s)
    parts.append(f'<path d="M{x-5:.1f},{y} l5,-5 l5,5 l-5,5 z" fill="{PAPER}" stroke="{RED}" stroke-width="1.5"/>')
    sans(parts, x, y + 16, text1, 10, SOFT, "middle")
    sans(parts, x, y + 28, text2, 10, SOFT, "middle")
inj("2022", ay + 12, "kneecap, Feb 25", "missed final 24")
inj("2025", ay + 12, "leg, Mar 12 + Apr 7", "missed 13")
legend(parts, mx, h - 24, [("Rasmussen", RED, "dot")])
parts.append(f'<path d="M{mx+130},{h-28} l5,-5 l5,5 l-5,5 z" fill="{PAPER}" stroke="{RED}" stroke-width="1.5"/>')
sans(parts, mx + 146, h - 24, "season-ending injury", 12, INK)
source(parts, h, "Source: MoneyPuck, regular seasons 2018-19 to 2025-26. 2020-21 was a 56-game season.")
close(parts, "c1-career-arc.svg")

# =====================================================================
# C2  Goals vs expected goals, dumbbell per season (all situations)
# =====================================================================
mp_tot = {}
for s in SEASONS:
    for r in csv.DictReader(open(RAW / "mp" / f"skaters_{s}.csv")):
        if r["playerId"] == "8479992" and r["situation"] == "all":
            mp_tot[s] = (float(r["I_F_goals"]), float(r["I_F_xGoals"]), int(r["games_played"]))
cg = sum(v[0] for v in mp_tot.values()); cx_ = sum(v[1] for v in mp_tot.values())
row_h = 34
h = 70 + row_h * len(SLOTS) + 70
parts = svg_open(h, "Every season he has scored fewer goals than his chances were worth",
                 "All situations. Gray = expected goals from his shot mix, red = actual goals. Gap printed on each row.")
mx = 90; bw = W - mx - 130; vmax = 20
def X(v): return mx + bw * v / vmax
y = 70
for t in range(0, 21, 5):
    parts.append(f'<line x1="{X(t):.1f}" y1="{y-8}" x2="{X(t):.1f}" y2="{y + row_h*len(SLOTS) - 14}" stroke="{RULE}" stroke-width="1"/>')
    mono(parts, X(t), y - 12, str(t), 10.5, SOFT, "middle")
for s in SLOTS:
    yy = y + row_h * SLOTS.index(s) + 8
    mono(parts, mx - 12, yy + 4, lab(s), 11.5, INK if s != "2019" else MUTED, "end")
    if s == "2019":
        sans(parts, X(0) + 4, yy + 4, "no NHL games (AHL, back injury)", 10.5, MUTED)
        continue
    g, xg, gp = mp_tot[s]
    parts.append(f'<line x1="{X(g):.1f}" y1="{yy}" x2="{X(xg):.1f}" y2="{yy}" stroke="{RED}" stroke-width="3" stroke-opacity="0.35" stroke-linecap="round"/>')
    parts.append(f'<circle cx="{X(xg):.1f}" cy="{yy}" r="6" fill="{GRAY}" stroke="{PAPER}" stroke-width="2"/>')
    parts.append(f'<circle cx="{X(g):.1f}" cy="{yy}" r="6" fill="{RED}" stroke="{PAPER}" stroke-width="2"/>')
    mono(parts, X(xg) + 12, yy + 4, f"{int(g)} G on {xg:.1f} xG ({g-xg:+.1f}), {gp} GP", 10.5, SOFT)
yb = y + row_h * len(SLOTS) + 2
parts.append(f'<line x1="0" y1="{yb-6}" x2="{W}" y2="{yb-6}" stroke="{RULE}" stroke-width="1"/>')
sans(parts, 0, yb + 12, f"Career: {int(cg)} goals on {cx_:.1f} expected, {cg-cx_:+.1f}. Never once finished a season above his xG.", 12.5, INK, weight="600")
legend(parts, 0, yb + 34, [("Expected goals", GRAY, "dot"), ("Actual goals", RED, "dot")])
source(parts, h, "Source: MoneyPuck skater tables, all situations, regular season, 2018-19 to 2025-26 (playerId 8479992).")
close(parts, "c2-goals-vs-xg.svg")

# =====================================================================
# C3  Danger-bucket conversion vs league forwards
# =====================================================================
agg = {}
for b in ("ld", "md", "hd"):
    att = sum(shots[s]["buckets"][b]["att"] for s in SEASONS)
    g = sum(shots[s]["buckets"][b]["g"] for s in SEASONS)
    lg = sum(shots[s]["buckets"][b]["att"] * shots[s]["buckets"][b]["league_fw_sh_per_att"] for s in SEASONS) / att
    agg[b] = (att, g, g / att, lg)
h = 360
md_gap = agg["md"][3] - agg["md"][2]
parts = svg_open(h, "Where the goals go missing: the medium-danger shot",
                 "Goals per unblocked attempt by danger zone, 2018-19 to 2025-26. League rate is weighted to his own shot mix.")
legend(parts, 0, 60, [("Rasmussen", RED, "bar"), ("League forwards", BLUE, "bar")])
mx = 50; my = 74; pw = W - mx - 20; ph = 190; ymax = 0.30
def Y(v): return my + ph - ph * v / ymax
for t in (0, 0.1, 0.2, 0.3):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE}" stroke-width="1"/>')
    mono(parts, mx - 8, Y(t) + 4, f"{int(t*100)}%", 10.5, SOFT, "end")
names = {"ld": "Low danger", "md": "Medium danger", "hd": "High danger"}
gw = pw / 3; barw = 62; gapb = 10
for i, b in enumerate(("ld", "md", "hd")):
    att, g, r, lg = agg[b]
    cx = mx + gw * (i + 0.5)
    x1 = cx - barw - gapb / 2; x2 = cx + gapb / 2
    parts.append(f'<rect x="{x1:.1f}" y="{Y(r):.1f}" width="{barw}" height="{Y(0)-Y(r):.1f}" rx="3" fill="{RED}"/>')
    parts.append(f'<rect x="{x2:.1f}" y="{Y(lg):.1f}" width="{barw}" height="{Y(0)-Y(lg):.1f}" rx="3" fill="{BLUE}"/>')
    mono(parts, x1 + barw / 2, Y(r) - 6, f"{100*r:.1f}%", 11, INK, "middle", "600")
    mono(parts, x2 + barw / 2, Y(lg) - 6, f"{100*lg:.1f}%", 11, INK, "middle", "600")
    sans(parts, cx, Y(0) + 18, names[b], 12, INK, "middle", "600")
    mono(parts, cx, Y(0) + 33, f"{int(g)} G on {int(att)} attempts", 10.5, SOFT, "middle")
# callout for medium danger
cxm = mx + gw * 1.5
sans(parts, cxm, my + 6, f"Medium danger: {100*agg['md'][2]:.1f}% vs {100*agg['md'][3]:.1f}%, a {100*md_gap:.1f}-point gap", 11.5, INK, "middle", "600")
sans(parts, cxm, my + 21, f"At the league rate his {int(agg['md'][0])} medium-danger attempts are worth {agg['md'][0]*agg['md'][3]:.0f} goals. He scored {int(agg['md'][1])}.", 10.5, SOFT, "middle")
source(parts, h, "Source: MoneyPuck shot data, unblocked attempts, regular season, all situations; MoneyPuck danger bands.")
close(parts, "c3-danger-conversion.svg")

# =====================================================================
# C4  Luck test: normal curve of goals expected from his shot mix
# =====================================================================
mu, sd, obs = luck["xg"], luck["sd"], luck["observed"]
z = luck["z"]  # -3.27 as computed on the unrounded shot table
p_norm = 0.5 * (1 + math.erf(z / math.sqrt(2)))
one_in = round(1 / p_norm, -3)
h = 360
parts = svg_open(h, "Could 53 goals on those chances be bad luck? Almost certainly not",
                 f"If his {luck['n_attempts']} unblocked attempts scored at their expected rates, the total lands near {mu:.1f} (sd {sd:.1f}). He scored {obs}.")
mx = 50; my = 64; pw = W - mx - 30; ph = 200
xmin, xmax = 45, 110
def X(v): return mx + pw * (v - xmin) / (xmax - xmin)
pdf = lambda v: math.exp(-0.5 * ((v - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))
pmax = pdf(mu)
def Y(v): return my + ph - ph * pdf(v) / pmax * 0.92
pts = [(X(v), Y(v)) for v in [xmin + i * (xmax - xmin) / 260 for i in range(261)]]
# tail shading below observed
tail = [(X(v), Y(v)) for v in [xmin + i * (obs - xmin) / 60 for i in range(61)]]
d = f"M{tail[0][0]:.1f},{my+ph} " + " ".join(f"L{x:.1f},{y:.1f}" for x, y in tail) + f" L{tail[-1][0]:.1f},{my+ph} Z"
parts.append(f'<path d="{d}" fill="{RED}" fill-opacity="0.25"/>')
d = " ".join(f"{'M' if i==0 else 'L'}{x:.1f},{y:.1f}" for i, (x, y) in enumerate(pts))
parts.append(f'<path d="{d}" fill="none" stroke="{SOFT}" stroke-width="2"/>')
parts.append(f'<line x1="{mx}" y1="{my+ph}" x2="{mx+pw}" y2="{my+ph}" stroke="{RULE}" stroke-width="1"/>')
for t in range(50, 111, 10):
    mono(parts, X(t), my + ph + 16, str(t), 10.5, SOFT, "middle")
    parts.append(f'<line x1="{X(t):.1f}" y1="{my+ph}" x2="{X(t):.1f}" y2="{my+ph+4}" stroke="{RULE}"/>')
sans(parts, mx + pw / 2, my + ph + 34, "Goals from 859 unblocked attempts, if finishing were exactly league-average for each shot", 11.5, SOFT, "middle")
# expected marker
parts.append(f'<line x1="{X(mu):.1f}" y1="{my+8}" x2="{X(mu):.1f}" y2="{my+ph}" stroke="{GRAY}" stroke-width="1.5" stroke-dasharray="3 3"/>')
mono(parts, X(mu) + 6, my + 20, f"expected {mu:.1f}", 11, SOFT)
# observed
parts.append(f'<line x1="{X(obs):.1f}" y1="{my+8}" x2="{X(obs):.1f}" y2="{my+ph}" stroke="{RED}" stroke-width="2.5"/>')
sans(parts, X(obs) + 8, my + 20, f"actual: {obs} goals", 12.5, INK, "start", "600")
sans(parts, X(obs) + 8, my + 36, f"{abs(z):.1f} standard deviations below expected", 11, SOFT, "start")
sans(parts, X(obs) + 8, my + 52, f"about 1 in {int(one_in):,}", 12.5, RED, "start", "600")
sans(parts, X(obs) + 8, my + 68, "odds of a shooter this unlucky by chance alone", 11, SOFT, "start")
sans(parts, X(obs) + 8, my + 84, "the honest read: he is a below-average finisher", 11, SOFT, "start")
source(parts, h, f"Source: MoneyPuck xG per attempt, 2018-19 to 2025-26; normal approximation, z = {z:.2f}, one-tailed p = {p_norm:.4f}.")
close(parts, "c4-luck-test.svg")

# =====================================================================
# C5  Role splits from per-game logs
# =====================================================================
def rates(gs):
    toi = sum(g["toi"] for g in gs)
    return len(gs), toi, 60 * sum(g["p"] for g in gs) / toi, 60 * sum(g["ixg"] for g in gs) / toi
buckets = [("At center", "5+ faceoffs taken", [g for g in games if g["fo"] >= 5]),
           ("At wing", "under 5 faceoffs", [g for g in games if g["fo"] < 5]),
           None,
           ("Under 12 min", "TOI per game", [g for g in games if g["toi"] < 12]),
           ("12 to 15 min", "TOI per game", [g for g in games if 12 <= g["toi"] < 15]),
           ("15+ min", "TOI per game", [g for g in games if g["toi"] >= 15])]
h = 380
parts = svg_open(h, "Center or wing, third line or fourth: the output barely moves",
                 "Career points/60 and individual xG/60 (all situations, own TOI) by the role he played that night. 454 game logs.")
legend(parts, 0, 60, [("Points / 60", RED, "bar"), ("Individual xG / 60", AMBER, "bar")])
mx = 50; my = 88; pw = W - mx - 20; ph = 180; ymax = 2.0
def Y(v): return my + ph - ph * v / ymax
for t in (0, 0.5, 1.0, 1.5, 2.0):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE}" stroke-width="1"/>')
    mono(parts, mx - 8, Y(t) + 4, f"{t:.1f}", 10.5, SOFT, "end")
slot = pw / 6; barw = 42; gapb = 6
for i, b in enumerate(buckets):
    if b is None:
        xg_ = mx + slot * (i + 0.5)
        parts.append(f'<line x1="{xg_:.1f}" y1="{my}" x2="{xg_:.1f}" y2="{Y(0)+40}" stroke="{RULE}" stroke-width="1" stroke-dasharray="3 3"/>')
        continue
    name, sub, gs = b
    n, toi, p60, ixg60 = rates(gs)
    cx = mx + slot * (i + 0.5)
    x1 = cx - barw - gapb / 2; x2 = cx + gapb / 2
    parts.append(f'<rect x="{x1:.1f}" y="{Y(p60):.1f}" width="{barw}" height="{Y(0)-Y(p60):.1f}" rx="3" fill="{RED}"/>')
    parts.append(f'<rect x="{x2:.1f}" y="{Y(ixg60):.1f}" width="{barw}" height="{Y(0)-Y(ixg60):.1f}" rx="3" fill="{AMBER}"/>')
    mono(parts, x1 + barw / 2, Y(p60) - 5, f"{p60:.2f}", 10.5, INK, "middle", "600")
    mono(parts, x2 + barw / 2, Y(ixg60) - 5, f"{ixg60:.2f}", 10.5, INK, "middle", "600")
    sans(parts, cx, Y(0) + 17, name, 12, INK, "middle", "600")
    mono(parts, cx, Y(0) + 31, sub, 10, SOFT, "middle")
    mono(parts, cx, Y(0) + 44, f"n = {n} games", 10, SOFT, "middle")
sans(parts, mx + slot * 1, my - 8, "By position", 11.5, SOFT, "middle")
sans(parts, mx + slot * 4.5, my - 8, "By minutes", 11.5, SOFT, "middle")
source(parts, h, "Source: NHL API game logs, 2018-19 to 2025-26. Center = 5+ faceoffs taken that night (faceoffs are the proxy).")
close(parts, "c5-role-splits.svg")

# =====================================================================
# C6  DET 5v5 lines with vs without Rasmussen
# =====================================================================
LS = ["2022", "2023", "2024", "2025"]
h = 340
parts = svg_open(h, "Detroit's 5v5 lines with Rasmussen on them vs the rest of the forward group",
                 "xG share of Detroit's 5v5 forward-line minutes, with vs without Rasmussen on the line. Minutes under each pair.")
legend(parts, 0, 60, [("Lines with Rasmussen", RED, "bar"), ("Lines without", BLUE, "bar")])
mx = 50; my = 76; pw = W - mx - 20; ph = 170; ymin, ymax = 0.40, 0.58
def Y(v): return my + ph - ph * (v - ymin) / (ymax - ymin)
for t in (0.40, 0.45, 0.50, 0.55):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE if t != 0.5 else SOFT}" stroke-width="1"/>')
    mono(parts, mx - 8, Y(t) + 4, f"{int(t*100)}%", 10.5, SOFT, "end")
slot = pw / 4; barw = 54; gapb = 8
for i, s in enumerate(LS):
    wt, wx, _, _ = lines[s]["with"]; ot, ox, _, _ = lines[s]["without"]
    cx = mx + slot * (i + 0.5)
    x1 = cx - barw - gapb / 2; x2 = cx + gapb / 2
    parts.append(f'<rect x="{x1:.1f}" y="{Y(wx):.1f}" width="{barw}" height="{Y(ymin)-Y(wx):.1f}" rx="3" fill="{RED}"/>')
    parts.append(f'<rect x="{x2:.1f}" y="{Y(ox):.1f}" width="{barw}" height="{Y(ymin)-Y(ox):.1f}" rx="3" fill="{BLUE}"/>')
    mono(parts, x1 + barw / 2, Y(wx) - 5, f"{100*wx:.1f}%", 10.5, INK, "middle", "600")
    mono(parts, x2 + barw / 2, Y(ox) - 5, f"{100*ox:.1f}%", 10.5, INK, "middle", "600")
    mono(parts, cx, Y(ymin) + 17, lab(s), 11.5, INK, "middle")
    mono(parts, cx, Y(ymin) + 31, f"{int(wt)} min with, {int(ot):,} without", 10, SOFT, "middle")
    d = 100 * (wx - ox)
    mono(parts, cx, Y(ymin) + 45, f"{d:+.1f} pts", 10.5, RED if d > 0 else BLUE, "middle", "600")
source(parts, h, "Source: MoneyPuck line tables, 5v5, regular season. In three of four seasons his lines out-chanced the rest.")
close(parts, "c6-lines-with-without.svg")

# =====================================================================
# C7  Rolling 20-game rates across the career
# =====================================================================
# build x positions: game index in date order, with gaps between seasons
season_of = [g["season"] for g in games]
starts = {}
for i, s in enumerate(season_of):
    starts.setdefault(s, i)
order = sorted(starts, key=lambda s: starts[s])
GAP = 8; BIGGAP = 28
xpos = [0.0] * len(games)
cur = 0.0
for i, g in enumerate(games):
    if i > 0 and g["season"] != games[i - 1]["season"]:
        cur += BIGGAP if g["season"] == "20202021" else GAP
    xpos[i] = cur; cur += 1
total = cur
h = 404
parts = svg_open(h, "The whole career in one line: a 2022-24 peak, then a slide",
                 "Rolling 20-game points/60 (all situations, over total TOI) and individual xG/60, with season dividers.")
legend(parts, 0, 60, [("Points / 60", RED, "line"), ("Individual xG / 60", AMBER, "line")])
mx = 40; my = 84; pw = W - mx - 30; ph = 200; ymax = 3.0
def X(i): return mx + pw * xpos[i] / total
def Y(v): return my + ph - ph * v / ymax
for t in (0, 1, 2, 3):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE}" stroke-width="1"/>')
    mono(parts, mx - 8, Y(t) + 4, f"{t:.1f}", 10.5, SOFT, "end")
# season bands + labels
for s in order:
    i0 = starts[s]; i1 = max(i for i, ss in enumerate(season_of) if ss == s)
    if s != order[0]:
        parts.append(f'<line x1="{X(i0)-3:.1f}" y1="{my}" x2="{X(i0)-3:.1f}" y2="{my+ph}" stroke="{RULE}" stroke-width="1"/>')
    mono(parts, (X(i0) + X(i1)) / 2, my + ph + 16, lab(s[:4]), 10.5, INK, "middle")
# the 2019-20 gap
gx0 = X(max(i for i, ss in enumerate(season_of) if ss == "20182019")) + 2; gx1 = X(starts["20202021"]) - 4
parts.append(f'<rect x="{gx0:.1f}" y="{my}" width="{gx1-gx0:.1f}" height="{ph}" fill="{PANEL}"/>')
parts.append(f'<text transform="translate({(gx0+gx1)/2+4:.1f},{my+ph/2:.1f}) rotate(-90)" font-size="9.5" fill="{SOFT}" text-anchor="middle">19-20: AHL, back injury</text>')
# lines
for key, col in (("ixg60", AMBER), ("p60", RED)):
    d = ""
    prev_s = None
    for r in rolling:
        i = r["idx"]
        cmd = "M" if d == "" or (season_of[i] == "20202021" and prev_s == "20182019") else "L"
        d += f"{cmd}{X(i):.1f},{Y(r[key]):.1f} "
        prev_s = season_of[i]
    parts.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
# injuries: numbered markers on the plot, key below (labels would collide at the right edge)
marks = [("2023-02-25", "kneecap, Feb 25 2023 (season over)"), ("2025-02-23", "head hit, Feb 2025 (missed 4)"),
         ("2025-11-20", "IR, Nov 2025 (missed 3)"), ("2026-03-12", "leg, Mar 2026 (missed 9, then 4 more)")]
key = []
for n, (date, text) in enumerate(marks, 1):
    i = max(j for j, g in enumerate(games) if g["date"] <= date)  # last game on or before the date
    x = X(i)
    parts.append(f'<line x1="{x:.1f}" y1="{my-4}" x2="{x:.1f}" y2="{my+ph}" stroke="{RED}" stroke-width="1" stroke-dasharray="2 3"/>')
    parts.append(f'<circle cx="{x:.1f}" cy="{my-12}" r="7" fill="{RED}"/>')
    mono(parts, x, my - 8.5, str(n), 9.5, PAPER, "middle", "600")
    key.append(f"{n} {text}")
sans(parts, 0, h - 56, "Injuries:  " + "    ".join(key[:2]), 10.5, SOFT)
sans(parts, 66, h - 42, "    ".join(key[2:]), 10.5, SOFT)
# peak annotation
peak = max(rolling, key=lambda r: r["p60"])
sans(parts, X(peak["idx"]) - 8, Y(peak["p60"]) - 8, f"peak {peak['p60']:.1f} P/60, {peak['date'][:7]}", 10, INK, "end", "600")
last20 = games[-20:]
sans(parts, 0, h - 26, f"The line ends at zero: his last 20 games of 2025-26 ({sum(g['toi'] for g in last20):.0f} minutes) produced no points. Last value: {rolling[-1]['ixg60']:.2f} ixG/60.", 10.5, SOFT)
source(parts, h, "Source: NHL API game logs and MoneyPuck shot xG, 2018-19 to 2025-26. Windows run across season breaks.")
close(parts, "c7-rolling.svg")

# =====================================================================
# C8  Age-curve comps: change in 5v5 P/60 from age 24-26 base to 27-28
# =====================================================================
rows = []
skipped = []
for c in age["comps"]:
    fut = [f for f in c["future"][:2] if f]
    if not fut:
        skipped.append(c["name"]); continue
    gp = sum(f["gp"] for f in fut)
    m = sum(f["p60"] * f["gp"] for f in fut) / gp
    rows.append((c["name"], c["base"]["p60"], m, m - c["base"]["p60"], gp))
rows.sort(key=lambda r: r[3])
vals = [r[3] for r in rows]
med = vals[len(vals) // 2] if len(vals) % 2 else (vals[len(vals)//2 - 1] + vals[len(vals)//2]) / 2
improved = sum(1 for v in vals if v > 0)
big = sum(1 for v in vals if v >= 0.5)
NAMED = {"Mike Santorelli": "Santorelli", "Zack Kassian": "Kassian", "Nick Paul": "Nick Paul", "Matt Calvert": "Calvert",
         "Radek Faksa": "Faksa", "Riley Sheahan": "Sheahan"}
h = 330
parts = svg_open(h, "What happened next to 30 forwards who looked like him at 24 to 26",
                 f"Change in 5v5 P/60, age 24-26 base to age 27-28 average. {improved} of {len(rows)} improved, median {med:+.2f}; {len(skipped)} of 30 out of the NHL.")
mx = 40; my = 80; pw = W - mx - 40; ph = 130
xmin, xmax = -0.8, 1.2
def X(v): return mx + pw * (v - xmin) / (xmax - xmin)
ybase = my + ph
parts.append(f'<line x1="{mx}" y1="{ybase}" x2="{mx+pw}" y2="{ybase}" stroke="{RULE}" stroke-width="1"/>')
for t in (-0.5, 0, 0.5, 1.0):
    parts.append(f'<line x1="{X(t):.1f}" y1="{my}" x2="{X(t):.1f}" y2="{ybase}" stroke="{RULE if t else SOFT}" stroke-width="1"/>')
    mono(parts, X(t), ybase + 16, f"{t:+.1f}" if t else "0", 10.5, SOFT, "middle")
sans(parts, mx + pw / 2, ybase + 34, "Change in 5v5 points per 60, age 24-26 base to age 27-28 (GP-weighted)", 11.5, SOFT, "middle")
# beeswarm: stack dots that would collide
R = 6.5
placed = []
for name, b, m, dv, gp in rows:
    x = X(dv); lvl = 0
    while any(abs(px - x) < 2 * R + 1 and pl == lvl for px, pl in placed):
        lvl += 1
    placed.append((x, lvl))
    y = ybase - 12 - lvl * (2 * R + 1)
    named = name in NAMED
    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R}" fill="{BLUE if named else GRAY}" stroke="{PAPER}" stroke-width="1.5"/>')
# labels for named dots, staggered above the swarm
tops = {}
for (name, b, m, dv, gp), (x, lvl) in zip(rows, placed):
    if name in NAMED:
        y = ybase - 12 - lvl * (2 * R + 1)
        tops[name] = (x, y, dv)
# assign label rows so they don't collide horizontally
lab_rows = []
for name in sorted(tops, key=lambda n: tops[n][0]):
    x, y, dv = tops[name]
    text = f"{NAMED[name]} {dv:+.2f}"
    wpx = 6.6 * len(text)
    row = 0
    while any(abs(lx - x) < (lw + wpx) / 2 + 8 and lr == row for lx, lw, lr in lab_rows):
        row += 1
    lab_rows.append((x, wpx, row))
    ly = my + 8 + row * 14
    parts.append(f'<line x1="{x:.1f}" y1="{ly+3}" x2="{x:.1f}" y2="{y-R-1:.1f}" stroke="{BLUE}" stroke-width="1" stroke-opacity="0.6"/>')
    mono(parts, x, ly, text, 10, INK, "middle", "600", halo=True)
# median
# median line; its tag sits below the axis so it stays clear of the named-comp labels above the swarm
parts.append(f'<line x1="{X(med):.1f}" y1="{my+2}" x2="{X(med):.1f}" y2="{ybase+6}" stroke="{RED}" stroke-width="2"/>')
mono(parts, X(med) + 6, ybase + 16, f"median {med:+.2f}", 10.5, RED, "start", "600", halo=True)
sans(parts, 0, h - 40, f"Smith-Pelly and Lindblom were out of the NHL by 27-28 and are not plotted. {big} of {len(rows)} gained 0.5+ P/60. His base: {age['target']['p60']:.2f} P/60.", 10.5, SOFT)
legend(parts, 0, h - 22, [("Named comp", BLUE, "dot"), ("Other comp", GRAY, "dot"), ("Median", RED, "line")])
source(parts, h, "Source: MoneyPuck 2010-11 to 2025-26. Comps = 30 nearest forwards on P/60, G/60, ixG/60, xGF%, TOI/GP, game score.")
close(parts, "c8-age-comps.svg")

# =====================================================================
# C9  2017 first-round skaters: points per game, GAx at the end
# =====================================================================
D = sorted(draft, key=lambda r: r["overall"])
row_h = 17
h = 66 + row_h * len(D) + 44
parts = svg_open(h, "The 2017 first round, pick by pick: points per game, with goals above expected",
                 "30 first-round skaters (No. 26 Oettinger is a goalie). Career NHL points per game; GAx = career goals minus xG.")
mx = 178; bw = W - mx - 232; vmax = 1.2
rank_ppg = 1 + sum(1 for r in D if r["p_per_gp"] > 0.34)
def X(v): return mx + bw * v / vmax
y = 60
for t in (0, 0.25, 0.5, 0.75, 1.0):
    parts.append(f'<line x1="{X(t):.1f}" y1="{y-6}" x2="{X(t):.1f}" y2="{y + row_h*len(D) - 4}" stroke="{RULE}" stroke-width="1"/>')
    mono(parts, X(t), y - 10, f"{t:.2f}".rstrip("0").rstrip(".") if t else "0", 10, SOFT, "middle")
mono(parts, mx + bw + 14, y - 10, "GP", 10, SOFT, "start")
mono(parts, mx + bw + 62, y - 10, "GAx", 10, SOFT, "start")
mono(parts, mx + bw + 108, y - 10, "25-26", 10, SOFT, "start")
for r in D:
    ras = r["name"] == "Michael Rasmussen"
    col = RED if ras else (GRAY if r["pos"] != "D" else RULE)
    nm = f"{r['overall']}. {r['name']}" + (" (D)" if r["pos"] == "D" else "")
    sans(parts, mx - 8, y + 12, nm, 11, INK if ras else SOFT, "end", "600" if ras else None)
    wpx = max(1, bw * r["p_per_gp"] / vmax)
    parts.append(f'<rect x="{mx}" y="{y+2}" width="{wpx:.1f}" height="{row_h-5}" rx="2" fill="{col}"/>')
    mono(parts, X(r["p_per_gp"]) + 5, y + 12, f"{r['p_per_gp']:.2f}", 10, INK if ras else SOFT, "start", "600" if ras else None)
    mono(parts, mx + bw + 14, y + 12, f"{int(r['gp'])}", 10, INK if ras else SOFT)
    mono(parts, mx + bw + 62, y + 12, f"{r['gax']:+.1f}", 10, (RED if ras else SOFT), "start", "600" if ras else None)
    l26 = f"{int(r['p_2025'])} in {int(r['gp_2025'])}" if r["gp_2025"] else "no NHL"
    mono(parts, mx + bw + 108, y + 12, l26, 10, INK if ras else SOFT)
    y += row_h
sans(parts, 0, y + 14, f"His -25.3 GAx is the worst in the round. 0.34 points per game ranks {ordinal(rank_ppg)} of 30, ahead of all but two defensemen.", 10.5, SOFT)
source(parts, h, "Source: MoneyPuck career totals through 2025-26, regular season. 25-26 column = points in games last season.")
close(parts, "c9-draft-class.svg")

# =====================================================================
# C10  Penalty kill: xGA/60 percentile by season
# =====================================================================
PS = [s for s in SEASONS if s in pk and "xGA60" in pk[s]]
h = 340
parts = svg_open(h, "On the penalty kill, the chances against have mostly been fine",
                 "On-ice PK xGA/60 rank among forwards with 60+ PK minutes. Taller bar = better than more of the league.")
mx = 100; my = 62; pw = W - mx - 20; ph = 180
def Y(v): return my + ph - ph * v / 100
for t in (0, 25, 50, 75, 100):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE if t != 50 else SOFT}" stroke-width="1"/>')
    mono(parts, mx - 8, Y(t) + 4, "50 (median)" if t == 50 else f"{t}", 10.5, SOFT, "end")
slot = pw / len(SLOTS[2:]); barw = 56
for i, s in enumerate(SLOTS[2:]):
    cx = mx + slot * (i + 0.5)
    if s not in pk or "xGA60" not in pk[s]:
        mono(parts, cx, Y(0) + 17, lab(s), 11.5, INK, "middle")
        mono(parts, cx, Y(0) + 31, "under 60 PK min", 10, MUTED, "middle")
        continue
    p = pk[s]["xGA60_pct_better_than"]
    parts.append(f'<rect x="{cx-barw/2:.1f}" y="{Y(p):.1f}" width="{barw}" height="{Y(0)-Y(p):.1f}" rx="3" fill="{RED}"/>')
    mono(parts, cx, Y(p) - 6, f"better than {p}%", 10.5, INK, "middle", "600")
    mono(parts, cx, Y(0) + 17, lab(s), 11.5, INK, "middle")
    mono(parts, cx, Y(0) + 31, f"xGA/60 {pk[s]['xGA60']:.1f}", 9.5, SOFT, "middle")
    mono(parts, cx, Y(0) + 43, f"median {pk[s]['league_med_xGA60']:.1f}", 9.5, SOFT, "middle")
    mono(parts, cx, Y(0) + 55, f"{pk[s]['pk_toi_min']} min, n={pk[s]['n_fw']}", 9.5, SOFT, "middle")
source(parts, h, "Source: MoneyPuck 4v5 on-ice rates. Actual GA/60 swings more (12th pct in 21-22, 75th in 23-24); xGA is steadier.")
close(parts, "c10-pk.svg")

# =====================================================================
# C11  Team context: DET 5v5 xGF% rank and sv%
# =====================================================================
TS = ["2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
h = 300
parts = svg_open(h, "The team around him: eight seasons at or near the bottom of the league",
                 "Detroit's 5v5 xG share rank (left) and 5v5 save percentage (right), 2018-19 to 2025-26. Gray = his AHL season.")
# left panel: rank
lx = 40; lw = 330; my = 88; ph = 140
def XL(i): return lx + lw * (i + 0.5) / len(TS)
def YR(r, n): return my + ph * (r - 1) / 31
sans(parts, lx, my - 28, "5v5 xG share, league rank (1 = best, taller = better)", 11.5, INK, weight="600")
for t in (1, 8, 16, 24, 32):
    parts.append(f'<line x1="{lx}" y1="{YR(t,32):.1f}" x2="{lx+lw}" y2="{YR(t,32):.1f}" stroke="{RULE}" stroke-width="1"/>')
    mono(parts, lx - 6, YR(t, 32) + 4, str(t), 10, SOFT, "end")
for i, s in enumerate(TS):
    r = team[s]["xGF%_rank"]; n = team[s]["n"]
    c = RED if s != "2019" else GRAY
    top = YR(r, n)
    parts.append(f'<rect x="{XL(i)-12:.1f}" y="{top:.1f}" width="24" height="{my+ph-top:.1f}" rx="2" fill="{c}" fill-opacity="{0.9 if s != '2019' else 0.6}"/>')
    mono(parts, XL(i), top - 5, f"{r}/{n}", 9, INK, "middle", "600")
    mono(parts, XL(i), my + ph + 16, lab(s), 9.5, INK if s != "2019" else MUTED, "middle")
    mono(parts, XL(i), my - 8, f"{100*team[s]['xGF%']:.1f}%", 9, SOFT, "middle")
# right panel: sv%
rx = 430; rw = 310
def XR(i): return rx + rw * (i + 0.5) / len(TS)
smin, smax = 0.895, 0.925
def YS(v): return my + ph - ph * (v - smin) / (smax - smin)
sans(parts, rx, my - 28, "5v5 save percentage", 11.5, INK, weight="600")
for t in (0.90, 0.91, 0.92):
    parts.append(f'<line x1="{rx}" y1="{YS(t):.1f}" x2="{rx+rw}" y2="{YS(t):.1f}" stroke="{RULE}" stroke-width="1"/>')
    mono(parts, rx - 6, YS(t) + 4, f".{int(round(t*1000))}", 10, SOFT, "end")
d = " ".join(f"{'M' if i==0 else 'L'}{XR(i):.1f},{YS(team[s]['sv%']):.1f}" for i, s in enumerate(TS))
parts.append(f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="2" stroke-linejoin="round"/>')
for i, s in enumerate(TS):
    v = team[s]["sv%"]
    parts.append(f'<circle cx="{XR(i):.1f}" cy="{YS(v):.1f}" r="4.5" fill="{BLUE if s != '2019' else GRAY}" stroke="{PAPER}" stroke-width="2"/>')
    up = i % 2 == 0
    mono(parts, XR(i), YS(v) + (-9 if up else 16), f".{int(round(v*1000))}", 9, SOFT, "middle")
    mono(parts, XR(i), my + ph + 16, lab(s), 9.5, INK if s != "2019" else MUTED, "middle")
sans(parts, 0, h - 26, "Detroit never ranked better than 21st in 5v5 xG share across his eight seasons; sv% rank ran 9th to 30th. Gray = his AHL season.", 10.5, SOFT)
source(parts, h, "Source: MoneyPuck team tables, 5v5, regular season. 2018-19 to 2020-21 had 31 teams; 2021-22 onward 32.")
close(parts, "c11-team-context.svg")

# =====================================================================
# C12  Evolving Hockey GAR vs xGAR by season
# =====================================================================
gar_tot = sum(eh["gar"][s]["GAR"][0] for s in EHS); xgar_tot = sum(eh["xgar"][s]["xGAR"][0] for s in EHS)
h = 400
parts = svg_open(h, "Goals above replacement: one real peak, then back to the margins",
                 f"GAR = goals above replacement from results; xGAR from chances. Career: GAR {gar_tot:.1f}, xGAR {xgar_tot:.1f}")
lx_end = legend(parts, 0, 60, [("GAR (results)", RED, "bar"), ("xGAR (chances)", GRAY, "bar")])
mono(parts, lx_end, 60, "small number = percentile among forwards", 10.5, SOFT)
mx = 50; my = 76; pw = W - mx - 20; ph = 190; ymin, ymax = -8, 12
def Y(v): return my + ph - ph * (v - ymin) / (ymax - ymin)
for t in (-5, 0, 5, 10):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE if t else SOFT}" stroke-width="1"/>')
    mono(parts, mx - 8, Y(t) + 4, f"{t:+d}" if t else "0", 10.5, SOFT, "end")
slot = pw / len(EHSLOTS); barw = 30; gapb = 4
for i, s in enumerate(EHSLOTS):
    cx = mx + slot * (i + 0.5)
    mono(parts, cx, Y(ymin) + 17, s, 11, INK if s != "19-20" else MUTED, "middle")
    if s == "19-20":
        mono(parts, cx, Y(ymin) + 31, "AHL", 10, MUTED, "middle"); continue
    g, gp_ = eh["gar"][s]["GAR"]; x, xp = eh["xgar"][s]["xGAR"]
    x1 = cx - barw - gapb / 2; x2 = cx + gapb / 2
    for xx, v, c in ((x1, g, RED), (x2, x, GRAY)):
        top, bot = (Y(v), Y(0)) if v >= 0 else (Y(0), Y(v))
        parts.append(f'<rect x="{xx:.1f}" y="{top:.1f}" width="{barw}" height="{max(bot-top,1):.1f}" rx="2" fill="{c}"/>')
    for xx, v, p in ((x1, g, gp_), (x2, x, xp)):
        ly = Y(v) - 6 if v >= 0 else Y(v) + 12
        mono(parts, xx + barw / 2, ly, f"{v:+.1f}", 10, INK, "middle", "600")
        mono(parts, xx + barw / 2, ly - 11 if v >= 0 else ly + 11, ordinal(p), 9, SOFT, "middle")
# 25-26 component strip
yb = Y(ymin) + 46
parts.append(f'<line x1="0" y1="{yb-10}" x2="{W}" y2="{yb-10}" stroke="{RULE}" stroke-width="1"/>')
c26 = eh["gar"]["25-26"]
sans(parts, 0, yb + 6, "2025-26 split:", 11.5, INK, weight="600")
xx = 110
for label, key in (("Offense", "Off_GAR"), ("Defense", "Def_GAR"), ("Penalty kill", "SHD_GAR")):
    v, p = c26[key]
    c = RED if v < 0 else BLUE
    sans(parts, xx, yb + 6, f"{label} {v:+.1f}", 11.5, INK)
    mono(parts, xx + 8 + 7 * len(f"{label} {v:+.1f}"), yb + 6, f"({ordinal(p)} pct)", 10.5, c, "start", "600")
    xx += 200
sans(parts, 0, yb + 24, "In 2025-26 the defense and penalty-kill components were career bests; the offense component sat in the league's bottom 5%.", 10.5, SOFT)
sans(parts, 0, yb + 40, "The 2022-23 peak: 9.3 GAR (82nd percentile) on 3.7 xGAR (56th). Results ran well ahead of the chances that season.", 10.5, SOFT)
source(parts, h, "Source: Evolving Hockey (evolving-hockey.com), regular seasons 2018-19 to 2025-26. Forward percentiles, 20+ GP.")
close(parts, "c12-gar-xgar.svg")

# =====================================================================
# C13  RAPM even-strength isolated impact, one dot per season
# =====================================================================
h = 470
parts = svg_open(h, "Isolated even-strength impact, season by season (Evolving Hockey RAPM)",
                 "Teammates, competition, zone starts and score regressed out. Right = creates more chances, up = allows fewer.")
mx = 70; my = 70; pw = W - mx - 30; ph = 300
xmin, xmax = -0.22, 0.22; ymin, ymax = -0.14, 0.14
def X(v): return mx + pw * (v - xmin) / (xmax - xmin)
def Y(v): return my + ph - ph * (v - ymin) / (ymax - ymin)
for t in (-0.2, -0.1, 0, 0.1, 0.2):
    parts.append(f'<line x1="{X(t):.1f}" y1="{my}" x2="{X(t):.1f}" y2="{my+ph}" stroke="{RULE if t else SOFT}" stroke-width="1"/>')
    mono(parts, X(t), my + ph + 16, f"{t:+.1f}" if t else "0", 10.5, SOFT, "middle")
for t in (-0.1, 0, 0.1):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE if t else SOFT}" stroke-width="1"/>')
    mono(parts, mx - 8, Y(t) + 4, f"{t:+.1f}" if t else "0", 10.5, SOFT, "end")
sans(parts, mx + pw / 2, my + ph + 36, "RAPM xGF/60 impact (offense created per 60; right = better)", 11.5, SOFT, "middle")
parts.append(f'<text transform="translate(16,{my+ph/2}) rotate(-90)" font-size="11.5" fill="{SOFT}" text-anchor="middle">RAPM xGA/60 impact, sign flipped (defense; up = better)</text>')
# quadrant labels
sans(parts, mx + pw - 6, my + 14, "creates and suppresses", 10.5, MUTED, "end")
sans(parts, mx + 6, my + 14, "suppresses, does not create", 10.5, MUTED, "start")
sans(parts, mx + 6, my + ph - 8, "neither", 10.5, MUTED, "start")
sans(parts, mx + pw - 6, my + ph - 8, "creates, leaks", 10.5, MUTED, "end")
pts = [(s, eh["rapm_ev"][s]["xGF/60"][0], -eh["rapm_ev"][s]["xGA/60"][0]) for s in EHS]
d = " ".join(f"{'M' if i==0 else 'L'}{X(x):.1f},{Y(y):.1f}" for i, (s, x, y) in enumerate(pts))
parts.append(f'<path d="{d}" fill="none" stroke="{RED}" stroke-width="1.5" stroke-opacity="0.45" stroke-linejoin="round"/>')
offs = {"18-19": (-10, 4, "end"), "20-21": (10, 14, "start"), "21-22": (-10, 4, "end"), "22-23": (10, 4, "start"),
        "23-24": (10, 14, "start"), "24-25": (10, -6, "start"), "25-26": (-11, 4, "end")}
for i, (s, x, y) in enumerate(pts):
    last = s == "25-26"
    parts.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="{7 if last else 6}" fill="{RED}" fill-opacity="{1 if last or s == "22-23" else 0.55}" stroke="{PAPER}" stroke-width="2"/>')
    dx, dy, an = offs[s]
    sans(parts, X(x) + dx, Y(y) + dy, s, 11, INK, an, "600")
    mono(parts, X(x) + dx, Y(y) + dy + 12, f"{x:+.2f} / {y:+.2f}", 9.5, SOFT, an)
sans(parts, 0, h - 24, "Only 2022-23 landed in the good-both-ways quadrant (81st pct offense, 75th defense). 2025-26: 34th pct offense, 55th defense.", 10.5, SOFT)
source(parts, h, "Source: Evolving Hockey (evolving-hockey.com) RAPM EV rates, regular seasons 2018-19 to 2025-26.")
close(parts, "c13-rapm-off-def.svg")

# =====================================================================
# C14  Quality of teammates and competition, percentiles by season
# =====================================================================
h = 330
parts = svg_open(h, "Bottom-quartile linemates every season, and mostly ordinary competition",
                 "Teammate and competition quality = RAPM xG impact of the skaters he shared EV ice with (forward percentile).")
legend(parts, 0, 60, [("Teammates", RED, "line"), ("Competition", BLUE, "line")])
mx = 108; my = 76; pw = W - mx - 30; ph = 170
def Y(v): return my + ph - ph * v / 100
slot = pw / len(EHSLOTS)
def Xs(s): return mx + slot * (EHSLOTS.index(s) + 0.5)
for t in (0, 25, 50, 75, 100):
    parts.append(f'<line x1="{mx}" y1="{Y(t):.1f}" x2="{mx+pw}" y2="{Y(t):.1f}" stroke="{RULE if t != 50 else SOFT}" stroke-width="1"/>')
    mono(parts, mx - 8, Y(t) + 4, {50: "50 (median)", 25: "25 (quartile)"}.get(t, str(t)), 10.5, SOFT, "end")
gx = mx + slot * EHSLOTS.index("19-20")
parts.append(f'<rect x="{gx:.1f}" y="{my}" width="{slot:.1f}" height="{ph}" fill="{PANEL}"/>')
sans(parts, Xs("19-20"), my + ph / 2 + 4, "AHL", 10.5, MUTED, "middle")
for key, col, name, dy in (("qoc", BLUE, "Competition", -9), ("qot", RED, "Teammates", 14)):
    ser = [(s, eh[key][s]["RAPM_xG±/60"][1]) for s in EHS]
    segs = [ser[:1], ser[1:]]
    for seg in segs:
        if len(seg) > 1:
            d = " ".join(f"{'M' if i==0 else 'L'}{Xs(s):.1f},{Y(v):.1f}" for i, (s, v) in enumerate(seg))
            parts.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')
    parts.append(f'<line x1="{Xs("18-19"):.1f}" y1="{Y(ser[0][1]):.1f}" x2="{Xs("20-21"):.1f}" y2="{Y(ser[1][1]):.1f}" stroke="{col}" stroke-width="1.5" stroke-dasharray="3 4" stroke-opacity="0.6"/>')
    for s, v in ser:
        parts.append(f'<circle cx="{Xs(s):.1f}" cy="{Y(v):.1f}" r="4.5" fill="{col}" stroke="{PAPER}" stroke-width="2"/>')
        mono(parts, Xs(s), Y(v) + (-9 if v < 12 else dy), ordinal(v), 10, INK, "middle", "600")
for s in EHSLOTS:
    mono(parts, Xs(s), my + ph + 16, s, 11, INK if s != "19-20" else MUTED, "middle")
sans(parts, 0, h - 26, "Teammate quality never topped the 25th percentile (0th in 2018-19). Competition ran 41st to 66th, then fell to 21st in 2025-26.", 10.5, SOFT)
source(parts, h, "Source: Evolving Hockey (evolving-hockey.com) QoT / QoC EV rates, regular seasons 2018-19 to 2025-26.")
close(parts, "c14-qot-qoc.svg")

# ---- contact sheet HTML ----
names = ["c1-career-arc", "c2-goals-vs-xg", "c3-danger-conversion", "c4-luck-test", "c5-role-splits", "c6-lines-with-without",
         "c7-rolling", "c8-age-comps", "c9-draft-class", "c10-pk", "c11-team-context", "c12-gar-xgar", "c13-rapm-off-def", "c14-qot-qoc"]
html = ["<!doctype html><meta charset='utf-8'><style>body{margin:0;padding:12px;background:#fff;width:776px}figure{margin:0 0 14px 0}svg{display:block}</style>"]
for n in names:
    html.append(f"<figure>{(OUT / (n + '.svg')).read_text()}</figure>")
(OUT / "contact-sheet.html").write_text("\n".join(html))
print("wrote contact-sheet.html")
print("done")
