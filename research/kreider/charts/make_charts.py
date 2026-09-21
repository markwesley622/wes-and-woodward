#!/usr/bin/env python3
"""Inline-ready SVG charts for the Wes & Woodward Chris Kreider column.
Dependency-free. Site tokens + validated palette from the wings-type kit:
Kreider #ce1126, comps #2a78d6 / #c98500, field grey #b3b1ad."""
import json, csv, math, statistics, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"; OUT = ROOT / "charts"
PAPER = "#d7d6d3"; PANEL = "#e7e6e3"; RULE = "#c4c3bf"; INK = "#141414"; SOFT = "#575653"; MUTED = "#8a8781"
RED = "#ce1126"; BLUE = "#2a78d6"; AMBER = "#c98500"; GRAY = "#b3b1ad"; DARK = "#141414"
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

eh = json.load(open(RAW/"eh_ranks.json")); arc = json.load(open(RAW/"kreider_mp_arc.json"))
st = json.load(open(RAW/"kreider_shottype.json")); ranks = json.load(open(RAW/"tip_ranks.json"))
seg = json.load(open(RAW/"kreider_segments_2025.json")); age = json.load(open(RAW/"age_comps.json"))
p5 = json.load(open(RAW/"kreider_5v5_pcts.json")); feat = json.load(open(RAW/"forward_features_2025.json"))
dims = json.load(open(RAW/"similarity_2025.json"))["style_dims"]

# ---------- c1: value arc (EH GAR / xGAR percentile among forwards, by season) ----------
def c1():
    seasons = ['18-19','19-20','20-21','21-22','22-23','23-24','24-25','25-26']
    h = 330; p = svg_open(h, "Kreider was a top-quartile forward for six seasons. The last two are middle-six.",
                          "Evolving Hockey GAR and xGAR, percentile among forwards with 41+ GP, by season")
    x0, x1, y0, y1 = 60, 720, 60, 270
    def X(i): return x0 + i*(x1-x0)/(len(seasons)-1)
    def Y(v): return y1 - (v/100)*(y1-y0)
    for v in (0,25,50,75,100):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="{RULE}" stroke-width="{1.5 if v==50 else 0.8}"/>'); txt(p, x0-8, Y(v)+4, f"{v}", 11, SOFT, "end", mono=True)
    p.append(f'<rect x="{x0}" y="{Y(75)}" width="{x1-x0}" height="{Y(50)-Y(75)}" fill="{PANEL}" opacity="0.6"/>')
    txt(p, x1, Y(75)-4, "top quartile above this line", 10.5, MUTED, "end")
    K = eh["Chris Kreider"]
    for key, col, lab in (("xGAR_pct", GRAY, "xGAR (chance-based)"), ("GAR_pct", RED, "GAR (results)")):
        pts = [(X(i), Y(K[s][key])) for i, s in enumerate(seasons)]
        p.append('<polyline fill="none" stroke="%s" stroke-width="%s" points="%s"/>' % (col, 3 if col==RED else 2.2, " ".join(f"{x:.1f},{y:.1f}" for x,y in pts)))
        for (x,y), s in zip(pts, seasons):
            p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{col}" stroke="{PAPER}" stroke-width="1.5"/>')
            if col==RED: txt(p, x+(12 if s=="18-19" else 0), y+18 if s in ("18-19","24-25","25-26") else y-10, f'{K[s]["GAR_pct"]}', 11, RED, "middle", 600, True)
    for i, s in enumerate(seasons): txt(p, X(i), y1+18, "20"+s.replace("-", "-"), 11, SOFT, "middle", mono=True)
    txt(p, X(3), Y(100)-8, "52-goal year (xGAR 98th)", 10.5, MUTED, "middle")
    legend(p, x0, h-30, [("GAR (results)", RED), ("xGAR (chance-based)", GRAY)])
    source(p, h, "Evolving Hockey GAR / xGAR (subscriber data). Forwards with 41+ GP, n = 353-395 per season.")
    close(p, "c1-value-arc.svg")

# ---------- c2: 5v5 goals vs chances, percentiles 2021-2025 ----------
def c2():
    ys = ["2021","2022","2023","2024","2025"]
    h = 300; p = svg_open(h, "At 5v5 the chances slipped one tier. The finishing fell two.",
                          "5v5 individual xG/60 and goals/60, percentile among forwards (41+ GP, 500+ 5v5 min)")
    x0, x1, y0, y1 = 60, 720, 60, 240
    def X(i): return x0 + 40 + i*(x1-x0-80)/(len(ys)-1)
    def Y(v): return y1 - (v/100)*(y1-y0)
    for v in (0,25,50,75,100):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="{RULE}" stroke-width="{1.5 if v==50 else 0.8}"/>'); txt(p, x0-8, Y(v)+4, f"{v}", 11, SOFT, "end", mono=True)
    for key, col, lab in (("ixg60_pct", GRAY, "ixG/60"), ("g60_pct", RED, "G/60")):
        pts = [(X(i), Y(p5[y][key])) for i, y in enumerate(ys)]
        p.append('<polyline fill="none" stroke="%s" stroke-width="%s" points="%s"/>' % (col, 3 if col==RED else 2.2, " ".join(f"{x:.1f},{y:.1f}" for x,y in pts)))
        for (x,y), yr in zip(pts, ys):
            p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{col}" stroke="{PAPER}" stroke-width="1.5"/>')
            val = p5[yr]["g60"] if col==RED else p5[yr]["ixg60"]
            txt(p, x, y+17 if col==RED else y-9, f'{val:.2f}', 10.5, RED if col==RED else SOFT, "middle", 600, True)
    for i, y in enumerate(ys): txt(p, X(i), y1+18, f"{y}-{str(int(y)+1)[2:]}", 11, SOFT, "middle", mono=True)
    legend(p, x0, h-30, [("Goals/60 (rank)", RED), ("Individual xG/60 (rank)", GRAY)])
    source(p, h, "MoneyPuck 5v5 skater totals. Labels are the raw rates per 60. 2025-26: 8 goals on 12.1 xG (P of 8 or fewer = 0.15).")
    close(p, "c2-5v5-arc.svg")

# ---------- c3: tip / deflection goals by season vs league leader ----------
def c3():
    rows = [r for r in st if r["season"] >= 20182019]
    h = 330; p = svg_open(h, "The deflection goals are the part that is still elite.",
                          "Goals scored on tips and deflections, per season, with Kreider's league rank")
    x0, x1, y0, y1 = 60, 720, 60, 250
    n = len(rows); bw = (x1-x0)/n
    mx = 20
    def Y(v): return y1 - (v/mx)*(y1-y0)
    for v in (0,5,10,15,20):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="{RULE}" stroke-width="0.8"/>'); txt(p, x0-8, Y(v)+4, f"{v}", 11, SOFT, "end", mono=True)
    for i, r in enumerate(rows):
        cx = x0 + i*bw + bw/2; v = r["tip_defl_goals"]; s = str(r["season"])
        p.append(f'<rect x="{cx-18}" y="{Y(v):.1f}" width="36" height="{y1-Y(v):.1f}" fill="{RED}"/>')
        txt(p, cx, Y(v)-6, f"{v}", 12, INK, "middle", 600, True)
        rk = ranks.get(s)
        if rk:
            lead = rk["top5"][0]
            if lead[0] != "Chris Kreider":
                p.append(f'<line x1="{cx-22}" x2="{cx+22}" y1="{Y(lead[1]):.1f}" y2="{Y(lead[1]):.1f}" stroke="{DARK}" stroke-width="2" stroke-dasharray="3,3"/>')
            txt(p, cx, y1+32, f'NHL rank {rk["rank"]}', 10.5, RED if rk["rank"]<=6 else SOFT, "middle", 600 if rk["rank"]<=6 else None)
        share = v / r["goals"] if r["goals"] else 0
        txt(p, cx, y1+46, f'{share:.0%} of {r["goals"]} G', 10, MUTED, "middle")
        txt(p, cx, y1+18, f'{s[:4]}-{s[6:]}', 11, SOFT, "middle", mono=True)
    txt(p, x1, Y(19), "dashed = that season's league leader", 10.5, MUTED, "end")
    source(p, h, "NHL API shot-type splits (goalsTipIn + goalsDeflected), regular season. Ranks vs all skaters, 2021-22 onward.")
    close(p, "c3-tip-goals.svg")

# ---------- c4: PP net-front scatter ----------
def c4():
    rows = [r for r in csv.DictReader(open(RAW/"mp_skaters_2025.csv")) if r["situation"]=="5on4" and r["position"]!="D" and float(r["icetime"])>=3000]
    def rate(r,k): return float(r[k])/float(r["icetime"])*3600
    pts = [(rate(r,"I_F_xGoals"), rate(r,"I_F_highDangerShots"), r["name"], r["team"]) for r in rows]
    h = 420; p = svg_open(h, "What Detroit's power play had at the net, and what it is about to lose.",
                          "5v4, forwards with 50+ PP minutes in 2025-26: individual xG/60 vs high-danger shots/60")
    x0, x1, y0, y1 = 60, 720, 60, 340
    mxx, mxy = 4.2, 7.0
    def X(v): return x0 + (v/mxx)*(x1-x0)
    def Y(v): return y1 - (v/mxy)*(y1-y0)
    for v in (0,1,2,3,4):
        p.append(f'<line x1="{X(v)}" x2="{X(v)}" y1="{y0}" y2="{y1}" stroke="{RULE}" stroke-width="0.8"/>'); txt(p, X(v), y1+16, f"{v}", 11, SOFT, "middle", mono=True)
    for v in (0,2,4,6):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="{RULE}" stroke-width="0.8"/>'); txt(p, x0-8, Y(v)+4, f"{v}", 11, SOFT, "end", mono=True)
    txt(p, (x0+x1)/2, y1+34, "individual xG per 60 on the power play", 11, SOFT, "middle")
    p.append(f'<text transform="translate(16,{(y0+y1)/2}) rotate(-90)" font-size="11" fill="{SOFT}" text-anchor="middle">high-danger shots per 60</text>')
    for x,y,n,t in pts: p.append(f'<circle cx="{X(min(x,mxx)):.1f}" cy="{Y(min(y,mxy)):.1f}" r="3" fill="{GRAY}" opacity="0.7"/>')
    hi = {"Chris Kreider":(RED,"Kreider (ANA)",-9,14),"Dylan Larkin":(BLUE,"Larkin",8,-6),"James van Riemsdyk":(BLUE,"van Riemsdyk (gone)",-8,-8),"Alex DeBrincat":(BLUE,"DeBrincat",9,-6),"Lucas Raymond":(BLUE,"Raymond",-9,4),"Emmitt Finnie":(BLUE,"Finnie",8,4),"Patrick Kane":(AMBER,"Kane (gone, 0 PP goals)",8,4),"Andrew Copp":(AMBER,"Copp",-9,-6),"Viktor Arvidsson":(AMBER,"Arvidsson (BOS)",9,-7),"J.T. Compher":(AMBER,"Compher",8,4),"Marco Kasper":(AMBER,"Kasper",8,4)}
    for x,y,n,t in pts:
        if n in hi:
            col, lab, dx, dy = hi[n]
            p.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="6" fill="{col}" stroke="{PAPER}" stroke-width="1.5"/>')
            txt(p, X(x)+dx, Y(y)+dy, lab, 11, INK, "end" if dx<0 else "start", 600)
    legend(p, x0, h-30, [("Kreider", RED), ("Red Wings 2025-26", BLUE), ("The middle-six comps", AMBER)])
    source(p, h, "MoneyPuck 5v4 skater totals, n = 275 forwards. Larkin, the only elite net-front presence Detroit has, asked out in June.")
    close(p, "c4-pp-netfront.svg")

# ---------- c5: style distance bars ----------
def c5():
    ids = list(feat); mu = {d: statistics.mean(feat[i][d] for i in ids) for d in dims}; sd = {d: statistics.pstdev(feat[i][d] for i in ids) for d in dims}
    Z = {i: {d: (feat[i][d]-mu[d])/sd[d] for d in dims} for i in ids}
    def dist(a,b): return math.sqrt(sum((Z[a][d]-Z[b][d])**2 for d in dims)/len(dims))
    K = "8475184"
    names = ["Jesper Bratt","Pavel Buchnevich","Patrick Kane","Lucas Raymond","James van Riemsdyk","Marco Kasper","Emmitt Finnie","Jonatan Berggren","Andrew Copp","Dylan Larkin","J.T. Compher","Alex DeBrincat","Michael Rasmussen","Mason Appleton","Viktor Arvidsson"]
    rows = []
    for n in names:
        for i in ids:
            if feat[i]["name"]==n: rows.append((n, feat[i]["team"], dist(K,i)))
    rows.sort(key=lambda r: r[2])
    alld = sorted(dist(a,b) for ai,a in enumerate(ids) for b in ids[ai+1:]); med = statistics.median(alld)
    h = 60 + 22*len(rows) + 70
    p = svg_open(h, "By how he plays, Kreider is a top-six winger, not a Copp.",
                 "Style distance from Kreider, 17 usage and rate dims z-scored across 384 forwards (lower = more alike)")
    x0, x1 = 200, 700; mx = 1.6
    def X(v): return x0 + (v/mx)*(x1-x0)
    y = 62
    for n, t, d in rows:
        col = RED if n in ("Andrew Copp","J.T. Compher","Viktor Arvidsson") else (BLUE if t=="DET" or n in ("James van Riemsdyk",) else GRAY)
        if n in ("Patrick Kane","Jesper Bratt","Pavel Buchnevich"): col = GRAY
        lab = n + (" (DET)" if t=="DET" else f" ({t})")
        txt(p, x0-8, y+4, lab, 11.5, INK, "end")
        p.append(f'<rect x="{x0}" y="{y-7}" width="{X(d)-x0:.1f}" height="14" fill="{col}"/>')
        txt(p, X(d)+6, y+4, f"{d:.2f}", 11, SOFT, "start", mono=True)
        y += 22
    p.append(f'<line x1="{X(med)}" x2="{X(med)}" y1="52" y2="{y-6}" stroke="{DARK}" stroke-width="1.5" stroke-dasharray="4,3"/>')
    txt(p, X(med)+5, 52, f"league median pair {med:.2f}", 10.5, MUTED)
    legend(p, x0, h-30, [("The three names in the premise", RED), ("Red Wings forwards", BLUE), ("Nearest league comps", GRAY)])
    source(p, h, "2025-26 style vector, same method as the Copp/Finnie/Kasper piece. Results (goals, points, sh%) excluded on purpose.")
    close(p, "c5-style-distance.svg")

# ---------- c6: 2025-26 in three segments ----------
def c6():
    T = seg["totals"]; keys = ["A: games 1-9","B: games 10-56","C: games 57-75"]
    labs = ["Games 1-9 (Oct 9 - Nov 6)","Games 10-56 (Nov 8 - Mar 6)","Games 57-75 (Mar 8 - Apr 16)"]
    h = 320; p = svg_open(h, "Nine goals in nine games, then one in the last nineteen, on the same chances.",
                          "Kreider 2025-26 by stretch: goals vs expected goals per game, all situations")
    x0, x1, y0, y1 = 60, 720, 60, 225; mx = 1.1
    def Y(v): return y1 - (v/mx)*(y1-y0)
    for v in (0,0.25,0.5,0.75,1.0):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="{RULE}" stroke-width="0.8"/>'); txt(p, x0-8, Y(v)+4, f"{v:.2f}", 11, SOFT, "end", mono=True)
    gw = (x1-x0)/3
    for i, k in enumerate(keys):
        t = T[k]; gpg = t["g"]/t["gp"]; xpg = t["xg"]/t["gp"]; cx = x0 + i*gw + gw/2
        p.append(f'<rect x="{cx-52}" y="{Y(xpg):.1f}" width="48" height="{y1-Y(xpg):.1f}" fill="{GRAY}"/>')
        p.append(f'<rect x="{cx+4}" y="{Y(gpg):.1f}" width="48" height="{y1-Y(gpg):.1f}" fill="{RED}"/>')
        txt(p, cx-28, Y(xpg)-6, f'{t["xg"]:.1f} xG', 11, SOFT, "middle", mono=True)
        txt(p, cx+28, Y(gpg)-6, f'{t["g"]} G', 11, RED, "middle", 600, True)
        txt(p, cx, y1+18, labs[i], 11, INK, "middle")
        txt(p, cx, y1+34, f'{t["att"]/t["gp"]:.1f} attempts/gm, P = {t["P_le"] if t["g"]<t["xg"] else round(1-t["P_le"],3)}', 10.5, MUTED, "middle")
    legend(p, x0, h-30, [("Goals per game", RED), ("Expected goals per game", GRAY)])
    source(p, h, "MoneyPuck shot file joined to the NHL game log. P = Poisson chance of a finish this far from the xG in that direction.")
    close(p, "c6-season-segments.svg")

# ---------- c7: age comps, next-season goals ----------
def c7():
    comps = [c for c in age["comps"] if c["next"]]
    h = 330; p = svg_open(h, "Players who looked like this at 33-35 scored a median of 12 the next year.",
                          "30 nearest production comps (2010-2024), next-season goals; two of the 30 did not play again")
    x0, x1, yb = 60, 700, 200; mx = 40
    def X(v): return x0 + (v/mx)*(x1-x0)
    for v in (0,10,20,30,40):
        p.append(f'<line x1="{X(v)}" x2="{X(v)}" y1="60" y2="{yb+6}" stroke="{RULE}" stroke-width="0.8"/>'); txt(p, X(v), yb+22, f"{v}", 11, SOFT, "middle", mono=True)
    txt(p, (x0+x1)/2, yb+40, "goals the following season", 11, SOFT, "middle")
    # beeswarm-ish stacking
    cols = {}
    for c in sorted(comps, key=lambda c: c["next"]["goals"]):
        g = int(c["next"]["goals"]); k = g//2; cols[k] = cols.get(k,0)+1; lvl = cols[k]
        cy = yb - 12*lvl + 6
        col = RED if g>=20 else (AMBER if g>=15 else GRAY)
        p.append(f'<circle cx="{X(g):.1f}" cy="{cy:.1f}" r="5" fill="{col}" stroke="{PAPER}" stroke-width="1"/>')
    med = statistics.median(c["next"]["goals"] for c in comps)
    p.append(f'<line x1="{X(med)}" x2="{X(med)}" y1="52" y2="{yb+6}" stroke="{DARK}" stroke-width="1.5" stroke-dasharray="4,3"/>'); txt(p, X(med)+5, 58, f"median {med:.0f}", 10.5, MUTED)
    p.append(f'<line x1="{X(22)}" x2="{X(22)}" y1="52" y2="{yb+6}" stroke="{RED}" stroke-width="1.5"/>'); txt(p, X(22)+5, 72, "Kreider's 22 last season", 10.5, RED)
    names20 = [c["name"] for c in comps if c["next"]["goals"]>=20]
    txt(p, x0, yb+62, "Reached 20 again: " + ", ".join(f'{c["name"]} ({int(c["next"]["goals"])})' for c in comps if c["next"]["goals"]>=20), 11, INK)
    txt(p, x0, yb+80, f'Base rate, every age-34 forward with 17-27 goals since 2010 (n = {age["base_rate"]["n"]}): median 16 next season, 6 reached 20, 1 in 26 did not play.', 11, SOFT)
    legend(p, x0, h-30, [("20+ goals", RED), ("15-19", AMBER), ("under 15", GRAY)])
    source(p, h, "MoneyPuck forward seasons 2010-2025; nearest by 5v5 P/60, G/60, ixG/60, on-ice xGF%, TOI/GP, game score/GP at age 33-35.")
    close(p, "c7-age-comps.svg")

for f in (c1, c2, c3, c4, c5, c6, c7): f()

# ---------- c8: NHL Edge skating, five seasons ----------
def c8():
    ed = json.load(open(RAW/"edge_kreider.json")); ss = ['2021-22','2022-23','2023-24','2024-25','2025-26']
    h = 330; p = svg_open(h, "The top gear is still there. He reaches it a third as often.",
                          "NHL Edge: speed bursts over 20 mph per game (bars) and max skating speed percentile (line), by season")
    x0, x1, y0, y1 = 60, 700, 70, 250; mx = 4.0
    def Y(v): return y1 - (v/mx)*(y1-y0)
    def Y2(v): return y1 - (v/100)*(y1-y0)
    for v in (0,1,2,3,4):
        p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(v)}" y2="{Y(v)}" stroke="{RULE}" stroke-width="0.8"/>'); txt(p, x0-8, Y(v)+4, f"{v:.0f}", 11, SOFT, "end", mono=True)
    for v in (0,25,50,75,100): txt(p, x1+8, Y2(v)+4, f"{v}", 10.5, MUTED, "start", mono=True)
    txt(p, x0, y0-12, "bursts per game", 10.5, SOFT, "start"); txt(p, x1, y0-12, "max speed, percentile", 10.5, MUTED, "end")
    gw = (x1-x0)/len(ss); pts=[]
    for i, s in enumerate(ss):
        v = ed[s]; cx = x0 + i*gw + gw/2; bpg = v['bursts_per_game']
        p.append(f'<rect x="{cx-30}" y="{Y(bpg):.1f}" width="60" height="{y1-Y(bpg):.1f}" fill="{RED}"/>')
        txt(p, cx, Y(bpg)+16, f"{bpg:.2f}", 12, "#f2f1ef", "middle", 600, True)
        txt(p, cx, y1+18, s, 11, SOFT, "middle", mono=True)
        txt(p, cx, y1+33, f"{v['bursts_20']} bursts, {v['bursts_pct']}th pct", 10.5, MUTED, "middle")
        pts.append((cx, Y2(v['max_speed_pct']), v['max_speed'], v['max_speed_pct']))
    p.append('<polyline fill="none" stroke="%s" stroke-width="2.2" points="%s"/>' % (DARK, " ".join(f"{x:.1f},{y:.1f}" for x,y,_,_ in pts)))
    for x,y,ms,pc in pts:
        p.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{DARK}" stroke="{PAPER}" stroke-width="1.5"/>'); txt(p, x, y-9, f"{ms:.1f} mph", 10.5, DARK, "middle", None, True)
    avg = ed['2025-26']['bursts_avg_f']/82
    p.append(f'<line x1="{x0}" x2="{x1}" y1="{Y(avg)}" y2="{Y(avg)}" stroke="{DARK}" stroke-width="1.2" stroke-dasharray="4,3"/>'); txt(p, x0+4, Y(avg)-5, f"avg forward, 82 games: {avg:.2f}/game", 10.5, MUTED)
    legend(p, x0, h-30, [("Bursts over 20 mph per game", RED), ("Max speed percentile", DARK)])
    source(p, h, "NHL Edge, regular season, percentiles vs forwards. 2024-25 was 68 games (vertigo, back); 2025-26 was 75.")
    close(p, "c8-edge-bursts.svg")

c8()
