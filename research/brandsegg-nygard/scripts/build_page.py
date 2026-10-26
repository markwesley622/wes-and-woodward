"""BRIEF.md + charts -> single HTML page. usage: build_page.py OUT_DIR"""
import re, json, html, sys
OUT = sys.argv[1]
md = open(f"{OUT}/BRIEF.md").read()
G = json.load(open(f"{OUT}/onice_games.json"))
def games_table():
    rows = []
    for s, lab in (("20252026", "2025-26"), ("20262027", "2026-27")):
        rows.append(f'<tr class="sec"><th colspan="12">{lab}</th></tr>')
        for g in G[s]:
            e, x, i = g["ev5v5"], g["xg"], g["ind"]
            rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in (g["date"], ("vs " if g["home"]=="DET" else "@ ") + g["opp"], f'{int(g["toi_all"]//60)}:{int(g["toi_all"]%60):02d}', f'{g["toi_by_state"].get("5v5",0)/60:.1f}', f'{g["toi_by_state"].get("PP",0)/60:.1f}', f'{e.get("CF",0)}-{e.get("CA",0)}', f'{x.get("xGF",0):.2f}-{x.get("xGA",0):.2f}', f'{e.get("GF",0)}-{e.get("GA",0)}', i.get("iSOG",0), f'{x.get("ixg_all",0):.2f}', i.get("pts",0), f'{g["zs"].get("O",0)}/{g["zs"].get("D",0)}/{g["zs"].get("N",0)}')) + "</tr>")
    head = "<tr>" + "".join(f"<th>{h}</th>" for h in ("Date", "Opp", "TOI", "5v5 min", "PP min", "5v5 CF-CA", "5v5 xGF-xGA", "5v5 GF-GA", "SOG", "ixG", "Pts", "ZS O/D/N")) + "</tr>"
    return f'<div class="tw"><table>{head}{"".join(rows)}</table></div>'
def inline(md_text):
    md_text = html.escape(md_text, quote=False)
    md_text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", md_text)
    md_text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", md_text)
    return md_text
out = []; lines = md.split("\n"); i = 0
while i < len(lines):
    L = lines[i]
    if L.startswith("# "): out.append(f"<h1>{inline(L[2:])}</h1>")
    elif L.startswith("## "): out.append(f"<h2>{inline(L[3:])}</h2>")
    elif L.startswith("### "): out.append(f"<h3>{inline(L[4:])}</h3>")
    elif L.startswith("{{chart:"):
        name = L[8:-2]; svg = open(f"{OUT}/charts/{name}.svg").read()
        svg = re.sub(r'\s(width|height)="\d+"', "", svg, count=2)
        out.append(f'<figure class="chart">{svg}</figure>')
    elif L.startswith("{{table:games}}"): out.append(games_table())
    elif L.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells): rows.append(cells)
            i += 1
        head = "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr>"
        body = "".join("<tr>" + "".join(f"<{'th' if j==0 else 'td'}>{inline(c)}</{'th' if j==0 else 'td'}>" for j, c in enumerate(r)) + "</tr>" for r in rows[1:])
        out.append(f'<div class="tw"><table class="cmp">{head}{body}</table></div>'); continue
    elif L.startswith("- "):
        items = []
        while i < len(lines) and lines[i].startswith("- "): items.append(f"<li>{inline(lines[i][2:])}</li>"); i += 1
        out.append("<ul>" + "".join(items) + "</ul>"); continue
    elif re.match(r"^\d+\. ", L):
        items = []
        while i < len(lines) and re.match(r"^\d+\. ", lines[i]): items.append(f"<li>{inline(re.sub(r'^\d+\. ', '', lines[i]))}</li>"); i += 1
        out.append("<ol>" + "".join(items) + "</ol>"); continue
    elif L.strip(): 
        para = [L]
        while i+1 < len(lines) and lines[i+1].strip() and not re.match(r"^(#|\||- |\d+\. |\{\{)", lines[i+1]): i += 1; para.append(lines[i])
        out.append(f"<p>{inline(' '.join(para))}</p>")
    i += 1
body = "\n".join(out)
page = f'''<title>Brandsegg-Nygård Glowup Brief</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: one 760px reading column on the Wes & Woodward warm-grey paper; charts bleed to the column edge; tables in mono. */
:root {{ --paper:#d7d6d3; --panel:#e7e6e3; --rule:#c4c3bf; --ink:#141414; --muted:#5f5e5a; --c-a:#2f55a8; --c-b:#ce1126; --accent:#ce1126; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --paper:#141414; --panel:#1f1f1f; --rule:#3a3a38; --ink:#f2f1ef; --muted:#a8a69f; --c-a:#5f86e0; --c-b:#e0343f; --accent:#e0343f; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --paper:#141414; --panel:#1f1f1f; --rule:#3a3a38; --ink:#f2f1ef; --muted:#a8a69f; --c-a:#5f86e0; --c-b:#e0343f; --accent:#e0343f; color-scheme:dark }}
body {{ background:var(--paper); color:var(--ink); font-family:"Space Grotesk",system-ui,sans-serif; font-size:16px; line-height:1.55; margin:0; padding-block:32px 64px; padding-left:max(16px,env(safe-area-inset-left,0px)); padding-right:max(16px,env(safe-area-inset-right,0px)); }}
main {{ max-width:760px; margin:0 auto; }}
h1 {{ font-size:clamp(26px,5vw,38px); line-height:1.1; text-wrap:balance; margin:0 0 12px; letter-spacing:-0.01em; }}
h2 {{ font-size:22px; margin:40px 0 10px; text-wrap:balance; border-top:2px solid var(--ink); padding-top:14px; }}
h3 {{ font-size:18px; margin:30px 0 8px; text-wrap:balance; }}
p {{ max-width:68ch; margin:0 0 14px; }}
ul,ol {{ max-width:68ch; padding-left:22px; }} li {{ margin-bottom:6px; }}
.tw {{ overflow-x:auto; margin:10px 0 18px; }}
table {{ border-collapse:collapse; width:100%; font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace; font-size:13px; font-variant-numeric:tabular-nums; }}
th,td {{ text-align:left; padding:6px 10px; border-bottom:1px solid var(--rule); vertical-align:top; }}
thead th, tr:first-child th {{ color:var(--muted); font-weight:500; font-size:12px; letter-spacing:0.04em; text-transform:uppercase; }}
table.cmp td:nth-child(2), table.cmp th:nth-child(2) {{ color:var(--c-a); }}
table.cmp td:nth-child(3), table.cmp th:nth-child(3) {{ color:var(--c-b); font-weight:500; }}
table.cmp tr:first-child th {{ color:var(--muted); font-weight:500; }}
tr.sec th {{ color:var(--ink); font-weight:600; background:var(--panel); text-transform:none; letter-spacing:0; font-size:13px; padding-top:10px; }}
figure.chart {{ margin:14px 0 22px; background:var(--panel); border-radius:6px; padding:12px; }}
figure.chart svg {{ width:100%; height:auto; display:block; }}
.meta {{ font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:12px; color:var(--muted); letter-spacing:0.04em; text-transform:uppercase; margin-bottom:24px; }}
@media (prefers-reduced-motion: reduce) {{ * {{ animation:none !important; transition:none !important; }} }}
</style>
<main>
<div class="meta">Wes &amp; Woodward research brief · built Oct 23, 2026 · private</div>
{body}
</main>'''
open(f"{OUT}/mbn-glowup-brief.html", "w").write(page); print("page", len(page), "bytes")
