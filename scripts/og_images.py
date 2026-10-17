#!/usr/bin/env python3
"""Link-preview images (og:image, 1200x630) for articles, player pages and prospect pages (Mark, 10/13).

  articles   public/og/<article slug>.png      the article's /analysis/ thumbnail at rest (puck down, ghost front, D)
             public/og/<article slug>-16x9.png, -4x3.png, -1x1.png
                                               the same thumbnail for the NewsArticle `image` list (Google wants
                                               all three ratios, 1200 px wide; src/lib/articles.js)
  players    public/og/players/<slug>.jpg      the commissioned illustration on site paper
             public/og/players/<slug>.png      the block-letter initials, for player pages with no illustration
  prospects  public/og/prospects/<slug>.png    the block-letter initials

Run after `npm run build` (line art is rendered from dist/ in headless Chromium via Playwright), then build again so
Base.astro sees the files: pages only point og:image at a file that exists, otherwise the site icon.
`--articles` renders the article images only (use it when publishing a new article).
"""
import functools, http.server, json, pathlib, re, socketserver, sys, threading
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIST, PUB = ROOT / "dist", ROOT / "public"
OG = PUB / "og"
W, H = 1200, 630
PAPER = (0xE9, 0xE8, 0xE5)
# article image ratios: name -> CSS frame (shot at 3x) and the width of the 16:9 thumbnail inside it
RATIOS = {"16x9": (400, 225, 372), "4x3": (400, 300, 380), "1x1": (400, 400, 384)}
# articles are shot from /analysis/, which carries every article's thumbnail as #an-<slug> (the homepage only shows three)
ANALYSIS = "analysis/index.html"


def article_slugs():
    return sorted(set(re.findall(r'id="an-([a-z0-9-]+)"', (DIST / ANALYSIS).read_text())))


def player_art():
    """Illustration fitted to the full height, bottom edge on the bottom edge (the art box rule), centred."""
    out = OG / "players"; out.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted((ROOT / "data/site/players").glob("*.json")):
        P = json.loads(f.read_text())
        src = PUB / "players" / f"{P['playerId']}-art.webp"
        if not src.exists() or not (DIST / "players" / P["slug"] / "index.html").exists():
            continue
        art = Image.open(src).convert("RGBA")
        h = H; w = round(art.width * h / art.height)
        art = art.resize((w, h), Image.LANCZOS)
        canvas = Image.new("RGB", (W, H), PAPER)
        canvas.paste(art, ((W - w) // 2, H - h), art)
        canvas.save(out / f"{P['slug']}.jpg", quality=86, optimize=True, progressive=True)
        n += 1
    return n


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


def serve():
    handler = functools.partial(Quiet, directory=str(DIST))
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}"


# Lift one element out of the page into a fixed 400x210 box at the top-left (shot at 3x = 1200x630). Moving it to
# <body> escapes any transformed or clipped ancestor; Astro's scoped styles travel with the element's attributes.
LIFT = """([sel, p, mode, fw, fh, tw]) => {
  const el = document.querySelector(sel);
  if (!el) return false;
  const frame = document.createElement('div');
  Object.assign(frame.style, { position: 'fixed', left: '0', top: '0', width: fw + 'px', height: fh + 'px', zIndex: '2147483647',
    display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden',
    background: mode === 'thumb' ? 'var(--ghost)' : 'var(--paper)' });
  document.body.appendChild(frame);
  frame.appendChild(el);
  el.dataset.still = '1';                                 // article thumbs: hold the resting pose, no loop
  if (mode === 'thumb') {                                 // keep the card's own 16:9 framing, inset on the same grey
    Object.assign(el.style, { position: 'relative', width: tw + 'px', height: 'auto', aspectRatio: '16 / 9', margin: '0', borderRadius: '0', transform: 'none', flex: 'none' });
  } else {                                                // initials: fill the frame (letters sit in a 4:3 viewBox, centred)
    Object.assign(el.style, { position: 'relative', width: '400px', height: '210px', aspectRatio: 'auto', margin: '0', transform: 'none', flex: 'none' });
    el.querySelectorAll('.tag').forEach((t) => { t.style.display = 'none'; });   // no jersey-number label
  }
  if (p !== null) el.style.setProperty('--p', String(p));
  return true;
}"""


def shoot(page, url, sel, p, mode, dest, frame=(400, 210, 344)):
    fw, fh, tw = frame
    page.goto(url, wait_until="networkidle")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(300)
    if not page.evaluate(LIFT, [sel, p, mode, fw, fh, tw]):
        return False
    page.wait_for_timeout(250)
    dest.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(dest), clip={"x": 0, "y": 0, "width": fw, "height": fh})
    img = Image.open(dest).convert("RGB")
    assert img.size == (fw * 3, fh * 3), img.size
    img.quantize(colors=96, method=Image.MEDIANCUT).save(dest, optimize=True)   # line art: small palette PNG
    return True


def line_art(articles_only=False):
    from playwright.sync_api import sync_playwright
    httpd, base = serve()
    done = {"articles": 0, "players": 0, "prospects": 0}
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch()
            page = b.new_page(viewport={"width": 1200, "height": 800}, device_scale_factor=3, reduced_motion="no-preference")
            for slug in article_slugs():
                done["articles"] += shoot(page, base + "/analysis/", f"#an-{slug}", None, "thumb", OG / f"{slug}.png")
                for name, frame in RATIOS.items():
                    done["articles"] += shoot(page, base + "/analysis/", f"#an-{slug}", None, "thumb", OG / f"{slug}-{name}.png", frame)
            for kind in (() if articles_only else ("players", "prospects")):
                for d in sorted((DIST / kind).iterdir()):
                    html = d / "index.html"
                    if not html.exists() or "data-initials" not in html.read_text():
                        continue                              # illustrated player pages are handled by player_art()
                    if kind == "players" and re.search(r'/players/\d+-art\.webp', html.read_text()):
                        continue
                    done[kind] += shoot(page, f"{base}/{kind}/{d.name}/", "[data-initials]", None, "initials", OG / kind / f"{d.name}.png")
            b.close()
    finally:
        httpd.shutdown()
    return done


if __name__ == "__main__":
    assert (DIST / "index.html").exists(), "run `npm run build` first"
    only = "--articles" in sys.argv
    if not only:
        print("illustrated players:", player_art())
    print("line art:", line_art(only))
