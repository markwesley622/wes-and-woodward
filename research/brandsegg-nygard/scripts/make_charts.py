"""SVG charts for the MBN glow-up brief. usage: make_charts.py OUT_DIR. Colors via CSS vars with light fallbacks so files stand alone."""
import json, sys, math, html
OUT = sys.argv[1]
S = json.load(open(f"{OUT}/summary.json")); G = json.load(open(f"{OUT}/onice_games.json")); T = json.load(open(f"{OUT}/team_table.json"))
A, B = "20252026", "20262027"; LA, LB = "2025-26", "2026-27"
STYLE = """<style>
.wwc .a{fill:var(--c-a,#2f55a8)}.wwc .b{fill:var(--c-b,#ce1126)}.wwc .sa{stroke:var(--c-a,#2f55a8)}.wwc .sb{stroke:var(--c-b,#ce1126)}.wwc .ink{fill:var(--ink,#141414)}.wwc .mut{fill:var(--muted,#5f5e5a)}.wwc .grid{stroke:var(--rule,#c4c3bf);stroke-width:1}.wwc .ax{stroke:var(--ink,#141414);stroke-width:1}.wwc .surf{fill:var(--panel,#e7e6e3)}.wwc .rink{stroke:var(--rule,#c4c3bf);fill:none;stroke-width:1.5}.wwc text{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:11px}.wwc .t{font-family:"Space Grotesk",system-ui,sans-serif;font-size:14px;font-weight:600}.wwc .sub{font-size:11px}
</style>"""
def svg(w, h, body, title, desc):
    return f'<svg class="wwc" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d"><title id="t">{html.escape(title)}</title><desc id="d">{html.escape(desc)}</desc>{STYLE}{body}</svg>'
def txt(x, y, s, cls="ink", anchor="start", extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}" {extra}>{html.escape(str(s))}</text>'
def legend(x, y):
    return (f'<rect x="{x}" y="{y-9}" width="12" height="12" rx="2" class="a"/>' + txt(x+17, y+1, f"{LA} (first 10 GP)", "mut") +
            f'<rect x="{x+165}" y="{y-9}" width="12" height="12" rx="2" class="b"/>' + txt(x+182, y+1, f"{LB} (first 10 GP)", "mut"))

# ---- c1 shot map: two half rinks, unblocked attempts, area ~ xG
def halfrink(ox, oy, scale):
    # offensive half: x from 25 (red line) .. 100 (boards); y -42.5..42.5 ; draw rotated so net at top
    # map rink (x,y) -> svg: sx = ox + (y+42.5)*scale ; sy = oy + (100-x)*scale
    w = 85*scale; h = 75*scale
    r = 28*scale
    d = (f'<path class="rink" d="M{ox},{oy+h} L{ox},{oy+r} A{r},{r} 0 0 1 {ox+r},{oy} L{ox+w-r},{oy} A{r},{r} 0 0 1 {ox+w},{oy+r} L{ox+w},{oy+h} Z"/>'
         f'<line class="rink" x1="{ox}" y1="{oy+(100-89)*scale:.1f}" x2="{ox+w}" y2="{oy+(100-89)*scale:.1f}" style="stroke:var(--c-b,#ce1126);opacity:.6"/>'  # goal line
         f'<line class="rink" x1="{ox}" y1="{oy+(100-25)*scale:.1f}" x2="{ox+w}" y2="{oy+(100-25)*scale:.1f}" style="stroke-dasharray:4 4"/>'  # blue line at x=25
         f'<rect class="rink" x="{ox+(42.5-3)*scale:.1f}" y="{oy+(100-89)*scale:.1f}" width="{6*scale:.1f}" height="{4*scale:.1f}" rx="1"/>'
         f'<circle class="rink" cx="{ox+(42.5+22)*scale:.1f}" cy="{oy+(100-69)*scale:.1f}" r="{15*scale:.1f}"/><circle class="rink" cx="{ox+(42.5-22)*scale:.1f}" cy="{oy+(100-69)*scale:.1f}" r="{15*scale:.1f}"/>')
    return d
def c1():
    sc = 3.2; W = 700; H = 375
    body = txt(16, 24, "Same volume, different ice: every unblocked attempt, first 10 games", "t") + txt(16, 42, "Dot area = MoneyPuck xG. Filled ring = goal. Dashed line = blue line, red line = goal line.", "mut sub")
    for i, (s, lab, cls, scls) in enumerate(((A, LA, "a", "sa"), (B, LB, "b", "sb"))):
        ox = 40 + i*340; oy = 70
        body += halfrink(ox, oy, sc)
        shots = [x for g in G[s] for x in g["ishots"]]
        for sh in sorted(shots, key=lambda z: -z["xg"]):
            x, y = abs(sh["x"]), sh["y"]
            if x < 25: x = 25.5
            sx = ox + (y+42.5)*sc; sy = oy + (100-x)*sc
            r = max(2.2, 2.2 + 26*math.sqrt(sh["xg"]))
            goal = sh["goal"] == "1"
            body += f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r:.1f}" class="{cls}" style="opacity:.55"/>' + (f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r+2.5:.1f}" class="{scls}" style="fill:none;stroke-width:2"/>' if goal else "")
        st = S[s]
        body += txt(ox, oy + 75*sc + 20, f"{lab}: {st['shots_mp']} attempts, {st['ixg_all']} xG", "ink") + txt(ox, oy + 75*sc + 36, f"avg {st['avg_dist']} ft out, {st['share_inside_25ft']:.0f}% inside 25 ft", "mut") + txt(ox, oy + 75*sc + 50, f"{st['hd_shots_0.1plus']} attempts worth 0.10+ xG", "mut")
    return svg(W, H, body, "Shot map, first 10 games of each season", "Two half-rink scatter plots of Brandsegg-Nygård's unblocked shot attempts; 2026-27 attempts cluster in the low slot while 2025-26 attempts sit at the circles and points.")

# ---- c2 deployment dumbbells
def c2():
    rows = [("TOI per game (min)", S[A]["toi_per_gp"], S[B]["toi_per_gp"], 0, 22, "{:.1f}"),
            ("5v5 TOI per game (min)", S[A]["toi_5v5_per_gp"], S[B]["toi_5v5_per_gp"], 0, 22, "{:.1f}"),
            ("Shifts per game", S[A]["shifts_per_gp"], S[B]["shifts_per_gp"], 0, 25, "{:.1f}"),
            ("Last 5 min, 1-goal game (min/GP)", S[A]["close_late_min_per_gp"], S[B]["close_late_min_per_gp"], 0, 1.2, "{:.2f}"),
            ("Share of team PP time (%)", S[A]["pp_share_of_team"], S[B]["pp_share_of_team"], 0, 100, "{:.0f}"),
            ("5v5 time beside DET's 3 most-used F (%)", 100*S[A]["qot_top3F_share"], 100*S[B]["qot_top3F_share"], 0, 100, "{:.0f}"),
            ("5v5 time against opp's 3 most-used F (%)", 100*S[A]["qoc_top3F_share"], 100*S[B]["qoc_top3F_share"], 0, 100, "{:.0f}"),
            ("Offensive-zone start share, O/(O+D) (%)", S[A]["oZS_pct"], S[B]["oZS_pct"], 0, 100, "{:.0f}")]
    W, H = 700, 60 + 34*len(rows) + 30; x0, x1 = 300, 660
    body = txt(16, 24, "Deployment: a third-liner became a second-liner", "t") + legend(16, 44)
    for i, (lab, a, b, lo, hi, fmt) in enumerate(rows):
        y = 78 + i*34
        xa = x0 + (a-lo)/(hi-lo)*(x1-x0); xb = x0 + (b-lo)/(hi-lo)*(x1-x0)
        body += txt(x0-12, y+4, lab, "ink", "end") + f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" class="grid"/>'
        body += f'<line x1="{xa:.1f}" y1="{y}" x2="{xb:.1f}" y2="{y}" class="ax" style="stroke-width:2;stroke:var(--rule,#c4c3bf)"/>'
        body += f'<circle cx="{xa:.1f}" cy="{y}" r="6" class="a"/><circle cx="{xb:.1f}" cy="{y}" r="6" class="b"/>'
        la, lb = fmt.format(a), fmt.format(b)
        left, right = (xa, xb) if xa <= xb else (xb, xa)
        body += txt(left-10, y+4, la if xa <= xb else lb, "mut", "end") + txt(right+10, y+4, lb if xa <= xb else la, "ink")
    return svg(W, H, body, "Deployment comparison", "Dumbbell chart of eight deployment measures for the two 10-game samples; minutes, shifts, late-close usage and linemate quality all rose, zone starts and competition barely moved.")

# ---- c3 xGF% by score state
def c3():
    states = [("tied", "Tied"), ("lead", "Leading"), ("trail", "Trailing")]
    W, H = 700, 300; x0, y0, x1, y1 = 70, 70, 660, 240
    body = txt(16, 24, "5v5 expected-goal share by score state", "t") + legend(16, 44)
    for v in (30, 40, 50, 60, 70, 80, 90):
        y = y1 - (v-30)/60*(y1-y0)
        body += f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" class="{"ax" if v==50 else "grid"}"/>' + txt(x0-8, y+4, f"{v}%", "mut", "end")
    gw = (x1-x0)/3
    for i, (k, lab) in enumerate(states):
        gx = x0 + i*gw + gw*0.2
        for j, (s, cls) in enumerate(((A, "a"), (B, "b"))):
            d = S[s]["by_score"][k]; v = d["xgf_pct"]; bw = gw*0.25
            x = gx + j*(bw+6); y = y1 - (v-30)/60*(y1-y0)
            body += f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{y1-y:.1f}" rx="3" class="{cls}"/>'
            body += txt(x+bw/2, y-6, f"{v:.0f}%", "ink", "middle")
        da, db = S[A]["by_score"][k], S[B]["by_score"][k]
        body += txt(gx + (gw*0.25+3), y1+17, lab, "ink", "middle") + txt(gx + (gw*0.25+3), y1+32, f"xG {da['xgf']}-{da['xga']} vs {db['xgf']}-{db['xga']}", "mut", "middle")
    return svg(W, H, body, "xGF% by score state", "Grouped bars: 2025-26 was 52% tied, 43% leading and 86% trailing; 2026-27 is 65% tied, 71% leading and 60% trailing.")

# ---- c4 goals vs expected
def c4():
    W, H = 700, 250; x0, x1 = 230, 640
    rows = [(LA, "a", S[A]), (LB, "b", S[B])]
    body = txt(16, 24, "5v5 on-ice goals vs expected goals", "t") + txt(16, 42, "Hollow bar = expected (MoneyPuck). Solid = actual.", "mut sub")
    mx = 14
    def bar(y, val, cls, hollow):
        w = val/mx*(x1-x0)
        st = f'style="fill:none;stroke-width:2"' if hollow else ""
        return f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="14" rx="3" class="{("s"+cls) if hollow else cls}" {st}/>'
    y = 70
    for lab, cls, st in rows:
        body += txt(x0-12, y+12, f"{lab} goals for", "ink", "end") + bar(y, st["xgf"], cls, True) + bar(y+16, st["gf"], cls, False)
        body += txt(x0 + st["xgf"]/mx*(x1-x0) + 8, y+12, f"{st['xgf']} xGF", "mut") + txt(x0 + st["gf"]/mx*(x1-x0) + 8, y+28, f"{st['gf']} GF, on-ice sh% {st['on_sh_pct']}", "ink")
        y += 44
        body += txt(x0-12, y+12, f"{lab} goals against", "ink", "end") + bar(y, st["xga"], cls, True) + bar(y+16, st["ga"], cls, False)
        body += txt(x0 + st["xga"]/mx*(x1-x0) + 8, y+12, f"{st['xga']} xGA", "mut") + txt(x0 + st["ga"]/mx*(x1-x0) + 8, y+28, f"{st['ga']} GA, on-ice sv% {st['on_sv_pct']}", "ink")
        y += 50
    return svg(W, H, body, "Goals vs expected goals, 5v5 on-ice", "Paired bars: 2025-26 on-ice 1 goal for on 4.8 expected and 6 against on 3.1; 2026-27 10 for on 7.7 expected and 1 against on 4.5.")

# ---- c5 team strip
def c5():
    W, H = 700, 330; x0, x1 = 60, 660
    body = txt(16, 24, "5v5 xGF% among Red Wings skaters, first 10 games (60+ min)", "t") + legend(16, 44)
    for i, (s, cls, lab) in enumerate(((A, "a", LA), (B, "b", LB))):
        y = 110 + i*110
        body += txt(16, y-38, lab, "ink") + f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" class="grid"/>'
        for v in (35, 40, 45, 50, 55, 60, 65):
            x = x0 + (v-33)/34*(x1-x0); body += f'<line x1="{x:.1f}" y1="{y-5}" x2="{x:.1f}" y2="{y+5}" class="{"ax" if v==50 else "grid"}"/>' + txt(x, y+22, f"{v}", "mut", "middle")
        rows = T[s]; placed = []
        for r in rows:
            me = "Brandsegg" in r["name"]; x = x0 + (r["xgf_pct"]-33)/34*(x1-x0)
            lvl = 0
            while any(abs(x-px) < 9 and pl == lvl for px, pl in placed): lvl += 1
            placed.append((x, lvl)); yy = y - 12 - lvl*11 if not me else y
            if me: body += f'<circle cx="{x:.1f}" cy="{y}" r="8" class="{cls}"/>' + txt(x, y-16, f"MBN {r['xgf_pct']}%", "ink", "middle")
            else: body += f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="4" class="mut" style="opacity:.75"/>'
        others = [r for r in rows if "Brandsegg" not in r["name"]]
        body += txt(x1, y+40, f"next best: {others[0]['name']} {others[0]['xgf_pct']}%; team off-ice with him on bench {S[s]['off_xgf_pct']}%", "mut", "end")
    return svg(W, H, body, "Team xGF% strip", "Strip plots of Red Wings skaters' 5v5 xGF% over each 10-game sample; Brandsegg-Nygård is first in both years.")

# ---- c6 linemates
def c6():
    W, H = 700, 330; x0, x1 = 230, 640
    body = txt(16, 24, "Who he skated with at 5v5 (minutes, first 10 games)", "t") + legend(16, 44)
    mx = 95
    for i, (s, cls) in enumerate(((A, "a"), (B, "b"))):
        mates = list(S[s]["top_mates"].items())[:6]; y = 70 + i*130
        for j, (k, v) in enumerate(mates):
            name, pos = k.split("|"); yy = y + j*19
            body += txt(x0-12, yy+10, f"{name} ({pos})", "ink", "end") + f'<rect x="{x0}" y="{yy}" width="{v/mx*(x1-x0):.1f}" height="12" rx="3" class="{cls}"/>' + txt(x0 + v/mx*(x1-x0) + 6, yy+10, f"{v:.0f}", "mut")
    return svg(W, H, body, "Linemates", "Horizontal bars of 5v5 minutes with each teammate: Compher and Copp in 2025-26, Finnie and DeBrincat in 2026-27.")

for name, fn in (("c1_shotmap", c1), ("c2_deployment", c2), ("c3_scorestate", c3), ("c4_goals_vs_xg", c4), ("c5_team_strip", c5), ("c6_linemates", c6)):
    open(f"{OUT}/charts/{name}.svg", "w").write(fn()); print("wrote", name)
