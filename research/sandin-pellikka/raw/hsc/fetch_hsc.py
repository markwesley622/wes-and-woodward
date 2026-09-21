#!/usr/bin/env python3
"""HockeyStatCards (hockeystatcards.com) fetcher.

The site is a TanStack Start app that server-renders its tables, so a plain GET
returns the data; no browser or Patreon login is needed for the public card.
Ratings are Dom Luszczyszyn's Game Score model, underlying data Natural Stat Trick.

  players/<nhlPlayerId>            -> skater card (season ratings + percentiles)
  players/<nhlPlayerId>?tab=logs   -> game-by-game log (TOI, iXG, xGF/xGA, GF/GA, GS)
"""
import json, re, ssl, sys, urllib.request
import certifi
from bs4 import BeautifulSoup

CTX = ssl.create_default_context(cafile=certifi.where())
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/140.0 Safari/537.36"


def _html(url, tries=5):
    """GET with backoff. The site rate-limits fairly aggressively (HTTP 429);
    keep requests spaced out when pulling a cohort of players."""
    import time
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, context=CTX, timeout=60).read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == tries - 1:
                raise
            time.sleep(10 * (i + 1))
    raise RuntimeError("unreachable")


def _tables(soup):
    out = []
    for tbl in soup.find_all("table"):
        head = [th.get_text(" ", strip=True) for th in tbl.find_all("th")]
        rows = []
        for tr in tbl.find_all("tr"):
            cells = [td.get_text(" ", strip=True) for td in tr.find_all("td")]
            if cells:
                rows.append(cells)
        if head and rows:
            out.append({"header": head, "rows": rows})
    return out


def card(pid):
    soup = BeautifulSoup(_html(f"https://hockeystatcards.com/players/{pid}"), "html.parser")
    text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))
    stats, ratings = {}, {}
    # Header strip: "Game score -0.01 15 % Offense -1.0 53 % Defense -4.6 3 % Net -5.6 14 %"
    for lbl, val, pct in re.findall(
            r"(Game score|Offense|Defense|Net) (-?\d+(?:\.\d+)?) (\d+) ?%", text):
        ratings[lbl] = {"value": float(val), "percentile": int(pct)}
    # Card stat tiles: "16:13 TOI", "41.21 xGF", "3.94 ixG"
    for val, lbl in re.findall(
            r"(-?\d+(?:\.\d+)?|\d+:\d+) "
            r"(TOI|Goals|Assists|Points|ixG|Game Score|xGF|GF|xGA|GA|PK xGA|PP Goals For)\b", text):
        stats.setdefault(lbl, val)
    return {"playerId": pid, "ratings": ratings, "stats": stats,
            "text": text, "tables": _tables(soup)}


def logs(pid):
    soup = BeautifulSoup(_html(f"https://hockeystatcards.com/players/{pid}?tab=logs"), "html.parser")
    for t in _tables(soup):
        if "Date" in t["header"] and "Game Score" in " ".join(t["header"]):
            return [dict(zip(t["header"], r)) for r in t["rows"]]
    return []


if __name__ == "__main__":
    pid = sys.argv[1] if len(sys.argv) > 1 else "8484223"
    json.dump({"card": card(pid), "logs": logs(pid)},
              open(f"hsc_{pid}.json", "w"), indent=1)
    print(f"wrote hsc_{pid}.json")
