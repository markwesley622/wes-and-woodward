#!/usr/bin/env python3
"""Per-game game scores for every Red Wings skater with 20+ GP (HockeyStatCards logs, cached
under data/raw/players/<id>/hsc_logs.json) -> data/site/team_gamescores.json with each
player's average, best and worst game, and counts at 2.0+ / below zero. Feeds the footnotes
in the player-page game-log tiles. HSC rate-limits: requests are spaced out."""
import json, pathlib, sys, time
ROOT = pathlib.Path(__file__).resolve().parents[1]
SEASON = json.loads((ROOT / "pipeline" / "config.json").read_text())["nhl_season"]
sys.path.insert(0, str(ROOT / "research" / "sandin-pellikka" / "raw" / "hsc")); import fetch_hsc as h

def f(v):
    try: return float(v)
    except (TypeError, ValueError): return None

skaters = [p for p in json.load((ROOT / "data" / "site" / "skaters.json").open()) if p["gamesPlayed"] >= 20]
nhl_log_dates = {}
out = []
for i, p in enumerate(skaters):
    pid = p["playerId"]; raw = ROOT / "data" / "raw" / "players" / str(pid); raw.mkdir(parents=True, exist_ok=True)
    path = raw / "hsc_logs.json"
    if not path.exists():
        path.write_text(json.dumps(h.logs(pid, season=SEASON, gtype=2), indent=1)); time.sleep(4)
    logs = json.load(path.open())
    games = [(g["Date"], f(g.get("Game Score"))) for g in logs if f(g.get("Game Score")) is not None]
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
