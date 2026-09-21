#!/usr/bin/env python3
"""Inline-ready SVG charts for the Wes & Woodward Sandin-Pellikka column.
Dependency-free. Same kit as the Kreider / Rasmussen packages:
subject #ce1126, secondary #2a78d6, accent #c98500, field grey #b3b1ad."""
import json, math, pathlib, statistics

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW, OUT = ROOT / "raw", ROOT / "charts"
PAPER = "#d7d6d3"; PANEL = "#e7e6e3"; RULE = "#c4c3bf"; INK = "#141414"; SOFT = "#575653"; MUTED = "#8a8781"
RED = "#ce1126"; BLUE = "#2a78d6"; AMBER = "#c98500"; GRAY = "#b3b1ad"
SANS = "'Space Grotesk', ui-sans-serif, system-ui, sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, monospace"
W = 760

def esc(s): return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def svg_open(h, title, sub=None):
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" '
         f'aria-label="{esc(title)}" font-family="{SANS}" style="max-width:100%;height:auto;background:{PAPER}">',
         f'<rect width="{W}" height="{h}" fill="{PAPER}"/>',
         f'<text x="0" y="20" font-size="17" font-weight="600" fill="{INK}">{esc(title)}</text>']
    if sub: p.append(f'<text x="0" y="38" font-size="12" fill="{SOFT}">{esc(sub)}</text>')
    return p
def source(p, h, text): p.append(f'<text x="0" y="{h-8}" font-size="10.5" font-family="{MONO}" fill="{MUTED}">{esc(text)}</text>')
def close(p, name):
    p.append("</svg>"); (OUT / name).write_text("\n".join(p)); print("wrote", name)
def txt(p, x, y, s, size=12, fill=INK, anchor="start", weight=None, mono=False):
    w = f' font-weight="{weight}"' if weight else ""; f = f' font-family="{MONO}"' if mono else ""
    p.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}{f}>{esc(s)}</text>')
def legend(p, x, y, items):
    cx = x
    for name, col in items:
        p.append(f'<circle cx="{cx+5}" cy="{y-4}" r="5" fill="{col}"/>'); txt(p, cx+15, y, name); cx += 15 + 7.0*len(name) + 22

A = json.load(open(RAW / "analysis.json"))
ROLL = json.load(open(RAW / "asp_rolling10.json"))
GAMES = json.load(open(RAW / "asp_gamelog_merged.json"))
PCT = json.load(open(RAW / "asp_percentiles_5v5.json"))


# ---------- c1: ice time fell, the underlying play did not ----------
def c1():
    h = 400
    p = svg_open(h, "His ice time fell by a quarter. His share of the chances did not move.",
                 "Rolling 10-game average: total ice time per game (left) and on-ice 5v5 xGF% (right), 2025-26")
    x0, x1, y0, y1 = 52, 700, 78, 280
    n = len(ROLL)
    def X(i): return x0 + i * (x1 - x0) / (n - 1)
    def Yt(v): return y1 - (v - 8) / (24 - 8) * (y1 - y0)      # TOI 8-24 min
    def Yx(v): return y1 - (v - 35) / (65 - 35) * (y1 - y0)    # xGF% 35-65
    for v in (10, 14, 18, 22):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Yt(v):.1f}" y2="{Yt(v):.1f}" stroke="{RULE}" stroke-width="0.8"/>')
        txt(p, x0 - 8, Yt(v) + 4, f"{v}", 11, SOFT, "end", mono=True)
    for v in (40, 50, 60):
        txt(p, x1 + 8, Yx(v) + 4, f"{v}%", 11, BLUE, "start", mono=True)
    p.append(f'<line x1="{x0}" x2="{x1}" y1="{Yx(50):.1f}" y2="{Yx(50):.1f}" stroke="{BLUE}" stroke-width="1" stroke-dasharray="3 3" opacity="0.5"/>')
    for key, Y, col, wd in (("toi", Yt, RED, 3), ("xgfpct", Yx, BLUE, 2.2)):
        pts = " ".join(f"{X(i):.1f},{Y(r[key]):.1f}" for i, r in enumerate(ROLL))
        p.append(f'<polyline fill="none" stroke="{col}" stroke-width="{wd}" points="{pts}"/>')
    # endpoint callouts
    txt(p, X(0) + 4, Yt(ROLL[0]["toi"]) - 10, f'{ROLL[0]["toi"]:.1f} min', 11, RED, "start", 600, True)
    txt(p, X(n-1) - 4, Yt(ROLL[-1]["toi"]) - 10, f'{ROLL[-1]["toi"]:.1f} min', 11, RED, "end", 600, True)
    txt(p, X(0) + 4, Yx(ROLL[0]["xgfpct"]) + 16, f'{ROLL[0]["xgfpct"]:.0f}%', 11, BLUE, "start", 600, True)
    txt(p, X(n-1) - 4, Yx(ROLL[-1]["xgfpct"]) + 16, f'{ROLL[-1]["xgfpct"]:.0f}%', 11, BLUE, "end", 600, True)
    # event marks (game numbers in his own game log)
    for gno, lab, dy, anc in ((59, "Olympic break", -26, "end"), (63, "deadline: Faulk in", -10, "end")):
        i = next((k for k, r in enumerate(ROLL) if r["g"] >= gno), None)
        if i is None: continue
        p.append(f'<line x1="{X(i):.1f}" x2="{X(i):.1f}" y1="{y0+dy+4}" y2="{y1}" stroke="{MUTED}" stroke-width="1" stroke-dasharray="2 3"/>')
        txt(p, X(i) - 4, y0 + dy, lab, 10.5, MUTED, anc)
    for i, r in enumerate(ROLL):
        if r["g"] % 10 == 0 or i == n - 1:
            txt(p, X(i), y1 + 18, f'g{r["g"]}', 10.5, SOFT, "middle", mono=True)
    txt(p, 0, y1 + 52, "First 34 games: 18.4 min a night, 48.1% xGF.   Last 34 games: 14.0 min, 47.0% xGF.", 12.5, INK, weight=600)
    txt(p, 0, y1 + 70, "Seven straight healthy scratches after the March 6 deadline, then Grand Rapids on March 23.", 11.5, SOFT)
    legend(p, 0, h - 26, [("ice time per game, all situations", RED), ("on-ice xGF%, 5v5", BLUE)])
    source(p, h, "HockeyStatCards game logs (Natural Stat Trick data) joined to the NHL API game log. 10-game rolling mean.")
    close(p, "c1-toi-vs-play.svg")


# ---------- c2: the luck ledger ----------
def c2():
    h = 340
    p = svg_open(h, "Twelve and a half goals separated what happened from what was supposed to happen.",
                 "On-ice goals vs expected goals with Sandin-Pellikka on the ice, all situations, 2025-26")
    x0, y0 = 60, 78
    bw, gap = 300, 60
    mx = 60.0
    def L(v): return v / mx * bw
    s = A["asp_season"]["all"]
    rowsd = [("Goals for", s["xgf"], s["gf"], "shooting"), ("Goals against", s["xga"], s["ga"], "goaltending")]
    for k, (lab, x, a, note) in enumerate(rowsd):
        y = y0 + k * 92
        txt(p, 0, y - 12, lab, 12.5, INK, weight=600)
        p.append(f'<rect x="{x0}" y="{y}" width="{L(x):.1f}" height="22" fill="{GRAY}"/>')
        p.append(f'<rect x="{x0}" y="{y+28}" width="{L(a):.1f}" height="22" fill="{RED if k==0 else INK}"/>')
        txt(p, x0 + L(x) + 8, y + 16, f"{x:.1f} expected", 11.5, SOFT, mono=True)
        txt(p, x0 + L(a) + 8, y + 44, f"{a:.0f} actual", 11.5, INK, "start", 600, True)
        d = a - x
        txt(p, x0 + bw + 130, y + 30, f"{d:+.1f} goals ({note})", 12, RED if (k == 0) == (d < 0) else INK, weight=600)
    txt(p, 0, h - 62, "Net: 12.5 goals of on-ice variance against him, which is most of a -20.", 13, INK, weight=600)
    txt(p, 0, h - 42, "His on-ice 5v5 save percentage, .885, was the lowest of any Red Wing with 300+ minutes. The team ranged up to .938.", 11.5, SOFT)
    source(p, h, "MoneyPuck 2025-26 season summary, all situations. League 5v5 on-ice Sv% baseline .905.")
    close(p, "c2-luck-ledger.svg")


# ---------- c3: percentile bars ----------
def c3():
    order = [("Corsi share (CF%)", "CF%"), ("Chances created (xGF/60)", "xGF/60"),
             ("Own shot volume (ixG/60)", "ixG/60"), ("Chance share (xGF%)", "xGF%"),
             ("Relative chance share", "rel xGF%"), ("High-danger chances against/60", "HDCA/60"),
             ("Chances against (xGA/60)", "xGA/60"), ("Goals against (GA/60)", "GA/60"),
             ("On-ice PDO", "PDO")]
    h = 60 + len(order) * 30 + 66
    p = svg_open(h, "The offence was ordinary. The defending was bottom-decile. The results were worse than both.",
                 "Percentile among 237 NHL defencemen with 300+ 5v5 minutes, 2025-26 (higher is better on every row)")
    x0, x1 = 250, 700
    def X(v): return x0 + v / 100 * (x1 - x0)
    for v in (0, 25, 50, 75, 100):
        p.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="60" y2="{60+len(order)*30-8}" stroke="{RULE}" stroke-width="{1.4 if v==50 else 0.8}"/>')
        txt(p, X(v), 54, str(v), 10.5, SOFT, "middle", mono=True)
    for i, (lab, key) in enumerate(order):
        y = 60 + i * 30
        v = PCT[key]["pctile"]
        col = RED if v < 25 else (AMBER if v < 45 else BLUE)
        txt(p, 0, y + 15, lab, 12, INK)
        p.append(f'<rect x="{x0}" y="{y+4}" width="{max(X(v)-x0,2):.1f}" height="17" fill="{col}"/>')
        txt(p, X(v) + 8, y + 17, f'{v:.0f}', 11.5, col, "start", 600, True)
    txt(p, 0, h - 44, "Read the bottom four rows together: he gave up more, and then more went in than should have.", 12, INK, weight=600)
    source(p, h, "MoneyPuck 2025-26 season summary, 5v5. Rates inverted where lower is better.")
    close(p, "c3-percentiles.svg")


# ---------- c4: age-20 cohort scatter ----------
def c4():
    coh = A["cohort"]
    h = 462
    p = svg_open(h, "He had the lowest puck luck of any age-20 defenceman in sixteen years.",
                 "Defencemen with 40+ NHL games in their age-20 season, 2010-11 to 2025-26 (n = 69)")
    x0, x1, y0, y1 = 62, 700, 66, 330
    xs = [c["rel"] for c in coh]; ys = [c["pdo"] for c in coh]
    xlo, xhi, ylo, yhi = -11, 8, 96, 104
    def X(v): return x0 + (v - xlo) / (xhi - xlo) * (x1 - x0)
    def Y(v): return y1 - (v - ylo) / (yhi - ylo) * (y1 - y0)
    p.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="{PANEL}" opacity="0.45"/>')
    for v in (96, 98, 100, 102, 104):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{RULE}" stroke-width="{1.4 if v==100 else 0.8}"/>')
        txt(p, x0 - 8, Y(v) + 4, str(v), 11, SOFT, "end", mono=True)
    for v in (-10, -5, 0, 5):
        p.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{y0}" y2="{y1}" stroke="{RULE}" stroke-width="{1.4 if v==0 else 0.8}"/>')
        txt(p, X(v), y1 + 18, f"{v:+d}" if v else "0", 11, SOFT, "middle", mono=True)
    LABEL = {"Erik Karlsson", "Cale Makar", "Lane Hutson", "Moritz Seider", "Rasmus Dahlin",
             "Drew Doughty", "Darnell Nurse", "Denton Mateychuk", "Tom Willander", "Victor Hedman"}
    for c in coh:
        if c["name"] == "Axel Sandin-Pellikka": continue
        p.append(f'<circle cx="{X(c["rel"]):.1f}" cy="{Y(c["pdo"]):.1f}" r="4.5" fill="{GRAY}" opacity="0.85"/>')
        if c["name"] in LABEL:
            txt(p, X(c["rel"]), Y(c["pdo"]) - 9, c["name"].split()[-1], 10, SOFT, "middle")
    a = next(c for c in coh if c["name"] == "Axel Sandin-Pellikka")
    p.append(f'<circle cx="{X(a["rel"]):.1f}" cy="{Y(a["pdo"]):.1f}" r="7.5" fill="{RED}" stroke="{PAPER}" stroke-width="2"/>')
    txt(p, X(a["rel"]) + 14, Y(a["pdo"]) + 4, "Sandin-Pellikka", 12, RED, "start", 600)
    txt(p, x0, y1 + 44, "Relative chance share (on-ice xGF% minus the same team without him)  →", 11.5, SOFT)
    txt(p, x0, y0 - 12, "↑ On-ice PDO (shooting + save percentage behind him)", 11.5, SOFT)
    txt(p, 0, h - 56, "He is bottom-third on the horizontal axis, which is real, and dead last on the vertical, which is not his doing.", 12, INK, weight=600)
    txt(p, 0, h - 38, "Karlsson, Dahlin, Hanifin and Ferraro sat in the same corner at the same age.", 11.5, SOFT)
    source(p, h, "NHL API bios for the cohort; MoneyPuck 5v5 season summaries 2010-2025. Age on September 15.")
    close(p, "c4-age20-scatter.svg")


# ---------- c5: what happened to the ones who graded out badly ----------
def c5():
    tiers = A["cohort_tiers"]
    h = 330
    p = svg_open(h, "Grading out badly at twenty told you almost nothing about what came next.",
                 "Career NHL games played, by age-20 relative chance share. Age-20 seasons 2010-11 to 2020-21 (n = 57)")
    x0, x1 = 240, 600
    def X(v): return x0 + min(v, 1300) / 1300 * (x1 - x0)
    for i, t in enumerate(tiers):
        y = 78 + i * 74
        txt(p, 0, y, t["label"], 12.5, INK, weight=600)
        txt(p, 0, y + 17, f'n = {t["n"]}', 11, SOFT, mono=True)
        gps = [gp for _, gp in t["names"]]
        for gp in gps:
            p.append(f'<circle cx="{X(gp):.1f}" cy="{y+6}" r="4.5" fill="{GRAY}" opacity="0.8"/>')
        m = t["medianCareerGP"]
        p.append(f'<line x1="{X(m):.1f}" x2="{X(m):.1f}" y1="{y-10}" y2="{y+22}" stroke="{RED}" stroke-width="2.5"/>')
        txt(p, X(m), y + 36, f"median {m:.0f} games", 11, RED, "middle", 600, True)
        txt(p, x1 + 20, y + 10, f'{t["pct500"]:.0f}% reached 500 games', 11, SOFT, mono=True)
    for v in (0, 400, 800, 1200):
        txt(p, X(v), 60, str(v), 10.5, SOFT, "middle", mono=True)
    txt(p, 0, h - 46, "Correlation between age-20 relative chance share and career games: r = +0.31.", 12.5, INK, weight=600)
    txt(p, 0, h - 28, "The worst-grading tier still produced Karlsson, Carlson, Leddy, Brodin, Lindholm and Nurse. "
                      "Caveat: everyone here already played 40 NHL games at twenty.", 11, SOFT)
    source(p, h, "NHL API career totals as of Sept 18, 2026; MoneyPuck 5v5 season summaries.")
    close(p, "c5-cohort-outcomes.svg")


# ---------- c6: Chiarot's partners ----------
def c6():
    pr = [d for d in A["pairings"] if "Chiarot" in d["name"] and d["toi"] >= 100]
    pr.sort(key=lambda d: -d["toi"])
    h = 100 + len(pr) * 42 + 60
    p = svg_open(h, "Same partner, same result: the 20-year-old and the $6.5M deadline rental.",
                 "Ben Chiarot's pairings, 5v5 chance share and minutes, Detroit 2025-26")
    x0, x1 = 210, 640
    def X(v): return x0 + (v - 25) / (65 - 25) * (x1 - x0)
    for v in (30, 40, 50, 60):
        p.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="64" y2="{64+len(pr)*42-10}" stroke="{RULE}" stroke-width="{1.4 if v==50 else 0.8}"/>')
        txt(p, X(v), 58, f"{v}%", 10.5, SOFT, "middle", mono=True)
    for i, d in enumerate(pr):
        y = 70 + i * 42
        other = d["name"].replace("Chiarot-", "").replace("-Chiarot", "")
        hl = "Sandin-Pellikka" in other
        col = RED if hl else (AMBER if "Faulk" in other else GRAY)
        txt(p, 0, y + 16, f"with {other}", 12, INK if hl else SOFT, weight=600 if hl else None)
        p.append(f'<rect x="{X(25)}" y="{y+4}" width="{X(d["xgfPct"])-X(25):.1f}" height="18" fill="{col}"/>')
        txt(p, X(d["xgfPct"]) + 8, y + 17, f'{d["xgfPct"]:.0f}%', 11.5, RED if hl else (AMBER if col == AMBER else SOFT), "start", 600, True)
        txt(p, x1 + 60, y + 17, f'{d["toi"]:.0f} min', 11, MUTED, "end", mono=True)
    txt(p, 0, h - 44, "Chiarot alongside Sandin-Pellikka: 46%, over 573 minutes. Chiarot alongside Faulk: 47%, over 249.", 12, INK, weight=600)
    txt(p, 0, h - 26, "The one pairing that worked, Johansson and Sandin-Pellikka, went 58% and was outscored 6-10.", 11.5, SOFT)
    source(p, h, "MoneyPuck 2025-26 line file, Detroit pairings with 100+ 5v5 minutes.")
    close(p, "c6-chiarot-partners.svg")



# ---------- c7: GAR vs xGAR, the results-vs-chances split ----------
def c7():
    P = A["eh_percentiles"]
    g = P["gar_all_seasons_d2526.csv"]; x = P["xgar_all_seasons_d2526.csv"]
    pairs = [("Even-strength offence", g["EVO_GAR"], x["xEVO_GAR"]),
             ("Even-strength defence", g["EVD_GAR"], x["xEVD_GAR"]),
             ("Total value", g["GAR"], x["xGAR"])]
    h = 360
    p = svg_open(h, "By chances he was an above-average NHL defenceman. By results he was below replacement.",
                 "Evolving Hockey GAR (what happened) vs xGAR (what the chances deserved), percentile among 249 NHL defencemen with 20+ GP")
    x0, x1 = 235, 690
    def X(v): return x0 + v / 100 * (x1 - x0)
    for v in (0, 25, 50, 75, 100):
        p.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="70" y2="{70+len(pairs)*82-22}" stroke="{RULE}" stroke-width="{1.4 if v==50 else 0.8}"/>')
        txt(p, X(v), 64, str(v), 10.5, SOFT, "middle", mono=True)
    for i, (lab, gg, xx) in enumerate(pairs):
        y = 78 + i * 82
        txt(p, 0, y + 4, lab, 12.5, INK, weight=600)
        for j, (d, col, tag) in enumerate(((gg, INK, "GAR"), (xx, RED, "xGAR"))):
            yy = y + j * 26
            p.append(f'<rect x="{x0}" y="{yy-11}" width="{max(X(d["pctile"])-x0,2):.1f}" height="17" fill="{col}"/>')
            txt(p, X(d["pctile"]) + 8, yy + 2, f'{d["pctile"]:.0f}  ({d["value"]:+.1f})', 11, col, "start", 600, True)
            txt(p, x0 - 10, yy + 2, tag, 11, col, "end", mono=True)
    txt(p, 0, h - 62, "Total value: 20th percentile by results, 58th by chances. The gap is 5.2 goals.", 12.5, INK, weight=600)
    txt(p, 0, h - 42, "The even-strength offence gap is the whole story: 44th percentile scored, 82nd percentile created.", 11.5, SOFT)
    source(p, h, "Evolving Hockey GAR / xGAR (subscriber data), 2025-26 regular season. Defencemen with 20+ GP, n = 249.")
    close(p, "c7-gar-vs-xgar.svg")


# ---------- c8: quality of competition vs ice time, by phase ----------
def c8():
    ph = A["qoc"]["phases"]
    h = 420
    p = svg_open(h, "They cut his minutes and gave him harder opponents, not easier ones.",
                 "By phase: his 5v5 ice time per game, and the quality of the opponents he faced (TOI-weighted mean opponent xGAR/60)")
    x0, x1, y0, y1 = 70, 700, 76, 268
    n = len(ph)
    def X(i): return x0 + 55 + i * (x1 - x0 - 110) / (n - 1)
    def Yt(v): return y1 - (v - 9) / (17 - 9) * (y1 - y0)
    def Yq(v): return y1 - (v - 0.10) / (0.36 - 0.10) * (y1 - y0)
    for v in (10, 12, 14, 16):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Yt(v):.1f}" y2="{Yt(v):.1f}" stroke="{RULE}" stroke-width="0.8"/>')
        txt(p, x0 - 8, Yt(v) + 4, f"{v}", 11, RED, "end", mono=True)
    for v in (0.15, 0.25, 0.35):
        txt(p, x1 + 8, Yq(v) + 4, f"{v:.2f}", 11, BLUE, "start", mono=True)
    for key, Y, col, dat in (("toi5v5PerGp", Yt, RED, ph), ("qoc", Yq, BLUE, ph)):
        pts = [(X(i), Y(r[key])) for i, r in enumerate(dat)]
        p.append('<polyline fill="none" stroke="%s" stroke-width="3" points="%s"/>' % (col, " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)))
        for a, b in pts:
            p.append(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="5" fill="{col}" stroke="{PAPER}" stroke-width="1.5"/>')
    for i, r in enumerate(ph):
        txt(p, X(i), Yt(r["toi5v5PerGp"]) + 20, f'{r["toi5v5PerGp"]:.1f}', 11, RED, "middle", 600, True)
        txt(p, X(i), Yq(r["qoc"]) - 12, f'{r["qoc"]:.2f}', 11, BLUE, "middle", 600, True)
        for k, line in enumerate(r["label"].replace(" - ", "-").split(" ")):
            txt(p, X(i), y1 + 22 + k * 13, line, 10.5, SOFT, "middle")
    txt(p, 0, y1 + 80, "Game-level correlation between his ice time that night and the quality of his opponents: r = -0.21.", 12.5, INK, weight=600)
    txt(p, 0, y1 + 100, "His five games before the demotion were his lowest minutes and his toughest competition of the season.", 11.5, SOFT)
    legend(p, 0, h - 26, [("5v5 ice time per game", RED), ("opponent quality (xGAR/60)", BLUE)])
    source(p, h, "NHL shift charts rebuilt to 5v5 seconds, opponents scored by Evolving Hockey 2025-26 xGAR/60. 93.8% of opponent seconds scored.")
    close(p, "c8-qoc-vs-icetime.svg")


for f in (c1, c2, c3, c4, c5, c6, c7, c8):
    f()

# ---- contact sheet ----
names = ["c1-toi-vs-play", "c7-gar-vs-xgar", "c2-luck-ledger", "c3-percentiles",
         "c8-qoc-vs-icetime", "c4-age20-scatter", "c5-cohort-outcomes", "c6-chiarot-partners"]
html = ["<!doctype html><meta charset='utf-8'><style>body{margin:0;padding:12px;background:#fff;width:776px}"
        "figure{margin:0 0 14px 0}svg{display:block}</style>"]
for n in names:
    html.append(f"<figure>{(OUT / (n + '.svg')).read_text()}</figure>")
(OUT / "contact-sheet.html").write_text("\n".join(html))
print("wrote contact-sheet.html")
