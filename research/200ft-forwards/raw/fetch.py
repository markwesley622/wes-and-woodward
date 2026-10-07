#!/usr/bin/env python3
"""Pull MoneyPuck team + skater season summaries (2008-2025) and NHL playoff brackets."""
import ssl, urllib.request, pathlib, certifi, time, json
CTX = ssl.create_default_context(cafile=certifi.where())
HERE = pathlib.Path(__file__).parent
def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (wings-data-pipeline)"})
    with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
        return r.read().decode("utf-8")
for y in range(2008, 2026):
    for kind in ("teams", "skaters", "goalies"):
        p = HERE / "mp" / f"{kind}_{y}.csv"
        if p.exists(): continue
        try:
            p.write_text(get(f"https://moneypuck.com/moneypuck/playerData/seasonSummary/{y}/regular/{kind}.csv"))
            print("ok", p.name)
        except Exception as e:
            print("FAIL", p.name, e)
        time.sleep(0.4)
for y in range(2009, 2027):
    p = HERE / "nhl" / f"bracket_{y}.json"
    if p.exists(): continue
    try:
        p.write_text(get(f"https://api-web.nhle.com/v1/playoff-bracket/{y}")); print("ok", p.name)
    except Exception as e:
        print("FAIL", p.name, e)
    time.sleep(0.3)
    p = HERE / "nhl" / f"standings_{y}.json"
    # last day of regular season differs; use standings-season lookup later
