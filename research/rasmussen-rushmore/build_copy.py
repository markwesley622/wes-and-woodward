#!/usr/bin/env python3
"""Mark's Google Doc tab -> data/site/articles/michael-rasmussen-mt-rushmore-copy.json (parts + idx anchors).

Copy runs verbatim. The 26 approved style-review edits (research/style/rasmussen-apply-2026-10-19.json) were applied
in the Doc itself on 10/19 and the export verified against research/style/rasmussen-final-expected-2026-10-19.txt,
so there is no FIX list here. Usage:
  python3 build_copy.py            # fetch the Doc tab export
  python3 build_copy.py draft.txt  # or read a saved export
"""
import html, json, pathlib, re, sys, urllib.request, ssl

DOC = "https://docs.google.com/document/d/1p8g-ROOP74WX7G2nJs1xgcVkV23qx4LKO52xSl5QdlM/export?format=txt&tab=t.v1j37f4b7w8g"
OUT = pathlib.Path(__file__).resolve().parents[2] / "data/site/articles/michael-rasmussen-mt-rushmore-copy.json"

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
    "The case for Michael Rasmussen": "case",
    "The case for the other three": "others",
    "So what happened on October 15?": "oct15",
}
parts, idx = [], {}
for l in lines[1:]:
    if l in HEADS:
        idx[HEADS[l]] = len(parts); parts.append(f'<h3 class="art">{html.escape(l, quote=False)}</h3>')
    else:
        parts.append(f"<p>{html.escape(l, quote=False)}</p>")
missing = [h for h in HEADS if HEADS[h] not in idx]
assert not missing, f"headings not found: {missing}"

# contextual internal links: (context that must appear once, the words inside it to link, href). Copy is unchanged;
# only the anchor words get wrapped.
LINKS = [
    ("were any even more inept than Michael Rasmussen?", "Michael Rasmussen", "/players/michael-rasmussen/"),
    ("Four of the 47 are Red Wings, and that’s depressing.", "Red Wings", "/team/"),
    ("when the NHL started tracking time on ice.", "time on ice", "/glossary/time-on-ice/"),
    ("he dished out a paltry 39 hits over the course of his drought, 5.6 per 60 minutes", "hits", "/glossary/hits/"),
    ("Marco Kasper. A smaller-framed forward who threw 91 hits", "Marco Kasper", "/players/marco-kasper/"),
    ("the primary on Andrew Copp’s game-winner.", "Andrew Copp", "/players/andrew-copp/"),
]
for ctx, anchor, href in LINKS:
    hits = [i for i, p in enumerate(parts) if ctx in p and p.startswith("<p>")]
    assert len(hits) == 1 and anchor in ctx, (ctx, hits)
    i = hits[0]
    parts[i] = parts[i].replace(ctx, ctx.replace(anchor, f'<a href="{href}">{anchor}</a>', 1), 1)

def find(s):  # index of the paragraph AFTER which a figure goes
    hits = [i for i, p in enumerate(parts) if s in p]
    assert len(hits) == 1, (s, hits)
    return hits[0]
idx.update({
    "fig_fates": find("19 of the 47 streaks are left."),                   # c4: what happened to the other 45
    "fig_trusted": find("merely the fifth-worst team in hockey"),              # c2: the seven at 13+ a night, after the Glendening reveal (Mark 10/19)
    "fig_onice": find("You’re on Mt. Rushmore!"),  # c3: on-ice goals, all 28 (closes his case)
})
words = len(re.sub("<[^>]+>", "", re.sub(r"</?(?:p|li|ul|ol|h3)\b[^>]*>", " ", title + " " + " ".join(parts))).split())
OUT.parent.mkdir(parents=True, exist_ok=True)
json.dump(dict(title=title, parts=parts, idx=idx, words=words), open(OUT, "w"), indent=1, ensure_ascii=False)
print(title, "|", len(parts), "parts |", words, "words |", idx)
