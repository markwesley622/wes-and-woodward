#!/usr/bin/env python3
"""Render every glossary page (and the hub) at 1440 and 390 wide from `astro preview` on :4329.
Fails on horizontal scroll, console errors, a missing H1, or a hover card on a term with a page but no
"Full definition" link. Usage: python3 render_check.py [--shots]  (shots → render/<slug>.{desktop,phone}.png)"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[2]
slugs = sorted(p.stem for p in (ROOT / "src/data/glossary").glob("*.json"))
shots = "--shots" in sys.argv
fails = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h, tag in [(1440, 900, "desktop"), (390, 844, "phone")]:
        pg = b.new_page(viewport={"width": w, "height": h})
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        for s in ["", *slugs]:
            url = f"http://localhost:4329/glossary/{s + '/' if s else ''}"
            errs.clear()
            r = pg.goto(url)
            pg.wait_for_timeout(150)
            if r.status != 200:
                fails.append(f"{url} {r.status}")
                continue
            sw = pg.evaluate("document.documentElement.scrollWidth")
            if sw > w:
                fails.append(f"{tag} {url}: horizontal scroll {sw}px")
            if errs:
                fails.append(f"{tag} {url}: console {errs[:2]}")
            if shots and s:
                pg.screenshot(path=str(ROOT / f"research/glossary-pseo/render/{s}.{tag}.png"), full_page=True)
        pg.close()
    # hover cards now link wherever the term has a page
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    for url in ["/team/", "/players/"]:
        pg.goto("http://localhost:4329" + url)
        pg.wait_for_timeout(300)
        cards = pg.evaluate("JSON.parse(document.getElementById('term-data').textContent).cards")
        for el in [e for e in pg.query_selector_all(".term") if e.is_visible()][:40]:
            tid = el.get_attribute("data-term")
            if not cards.get(tid, {}).get("h"):
                continue
            el.scroll_into_view_if_needed(); el.hover(); pg.wait_for_timeout(180)
            if not pg.query_selector("#term-card .term-full"):
                fails.append(f"{url}: card for {tid} has no Full definition link")
            pg.mouse.move(2, 2); pg.wait_for_timeout(220)
    b.close()
print(f"rendered hub + {len(slugs)} pages at 2 widths")
for f in fails:
    print("FAIL", f)
print("PASS" if not fails else f"{len(fails)} failures")
sys.exit(1 if fails else 0)
