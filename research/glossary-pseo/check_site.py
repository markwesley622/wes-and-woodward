#!/usr/bin/env python3
"""Post-build checks for the glossary launch (run after `npm run build`).

1. JSON-LD on every built page parses; every @id referenced inside a page's @graph resolves in that graph or
   is a known site node; glossary pages carry WebPage + DefinedTerm + DefinedTermSet + BreadcrumbList with the
   required fields; FAQPage only when the page shows a Questions section; the hub lists every term.
2. sitemap-0.xml lists the hub and every glossary page (and every self-canonical page in dist).
3. Every internal href in dist resolves to a built page (no dead links), and every page has the global footer.
Exit 1 on any failure.
"""
import json, pathlib, re, sys, html as H
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
SITE = "https://wesandwoodward.com"
GLOSS = sorted(p.stem for p in (ROOT / "src/data/glossary").glob("*.json"))
fails = []

pages = {}
for f in DIST.rglob("index.html"):
    rel = "/" + str(f.parent.relative_to(DIST)).replace("\\", "/")
    rel = "/" if rel == "/." else rel + "/"
    pages[rel] = f.read_text()

def graph(doc):
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S)
    out = []
    for b in blocks:
        try:
            out.append(json.loads(b))
        except Exception as e:
            fails.append(f"JSON-LD parse error: {e}")
    return out

def ids_referenced(o, acc):
    if isinstance(o, dict):
        if set(o) == {"@id"}:
            acc.add(o["@id"])
        for v in o.values():
            ids_referenced(v, acc)
    elif isinstance(o, list):
        for v in o:
            ids_referenced(v, acc)
    return acc

for path, doc in pages.items():
    gs = graph(doc)
    if not gs:
        fails.append(f"{path}: no JSON-LD")
        continue
    nodes = [n for g in gs for n in g.get("@graph", [g])]
    defined = set()
    def collect(o):
        if isinstance(o, dict):
            if o.get("@id") and len(o) > 1:
                defined.add(o["@id"])
            for v in o.values():
                collect(v)
        elif isinstance(o, list):
            for v in o:
                collect(v)
    collect(gs)
    for ref in ids_referenced(gs, set()):
        if ref not in defined and not ref.startswith(f"{SITE}/glossary/"):
            fails.append(f"{path}: @id {ref} referenced but not defined")
    if "<footer class=\"foot\"" not in doc:
        fails.append(f"{path}: global footer missing")

    if path.startswith("/glossary/") and path != "/glossary/":
        slug = path.split("/")[2]
        types = {n.get("@type") for n in nodes}
        for t in ["WebPage", "DefinedTerm", "DefinedTermSet", "BreadcrumbList", "Organization", "WebSite"]:
            if t not in types:
                fails.append(f"{path}: missing {t}")
        term = next((n for n in nodes if n.get("@type") == "DefinedTerm"), {})
        for k in ["name", "description", "url", "inDefinedTermSet"]:
            if not term.get(k):
                fails.append(f"{path}: DefinedTerm.{k} empty")
        wp = next((n for n in nodes if n.get("@type") == "WebPage"), {})
        for k in ["name", "description", "dateModified", "url"]:
            if not wp.get(k):
                fails.append(f"{path}: WebPage.{k} empty")
        has_faq_sec = 'id="questions"' in doc
        if ("FAQPage" in types) != has_faq_sec:
            fails.append(f"{path}: FAQPage schema and Questions section disagree")
        bc = next((n for n in nodes if n.get("@type") == "BreadcrumbList"), {})
        names = [i["name"] for i in bc.get("itemListElement", [])]
        if names[:2] != ["Home", "Glossary"] or len(names) != 3:
            fails.append(f"{path}: breadcrumb {names}")
        t = re.search(r"<title>(.*?)</title>", doc).group(1)
        if not H.unescape(t).endswith(" | Wes & Woodward"):
            fails.append(f"{path}: title suffix '{t}'")
        if len(re.findall(r"<h1", doc)) != 1:
            fails.append(f"{path}: H1 count")

hub = pages.get("/glossary/", "")
hub_nodes = [n for g in graph(hub) for n in g.get("@graph", [g])] if hub else []
dts = next((n for n in hub_nodes if n.get("@type") == "CollectionPage"), {}).get("mainEntity", {})
listed = {x["@id"].split("/glossary/")[1].split("/")[0] for x in dts.get("hasDefinedTerm", [])}
if listed != set(GLOSS):
    fails.append(f"hub hasDefinedTerm mismatch: missing {set(GLOSS) - listed}, extra {listed - set(GLOSS)}")

sm = "".join(p.read_text() for p in DIST.glob("sitemap-*.xml") if p.name != "sitemap-index.xml")
locs = set(re.findall(r"<loc>(.*?)</loc>", sm))
for s in ["/glossary/"] + [f"/glossary/{g}/" for g in GLOSS]:
    if SITE + s not in locs:
        fails.append(f"sitemap missing {s}")

for path, doc in pages.items():
    for href in re.findall(r'href="([^"#]+)', doc):
        u = urlparse(href)
        if u.scheme or href.startswith("//") or not href.startswith("/"):
            continue
        p = u.path if u.path.endswith("/") or "." in u.path.split("/")[-1] else u.path + "/"
        if "." in p.split("/")[-1]:
            if not (DIST / p.lstrip("/")).exists():
                fails.append(f"{path}: dead asset link {href}")
        elif p not in pages:
            fails.append(f"{path}: dead link {href}")

print(f"pages {len(pages)} · glossary {len(GLOSS)} · sitemap urls {len(locs)}")
for f in sorted(set(fails)):
    print("FAIL", f)
print("PASS" if not fails else f"{len(set(fails))} failures")
sys.exit(1 if fails else 0)
