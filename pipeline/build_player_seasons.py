#!/usr/bin/env python3
"""Past Detroit seasons for the season dropdown on NHL player pages (Mark, 10/12).

Every earlier regular season a player spent with Detroit gets
data/site/players/seasons/<playerId>/<season>.json, carrying the same season-specific fields as his
main JSON (score, season line, MoneyPuck tiles, impact map, comps, game log, game-score tiles), so the
page template renders it unchanged. The page swaps a season in on the same URL; the season pages it
fetches are noindex and out of the sitemap (Mark: same URL, off the index).

Game logs: the three most recent seasons only, and never before 2025-26, the first season
HockeyStatCards covers (the W&W game score needs both it and MoneyPuck, and Mark ruled out a
MoneyPuck-only log for 2024-25). Split seasons: the line and the log are Detroit games only; MoneyPuck's
season file has one row per player, so its xG tiles cover the full season and the page says so.

Past seasons do not change, so raw pulls are cached under data/raw/players/<id>/seasons/<season>/ and
fetched only when missing; a nightly run rebuilds from cache in seconds. Run after build_player.py
(it reads data/site/players/*.json for who gets seasons).

Usage: python3 pipeline/build_player_seasons.py [playerId ...]
"""
import csv, json, pathlib, shutil, sys, time, urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_player as bp
from build_player import ROOT, SEASON, CTX, f, read_csv

LOG_FROM = "20252026"      # first season HockeyStatCards has game logs for
LOG_SEASONS = 3            # Mark, 10/12: game logs for the recent three seasons only
SITE = ROOT / "data" / "site" / "players" / "seasons"


def label(season): return f"{season[:4]}-{season[6:]}"
def back(season, n): return f"{int(season[:4]) - n}{int(season[4:]) - n}"
def has_log(season): return season >= max(LOG_FROM, back(SEASON, LOG_SEASONS - 1))


def det_rows(land, season):
    return [t for t in land.get("seasonTotals", []) if t.get("season") == int(season) and t.get("gameTypeId") == 2
            and t.get("leagueAbbrev") == "NHL" and "Detroit" in t.get("teamName", {}).get("default", "")]


def det_seasons(land):
    return sorted({str(t["season"]) for t in land.get("seasonTotals", []) if det_rows(land, t.get("season", 0))
                   and str(t["season"]) < SEASON})


def det_line(land, season):
    """His Detroit line that season (summed if the API splits it), shaped like build_player.season_line()."""
    rows = det_rows(land, season)
    s = lambda k: sum((t.get(k) or 0) for t in rows)
    big = max(rows, key=lambda t: t.get("gamesPlayed") or 0)
    return {"league": "NHL", "team": None, "gp": s("gamesPlayed"), "goals": s("goals"), "assists": s("assists"), "points": s("points"),
            "plusMinus": s("plusMinus"), "pim": s("pim"), "shots": s("shots"), "shootingPct": big.get("shootingPctg"), "toiPerGame": big.get("avgToi"),
            "ppPoints": s("powerPlayPoints"), "wins": s("wins"), "losses": s("losses"), "otLosses": s("otLosses"), "gaa": big.get("goalsAgainstAvg"),
            "savePct": big.get("savePctg"), "shutouts": s("shutouts")}


def mp_league(kind, year):
    """MoneyPuck's season summary (skaters/goalies) for a past season: the research package's copy when it
    has one (research/rasmussen/raw/mp, 2010-2025 skaters), else a cached download."""
    p = ROOT / "research" / "rasmussen" / "raw" / "mp" / f"{kind}_{year}.csv"
    if p.exists(): return read_csv(p)
    p = ROOT / "data" / "raw" / "moneypuck" / "seasons" / f"{kind}_{year}.csv"
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(f"https://moneypuck.com/moneypuck/playerData/seasonSummary/{year}/regular/{kind}.csv", headers={"User-Agent": "Mozilla/5.0 (wings-data-pipeline)"})
        p.write_bytes(urllib.request.urlopen(req, context=CTX, timeout=120).read())
    return read_csv(p)


def cached(path, pull):
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(pull(), indent=1))
    return json.load(path.open())


def logs(pid, season, goalie=False):
    """Detroit games that season: NHL box score, plus HockeyStatCards and MoneyPuck per-game for skaters."""
    raw = ROOT / "data" / "raw" / "players" / str(pid) / "seasons" / season
    nhl = cached(raw / "gamelog_nhl.json", lambda: bp.get(f"https://api-web.nhle.com/v1/player/{pid}/game-log/{season}/2")).get("gameLog", [])
    nhl = [g for g in nhl if g.get("teamAbbrev") == "DET"]
    if goalie or not nhl: return nhl, [], []
    sys.path.insert(0, str(ROOT / "research" / "sandin-pellikka" / "raw" / "hsc")); import fetch_hsc as h
    def pull_hsc():
        out = h.logs(pid, season=season, gtype=2); time.sleep(4); return out
    hsc = cached(raw / "hsc_logs.json", pull_hsc)
    # HockeyStatCards answers a season it does not have with the current one; never join that by date
    dates = {g["gameDate"][5:] for g in nhl}
    if hsc and sum(1 for g in hsc if g.get("Date") in dates) < 0.5 * len(nhl):
        print(f"  HSC log for {pid} {season} does not match his NHL dates; no game score that season"); hsc = []
    mp = cached(raw / "mp_games.json", lambda: bp.mp_games(pid, season[:4]))
    return nhl, hsc, mp


def team_file(season):
    """That season's team context for the game-score tiles: every Red Wing with 20+ GP (MoneyPuck's season
    file), his Detroit games only, same stats as build_team_gamescores.py."""
    path = ROOT / "data" / "site" / f"team_gamescores_{season}.json"
    rows = [r for r in mp_league("skaters", season[:4]) if r["situation"] == "all" and r["team"] == "DET" and f(r["games_played"]) >= 20]
    out = []
    for r in rows:
        pid = int(r["playerId"]); nhl, hsc, mp = logs(pid, season)
        games = [(g["date"][5:], g["gameScore"]) for g in bp.skater_games(nhl, hsc, mp) if g["gameScore"] is not None]
        if not games: continue
        gs = [v for _, v in games]; best = max(games, key=lambda t: t[1]); worst = min(games, key=lambda t: t[1])
        out.append({"playerId": pid, "name": r["name"], "position": r["position"], "games": len(gs), "average": round(sum(gs) / len(gs), 2),
                    "best": {"date": best[0], "value": best[1]}, "worst": {"date": worst[0], "value": worst[1]},
                    "above2": sum(1 for v in gs if v >= 2), "below0": sum(1 for v in gs if v < 0)})
    out.sort(key=lambda r: -r["average"])
    path.write_text(json.dumps({"season": season, "minGames": 20, "players": out}, indent=1))
    print(f"site/team_gamescores_{season}.json: {len(out)} skaters")
    return path


def build_season(pid, land, season, team_path=None):
    name = f"{land['firstName']['default']} {land['lastName']['default']}"
    pos = land["position"]; group = "D" if pos == "D" else "F"; goalie = pos == "G"
    ehs, year = f"{season[2:4]}-{season[6:8]}", season[:4]
    line = det_line(land, season)
    nhl_gp = sum((t.get("gamesPlayed") or 0) for t in land.get("seasonTotals", []) if t.get("season") == int(season) and t.get("gameTypeId") == 2 and t.get("leagueAbbrev") == "NHL")
    others = sorted({t["teamName"]["default"] for t in land.get("seasonTotals", []) if t.get("season") == int(season) and t.get("gameTypeId") == 2
                     and t.get("leagueAbbrev") == "NHL" and "Detroit" not in t["teamName"]["default"]})
    note = (f"Detroit games only: {line['gp']} of his {nhl_gp} that season; the rest were with {' and '.join('the ' + t for t in others)}. The xG tiles are MoneyPuck's full-season numbers."
            if others else None)
    out = {"playerId": pid, "name": name, "season": season, "seasonLabel": label(season), "kind": "G" if goalie else "S", "current": False,
           "seasonLine": line, "standIn": None, "hsc": {}, "note": note, "impact": [], "comps": [], "myComponents": None,
           "gameLog": [], "gameScore": None, "teamGameScore": None, "hasLogSeason": has_log(season)}
    if goalie:
        nhl = logs(pid, season, goalie=True)[0] if has_log(season) else []
        score, games, sk = bp.goalie_season(pid, nhl, mp_league("goalies", year))
        out.update(score=score, gameLog=games, moneypuck=sk)
    else:
        score, impact, comps, mine = bp.skater_value(name, group, ehs, pos)
        out.update(score=score, impact=impact, comps=comps, myComponents=mine, moneypuck=bp.mp_skater(pid, name, group, mp_league("skaters", year)))
        if has_log(season):
            games = bp.skater_games(*logs(pid, season))
            if any(g["gameScore"] is not None for g in games):
                out.update(gameLog=games, gameScore=bp.game_score_summary(games), teamGameScore=bp.team_context(games, pid, team_path) if team_path else None)
    dest = SITE / str(pid); dest.mkdir(parents=True, exist_ok=True)
    (dest / f"{season}.json").write_text(json.dumps(out, indent=1))
    sc = out["score"]
    print(f"  {name} {label(season)}: {line['gp']} GP · W-Value {sc['value'] if sc else None} · {len(out['gameLog'])} logged games")


def main(only=None):
    players = [json.load(p.open()) for p in sorted((ROOT / "data" / "site" / "players").glob("*.json"))]
    if only: players = [P for P in players if P["playerId"] in only]
    work = []
    for P in players:
        land = json.load((ROOT / "data" / "raw" / "players" / str(P["playerId"]) / "landing.json").open())
        work.append((P["playerId"], land, det_seasons(land)))
    teams = {}
    for s in sorted({s for _, _, ss in work for s in ss if has_log(s)}):
        try: teams[s] = team_file(s)
        except Exception as e:   # the tiles keep their numbers; only the team footnotes wait for the next run
            print("FAILED team context", s, repr(e)); old = ROOT / "data" / "site" / f"team_gamescores_{s}.json"; teams[s] = old if old.exists() else None
    for pid, land, seasons in work:
        try:
            for s in seasons: build_season(pid, land, s, teams.get(s))
        except Exception as e:   # a failed pull keeps last night's files for this player and moves on
            print("FAILED", pid, repr(e)); continue
        for old in (SITE / str(pid)).glob("*.json"):   # seasons that no longer qualify go away
            if old.stem not in seasons: old.unlink()
    if not only:   # players no longer published lose their season files too
        live = {str(pid) for pid, _, _ in work}
        for d in SITE.glob("*"):
            if d.is_dir() and d.name not in live: shutil.rmtree(d)
    print(f"seasons built for {sum(1 for _, _, s in work if s)} players, {sum(len(s) for _, _, s in work)} seasons")


if __name__ == "__main__":
    main({int(a) for a in sys.argv[1:]} or None)
