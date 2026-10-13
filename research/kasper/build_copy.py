#!/usr/bin/env python3
"""Mark's Google Doc tab -> data/site/articles/marco-kasper-copy.json (parts + idx anchors).

Copy runs verbatim. The 42 style-review edits (research/style/edits-kasper-2026-10-13.json) were
applied in the Doc itself on 10/13, so there is no FIX list here. Usage:
  python3 build_copy.py            # fetch the Doc tab export
  python3 build_copy.py draft.txt  # or read a saved export
"""
import html, json, pathlib, re, sys, urllib.request, ssl

DOC = "https://docs.google.com/document/d/1p8g-ROOP74WX7G2nJs1xgcVkV23qx4LKO52xSl5QdlM/export?format=txt&tab=t.7db8p9ex0yu7"
OUT = pathlib.Path(__file__).resolve().parents[2] / "data/site/articles/marco-kasper-copy.json"

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
    "Marco Kasper’s rookie season was better than his box score": "rookie",
    "What’s worse than a sophomore slump? A Kasper": "slump",
    "How Marco Kasper’s second season impacted his career trajectory": "trajectory",
    "Getting back to the original trajectory": "back",
}
parts, idx, bullets = [], {}, []
def flush():
    global bullets
    if bullets:
        parts.append('<ul class="art">' + "".join(f"<li>{html.escape(b, quote=False)}</li>" for b in bullets) + "</ul>")
        bullets = []
for l in lines[1:]:
    if l.startswith("* "):
        bullets.append(l[2:].strip()); continue
    flush()
    if l in HEADS:
        idx[HEADS[l]] = len(parts); parts.append(f'<h3 class="art">{html.escape(l, quote=False)}</h3>')
    else:
        parts.append(f"<p>{html.escape(l, quote=False)}</p>")
flush()
missing = [h for h in HEADS if HEADS[h] not in idx]
assert not missing, f"headings not found: {missing}"

# contextual internal links: (context that must appear once, the words inside it to link, href). Copy is unchanged;
# only the anchor words get wrapped. Mark 10/13 asked for the player page and other contextual links.
LINKS = [
    ("What Marco Kasper did last year", "Marco Kasper", "/players/marco-kasper/"),
    ("His RAPM xG±/60", "RAPM xG±/60", "/glossary/rapm/"),
    ("His expected goals above replacement (xGAR)", "expected goals above replacement (xGAR)", "/glossary/wins-above-replacement/"),
    ("behind Dylan Larkin", "Dylan Larkin", "/players/dylan-larkin/"),
    ("five-on-five (ixG/60)", "five-on-five (ixG/60)", "/glossary/individual-expected-goals/"),
    ("his ice time went from 16:45", "ice time", "/glossary/time-on-ice/"),
    ("His expected goals only dropped", "expected goals", "/glossary/expected-goals/"),
    ("The Red Wings could stomach", "Red Wings", "/team/"),
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
    "fig_quarters": find("Most of his scoring came in the final 39 games"),       # c8
    "fig_rarity": find("Of those 172 forwards, four fell as far as he did."),      # c4
    "fig_peak": find("Instead? That expected peak is 45 points."),                # c2
    "fig_lines": find("The model’s three lines for Kasper"),                      # c1
    "fig_points": find("accidentally dying your hair purple"),                    # c3 (after the callback, not between setup and payoff)
    "fig_needs": find("All thanks to that second season."),                      # c6 (keeps "If that sounds unreasonable" next to its setup)
    "fig_starts": find("The realistic bar is lower"),                             # c7
})
words = len(re.sub("<[^>]+>", "", re.sub(r"</?(?:p|li|ul|h3)\b[^>]*>", " ", title + " " + " ".join(parts))).split())  # inline <a> tags must not split words
OUT.parent.mkdir(parents=True, exist_ok=True)
json.dump(dict(title=title, parts=parts, idx=idx, words=words), open(OUT, "w"), indent=1, ensure_ascii=False)
print(title, "|", len(parts), "parts |", words, "words |", idx)
