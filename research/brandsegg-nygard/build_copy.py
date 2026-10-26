#!/usr/bin/env python3
"""Mark's Google Doc tab (t.prjn1g3ev5cr) -> data/site/articles/michael-brandsegg-nygard-2026-glowup-copy.json (parts + idx anchors).

Copy runs verbatim. The 31 approved style-review edits (research/style/mbn-apply-2026-10-26.json, plus the M14 hyperlink)
were applied in the Doc itself on 10/26 and the export verified against research/style/mbn-final-expected-2026-10-26.txt.
Usage: python3 build_copy.py [saved_export.txt]"""
import html, json, pathlib, re, sys, urllib.request, ssl

DOC = "https://docs.google.com/document/d/1p8g-ROOP74WX7G2nJs1xgcVkV23qx4LKO52xSl5QdlM/export?format=txt&tab=t.prjn1g3ev5cr"
ROOT = pathlib.Path(__file__).resolve().parents[2]
SLUG = "michael-brandsegg-nygard-2026-glowup"
OUT = ROOT / f"data/site/articles/{SLUG}-copy.json"

if len(sys.argv) > 1:
    txt = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8-sig")
else:
    import certifi
    txt = urllib.request.urlopen(DOC, context=ssl.create_default_context(cafile=certifi.where())).read().decode("utf-8-sig")

lines = [l.strip() for l in txt.replace("\r\n", "\n").split("\n")]
lines = [l for l in lines if l]
title = lines[0]
HEADS = {
    "MBN in 2025-26 vs. 2026-27": "compare",
    "The shot map": "shotmap",
    "The minutes": "minutes",
    "The tiebreaker": "tiebreaker",
    "What all these changes have led to": "results",
    "Why MBN turned into Spider-Man and not the Green Goblin": "spiderman",
}
parts, idx = [], {}
for l in lines[1:]:
    if l in HEADS:
        idx[HEADS[l]] = len(parts); parts.append(f'<h3 class="art">{html.escape(l, quote=False)}</h3>')
    else:
        parts.append(f"<p>{html.escape(l, quote=False)}</p>")
missing = [h for h in HEADS if HEADS[h] not in idx]
assert not missing, f"headings not found: {missing}"

# internal links: (context that must appear once, the words inside it to link, href). Copy is unchanged; only the anchor
# words get wrapped. Player and glossary targets are checked against the built data so a bad slug fails here.
LINKS = [
    ("the biggest glow-up of 2026 is Michael Brandsegg-Nygard.", "Michael Brandsegg-Nygard", "/players/michael-brandsegg-nygard/"),
    ("he led the Red Wings in expected goals for percentage (xGF%)", "Red Wings", "/team/"),
    ("in expected goals for percentage (xGF%)", "expected goals for percentage", "/glossary/expected-goals/"),
    ("from 18.3 shot attempts per 60 to 17.8", "shot attempts per 60", "/glossary/individual-shot-attempts/"),
    ("almost exclusively with Emmitt Finnie and Alex DeBrincat.", "Emmitt Finnie", "/players/emmitt-finnie/"),
    ("and Alex DeBrincat.", "Alex DeBrincat", "/players/alex-debrincat/"),
    ("a struggling first line with Dylan Larkin and Lucas Raymond", "Dylan Larkin", "/players/dylan-larkin/"),
    ("and Lucas Raymond, and played", "Lucas Raymond", "/players/lucas-raymond/"),
    ("(cough…Gavin McKenna…cough)", "Gavin McKenna", "https://www.nhl.com/news/gavin-mckenna-absent-in-final-half-of-toronto-maple-leafs-loss-to-buffalo-sabres"),
    ("a 13% shooting line in front of a .978 goalie.", "13% shooting line", "/glossary/on-ice-shooting-and-save-percentage/"),
    ("hitting people 15 times for every 60 minutes played", "hitting people", "/glossary/hits/"),
]
slugs = {json.loads(f.read_text())["slug"] for f in (ROOT / "data/site/players").glob("*.json")}
for ctx, anchor, href in LINKS:
    if href.startswith("/players/"): assert href.split("/")[2] in slugs, href
    if href.startswith("/glossary/"): assert (ROOT / "src/content/glossary").exists() or (ROOT / "dist/glossary" / href.split("/")[2]).exists(), href
    hits = [i for i, p in enumerate(parts) if ctx in p and p.startswith("<p>")]
    assert len(hits) == 1 and anchor in ctx, (ctx, hits)
    i = hits[0]
    a = f'<a href="{href}"{" rel=\"noopener\"" if href.startswith("http") else ""}>{anchor}</a>'
    parts[i] = parts[i].replace(ctx, ctx.replace(anchor, a, 1), 1)

def find(s):  # index of the paragraph AFTER which a figure goes
    hits = [i for i, p in enumerate(parts) if s in p]
    assert len(hits) == 1, (s, hits)
    return hits[0]
idx.update({
    "fig_shotmap": find("may be underselling his scoring potential."),   # c1 between the "second benefit" and "Finally" paragraphs (Mark 10/26)
    "fig_deploy": find("against the opponent’s top line a little more often."),              # c2 after zone starts / matchups
    "fig_score": find("He’s driving it no matter what the score is."),                       # c3 closes the tiebreaker argument
    "fig_goals": find("in front of a .978 goalie."),                      # c4 goals vs expected, both years
})
words = len(re.sub("<[^>]+>", "", re.sub(r"</?(?:p|li|ul|ol|h3)\b[^>]*>", " ", title + " " + " ".join(parts))).split())
json.dump(dict(title=title, parts=parts, idx=idx, words=words), open(OUT, "w"), indent=1, ensure_ascii=False)
print(title, "|", len(parts), "parts |", words, "words |", idx)
