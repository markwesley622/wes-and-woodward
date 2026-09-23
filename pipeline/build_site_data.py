#!/usr/bin/env python3
"""Merge raw NHL API + MoneyPuck pulls into site-ready JSON in data/site/.

Outputs:
  team.json    - record, standings context, team-level xG/Corsi (all + 5on5), league ranks
  skaters.json - per-skater card data: counting stats + xG metrics + league percentiles
  goalies.json - per-goalie card data incl. GSAx (goals saved above expected)
  lines.json   - 5on5 forward lines and D pairs by TOI with xG%/CF%
  results.json - completed-game log for rolling/trend charts
  dashboard.json - the homepage glance block: standings line, xG-deserved record and
                   placement, MoneyPuck projection, and a row of league-ranked team tiles
"""
import csv
import datetime as dt
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


# ----------------------------------------------------------- dashboard.json
def ordinal(n):
    if n is None:
        return None
    n = int(n)
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def build_dashboard():
    """Homepage glance block. Three layers, each labelled by what it is:

    standings - the NHL's own table (record, points, place in division / conference /
                league / wild card, streak, last ten).
    deserved  - what the same games look like by expected goals: an xG-Pythagorean win
                share, the points that share produces (loser points at the league rate),
                and where that would place Detroit. All 32 teams are scored the same way.
    projected - MoneyPuck's season simulation (projected points, playoff / division / wild
                card odds, and what the next game is worth). Only meaningful in-season.
    tiles     - team-level rates with a league rank, the numbers the paywalled sites sell.
    """
    standings = json.load((RAW_NHL / "standings.json").open())["standings"]
    by_abbr = {r["teamAbbrev"]["default"]: r for r in standings}
    det = by_abbr[TEAM]
    mp_teams = read_csv(RAW_MP / "teams.csv")
    mp_all = {r["team"]: r for r in mp_teams if r["situation"] == "all"}
    mp_5v5 = {r["team"]: r for r in mp_teams if r["situation"] == "5on5"}
    mp_pp = {r["team"]: r for r in mp_teams if r["situation"] == "5on4"}
    mp_pk = {r["team"]: r for r in mp_teams if r["situation"] == "4on5"}

    gp = det["gamesPlayed"]
    max_gp = max(r["gamesPlayed"] for r in standings)
    state = "offseason" if max_gp >= 82 else ("preseason" if gp == 0 else "in_season")

    div_teams = [r for r in standings if r["divisionAbbrev"] == det["divisionAbbrev"]]
    conf_teams = [r for r in standings if r["conferenceAbbrev"] == det["conferenceAbbrev"]]
    streak = f'{det.get("streakCode", "")}{det.get("streakCount", "")}' if det.get("streakCount") else None

    standings_block = {
        "gamesPlayed": gp,
        "wins": det["wins"], "losses": det["losses"], "otLosses": det["otLosses"],
        "points": det["points"], "pointPctg": det.get("pointPctg"),
        "regulationWins": det.get("regulationWins"),
        "goalFor": det["goalFor"], "goalAgainst": det["goalAgainst"],
        "goalDifferential": det.get("goalDifferential"),
        "streak": streak,
        "lastTen": f'{det["l10Wins"]}-{det["l10Losses"]}-{det["l10OtLosses"]}' if det.get("l10GamesPlayed") else None,
        "division": {"name": det["divisionName"], "place": det["divisionSequence"], "teams": len(div_teams)},
        "conference": {"name": det["conferenceName"], "place": det["conferenceSequence"], "teams": len(conf_teams)},
        "league": {"place": det["leagueSequence"], "teams": len(standings)},
        "wildcard": det.get("wildcardSequence"),
        "clinch": det.get("clinchIndicator"),
        "asOf": det.get("date"),
    }

    # ---- deserved: xG-Pythagorean, every team scored identically
    otl_rate = sum(r["otLosses"] for r in standings) / max(1, sum(r["gamesPlayed"] for r in standings))

    def deserved_for(abbr):
        r = mp_all.get(abbr)
        s = by_abbr.get(abbr)
        if not r or not s or s["gamesPlayed"] == 0:
            return None
        xf, xa = f(r, "xGoalsFor"), f(r, "xGoalsAgainst")
        if xf + xa == 0:
            return None
        w = xf ** 2 / (xf ** 2 + xa ** 2)
        g = s["gamesPlayed"]
        pts = w * 2 * g + otl_rate * g
        return {"team": abbr, "xgWinPct": round(w, 4), "xgPoints": round(pts, 1),
                "xgPointsPer82": round(pts / g * 82, 1), "actualPoints": s["points"],
                "division": s["divisionAbbrev"], "conference": s["conferenceAbbrev"]}

    table = [d for d in (deserved_for(a) for a in by_abbr) if d]
    table.sort(key=lambda d: (-d["xgPoints"], -d["xgWinPct"]))
    mine = next((d for d in table if d["team"] == TEAM), None)
    deserved = None
    if mine:
        def place(pool):
            return next(i + 1 for i, d in enumerate(pool) if d["team"] == TEAM)
        deserved = {
            "xgWinPct": mine["xgWinPct"],
            "xgPoints": mine["xgPoints"],
            "xgPointsPer82": mine["xgPointsPer82"],
            "pointsAboveExpected": round(det["points"] - mine["xgPoints"], 1),
            "divisionPlace": place([d for d in table if d["division"] == mine["division"]]),
            "conferencePlace": place([d for d in table if d["conference"] == mine["conference"]]),
            "leaguePlace": place(table),
            "loserPointRate": round(otl_rate, 4),
            "table": [dict(d, leaguePlace=i + 1) for i, d in enumerate(table)],
            "method": "xG-Pythagorean (exponent 2) on MoneyPuck all-situations xGF/xGA; points = share x 2 x GP plus loser points at the league-wide rate; placement ranks all 32 teams the same way.",
        }

    # ---- projected: MoneyPuck simulation
    projected = {"source": "MoneyPuck season simulation", "available": False}
    sims_path = RAW_MP / "simulations.csv"
    if sims_path.exists():
        sims = [r for r in read_csv(sims_path) if r.get("teamCode") == TEAM]
        rows = {r["scenerio"]: r for r in sims}
        base = rows.get("ALL")
        if base and state == "in_season":
            projected.update({
                "available": True,
                "points": f(base, "points"),
                "playoffOdds": f(base, "madePlayoffs"),
                "divisionOdds": f(base, "wonDivision"),
                "wildcardOdds": f(base, "wildcard1Odds") + f(base, "wildcard2Odds"),
                "cupOdds": f(base, "wonCup"),
                "lotteryOdds": f(base, "draftLottery"),
            })
            # Pre-season projection: MoneyPuck overwrites its file after every result, so the
            # first projection seen for a season is persisted and shown as the static baseline.
            snap_path = RAW_MP / "preseason_projection.json"
            snaps = json.load(snap_path.open()) if snap_path.exists() else {}
            if CFG["nhl_season"] not in snaps:
                snaps[CFG["nhl_season"]] = {"points": f(base, "points"), "playoffOdds": f(base, "madePlayoffs"),
                                            "capturedAt": dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes")}
                snap_path.write_text(json.dumps(snaps, indent=1))
            projected["preseasonPoints"] = snaps[CFG["nhl_season"]]["points"]
            projected["preseasonPlayoffOdds"] = snaps[CFG["nhl_season"]]["playoffOdds"]
            if "WINREG" in rows and "LOSSREG" in rows:
                projected["nextGame"] = {
                    k: {"points": round(f(rows[k], "points") - f(base, "points"), 1),
                        "playoffOdds": round(f(rows[k], "madePlayoffs") - f(base, "madePlayoffs"), 4)}
                    for k in ("WINREG", "WINOT", "LOSSOT", "LOSSREG") if k in rows
                }
        elif base:
            projected["finalPoints"] = f(base, "points")

    # ---- next game
    next_game = None
    for name in ("schedule.json", "schedule_next.json"):
        path = RAW_NHL / name
        if not path.exists():
            continue
        for g in json.load(path.open())["games"]:
            if g.get("gameType") != CFG["game_type"] or g.get("gameState") not in ("FUT", "PRE"):
                continue
            is_home = g["homeTeam"]["abbrev"] == TEAM
            opp = g["awayTeam"] if is_home else g["homeTeam"]
            next_game = {"date": g["gameDate"], "opponent": opp["abbrev"], "home": is_home,
                         "season": str(g.get("season", ""))}
            break
        if next_game:
            break

    # ---- tiles: rates with a league rank (rank 1 = best)
    def per60(r, col):
        ice = f(r, "iceTime")
        return f(r, col) / ice * 3600 if ice else 0.0

    def ranked(pool, value_fn, higher_is_better=True):
        vals = {abbr: value_fn(r) for abbr, r in pool.items()}
        order = sorted(vals, key=lambda a: vals[a], reverse=higher_is_better)
        return vals[TEAM], order.index(TEAM) + 1, len(order)

    tiles = []

    v, rk, n = ranked(mp_5v5, lambda r: f(r, "xGoalsPercentage"))
    tiles.append({"key": "xg_share_5v5", "label": "5v5 expected-goal share", "value": round(v * 100, 1),
                  "unit": "%", "rank": rk, "of": n, "note": "MoneyPuck, five-on-five"})

    def adj_share(r):
        xf, xa = f(r, "flurryScoreVenueAdjustedxGoalsFor"), f(r, "flurryScoreVenueAdjustedxGoalsAgainst")
        return xf / (xf + xa) if xf + xa else 0.0
    v, rk, n = ranked(mp_5v5, adj_share)
    tiles.append({"key": "xg_share_5v5_adj", "label": "5v5 xG share, score & venue adjusted", "value": round(v * 100, 1),
                  "unit": "%", "rank": rk, "of": n, "note": "flurry, score and venue adjusted"})

    v, rk, n = ranked(mp_all, lambda r: f(r, "goalsFor") - f(r, "xGoalsFor"))
    tiles.append({"key": "finishing", "label": "Finishing, goals above expected", "value": round(v, 1),
                  "unit": "", "rank": rk, "of": n, "signed": True, "note": "all situations"})

    v, rk, n = ranked(mp_all, lambda r: f(r, "xGoalsAgainst") - f(r, "goalsAgainst"))
    tiles.append({"key": "gsax", "label": "Goaltending, goals saved above expected", "value": round(v, 1),
                  "unit": "", "rank": rk, "of": n, "signed": True, "note": "team GSAx, all situations"})

    v, rk, n = ranked(mp_pp, lambda r: per60(r, "xGoalsFor"))
    tiles.append({"key": "pp_xgf60", "label": "Power play xG per 60", "value": round(v, 2),
                  "unit": "", "rank": rk, "of": n, "note": "5v4, expected goals generated"})

    v, rk, n = ranked(mp_pk, lambda r: per60(r, "xGoalsAgainst"), higher_is_better=False)
    tiles.append({"key": "pk_xga60", "label": "Penalty kill xG against per 60", "value": round(v, 2),
                  "unit": "", "rank": rk, "of": n, "note": "4v5, lower is better"})

    for t in tiles:
        t["rankLabel"] = f'{ordinal(t["rank"])} of {t["of"]}'

    # ---- radar: seven dimensions of winning, as league percentiles, Detroit vs the average of
    # the top three teams in the standings right now (rank-based, 0 = worst team, 100 = best)
    def pct_rank(values, higher_is_better=True):
        teams = list(values)
        out = {}
        for a in teams:
            below = sum(1 for b in teams if b != a and ((values[b] < values[a]) if higher_is_better else (values[b] > values[a])))
            out[a] = round(100 * below / max(1, len(teams) - 1), 1)
        return out

    dims = [
        ("finishing", "Finishing", "goals above expected, all situations", {a: f(r, "goalsFor") - f(r, "xGoalsFor") for a, r in mp_all.items()}, True, "{:+.1f}"),
        ("goaltending", "Goaltending", "goals saved above expected, all situations", {a: f(r, "xGoalsAgainst") - f(r, "goalsAgainst") for a, r in mp_all.items()}, True, "{:+.1f}"),
        ("attacking", "Attacking", "5v5 expected goals for per 60", {a: per60(r, "xGoalsFor") for a, r in mp_5v5.items()}, True, "{:.2f}"),
        ("defending", "Defending", "5v5 expected goals against per 60 (lower is better)", {a: per60(r, "xGoalsAgainst") for a, r in mp_5v5.items()}, False, "{:.2f}"),
        ("possession", "Possession", "5v5 shot-attempt share", {a: f(r, "corsiPercentage") * 100 for a, r in mp_5v5.items()}, True, "{:.1f}%"),
        ("powerplay", "Power play", "5v4 expected goals for per 60", {a: per60(r, "xGoalsFor") for a, r in mp_pp.items()}, True, "{:.2f}"),
        ("penaltykill", "Penalty kill", "4v5 expected goals against per 60 (lower is better)", {a: per60(r, "xGoalsAgainst") for a, r in mp_pk.items()}, False, "{:.2f}"),
    ]
    top3 = [r["teamAbbrev"]["default"] for r in sorted(standings, key=lambda r: (-r["points"], -r.get("regulationWins", 0)))[:3]]
    radar = {"top3": top3, "dimensions": []}
    for key, label, note, values, hib, fmt in dims:
        pcts = pct_rank(values, hib)
        radar["dimensions"].append({
            "key": key, "label": label, "note": note,
            "det": pcts.get(TEAM), "detRaw": fmt.format(values.get(TEAM, 0)),
            "top3": round(sum(pcts.get(t, 0) for t in top3) / max(1, len(top3)), 1),
            "top3Raw": fmt.format(sum(values.get(t, 0) for t in top3) / max(1, len(top3))),
        })

    write("dashboard.json", {
        "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes"),
        "season": CFG["nhl_season"],
        "seasonLabel": f'{CFG["nhl_season"][:4]}-{CFG["nhl_season"][6:]}',
        "seasonState": state,
        "standings": standings_block,
        "deserved": deserved,
        "projected": projected,
        "nextGame": next_game,
        "tiles": tiles,
        "radar": radar,
    })


if __name__ == "__main__":
    build_team()
    build_skaters()
    build_goalies()
    build_lines()
    build_results()
    build_dashboard()
