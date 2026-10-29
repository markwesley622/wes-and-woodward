#!/usr/bin/env python3
"""SVG charts for the finishing-problem article, frozen to the Oct 29, 2026 pull so they never change under the copy.
usage: make_charts.py SHOTS_2026_CSV SHOTS_2025_CSV   (MoneyPuck shot files; the season tables come from raw/2026-10-29/)
Writes charts/c1_radar.svg .. c4_gibson_pk.svg and copies them to data/site/articles/red-wings-finishing-problem/.
Same house style as research/brandsegg-nygard/scripts/make_charts.py: CSS vars with light fallbacks so the files stand alone."""
import csv, html, json, math, pathlib, shutil, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW = HERE / "raw/2026-10-29"
OUT = HERE / "charts"; OUT.mkdir(exist_ok=True)
SITE = ROOT / "data/site/articles/red-wings-finishing-problem"; SITE.mkdir(parents=True, exist_ok=True)
SHOTS26, SHOTS25 = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])

STYLE = """<style>
.wwc .a{fill:var(--c-a,#2f55a8)}.wwc .b{fill:var(--c-b,#ce1126)}.wwc .sa{stroke:var(--c-a,#2f55a8)}.wwc .sb{stroke:var(--c-b,#ce1126)}.wwc .ink{fill:var(--ink,#141414)}.wwc .mut{fill:var(--muted,#5f5e5a)}.wwc .grid{stroke:var(--rule,#c4c3bf);stroke-width:1}.wwc .ax{stroke:var(--ink,#141414);stroke-width:1}.wwc .surf{fill:var(--panel,#e7e6e3)}.wwc .paper{fill:var(--paper,#e9e8e5)}.wwc .bar{fill:var(--muted,#5f5e5a);opacity:.55}.wwc .lbl{font-size:12px;letter-spacing:.08em;text-transform:uppercase;fill:var(--ink,#141414)}.wwc text{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11px}.wwc .t{font-family:"Space Grotesk",system-ui,sans-serif;font-size:14px;font-weight:600}.wwc .sub{font-size:11px}
</style>"""
def svg(w, h, body, title, desc):
    return f'<svg class="wwc" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d"><title id="t">{html.escape(title)}</title><desc id="d">{html.escape(desc)}</desc>{STYLE}{body}</svg>'
def txt(x, y, s, cls="ink", anchor="start", extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}" {extra}>{html.escape(str(s))}</text>'
def f(r, k): return float(r[k])
def i(r, k): return int(float(r[k] or 0))

# ---- c1 the team page radar, as it stood on Oct 29 (dashboard.json from the nightly build, commit 3b2cca6)
def c1():
    D = json.load(open(ROOT / "data/site/dashboard.json"))
    R = D["radar"]; assert D["generatedAt"].startswith("2026-10-29"), D["generatedAt"]
    N = len(R["dimensions"]); SIZE = 600; C = SIZE / 2; RAD = 205; LABEL = 250; PAD = 60   # PAD: room for the side labels
    ang = lambda k: -math.pi / 2 + 2 * math.pi * k / N
    pt = lambda k, v: (C + math.cos(ang(k)) * RAD * v / 100, C + math.sin(ang(k)) * RAD * v / 100)
    poly = lambda key: " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(k, d[key]) for k, d in enumerate(R["dimensions"])))
    NAMES = {"CAR": "Carolina", "MIN": "Minnesota", "EDM": "Edmonton", "BOS": "Boston"}
    top3 = ", ".join(NAMES.get(t, t) for t in R["top3"])
    body = ""
    for r in (25, 50, 75, 100): body += f'<circle cx="{C}" cy="{C}" r="{RAD * r / 100:.1f}" class="grid" style="fill:none"/>'
    for k in range(N):
        x, y = pt(k, 100); body += f'<line x1="{C}" y1="{C}" x2="{x:.1f}" y2="{y:.1f}" class="grid"/>'
    body += f'<polygon points="{poly("top3")}" style="fill:rgba(20,20,20,.06);stroke:var(--ink,#141414);stroke-width:1.6;stroke-dasharray:6 5"/>'
    body += f'<polygon points="{poly("det")}" style="fill:rgba(206,17,38,.18);stroke:var(--c-b,#ce1126);stroke-width:2.4"/>'
    for k, d in enumerate(R["dimensions"]):
        x, y = pt(k, d["top3"]); body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" class="paper" style="stroke:var(--ink,#141414);stroke-width:1.6"/>'
    for k, d in enumerate(R["dimensions"]):
        x, y = pt(k, d["det"]); body += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" class="b"/>'
    for k, d in enumerate(R["dimensions"]):
        c = math.cos(ang(k)); anchor = "start" if c > 0.2 else "end" if c < -0.2 else "middle"
        x, y = C + c * LABEL, C + math.sin(ang(k)) * LABEL
        body += txt(x, y, d["label"], "lbl", anchor, 'dominant-baseline="middle"')
        # the percentile beside each Detroit dot
        dx, dy = pt(k, d["det"]); off = 14 if d["det"] < 50 else -14
        body += txt(dx + (10 if c > 0.2 else -10 if c < -0.2 else 0), dy + (off if abs(c) <= 0.2 else 4), f"{d['det']:.0f}", "ink", anchor)
    y0 = SIZE + 16
    body += f'<rect x="20" y="{y0 - 2}" width="16" height="3" class="b"/>' + txt(44, y0 + 2, "Detroit", "ink")
    body += f'<rect x="120" y="{y0 - 2}" width="16" height="3" class="ink"/>' + txt(144, y0 + 2, f"Top three, average · {top3}", "ink")
    body += txt(20, y0 + 22, "League percentiles · 2026-27 through Oct. 28 · the team page as of Oct. 29", "mut")
    body = f'<g transform="translate({PAD},0)">{body}</g>'
    desc = "Radar of seven league percentiles for Detroit against the top-three average: " + "; ".join(f"{d['label']} {d['det']:.0f} vs {d['top3']:.0f}" for d in R["dimensions"]) + "."
    return svg(SIZE + 2 * PAD, SIZE + 50, body, "Seven dimensions of winning, Detroit against the top three, Oct. 29, 2026", desc)

# ---- c2 medium-danger conversion, all 32 teams
def c2():
    rows = [r for r in csv.DictReader(open(RAW / "teams.csv")) if r["situation"] == "all"]
    conv = sorted(((f(r, "mediumDangerGoalsFor") / f(r, "mediumDangerShotsFor") * 100, r["team"], f(r, "mediumDangerGoalsFor"), f(r, "mediumDangerShotsFor")) for r in rows), reverse=True)
    lg = sum(f(r, "mediumDangerGoalsFor") for r in rows) / sum(f(r, "mediumDangerShotsFor") for r in rows) * 100
    W, H = 700, 330; x0, y0, x1, y1 = 40, 70, 684, 280
    bw = (x1 - x0) / 32; vmax = 20
    sy = lambda v: y1 - (y1 - y0) * v / vmax
    body = txt(16, 24, "Medium-danger conversion, all 32 teams, through Oct. 28", "t") + txt(16, 42, "Goals divided by shots carrying .08 to .20 expected goals (MoneyPuck). Detroit in red.", "mut sub")
    for v in (5, 10, 15, 20):
        body += f'<line x1="{x0}" y1="{sy(v):.1f}" x2="{x1}" y2="{sy(v):.1f}" class="grid"/>' + txt(x0 - 6, sy(v) + 4, f"{v}%", "mut", "end")
    body += f'<line x1="{x0}" y1="{sy(lg):.1f}" x2="{x1}" y2="{sy(lg):.1f}" class="ax" style="stroke-dasharray:5 4"/>' + txt(x1, sy(lg) - 5, f"league {lg:.1f}%", "ink", "end")
    for k, (v, t, g, s) in enumerate(conv):
        x = x0 + k * bw + 2
        cls = "b" if t == "DET" else "bar"
        body += f'<rect x="{x:.1f}" y="{sy(v):.1f}" width="{bw - 4:.1f}" height="{y1 - sy(v):.1f}" rx="1.5" class="{cls}"/>'
        if t == "DET" or k == 0:
            body += txt(x + (bw - 4) / 2, sy(v) - 6, t, "ink" if t == "DET" else "mut", "middle")
        if t == "DET": body += txt(x + (bw - 4) / 2 - 24, sy(v) - 30, f"Detroit, {g:.0f} of {s:.0f}, {v:.1f}%", "ink", "middle")
    body += f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" class="ax"/>' + txt(x0, y1 + 18, "best", "mut") + txt(x1, y1 + 18, "worst", "mut", "end")
    body += txt(16, H - 12, "30th of 32. Only Los Angeles (5.8%) and Tampa Bay (6.2%) are lower. Detroit, 11 goals on 167 shots.", "mut")
    return svg(W, H, body, "Medium-danger conversion by team", f"Bar chart of medium-danger shooting percentage for all 32 teams; Detroit is 30th at 6.6% against a league rate of {lg:.1f}%.")

# ---- c3 Detroit shooters, medium-danger goals against expected (shot level, the article's numbers)
def c3():
    # MoneyPuck's season table (skaters.csv, all situations), the same numbers the copy quotes for Raymond, DeBrincat and Arvidsson
    agg = {}
    for r in csv.DictReader(open(RAW / "skaters.csv")):
        if r["team"] == "DET" and r["situation"] == "all":
            n = "Michael Brandsegg-Nygård" if "Brandsegg" in r["name"] else r["name"]
            agg[n] = [int(f(r, "I_F_mediumDangerShots")), f(r, "I_F_mediumDangerxGoals"), int(f(r, "I_F_mediumDangerGoals"))]
    names = ["Lucas Raymond", "Alex DeBrincat", "Viktor Arvidsson", "Dylan Larkin", "Andrew Copp", "Michael Brandsegg-Nygård", "Emmitt Finnie", "Michael Rasmussen"]
    data = [(n, *agg[n]) for n in names]
    W = 700; rowh = 34; H = 70 + rowh * len(data) + 36; x0, x1 = 230, 600; vmax = 3.6
    sx = lambda v: x0 + (x1 - x0) * v / vmax
    body = txt(16, 24, "Detroit's medium-danger shooters: goals against what the model expected", "t") + txt(16, 42, "Hollow bar = expected goals on those shots (MoneyPuck). Solid = goals. Regular season through Oct. 28.", "mut sub")
    for k, (n, shots, xg, g) in enumerate(data):
        y = 70 + k * rowh
        body += txt(x0 - 12, y + 16, n, "ink", "end")
        body += f'<rect x="{x0}" y="{y + 3}" width="{sx(xg) - x0:.1f}" height="11" rx="2" class="sb" style="fill:none;stroke-width:1.6"/>'
        if g: body += f'<rect x="{x0}" y="{y + 16}" width="{sx(g) - x0:.1f}" height="11" rx="2" class="b"/>'
        else: body += f'<line x1="{x0}" y1="{y + 21.5}" x2="{x0 + 3}" y2="{y + 21.5}" class="sb" style="stroke-width:11"/>'
        body += txt(sx(xg) + 8, y + 12, f"{xg:.1f} xG on {shots} shots", "mut") + txt(sx(max(g, 0.12)) + 8, y + 25, f"{g} goal{'s' if g != 1 else ''}", "ink")
    y = 70 + rowh * len(data)
    body += f'<line x1="{x0}" y1="{y + 4}" x2="{x1}" y2="{y + 4}" class="ax"/>'
    for v in (0, 1, 2, 3): body += txt(sx(v), y + 20, str(v), "mut", "middle") + f'<line x1="{sx(v):.1f}" y1="{y + 4}" x2="{sx(v):.1f}" y2="{y + 8}" class="ax"/>'
    tot_g = sum(d[3] for d in data[:3]); tot_x = sum(d[2] for d in data[:3]); tot_s = sum(d[1] for d in data[:3])
    body += txt(16, H - 8, f"Raymond, DeBrincat and Arvidsson together: {tot_g} goals on {tot_s} shots where the model expected {tot_x:.1f}.", "mut")
    return svg(W, H, body, "Medium-danger goals against expected, Detroit shooters", "Paired bars for eight Red Wings: expected goals on medium-danger shots against actual goals; Raymond is 0 on 2.8, DeBrincat 2 on 3.1, Arvidsson 1 on 2.7, Copp 1 on 1.9.")

# ---- c4 Gibson on the kill: cumulative save percentage by game, last season against this one
def gibson_curve(path):
    rows = [r for r in csv.DictReader(open(path)) if r["isPlayoffGame"] == "0" and r["goalieNameForShot"] == "John Gibson" and int(r["period"]) <= 4]
    def pk(r):   # strict 5-on-4 against him, the same split as MoneyPuck's 4on5 goalie table the article quotes
        hs, as_ = i(r, "homeSkatersOnIce"), i(r, "awaySkatersOnIce"); home = r["isHomeTeam"] in ("1", "1.0")
        shooter, goalie = (hs, as_) if home else (as_, hs)
        return shooter == 5 and goalie == 4 and i(r, "homeEmptyNet") == 0 and i(r, "awayEmptyNet") == 0
    games = sorted({r["game_id"] for r in rows}, key=int)
    out, s, g = [], 0, 0
    for gid in games:
        for r in rows:
            if r["game_id"] == gid and pk(r) and (i(r, "shotWasOnGoal") or i(r, "goal")): s += 1; g += i(r, "goal")
        out.append((s, g, (s - g) / s if s else None))
    return out
def c4():
    A, B = gibson_curve(SHOTS25), gibson_curve(SHOTS26)
    W, H = 700, 320; x0, y0, x1, y1 = 60, 66, 670, 262; gmax = 60
    sx = lambda gp: x0 + (x1 - x0) * gp / gmax
    sy = lambda v: y1 - (y1 - y0) * (v - 0.55) / (1.0 - 0.55)
    body = txt(16, 24, "John Gibson on the penalty kill: save percentage, running total by game", "t") + txt(16, 42, "Shots on goal at 5-on-4 against him. Last season in black, this season in red.", "mut sub")
    for v in (0.6, 0.7, 0.8, 0.9, 1.0):
        body += f'<line x1="{x0}" y1="{sy(v):.1f}" x2="{x1}" y2="{sy(v):.1f}" class="grid"/>' + txt(x0 - 8, sy(v) + 4, f".{v * 1000:.0f}"[:4], "mut", "end")
    lg = 0.856
    body += f'<line x1="{x0}" y1="{sy(lg):.1f}" x2="{x1}" y2="{sy(lg):.1f}" class="ax" style="stroke-dasharray:5 4"/>' + txt(x1, sy(lg) - 8, "league .856 last season", "mut", "end")
    def line(curve, cls, start=4):
        pts = [(sx(k + 1), sy(v)) for k, (s, g, v) in enumerate(curve) if v is not None and s >= 8]
        return f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" class="{cls}" style="fill:none;stroke-width:2.2;stroke-linejoin:round"/>' if pts else ""
    body += line(A, "ax") + line(B, "sb")
    sA, gA, vA = A[-1]; sB, gB, vB = B[-1]
    body += f'<circle cx="{sx(len(A)):.1f}" cy="{sy(vA):.1f}" r="4" class="ink"/>' + txt(sx(len(A)) - 8, sy(vA) + 20, f"2025-26: .{vA * 1000:.0f} ({gA} GA on {sA} shots, {len(A)} GP)", "ink", "end")
    body += f'<circle cx="{sx(len(B)):.1f}" cy="{sy(vB):.1f}" r="5" class="b"/>' + txt(sx(len(B)) + 10, sy(vB) + 4, f"2026-27: .{vB * 1000:.0f} ({gB} GA on {sB} shots, {len(B)} GP)", "ink")
    for gp in (10, 20, 30, 40, 50): body += txt(sx(gp), y1 + 18, f"GP {gp}", "mut", "middle") + f'<line x1="{sx(gp):.1f}" y1="{y1}" x2="{sx(gp):.1f}" y2="{y1 + 4}" class="ax"/>'
    body += f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" class="ax"/>'
    v8, v12 = A[7][2], A[11][2]
    body += txt(16, H - 10, f"Lines start at eight shots faced. Last season: .{v8 * 1000:.0f} through 8 GP, .{v12 * 1000:.0f} through 12, .{vA * 1000:.0f} at the end.", "mut")
    print("gibson 5v4:", "25-26", sA, gA, round(vA, 3), "through 8", round(v8, 3), "through 12", round(v12, 3), "| 26-27", sB, gB, round(vB, 3))
    return svg(W, H, body, "Gibson's penalty-kill save percentage, running total", f"Two lines: Gibson's cumulative shorthanded save percentage through 2025-26, finishing at .{vA * 1000:.0f} after a league-average start, and through eight games of 2026-27 at .{vB * 1000:.0f}.")

for name, fn in (("c1_radar", c1), ("c2_md_conversion", c2), ("c3_shooters", c3), ("c4_gibson_pk", c4)):
    s = fn(); (OUT / f"{name}.svg").write_text(s); shutil.copy(OUT / f"{name}.svg", SITE / f"{name}.svg"); print(name, len(s), "bytes")
