"""Pull the running prose out of a glossary page JSON (one paragraph per line) for style_metrics.py.
Usage: python3 extract_prose.py <slug> [--all] > out.txt
Default = the running prose the voice targets apply to (hero definition and dek, origin, calculation intro,
example and after, meaning, uses, limits, FAQ answers). --all adds the definitional micro-copy (variant
definitions) and the live-slot UI lines, which are short by design and skew paragraph metrics."""
import html, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
G = json.loads((ROOT / "src/data/glossary" / f"{sys.argv[1]}.json").read_text())
plain = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s)).strip()
C = G["calculation"]
paras = [G["hero"]["definition"], G["hero"]["dek"], *G["origin"], *C["intro"], C["example"], *C.get("after", []),
         *G["meaning"], *[u["html"] for u in G["uses"]], *[l["html"] for l in G["limits"]], *[f["a"] for f in G.get("faq", [])]]
if "--all" in sys.argv:
    paras += [v["def"] for v in C.get("variants", [])]
if "--all" in sys.argv and G.get("live"):
    paras += [G["live"].get("intro", ""), G["live"].get("smallSampleNote", "").replace("{gp}", "12")]
print("\n\n".join(plain(p) for p in paras if p))
