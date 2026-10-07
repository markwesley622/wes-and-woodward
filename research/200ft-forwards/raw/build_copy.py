#!/usr/bin/env python3
"""Mark's Google Doc copy -> data/site/articles/two-way-forwards-copy.json (parts + idx anchors). Fact fixes are listed in FIX and reported."""
import json, pathlib, re, html
SRC = pathlib.Path("/private/tmp/claude-501/-Users-markwesley/44b47499-45b5-4275-a5d5-36fa0e7f23e3/scratchpad/article.txt")
OUT = pathlib.Path(__file__).resolve().parents[3] / "data/site/articles/two-way-forwards-copy.json"
FIX = [  # (old, new, why). Mark 10/7: keep his 46% / 76 pts / 36 goals wording for Seider and Larkin; only these fixes are applied.
    ("Sprong ranked in the 3rd percentile for defense and Fabbri ranked in the 6th percentile", "Fabbri ranked in the 3rd percentile for defense and Sprong ranked in the 6th percentile", "percentiles were swapped (EH even-strength defense, 2023-24)"),
    ("In 2025-26? How about 30th in goals - xG?", "In 2025-26? How about 29th in goals - xG?", "Detroit was 29th in goals minus xG (30th in goals per 60)"),
    ("Andrew Copp led the entire NHL in goals below expected.", "Andrew Copp was among the five worst in the entire NHL in goals below expected.", "Lee, DeBrusk, Hertl and Meier were further under; Copp was 5th"),
    ("the Red Wings ranked 20th and 22nd in chances allowed", "the Red Wings ranked 22nd and 15th in chances allowed", "20th was 2023-24; the last two years are 22nd and 15th"),
    ("Michael Brandegg-Nygard", "Michael Brandsegg-Nygård", "spelling"),
    ("Andrei Vasilevsky-style", "Andrei Vasilevskiy-style", "spelling"),
    ("Andrei Vasilevsky became", "Andrei Vasilevskiy became", "spelling"),
    ("Matthew Barzal", "Mathew Barzal", "spelling"),
]
txt = SRC.read_text(encoding="utf-8-sig")
for old, new, why in FIX:
    assert old in txt, old
    txt = txt.replace(old, new)
lines = [l.strip() for l in txt.split("\n")]
lines = [l for l in lines if l]
title = lines[0]
HEADS = {"What the Red Wings prioritized in the draft": "draft", "How this translated to the professional level": "pro",
         "What teams who prioritized 2-way forwards were most successful?": "models", "The peak for this iteration of the Detroit Red Wings": "peak"}
parts, idx = [], {}
for l in lines[1:]:
    if l in HEADS:
        idx[HEADS[l]] = len(parts); parts.append(f'<h3 class="art">{html.escape(l)}</h3>')
    else:
        parts.append(f"<p>{html.escape(l, quote=False)}</p>")
# anchors: index of the paragraph AFTER which a figure goes
def find(s):
    for i, p in enumerate(parts):
        if s in p: return i
    raise KeyError(s)
idx.update({
    "fig_sprong": find("Their offense, theoretically"),
    "fig_goals": find("How about 29th in goals - xG"),
    "fig_forwards": find("much rejoicing in Motown"),
    "fig_ranks": find("Over time you can add to the offense"),
    "fig_grid": find("not enough to overcome the below average defense"),
    "fig_winners": find("Drew Doughty was their top defenseman"),
    "fig_larkin": find("Larkin’s main value actually comes"),
    "fig_comps": find("2016-17 Tampa Bay Lightning and the 2019-20 New York Islanders"),
})
words = len(re.sub("<[^>]+>", " ", " ".join(parts)).split())
json.dump(dict(title=title, parts=parts, idx=idx, words=words), open(OUT, "w"), indent=1, ensure_ascii=False)
print(title, len(parts), "parts", words, "words", idx)
