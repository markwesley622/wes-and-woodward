#!/usr/bin/env python3
"""Mark's Google Doc tab -> data/site/articles/dylan-larkin-copy.json (parts + idx anchors).

Copy runs verbatim. The style-review edits (research/style/edits-larkin-2026-10-17.json, 44 approved) were applied
in the Doc itself on 10/17, so there is no FIX list here. Usage:
  python3 build_copy.py            # fetch the Doc tab export
  python3 build_copy.py draft.txt  # or read a saved export
"""
import html, json, pathlib, re, sys, urllib.request, ssl

DOC = "https://docs.google.com/document/d/1p8g-ROOP74WX7G2nJs1xgcVkV23qx4LKO52xSl5QdlM/export?format=txt&tab=t.34iu4eg7zytr"
OUT = pathlib.Path(__file__).resolve().parents[2] / "data/site/articles/dylan-larkin-copy.json"

if len(sys.argv) > 1:
    txt = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8-sig")
else:
    try:
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        ctx = ssl.create_default_context()
    txt = urllib.request.urlopen(DOC, context=ctx).read().decode("utf-8-sig")

lines = [l.strip() for l in txt.replace("\r\n", "\n").split("\n")]
lines = [l for l in lines if l]
title = lines[0]
HEADS = {
    "What the numbers have to say": "numbers",
    "The noise": "noise",
    "Evidence of checking out": "evidence",
    "Is it possible it’s just rust?": "rust",
    "When the decline began": "decline",
}
parts, idx, items = [], {}, []
def flush():
    global items
    if items:
        parts.append('<ol class="art">' + "".join(f"<li>{html.escape(b, quote=False)}</li>" for b in items) + "</ol>")
        items = []
for l in lines[1:]:
    m = re.match(r"^\d+\.\s+(.*)$", l)
    if m:
        items.append(m.group(1).strip()); continue
    flush()
    if l in HEADS:
        idx[HEADS[l]] = len(parts); parts.append(f'<h3 class="art">{html.escape(l, quote=False)}</h3>')
    else:
        parts.append(f"<p>{html.escape(l, quote=False)}</p>")
flush()
missing = [h for h in HEADS if HEADS[h] not in idx]
assert not missing, f"headings not found: {missing}"

# contextual internal links: (context that must appear once, the words inside it to link, href). Copy is unchanged;
# only the anchor words get wrapped.
LINKS = [
    ("This isn’t a perfect analogy for Dylan Larkin.", "Dylan Larkin", "/players/dylan-larkin/"),
    ("If it were Anton Johansson", "Anton Johansson", "/players/anton-johansson/"),
    ("or even Axel Sandin-Pellikka", "Axel Sandin-Pellikka", "/players/axel-sandin-pellikka/"),
    ("The Detroit Red Wings definitely", "Detroit Red Wings", "/team/"),
    ("Game score (yes,", "Game score", "/glossary/game-score/"),
    ("5v5 expected-goal share</li>", "expected-goal share", "/glossary/expected-goals/"),
    ("Points per 60</li>", "per 60", "/glossary/per-60-rates/"),
    ("individual expected goals per 60 (ixG)", "individual expected goals per 60 (ixG)", "/glossary/individual-expected-goals/"),
    ("they don’t like to credit anyone with giveaways", "giveaways", "/glossary/takeaways-and-giveaways/"),
    ("he’s averaging 11.3 shot attempts per 60", "shot attempts", "/glossary/individual-shot-attempts/"),
    ("goals above replacement (Evolving-Hockey’s GAR)", "goals above replacement", "/glossary/wins-above-replacement/"),
]
for ctx, anchor, href in LINKS:
    hits = [i for i, p in enumerate(parts) if ctx in p and (p.startswith("<p>") or p.startswith("<ol"))]
    assert len(hits) == 1 and anchor in ctx, (ctx, hits)
    i = hits[0]
    parts[i] = parts[i].replace(ctx, ctx.replace(anchor, f'<a href="{href}">{anchor}</a>', 1), 1)

def find(s):  # index of the paragraph AFTER which a figure goes
    hits = [i for i, p in enumerate(parts) if s in p]
    assert len(hits) == 1, (s, hits)
    return hits[0]
idx.update({
    "fig_career": find("His best single game is four points"),            # c1: the seven metrics vs every five-game stretch
    "fig_speed": find("his longest skate of the season"),                  # c3: Edge bursts and distance
    "fig_giveaways": find("This is nearly double even his own norm."),     # c2: giveaway percentile by season
})
words = len(re.sub("<[^>]+>", "", re.sub(r"</?(?:p|li|ul|ol|h3)\b[^>]*>", " ", title + " " + " ".join(parts))).split())
OUT.parent.mkdir(parents=True, exist_ok=True)
json.dump(dict(title=title, parts=parts, idx=idx, words=words), open(OUT, "w"), indent=1, ensure_ascii=False)
print(title, "|", len(parts), "parts |", words, "words |", idx)
