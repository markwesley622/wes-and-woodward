#!/usr/bin/env python3
"""Merge raw NHL API + MoneyPuck pulls into site-ready JSON in data/site/.

Outputs:
  team.json    - record, standings context, team-level xG/Corsi (all + 5on5), league ranks
  skaters.json - per-skater card data: counting stats + xG metrics + league percentiles
  goalies.json - per-goalie card data incl. GSAx (goals saved above expected)
  lines.json   - 5on5 forward lines and D pairs by TOI with xG%/CF%
  results.json - completed-game log for rolling/trend charts
"""
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "pipeline" / "config.json").read_text())
RAW_NHL = ROOT / "data" / "raw" / "nhl"
RAW_MP = ROOT / "data" / "raw" / "moneypuck"
OUT = ROOT / "data" / "site"
OUT.mkdir(parents=True, exist_ok=True)

TEAM = CFG["team"]

# Percentile pools: minimum 5on5 icetime (seconds) to count as a "regular"
MIN_SKATER_5V5_SECONDS = 300 * 60
MIN_GOALIE_SECONDS = 600 * 60


def f(row, col):
    try:
        return float(row.get(col) or 0)
    except ValueError:
        return 0.0


def read_csv(path):
    with path.open() as fh:
        return list(csv.DictReader(fh))


def percentile(pool, value):
    """Share of pool values strictly below `value`, 0-100."""
    if not pool:
        return None
    below = sum(1 for v in pool if v < value)
    return round(100 * below / len(pool), 1)


def write(name, obj):
    path = OUT / name
    path.write_text(json.dumps(obj, indent=1))
    print(f"site/{name} written ({path.stat().st_size:,} bytes)")


def full_name(p):
    return f"{p['firstName']['default']} {p['lastName']['default']}"


# ---------------------------------------------------------------- team.json
def build_team():
    standings = json.load((RAW_NHL / "standings.json").open())["standings"]
    det = next(r for r in standings if r["teamAbbrev"]["default"] == TEAM)
    mp_teams = read_csv(RAW_MP / "teams.csv")

    def team_rank(metric, situation):
        rows = [r for r in mp_teams if r["situation"] == situation]
        ordered = sorted(rows, key=lambda r: f(r, metric), reverse=True)
        return next(i + 1 for i, r in enumerate(ordered) if r["team"] == TEAM)

    det_situ = {r["situation"]: r for r in mp_teams if r["team"] == TEAM}

    situations = {}
    for situ in ("all", "5on5", "5on4", "4on5"):
        r = det_situ.get(situ)
        if not r:
            continue
        situations[situ] = {
            "xGoalsPct": f(r, "xGoalsPercentage"),
            "corsiPct": f(r, "corsiPercentage"),
            "xGoalsFor": f(r, "xGoalsFor"),
            "xGoalsAgainst": f(r, "xGoalsAgainst"),
            "goalsFor": f(r, "goalsFor"),
            "goalsAgainst": f(r, "goalsAgainst"),
            "iceTime": f(r, "iceTime"),
        }

    write("team.json", {
        "season": CFG["nhl_season"],
        "record": {
            "wins": det["wins"],
            "losses": det["losses"],
            "otLosses": det["otLosses"],
            "points": det["points"],
            "pointPctg": det.get("pointPctg"),
            "goalFor": det["goalFor"],
            "goalAgainst": det["goalAgainst"],
            "divisionSequence": det.get("divisionSequence"),
            "wildcardSequence": det.get("wildcardSequence"),
        },
        "situations": situations,
        "leagueRanks": {
            "xGoalsPct_5on5": team_rank("xGoalsPercentage", "5on5"),
            "corsiPct_5on5": team_rank("corsiPercentage", "5on5"),
            "xGoalsFor_5on4": team_rank("xGoalsFor", "5on4"),
        },
    })


# ------------------------------------------------------------- skaters.json
def build_skaters():
    club = json.load((RAW_NHL / "club_stats.json").open())["skaters"]
    mp = read_csv(RAW_MP / "skaters.csv")

    mp_5v5 = {(r["playerId"], r["team"]): r for r in mp if r["situation"] == "5on5"}
    mp_all = {(r["playerId"], r["team"]): r for r in mp if r["situation"] == "all"}

    def pos_group(code):
        return "D" if code == "D" else "F"

    # League percentile pools among regulars, split F/D, 5on5 rates
    pools = {"F": {"xgPct": [], "ixg60": []}, "D": {"xgPct": [], "ixg60": []}}
    for r in mp.copy():
        if r["situation"] != "5on5" or f(r, "icetime") < MIN_SKATER_5V5_SECONDS:
            continue
        g = "D" if r["position"] == "D" else "F"
        pools[g]["xgPct"].append(f(r, "onIce_xGoalsPercentage"))
        pools[g]["ixg60"].append(f(r, "I_F_xGoals") / f(r, "icetime") * 3600)

    skaters = []
    for p in club:
        pid = str(p["playerId"])
        r5 = mp_5v5.get((pid, TEAM))
        ra = mp_all.get((pid, TEAM))
        g = pos_group(p["positionCode"])

        entry = {
            "playerId": p["playerId"],
            "name": full_name(p),
            "position": p["positionCode"],
            "headshot": p.get("headshot"),
            "gamesPlayed": p["gamesPlayed"],
            "goals": p["goals"],
            "assists": p["assists"],
            "points": p["points"],
            "shots": p["shots"],
            "shootingPct": p.get("shootingPctg"),
            "toiPerGame": round(p.get("avgTimeOnIcePerGame", 0), 1),
        }
        if ra:
            ixg_all = f(ra, "I_F_xGoals")
            entry["ixG"] = round(ixg_all, 2)
            entry["goalsAboveExpected"] = round(p["goals"] - ixg_all, 2)
            entry["gameScore"] = f(ra, "gameScore")
        if r5 and f(r5, "icetime") > 0:
            ice5 = f(r5, "icetime")
            xg_pct = f(r5, "onIce_xGoalsPercentage")
            ixg60 = f(r5, "I_F_xGoals") / ice5 * 3600
            entry["fiveOnFive"] = {
                "icetimeMinutes": round(ice5 / 60, 1),
                "onIceXgPct": xg_pct,
                "onIceCorsiPct": f(r5, "onIce_corsiPercentage"),
                "ixgPer60": round(ixg60, 3),
                "pctl_onIceXgPct": percentile(pools[g]["xgPct"], xg_pct),
                "pctl_ixgPer60": percentile(pools[g]["ixg60"], ixg60),
                "qualifiesForPercentiles": ice5 >= MIN_SKATER_5V5_SECONDS,
            }
        skaters.append(entry)

    skaters.sort(key=lambda s: s["points"], reverse=True)
    write("skaters.json", skaters)


# ------------------------------------------------------------- goalies.json
def build_goalies():
    club = json.load((RAW_NHL / "club_stats.json").open())["goalies"]
    mp = read_csv(RAW_MP / "goalies.csv")
    mp_all = {(r["playerId"], r["team"]): r for r in mp if r["situation"] == "all"}

    # League GSAx pool among goalies with meaningful minutes (all situations)
    pool = []
    for r in mp:
        if r["situation"] == "all" and f(r, "icetime") >= MIN_GOALIE_SECONDS:
            pool.append(f(r, "xGoals") - f(r, "goals"))

    goalies = []
    for p in club:
        pid = str(p["playerId"])
        ra = mp_all.get((pid, TEAM))
        entry = {
            "playerId": p["playerId"],
            "name": full_name(p),
            "headshot": p.get("headshot"),
            "gamesPlayed": p["gamesPlayed"],
            "gamesStarted": p.get("gamesStarted"),
            "wins": p["wins"],
            "losses": p["losses"],
            "otLosses": p.get("overtimeLosses"),
            "savePct": p.get("savePercentage"),
            "gaa": p.get("goalsAgainstAverage"),
            "shutouts": p.get("shutouts"),
        }
        if ra:
            gsax = f(ra, "xGoals") - f(ra, "goals")
            entry["gsax"] = round(gsax, 2)
            entry["pctl_gsax"] = percentile(pool, gsax)
            entry["qualifiesForPercentiles"] = f(ra, "icetime") >= MIN_GOALIE_SECONDS
        goalies.append(entry)

    goalies.sort(key=lambda g: g["gamesPlayed"], reverse=True)
    write("goalies.json", goalies)


# --------------------------------------------------------------- lines.json
def build_lines():
    rows = read_csv(RAW_MP / "lines_det.csv")

    def shape(r):
        ice = f(r, "icetime")
        return {
            "name": r["name"],
            "players": r["name"].split("-"),
            "gamesPlayed": int(f(r, "games_played")),
            "icetimeMinutes": round(ice / 60, 1),
            "xGoalsPct": f(r, "xGoalsPercentage"),
            "corsiPct": f(r, "corsiPercentage"),
            "xGoalsFor": f(r, "xGoalsFor"),
            "xGoalsAgainst": f(r, "xGoalsAgainst"),
            "goalsFor": f(r, "goalsFor"),
            "goalsAgainst": f(r, "goalsAgainst"),
        }

    by_ice = lambda r: f(r, "icetime")
    fwd = sorted((r for r in rows if r["position"] == "line"), key=by_ice, reverse=True)
    pairs = sorted((r for r in rows if r["position"] == "pairing"), key=by_ice, reverse=True)

    write("lines.json", {
        "situation": "5on5",
        "forwardLines": [shape(r) for r in fwd[:10]],
        "defensePairs": [shape(r) for r in pairs[:8]],
    })


# ------------------------------------------------------------- results.json
def build_results():
    sched = json.load((RAW_NHL / "schedule.json").open())["games"]
    results = []
    for g in sched:
        if g.get("gameState") not in ("OFF", "FINAL") or g["gameType"] != CFG["game_type"]:
            continue
        home, away = g["homeTeam"], g["awayTeam"]
        is_home = home["abbrev"] == TEAM
        us, them = (home, away) if is_home else (away, home)
        last_period = g.get("gameOutcome", {}).get("lastPeriodType", "REG")
        won = us["score"] > them["score"]
        results.append({
            "gameId": g["id"],
            "date": g["gameDate"],
            "opponent": them["abbrev"],
            "home": is_home,
            "goalsFor": us["score"],
            "goalsAgainst": them["score"],
            "result": "W" if won else ("OTL" if last_period != "REG" else "L"),
            "lastPeriodType": last_period,
        })
    results.sort(key=lambda r: r["date"])
    write("results.json", results)


if __name__ == "__main__":
    build_team()
    build_skaters()
    build_goalies()
    build_lines()
    build_results()
