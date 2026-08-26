#!/usr/bin/env python3
"""Fetch Red Wings data from the official NHL API into data/raw/nhl/."""
import json
import pathlib
import ssl
import urllib.request

import certifi

SSL_CTX = ssl.create_default_context(cafile=certifi.where())

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "pipeline" / "config.json").read_text())
OUT = ROOT / "data" / "raw" / "nhl"
OUT.mkdir(parents=True, exist_ok=True)

TEAM = CFG["team"]
SEASON = CFG["nhl_season"]
GAME_TYPE = CFG["game_type"]

ENDPOINTS = {
    "roster": f"https://api-web.nhle.com/v1/roster/{TEAM}/{SEASON}",
    "club_stats": f"https://api-web.nhle.com/v1/club-stats/{TEAM}/{SEASON}/{GAME_TYPE}",
    "schedule": f"https://api-web.nhle.com/v1/club-schedule-season/{TEAM}/{SEASON}",
    "standings": f"https://api-web.nhle.com/v1/standings/{CFG['standings_date']}",
}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "wings-data-pipeline/0.1"})
    with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
        return json.load(resp)


def main():
    for name, url in ENDPOINTS.items():
        data = fetch(url)
        path = OUT / f"{name}.json"
        path.write_text(json.dumps(data, indent=1))
        print(f"nhl/{name}.json written ({path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
