#!/usr/bin/env python3
"""Fetch MoneyPuck season-summary CSVs into data/raw/moneypuck/.

Keeps the full-league file (needed for percentile context) plus a
DET-filtered copy of each for convenience.
"""
import csv
import io
import json
import pathlib
import ssl
import urllib.request

import certifi

SSL_CTX = ssl.create_default_context(cafile=certifi.where())

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "pipeline" / "config.json").read_text())
OUT = ROOT / "data" / "raw" / "moneypuck"
OUT.mkdir(parents=True, exist_ok=True)

SEASON = CFG["mp_season"]
TEAM = CFG["team"]
FILES = ["skaters", "goalies", "lines", "teams"]
BASE = f"https://moneypuck.com/moneypuck/playerData/seasonSummary/{SEASON}/regular/"
# Season simulations: one row per team per scenario (ALL, WINREG, WINOT, LOSSOT, LOSSREG).
# `points` is the projected season total; the odds columns are probabilities 0-1.
# Between seasons the file holds final standings with every probability at 0.
SIMS_URL = "https://moneypuck.com/moneypuck/simulations/simulations_recent.csv"


def fetch_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (wings-data-pipeline)"})
    with urllib.request.urlopen(req, timeout=60, context=SSL_CTX) as resp:
        return resp.read().decode("utf-8")


def main():
    for name in FILES:
        text = fetch_text(BASE + name + ".csv")
        (OUT / f"{name}.csv").write_text(text)

        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        det = [r for r in rows if r.get("team") == TEAM]
        det_path = OUT / f"{name}_det.csv"
        with det_path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(det)
        print(f"moneypuck/{name}.csv: {len(rows):,} league rows, {len(det):,} DET rows")

    sims = fetch_text(SIMS_URL)
    (OUT / "simulations.csv").write_text(sims)
    n = sum(1 for r in csv.DictReader(io.StringIO(sims)) if r.get("teamCode") == TEAM)
    print(f"moneypuck/simulations.csv: {n} {TEAM} scenario rows")


if __name__ == "__main__":
    main()
