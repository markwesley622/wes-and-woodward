#!/usr/bin/env python3
"""Per-game quality of competition for Sandin-Pellikka, built from NHL shift charts.

Evolving Hockey's QoT/QoC table is season-only (its Filter Type dropdown offers
"Seasons" and nothing else), so the within-season question the column turns on —
did his competition get easier as his ice time was cut? — can't be answered there.
This rebuilds it from primary data:

  1. NHL shift charts (api.nhle.com .../shiftcharts) give every shift in a game.
  2. Reconstruct who is on the ice each second; keep only 5v5 seconds
     (both teams exactly five skaters, goalies excluded via the goalie bios list).
  3. For each second ASP is on, tally shared time with each opposing skater.
  4. Score each opponent by his EH 2025-26 xGAR per 60 and take the TOI-weighted mean.

That mirrors how EH builds QoC, at game resolution instead of season resolution.
"""
import csv, json, pathlib, ssl, time, urllib.parse, urllib.request
import certifi

HERE = pathlib.Path(__file__).resolve().parent
CTX = ssl.create_default_context(cafile=certifi.where())
ASP = 8484223


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (wings-data-pipeline)"})
    return json.load(urllib.request.urlopen(req, context=CTX, timeout=60))


def secs(period, clock):
    m, s = clock.split(":")
    return (int(period) - 1) * 1200 + int(m) * 60 + int(s)


def goalie_ids(season="20252026"):
    out, start = set(), 0
    while True:
        q = urllib.parse.urlencode({"isAggregate": "false", "isGame": "false", "start": start,
                                    "limit": 100,
                                    "cayenneExp": f"gameTypeId=2 and seasonId={season}"})
        d = get("https://api.nhle.com/stats/rest/en/goalie/bios?" + q)
        out |= {r["playerId"] for r in d["data"]}
        start += 100
        if start >= d["total"]:
            return out


def eh_quality():
    """EH 2025-26 xGAR per 60, all skaters, keyed by 'First Last'."""
    src = HERE.parents[1] / "rasmussen" / "raw" / "eh" / "xgar_all_seasons.csv"
    q = {}
    for r in csv.DictReader(open(src)):
        if r["Season"] != "25-26":
            continue
        toi = float(r["TOI_All"])
        if toi >= 60:
            q[r["Player"]] = float(r["xGAR"]) / toi * 60
    return q


def game_qoc(game_id, goalies, quality, names):
    q = urllib.parse.urlencode({"cayenneExp": f"gameId={game_id}"})
    rows = [r for r in get("https://api.nhle.com/stats/rest/en/shiftcharts?" + q)["data"]
            if r["typeCode"] == 517]
    teams = sorted({r["teamAbbrev"] for r in rows})
    on = {}          # second -> {team: set(playerId)}
    for r in rows:
        if r["playerId"] in goalies or not r["startTime"] or not r["endTime"]:
            continue
        names[r["playerId"]] = f'{r["firstName"]} {r["lastName"]}'
        a, b = secs(r["period"], r["startTime"]), secs(r["period"], r["endTime"])
        for t in range(a, b):
            on.setdefault(t, {}).setdefault(r["teamAbbrev"], set()).add(r["playerId"])
    shared, tot = {}, 0
    for t, d in on.items():
        if len(d) != 2 or any(len(v) != 5 for v in d.values()):
            continue                                    # not 5v5
        mine = next((k for k, v in d.items() if ASP in v), None)
        if mine is None:
            continue
        opp = teams[0] if teams[1] == mine else teams[1]
        tot += 1
        for p in d[opp]:
            shared[p] = shared.get(p, 0) + 1
    if not tot:
        return None
    num = den = 0.0
    for p, sec in shared.items():
        v = quality.get(names.get(p, ""))
        if v is not None:
            num += v * sec
            den += sec
    return dict(gameId=game_id, toi5v5=tot / 60, oppN=len(shared),
                coverage=den / sum(shared.values()),
                qoc=num / den if den else None)


def main():
    games = json.load(open(HERE / "eh" / "asp_deployment_by_date.json"))["games"]
    goalies, quality, names = goalie_ids(), eh_quality(), {}
    print(f"{len(goalies)} goalies, {len(quality)} skaters scored")
    out = []
    for i, g in enumerate(games, 1):
        r = game_qoc(int(g["gameId"]), goalies, quality, names)
        if r:
            r.update(date=g["date"], opp=g["opp"], toi=g["toi"], toiPct=g["toiPct"])
            out.append(r)
        if i % 10 == 0:
            print(f"  {i}/{len(games)}")
        time.sleep(0.2)
    json.dump(out, open(HERE / "asp_qoc_by_game.json", "w"), indent=1)
    print(f"wrote asp_qoc_by_game.json ({len(out)} games)")


if __name__ == "__main__":
    main()
