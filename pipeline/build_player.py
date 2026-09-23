#!/usr/bin/env python3
"""Build data/site/players/<playerId>.json for one Red Wing.

Sources (all cached under data/raw/players/<playerId>/):
  NHL API landing + game log      bio, season line, per-game box score
  HockeyStatCards game log        per-game iXG, on-ice xGF/xGA, GF/GA, Luszczyszyn Game Score
  MoneyPuck skaters.csv           individual + on-ice xG, league percentiles (via build_site_data pools)
  Evolving-Hockey exports         GAR / xGAR components + RAPM (research/rasmussen/raw/eh, subscriber export)

The W&W value score (0-100) is a league percentile, within position, of a shrunken
goals-above-replacement composite. Each component is pulled toward zero by a reliability
factor TOI/(TOI+k) whose k reflects how repeatable that component is; the likely range is
the reliability standard error mapped back to percentiles. Two versions: sustainable
(built on xGAR, chances) and results (built on GAR, goals). Headline = sustainable.

Usage: python3 pipeline/build_player.py 8481542 [--fetch]
"""
import csv, json, math, pathlib, ssl, sys, urllib.request
import certifi

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "pipeline" / "config.json").read_text())
SEASON = CFG["nhl_season"]; EH_SEASON = f"{SEASON[2:4]}-{SEASON[6:8]}"
EH = ROOT / "research" / "rasmussen" / "raw" / "eh"
CTX = ssl.create_default_context(cafile=certifi.where())

# reliability constants (minutes of all-situations TOI at which a component is half-trusted)
K = {"EVO": 500, "EVD": 1000, "PPO": 700, "SHD": 700, "Pens": 300}
Z80 = 1.2816


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "wings-data-pipeline/0.1"})
    return json.load(urllib.request.urlopen(req, context=CTX, timeout=30))


def f(v):
    try: return float(v)
    except (TypeError, ValueError): return 0.0


def shrink(toi, k):
    return toi / (toi + k) if toi > 0 else 0.0


def composite(row, keys, toi):
    """Shrunken sum of GAR-style components (goals)."""
    total, wsum = 0.0, 0.0
    for comp, col in keys.items():
        s = shrink(toi, K[comp]); total += s * f(row[col]); wsum += s
    return total, (wsum / len(keys) if keys else 0.0)


def percentile(pool, value):
    return round(100 * sum(1 for v in pool if v < value) / max(1, len(pool)), 1)


def build(pid, fetch=False):
    raw = ROOT / "data" / "raw" / "players" / str(pid); raw.mkdir(parents=True, exist_ok=True)
    if fetch or not (raw / "landing.json").exists():
        (raw / "landing.json").write_text(json.dumps(get(f"https://api-web.nhle.com/v1/player/{pid}/landing"), indent=1))
        (raw / "gamelog_nhl.json").write_text(json.dumps(get(f"https://api-web.nhle.com/v1/player/{pid}/game-log/{SEASON}/2"), indent=1))
    if fetch or not (raw / "hsc_logs.json").exists():
        sys.path.insert(0, str(ROOT / "research" / "sandin-pellikka" / "raw" / "hsc")); import fetch_hsc as h
        (raw / "hsc_logs.json").write_text(json.dumps(h.logs(pid), indent=1))
        (raw / "hsc_card.json").write_text(json.dumps(h.card(pid), indent=1))
    land = json.load((raw / "landing.json").open())
    nhl_log = json.load((raw / "gamelog_nhl.json").open())["gameLog"]
    hsc_log = json.load((raw / "hsc_logs.json").open())
    hsc_card = json.load((raw / "hsc_card.json").open()) if (raw / "hsc_card.json").exists() else {}
    name = f"{land['firstName']['default']} {land['lastName']['default']}"
    pos = land["position"]; group = "D" if pos == "D" else "F"

    # ---- Evolving-Hockey pools (same season, same position group, 20+ GP)
    def eh_rows(fn):
        return [r for r in csv.DictReader((EH / fn).open()) if r["Season"] == EH_SEASON]
    xg_rows, g_rows = eh_rows("xgar_all_seasons.csv"), eh_rows("gar_all_seasons.csv")
    rapm = {r["Player"]: r for r in eh_rows("rapm_ev_rates_all_seasons.csv")}
    grp = lambda r: ("D" if r["Position"] == "D" else "F") == group and int(r["GP"]) >= 20
    XK = {"EVO": "xEVO_GAR", "EVD": "xEVD_GAR", "PPO": "xPPO_GAR", "SHD": "xSHD_GAR", "Pens": "Pens_GAR"}
    GK = {"EVO": "EVO_GAR", "EVD": "EVD_GAR", "PPO": "PPO_GAR", "SHD": "SHD_GAR", "Pens": "Pens_GAR"}
    x_pool = [composite(r, XK, f(r["TOI_All"]))[0] for r in xg_rows if grp(r)]
    g_pool = [composite(r, GK, f(r["TOI_All"]))[0] for r in g_rows if grp(r)]
    me_x = next(r for r in xg_rows if r["Player"] == name); me_g = next(r for r in g_rows if r["Player"] == name)
    toi = f(me_x["TOI_All"])
    vx, rel = composite(me_x, XK, toi); vg, _ = composite(me_g, GK, toi)
    sd = (sum((v - sum(x_pool) / len(x_pool)) ** 2 for v in x_pool) / max(1, len(x_pool) - 1)) ** 0.5
    se = sd * math.sqrt(max(0.0, 1 - rel))
    score = {
        "value": percentile(x_pool, vx), "low": percentile(x_pool, vx - Z80 * se), "high": percentile(x_pool, vx + Z80 * se),
        "results": percentile(g_pool, vg), "goalsSustainable": round(vx, 1), "goalsResults": round(vg, 1),
        "reliability": round(rel, 3), "pool": len(x_pool), "group": group,
        "components": [
            {"key": c, "label": {"EVO": "Even-strength offense", "EVD": "Even-strength defense", "PPO": "Power play", "SHD": "Penalty kill", "Pens": "Penalties drawn minus taken"}[c],
             "sustainable": f(me_x[XK[c]]), "results": f(me_g[GK[c]]), "shrink": round(shrink(toi, K[c]), 2),
             "counted": round(shrink(toi, K[c]) * f(me_x[XK[c]]), 1)} for c in XK],
        "raw": {"xGAR": f(me_x["xGAR"]), "GAR": f(me_g["GAR"]), "WAR": f(me_g["WAR"]), "xWAR": f(me_x["xWAR"]), "toiAll": toi},
        "rapm": {k: f(v) for k, v in rapm.get(name, {}).items() if k not in ("Player", "Season", "Team", "Position")},
        "method": "League percentile within position (20+ GP) of a shrunken goals-above-replacement composite. Components: Evolving-Hockey xGAR (sustainable) or GAR (results): EV offense, EV defense, power play, penalty kill, penalties. Each is multiplied by TOI/(TOI+k) with k = 500/1000/700/700/300 minutes, so the least repeatable components count least until the minutes are there. Likely range = the reliability standard error (pool SD × sqrt(1 − mean reliability)) at 80%, mapped back to percentiles.",
    }

    # ---- MoneyPuck (from the site's skaters.json, already percentiled)
    sk = next((p for p in json.load((ROOT / "data" / "site" / "skaters.json").open()) if p["playerId"] == pid), {})

    # ---- game log: NHL box score joined to HockeyStatCards by date (HSC dates are MM-DD)
    hsc_by_date = {}
    for g in hsc_log:
        mmdd = g["Date"]; hsc_by_date[mmdd] = g
    games = []
    for g in sorted(nhl_log, key=lambda g: g["gameDate"]):
        mmdd = g["gameDate"][5:]; hx = hsc_by_date.get(mmdd, {})
        m, s = g["toi"].split(":")
        games.append({
            "gameId": g["gameId"], "date": g["gameDate"], "opponent": g["opponentAbbrev"], "home": g["homeRoadFlag"] == "H",
            "goals": g["goals"], "assists": g["assists"], "points": g["points"], "plusMinus": g["plusMinus"], "shots": g["shots"],
            "pim": g["pim"], "toi": round(int(m) + int(s) / 60, 1),
            "ixg": f(hx.get("iXG")) if hx else None, "xgf": f(hx.get("xGF")) if hx else None, "xga": f(hx.get("xGA")) if hx else None,
            "gf": f(hx.get("GF")) if hx else None, "ga": f(hx.get("GA")) if hx else None, "blocks": f(hx.get("Blk")) if hx else None,
            "gameScore": f(hx.get("Game Score")) if hx else None,
        })
    gs = [g["gameScore"] for g in games if g["gameScore"] is not None]
    best = max(games, key=lambda g: g["gameScore"] or -99); worst = min(games, key=lambda g: g["gameScore"] if g["gameScore"] is not None else 99)
    fs = land.get("featuredStats", {}).get("regularSeason", {}).get("subSeason", {})
    out = {
        "playerId": pid, "name": name, "slug": name.lower().replace(" ", "-"), "season": SEASON, "seasonLabel": f"{SEASON[:4]}-{SEASON[6:]}",
        "bio": {"number": land.get("sweaterNumber"), "position": pos, "shoots": land.get("shootsCatches"), "heightIn": land.get("heightInInches"),
                "weightLb": land.get("weightInPounds"), "birthDate": land.get("birthDate"), "birthplace": f"{land.get('birthCity', {}).get('default', '')}, {land.get('birthCountry', '')}",
                "draft": land.get("draftDetails"), "headshot": land.get("headshot"), "silhouette": f"/players/{pid}.png"},
        "seasonLine": {"gp": fs.get("gamesPlayed"), "goals": fs.get("goals"), "assists": fs.get("assists"), "points": fs.get("points"), "plusMinus": fs.get("plusMinus"),
                       "pim": fs.get("pim"), "shots": fs.get("shots"), "shootingPct": fs.get("shootingPctg"), "toiPerGame": fs.get("avgToi"), "ppPoints": fs.get("powerPlayPoints")},
        "moneypuck": sk, "hsc": hsc_card.get("ratings", {}), "score": score,
        "gameLog": games,
        "gameScore": {"average": round(sum(gs) / max(1, len(gs)), 2), "games": len(gs), "best": {"date": best["date"], "opponent": best["opponent"], "value": best["gameScore"]},
                      "worst": {"date": worst["date"], "opponent": worst["opponent"], "value": worst["gameScore"]}, "above2": sum(1 for v in gs if v >= 2), "below0": sum(1 for v in gs if v < 0)},
    }
    dest = ROOT / "data" / "site" / "players"; dest.mkdir(parents=True, exist_ok=True)
    (dest / f"{pid}.json").write_text(json.dumps(out, indent=1))
    print(f"site/players/{pid}.json written: {name} value {score['value']} ({score['low']}-{score['high']}) results {score['results']} · {len(games)} games, GS avg {out['gameScore']['average']}")


if __name__ == "__main__":
    build(int(sys.argv[1]), fetch="--fetch" in sys.argv)
