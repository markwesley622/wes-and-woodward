#!/usr/bin/env python3
"""Per-game game scores for every Red Wings skater with 20+ GP, read from the game logs that
build_player.py writes (data/site/players/<id>.json: the W&W game score, MoneyPuck and
HockeyStatCards averaged) -> data/site/team_gamescores.json with each player's average, best and
worst game, and counts at 2.0+ / below zero. Feeds the footnotes in the player-page game-log tiles,
so run it after build_player.py and then rebuild the player pages."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
SEASON = json.loads((ROOT / "pipeline" / "config.json").read_text())["nhl_season"]

def f(v):
    try: return float(v)
    except (TypeError, ValueError): return None

skaters = [p for p in json.load((ROOT / "data" / "site" / "skaters.json").open()) if p["gamesPlayed"] >= 20]
nhl_log_dates = {}
out = []
for i, p in enumerate(skaters):
    pid = p["playerId"]; path = ROOT / "data" / "site" / "players" / f"{pid}.json"
    if not path.exists(): continue
    games = [(g["date"][5:], g["gameScore"]) for g in json.load(path.open()).get("gameLog", []) if g.get("gameScore") is not None]
    if not games: continue
    gs = [v for _, v in games]
    best = max(games, key=lambda t: t[1]); worst = min(games, key=lambda t: t[1])
    out.append({"playerId": pid, "name": p["name"], "position": p["position"], "games": len(gs), "average": round(sum(gs) / len(gs), 2),
                "best": {"date": best[0], "value": best[1]}, "worst": {"date": worst[0], "value": worst[1]},
                "above2": sum(1 for v in gs if v >= 2), "below0": sum(1 for v in gs if v < 0)})
    print(f"{i+1}/{len(skaters)} {p['name']}: avg {out[-1]['average']} best {best[1]} ({best[0]}) worst {worst[1]} ({worst[0]}) 2+: {out[-1]['above2']} <0: {out[-1]['below0']}")
out.sort(key=lambda r: -r["average"])
(ROOT / "data" / "site" / "team_gamescores.json").write_text(json.dumps({"season": SEASON, "minGames": 20, "players": out}, indent=1))
print("site/team_gamescores.json written:", len(out), "skaters")
