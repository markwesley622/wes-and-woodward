#!/usr/bin/env python3
"""Mark's Google Doc tab (t.47n1rz9w3qbp) -> data/site/articles/red-wings-finishing-problem-copy.json (parts + idx anchors).

Copy runs verbatim. The 24 approved style-review edits plus Mark's own F06 fix (research/style/finishing-apply-2026-10-29.json)
were applied in the Doc on 10/29 and the export verified against research/style/finishing-final-expected-2026-10-29.txt.
The Doc's two hyperlinks (ESPN on "waiting on the sidelines", the predictions post on "just 75 points") do not survive the
txt export, so they are re-added here with the internal links.
Usage: python3 build_copy.py [saved_export.txt]"""
import html, json, pathlib, re, sys, urllib.request, ssl

DOC = "https://docs.google.com/document/d/1p8g-ROOP74WX7G2nJs1xgcVkV23qx4LKO52xSl5QdlM/export?format=txt&tab=t.47n1rz9w3qbp"
ROOT = pathlib.Path(__file__).resolve().parents[2]
SLUG = "red-wings-finishing-problem"
OUT = ROOT / f"data/site/articles/{SLUG}-copy.json"

if len(sys.argv) > 1:
    txt = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8-sig")
else:
    import certifi
    txt = urllib.request.urlopen(DOC, context=ssl.create_default_context(cafile=certifi.where())).read().decode("utf-8-sig")

lines = [l.strip() for l in txt.replace("\r\n", "\n").split("\n")]
lines = [l for l in lines if l]
title = lines[0]
# Doc heading levels: the three "What ..." lines are Heading 2, the three under them Heading 3
HEADS = {
    "What stayed the same in the Edmonton game": ("same", "h3"),
    "Medium danger finishing": ("medium", "h4"),
    "Penalty kill": ("pk", "h4"),
    "What was different in the Edmonton game": ("different", "h3"),
    "High-danger shots against": ("hd", "h4"),
    "What the Red Wings will take into the Chicago game tonight": ("chicago", "h3"),
}
parts, idx = [], {}
ul = []
def flush():
    global ul
    if ul:
        parts.append("<ul>" + "".join(f"<li>{html.escape(x, quote=False)}</li>" for x in ul) + "</ul>"); ul = []
for l in lines[1:]:
    if l.startswith("* "):
        ul.append(l[2:].strip()); continue
    flush()
    if l in HEADS:
        key, tag = HEADS[l]
        idx[key] = len(parts); parts.append(f'<{tag} class="art">{html.escape(l, quote=False)}</{tag}>')
    else:
        parts.append(f"<p>{html.escape(l, quote=False)}</p>")
flush()
missing = [h for h in HEADS if HEADS[h][0] not in idx]
assert not missing, f"headings not found: {missing}"

# links: (context that must appear once in a paragraph, the words inside it to link, href). Copy is unchanged; only the
# anchor words get wrapped. Player targets are checked against the built data so a bad slug fails here.
LINKS = [
    ("Larkin went and TOTALLY redeemed himself.", "Larkin", "/players/dylan-larkin/"),
    ("he’s waiting on the sidelines for a trade to get finalized.", "waiting on the sidelines", "https://www.espn.com/nhl/story/_/id/50319798/sources-red-wings-play-dylan-larkin-trade-related-reasons"),
    ("The rest is Postava history.", "Postava", "/players/michal-postava/"),
    ("the Larkin and Edvinsson-shaped cloud", "Edvinsson", "/players/simon-edvinsson/"),
    ("The Red Wings are finishing medium-danger chances at 6.6%", "Red Wings", "/team/"),
    ("finishing medium-danger chances at 6.6%, 30th", "medium-danger chances", "/glossary/scoring-chances/"),
    ("is Lucas Raymond, who is 0-24 with 2.8 xG on those shots.", "Lucas Raymond", "/players/lucas-raymond/"),
    ("who is 0-24 with 2.8 xG on those shots.", "xG", "/glossary/individual-expected-goals/"),
    ("Arvidsson, who has five goals overall", "Arvidsson", "/players/viktor-arvidsson/"),
    ("DeBrincat is 2-25 with 3.1 xG.", "DeBrincat", "/players/alex-debrincat/"),
    ("a player like Copp who is 1-16", "Copp", "/players/andrew-copp/"),
    ("He has an .875 save percentage on the PK", "save percentage", "/glossary/save-percentage/"),
    ("compared to John Gibson’s .633.", "John Gibson", "/players/john-gibson/"),
    ("0.4 goals saved above expected for Postava", "goals saved above expected", "/glossary/goals-saved-above-expected/"),
    ("They give up the 5th fewest high-danger shots in the league on the kill", "high-danger shots", "/glossary/high-danger-chances/"),
    ("Detroit held Edmonton to 1.06 expected goals at 5v5", "expected goals", "/glossary/expected-goals/"),
    ("the trajectory of Mo Seider and Lucas Raymond.", "Mo Seider", "/players/moritz-seider/"),
    ("they would get just 75 points, but this team", "just 75 points", "/analysis/2026-27-predictions/"),
]
slugs = {json.loads(f.read_text())["slug"] for f in (ROOT / "data/site/players").glob("*.json")}
for ctx, anchor, href in LINKS:
    if href.startswith("/players/"): assert href.split("/")[2] in slugs, href
    if href.startswith("/glossary/"): assert (ROOT / "dist/glossary" / href.split("/")[2]).exists(), href
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
    "fig_radar": find("-shaped cloud hanging around the organization."),   # c1 the team-page radar as of Oct 29, closes the opening
    "fig_conv": find("Detroit finishes nowhere else."),                                # c2 medium-danger conversion, all 32 teams
    "fig_shooters": find("where the model expected 8.5."),                            # c3 the shooters, goals vs expected
    "fig_gibson": find("he was 2.7 goals better than average."),                       # c4 Gibson's running PK save percentage
})
words = len(re.sub("<[^>]+>", "", re.sub(r"</?(?:p|li|ul|ol|h3|h4)\b[^>]*>", " ", title + " " + " ".join(parts))).split())
json.dump(dict(title=title, parts=parts, idx=idx, words=words), open(OUT, "w"), indent=1, ensure_ascii=False)
print(title, "|", len(parts), "parts |", words, "words |", idx)
