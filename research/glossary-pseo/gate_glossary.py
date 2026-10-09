#!/usr/bin/env python3
"""Gate for glossary pages (contract: TEMPLATE.md). Usage: python3 gate_glossary.py [slug ...]  (default: every page)

Checks one src/data/glossary/<slug>.json against the template:
  slots present, title/H1/meta rules, keyword placement, copy rules (no em dashes, en dashes, colon in title/H1),
  FAQ count, sources present. Exit 1 on any failure.
"""
import html, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DIR = ROOT / "src" / "data" / "glossary"
STOP = {"in", "the", "a", "an", "of", "for", "on", "is", "what", "does", "mean", "how"}
REQUIRED = ["slug", "reviewed", "stat", "keywords", "seo", "hero", "facts", "origin", "calculation", "meaning", "uses", "limits", "related", "sources", "method"]


def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


def toks(s):
    return [t for t in re.findall(r"[a-z0-9%]+", s.lower())]


def phrase_in(kw, text):
    """Exact phrase, or the keyword's tokens in order with only stopwords between them."""
    k = [t for t in toks(kw)]
    sep = r"(?:\s+(?:" + "|".join(sorted(STOP)) + r"))*\s+"
    pat = r"\b" + sep.join(re.escape(t) for t in k) + r"\b"
    return re.search(pat, " ".join(toks(text))) is not None


def sentence_has(kw, text):
    """All non-stopword tokens of the keyword inside one sentence (any order)."""
    need = {t for t in toks(kw) if t not in STOP}
    for sent in re.split(r"(?<=[.!?])\s+", text):
        if need <= set(toks(sent)):
            return True
    return False


def body_text(G):
    parts = [G["hero"]["definition"], G["hero"]["dek"], *G["origin"], *G["calculation"]["intro"], *G["calculation"].get("inputs", []),
             G["calculation"]["example"], *G["calculation"].get("after", []), *[v["def"] for v in G["calculation"].get("variants", [])],
             *G["meaning"], *[u["html"] for u in G["uses"]], *[l["html"] for l in G["limits"]], *[f["a"] for f in G.get("faq", [])]]
    return plain(" ".join(parts))


def check(path):
    G = json.loads(path.read_text())
    fails = []
    for k in REQUIRED:
        if k not in G:
            fails.append(f"missing slot {k}")
    if fails:
        return fails
    title, h1, meta = G["seo"]["title"], G["seo"]["h1"], G["seo"]["description"]
    if ":" in title or ":" in h1 or "|" in title or "|" in h1:
        fails.append("colon or pipe in title/H1")
    if len(title) > 60:
        fails.append(f"title {len(title)} chars > 60")
    if len(meta) > 160:
        fails.append(f"meta description {len(meta)} chars > 160")
    body = body_text(G)
    first100 = " ".join(body.split()[:100])
    pk = G["keywords"]["primary"]
    for where, text in [("title", title), ("H1", h1), ("meta", meta), ("first 100 words", first100)]:
        if not phrase_in(pk, text):
            fails.append(f"primary '{pk}' missing from {where}")
    for kw in G["keywords"].get("supporting", []):
        if not (phrase_in(kw, body) or sentence_has(kw, body)):
            fails.append(f"supporting '{kw}' not in body")
    raw = path.read_text()
    if "—" in raw:
        fails.append("em dash in page copy")
    if re.search(r"20\d\d–\d\d", raw):
        fails.append("en dash in a season range (site prose uses 2025-26)")
    if len(G.get("faq", [])) > 4:
        fails.append("more than 4 FAQs")
    if len(G["facts"]) not in (4, 8):
        fails.append("facts must be 4 or 8 tiles (one or two grid rows)")
    if not G["sources"]:
        fails.append("no sources")
    return fails


slugs = sys.argv[1:] or [p.stem for p in sorted(DIR.glob("*.json"))]
bad = 0
for s in slugs:
    f = check(DIR / f"{s}.json")
    print(f"{s}: {'PASS' if not f else 'FAIL'}")
    for x in f:
        print("  -", x)
    bad += bool(f)
sys.exit(1 if bad else 0)
