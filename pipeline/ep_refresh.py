#!/usr/bin/env python3
"""Refresh the EliteProspects inputs for the prospect system (run whenever the pipeline should catch up:
new signings, this season's lines, the current-season league tables). Needs ep_receiver.py serving and
ep_worker.js running on an eliteprospects.com tab in Mark's personal Chrome (Browser 2).

    python3 pipeline/ep_receiver.py &            # once
    python3 pipeline/ep_refresh.py               # queues: DET system page -> every system player page
    python3 pipeline/ep_league_pull.py 2026-2027 # then the current-season league tables (re-pulls nothing
                                                 #   already on disk unless you delete it first)
    python3 pipeline/build_prospects.py          # then rebuild the site data

The cohort (draft classes 2008-2019 and their player pages) is historical and is not re-pulled here.
"""
import json, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EP = ROOT / "data" / "raw" / "ep"
SERVER = "http://127.0.0.1:8765"
SYSTEM_URL = "https://www.eliteprospects.com/team/60/detroit-red-wings/in-the-system"


def enqueue(tasks):
    req = urllib.request.Request(SERVER + "/enqueue", data=json.dumps({"tasks": tasks}).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=30))


def main():
    sysf = EP / "system" / "DET.json"
    before = sysf.stat().st_mtime if sysf.exists() else 0
    print("system page:", enqueue([{"type": "system", "key": "DET", "url": SYSTEM_URL, "force": True}]), flush=True)
    while not sysf.exists() or sysf.stat().st_mtime <= before:
        time.sleep(5)
    d = json.load(sysf.open())
    players = d["skaters"] + d["goalies"]
    tasks = [{"type": "player", "key": p["id"], "url": f"https://www.eliteprospects.com/player/{p['id']}/x", "force": True} for p in players]
    print(f"{len(players)} system players:", enqueue(tasks), flush=True)
    keys = {t["key"] for t in tasks}; t0 = time.time()
    while True:
        time.sleep(15)
        fresh = sum(1 for k in keys if (EP / "player" / f"{k}.json").exists() and (EP / "player" / f"{k}.json").stat().st_mtime >= t0)
        print(f"  {fresh}/{len(keys)} refreshed", flush=True)
        if fresh >= len(keys): break
    print("refresh complete; now run ep_league_pull.py for the current season, then build_prospects.py")


if __name__ == "__main__":
    main()
