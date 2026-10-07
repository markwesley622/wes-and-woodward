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


def logs(pid, season=None, gtype=2):
    """Game log. HSC defaults to the CURRENT season (preseason once camps open) and, for a past
    season, to its playoffs (type 3); always pass the season and type=2 for a regular-season log."""
    q = f"?tab=logs&year={season}&type={gtype}" if season else "?tab=logs"
    soup = BeautifulSoup(_html(f"https://hockeystatcards.com/players/{pid}{q}"), "html.parser")
    for t in _tables(soup):
        if "Date" in t["header"] and "Game Score" in " ".join(t["header"]):
            return [dict(zip(t["header"], r)) for r in t["rows"]]
    return []


PLAYERS_FN = "9f02f15cc45d78c1c11da0f238fdfadc874ab97c10b7ddfcf15b6f96f0f35242"   # /players table server fn (main-*.js, "sQ")


def _seroval(v, ids):
    """Encode a plain dict/str/int the way TanStack Start's client does (seroval toJSON nodes)."""
    if isinstance(v, dict):
        i = len(ids); ids.append(i)
        return {"t": 10, "i": i, "p": {"k": list(v), "v": [_seroval(x, ids) for x in v.values()]}, "o": 0}
    return {"t": 1, "s": v} if isinstance(v, str) else {"t": 0, "s": v}


def _unseroval(n):
    t = n["t"]
    if t in (0, 1): return n["s"]
    if t == 2: return {0: None, 1: None, 2: True, 3: False}.get(n["s"])
    if t == 9: return [_unseroval(x) for x in n["a"]]
    if t in (10, 11): return {k: _unseroval(x) for k, x in zip(n["p"]["k"], n["p"]["v"])}
    raise ValueError(f"unhandled seroval node {n}")


def league_gamescores(season, gtype=2):
    """Every skater's season game score (the /players table: gamesPlayed, avgAdjGameScore,
    totalAdjGameScore = the sum of his game-log Game Score column). The table's server function caps
    pages at 200, so this walks the pages; sorted by player name so ties cannot shuffle across pages."""
    import time, urllib.parse
    rows, page, total = {}, 1, None
    while total is None or len(rows) < total:
        data = {"season": int(season), "type": gtype, "page": page, "pageSize": 200, "view": "gameScore", "sortKey": "player", "sortDir": "asc"}
        payload = urllib.parse.quote(json.dumps({"t": _seroval({"data": data}, []), "f": 127, "m": []}, separators=(",", ":")))
        req = urllib.request.Request(f"https://hockeystatcards.com/_serverFn/{PLAYERS_FN}?payload={payload}",
                                     headers={"User-Agent": UA, "x-tsr-serverFn": "true", "accept": "application/json"})
        res = _unseroval(json.loads(urllib.request.urlopen(req, context=CTX, timeout=60).read()))["result"]
        total = res["total"]
        if not res["rows"]: break
        for r in res["rows"]: rows[r["playerId"]] = r
        page += 1; time.sleep(2)
    if len(rows) != total:
        raise RuntimeError(f"HSC players table: got {len(rows)} of {total} rows")
    return list(rows.values())


if __name__ == "__main__":
    pid = sys.argv[1] if len(sys.argv) > 1 else "8484223"
    json.dump({"card": card(pid), "logs": logs(pid)},
              open(f"hsc_{pid}.json", "w"), indent=1)
    print(f"wrote hsc_{pid}.json")
