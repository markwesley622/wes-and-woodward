#!/usr/bin/env python3
"""Daniel Sprong 2023-24 split at Feb 29: goals vs MoneyPuck xG and shooting %, all situations and 5v5."""
import csv, json, ssl, urllib.request, certifi, pathlib
HERE = pathlib.Path(__file__).parent; PID = "8478466"; CUT = "2024-02-29"
ctx = ssl.create_default_context(cafile=certifi.where())
def get(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), context=ctx).read())
gl = get(f"https://api-web.nhle.com/v1/player/{PID}/game-log/20232024/2")["gameLog"]
date = {str(g["gameId"]): g["gameDate"] for g in gl}
S = {}
for r in csv.DictReader(open(HERE / "shots/shots_2023.csv")):
    if r["shooterPlayerId"].split(".")[0] != PID or r["isPlayoffGame"] != "0": continue
    gid = "2023" + "02" + str(int(float(r["game_id"])) % 10000).zfill(4) if len(r["game_id"].split(".")[0]) <= 5 else r["game_id"].split(".")[0]
    d = date[gid]; half = "through Feb 29" if d <= CUT else "Mar 1 on"
    five = r["homeSkatersOnIce"] == "5" and r["awaySkatersOnIce"] == "5"
    for key in [(half, "all")] + ([(half, "5v5")] if five else []):
        s = S.setdefault(key, dict(g=0, xg=0.0, sog=0, att=0))
        s["g"] += int(float(r["goal"])); s["xg"] += float(r["xGoal"]); s["att"] += 1
        s["sog"] += int(float(r["shotWasOnGoal"]))
for half in ("through Feb 29", "Mar 1 on"):
    G = [g for g in gl if (g["gameDate"] <= CUT) == (half == "through Feb 29")]
    print(half, "| NHL log: GP", len(G), "G", sum(g["goals"] for g in G), "A", sum(g["assists"] for g in G), "SOG", sum(g["shots"] for g in G),
          "S%", round(100 * sum(g["goals"] for g in G) / sum(g["shots"] for g in G), 1), "TOI/gm", round(sum(int(g["toi"].split(":")[0]) + int(g["toi"].split(":")[1]) / 60 for g in G) / len(G), 1))
    for sit in ("all", "5v5"):
        s = S[(half, sit)]
        print(f"   MoneyPuck {sit}: {s['g']} G on {s['xg']:.1f} xG ({s['g']-s['xg']:+.1f}), {s['sog']} SOG, S% {100*s['g']/s['sog']:.1f}, unblocked attempts {s['att']}")
json.dump({f"{k[0]}|{k[1]}": v for k, v in S.items()}, open(HERE / "sprong_split.json", "w"), indent=1)
