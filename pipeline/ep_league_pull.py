#!/usr/bin/env python3
"""Queue EliteProspects league scoring tables for the prospect system (runs against ep_receiver.py).

For every (league, season, position, age bucket) we pull page 1, read totalCount, then queue the rest.
EP's age filter is cumulative (U19 = everyone under 19), so exact-age cohorts are set differences
between neighbouring buckets; build_prospects.py does that. Rows carry EP player ids, position,
GP/G/A/PTS. Usage: python3 pipeline/ep_league_pull.py [season ...]   (default: both current seasons)
"""
import json, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EP = ROOT / "data" / "raw" / "ep"
SERVER = "http://127.0.0.1:8765"
LEAGUES = ["ahl", "ncaa", "shl", "ushl", "whl", "ohl", "qmjhl", "hockeyallsvenskan", "del", "liiga", "khl", "mhl", "nl", "vhl", "u20-nationell", "echl", "del2"]
SEASONS = sys.argv[1:] or ["2025-2026", "2026-2027"]
POS = ["F", "D"]
AGES = [f"U{a}" for a in range(17, 26)]


def key(lg, se, pos, age, page):
    return f"{lg}_{se}_{pos}_{age}_p{page}"


def url(lg, se, pos, age, page):
    return f"https://www.eliteprospects.com/league/{lg}/stats/{se}?position={pos}&age={age}" + (f"&page={page}" if page > 1 else "")


def enqueue(tasks):
    req = urllib.request.Request(SERVER + "/enqueue", data=json.dumps({"tasks": tasks}).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=30))


def done(k):
    return (EP / "league" / f"{k}.json").exists()


def main():
    first = [{"type": "league", "key": key(lg, se, p, a, 1), "url": url(lg, se, p, a, 1)} for lg in LEAGUES for se in SEASONS for p in POS for a in AGES]
    print("round 1:", enqueue(first), flush=True)
    pending = {t["key"] for t in first}
    queued_more = set()
    while pending:
        time.sleep(20)
        for k in list(pending):
            if done(k):
                pending.discard(k)
                d = json.load((EP / "league" / f"{k}.json").open())
                total = d.get("totalCount") or 0
                lg, se, p, a, _ = k.rsplit("_", 4)
                more = [{"type": "league", "key": key(lg, se, p, a, pg), "url": url(lg, se, p, a, pg)} for pg in range(2, (total + 99) // 100 + 1)]
                if more:
                    enqueue(more); queued_more.update(t["key"] for t in more)
        errs = {json.loads(l)["key"] for l in (EP / "errors.jsonl").open()} if (EP / "errors.jsonl").exists() else set()
        dead = {k for k in pending if k in errs and sum(1 for l in (EP / "errors.jsonl").open() if json.loads(l)["key"] == k) >= 3}
        pending -= dead
        print(f"round 1 pending {len(pending)}, round 2 queued {len(queued_more)}", flush=True)
    while any(not done(k) for k in queued_more):
        time.sleep(20)
        print("round 2 remaining", sum(1 for k in queued_more if not done(k)), flush=True)
    print("league pull complete")


if __name__ == "__main__":
    main()
