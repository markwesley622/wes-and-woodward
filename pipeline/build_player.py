#!/usr/bin/env python3
"""Build data/site/players/<playerId>.json for one Red Wing.

Sources (all cached under data/raw/players/<playerId>/):
  NHL API landing + game log      bio, season line, per-game box score
  HockeyStatCards game log        per-game iXG, on-ice xGF/xGA, GF/GA, Luszczyszyn Game Score
  MoneyPuck skaters.csv           individual + on-ice xG, league percentiles (via build_site_data pools)
  Evolving-Hockey exports         GAR / xGAR components + RAPM (research/rasmussen/raw/eh, subscriber export)

The W&W value score is a QBR-style 0-100 rating (positionless: 50 = the average NHL
skater, ~23 points per standard deviation, one decimal), NOT a percentile, of a shrunken
goals-above-replacement composite. Each component is pulled toward zero by a reliability
factor TOI/(TOI+k) whose k reflects how repeatable that component is; the likely range is
the reliability standard error mapped back to percentiles. Two versions: sustainable
(built on xGAR, chances) and results (built on GAR, goals). Headline = sustainable.

Usage: python3 pipeline/build_player.py 8481542 [--fetch]
"""
import csv, json, math, pathlib, re, ssl, sys, time, unicodedata, urllib.request
import certifi

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "pipeline" / "config.json").read_text())
SEASON = CFG["nhl_season"]; EH_SEASON = f"{SEASON[2:4]}-{SEASON[6:8]}"
EH = ROOT / "research" / "rasmussen" / "raw" / "eh"
CTX = ssl.create_default_context(cafile=certifi.where())

Z80 = 1.2816
XK = {"EVO": "xEVO_GAR", "EVD": "xEVD_GAR", "PPO": "xPPO_GAR", "SHD": "xSHD_GAR", "Pens": "Pens_GAR"}
GK = {"EVO": "EVO_GAR", "EVD": "EVD_GAR", "PPO": "PPO_GAR", "SHD": "SHD_GAR", "Pens": "Pens_GAR"}


def _corr(a, b):
    n = len(a); ma = sum(a) / n; mb = sum(b) / n
    sa = math.sqrt(sum((x - ma) ** 2 for x in a)); sb = math.sqrt(sum((y - mb) ** 2 for y in b))
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / (sa * sb) if sa and sb else 0.0


def reliability_constants(min_toi=800):
    """Measure each component's year-over-year repeatability across every season in the
    Evolving-Hockey exports (players with min_toi+ minutes in both years), and turn it into a
    shrink constant k such that TOI/(TOI+k) equals that repeatability at the mean TOI.
    Also returns the weights for blending sustainable (xGAR) and results (GAR): each
    proportional to its own repeatability. Nothing here is guessed."""
    def nxt(season):
        a, b = season.split("-"); return f"{int(a) + 1:02d}-{int(b) + 1:02d}"
    def yoy(fn, cols):
        by = {}
        for r in csv.DictReader((EH / fn).open()):
            if f(r["TOI_All"]) >= min_toi: by.setdefault(r["Player"], {})[r["Season"]] = r
        out = {}
        for c in cols:
            a, b, toi = [], [], []
            for seas in by.values():
                for sn, r in seas.items():
                    t = nxt(sn)
                    if t in seas: a.append(f(r[c])); b.append(f(seas[t][c])); toi.append(f(r["TOI_All"]))
            out[c] = (_corr(a, b), sum(toi) / len(toi))
        return out
    x = yoy("xgar_all_seasons.csv", list(XK.values()) + ["xGAR"])
    g = yoy("gar_all_seasons.csv", ["GAR"])
    K = {comp: round(x[col][1] * (1 - x[col][0]) / max(0.05, x[col][0])) for comp, col in XK.items()}
    rx, rg = x["xGAR"][0], g["GAR"][0]
    return K, {"sustainable": rx / (rx + rg), "results": rg / (rx + rg)}, {comp: round(x[col][0], 3) for comp, col in XK.items()}



def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "wings-data-pipeline/0.1"})
    return json.load(urllib.request.urlopen(req, context=CTX, timeout=30))


def f(v):
    try: return float(v)
    except (TypeError, ValueError): return 0.0


def norm(name):
    """Evolving-Hockey spells names its own way (Debrincat, Van Riemsdyk, no accents)."""
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower())


def eh_row(rows, name, team=None):
    """The player's row in an EH table; prefers the row for `team` when a midseason move split him."""
    hits = [r for r in rows if norm(r["Player"]) == norm(name)]
    if team:
        pref = [r for r in hits if r["Team"] == team]
        if pref: return pref[0]
    return hits[0] if hits else None


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


def qbr(pool, value):
    """QBR-style 0-100 rating, not a percentile: 50 is the average player at the position,
    each standard deviation is about 23 points (logistic on the z-score), one decimal."""
    mean = sum(pool) / len(pool)
    sd = (sum((v - mean) ** 2 for v in pool) / max(1, len(pool) - 1)) ** 0.5
    z = (value - mean) / sd if sd else 0.0
    return round(100 / (1 + math.exp(-z)), 1)


K, BLEND_MEASURED, REPEAT = reliability_constants()
# Editorial weighting (Mark, 9/23): sustainable a bit above results. The measured
# repeatability split (BLEND_MEASURED, ~53/47) is kept for reference in the JSON.
BLEND = {"sustainable": 0.60, "results": 0.40}


def build(pid, fetch=False):
    raw = ROOT / "data" / "raw" / "players" / str(pid); raw.mkdir(parents=True, exist_ok=True)
    if fetch or not (raw / "landing.json").exists():
        (raw / "landing.json").write_text(json.dumps(get(f"https://api-web.nhle.com/v1/player/{pid}/landing"), indent=1))
        (raw / "gamelog_nhl.json").write_text(json.dumps(get(f"https://api-web.nhle.com/v1/player/{pid}/game-log/{SEASON}/2"), indent=1))
    sys.path.insert(0, str(ROOT / "research" / "sandin-pellikka" / "raw" / "hsc")); import fetch_hsc as h
    if fetch or not (raw / "hsc_logs.json").exists():
        (raw / "hsc_logs.json").write_text(json.dumps(h.logs(pid, season=SEASON, gtype=2), indent=1)); time.sleep(4)
    if fetch or not (raw / "hsc_card.json").exists():
        try: (raw / "hsc_card.json").write_text(json.dumps(h.card(pid), indent=1))
        except Exception as e: print("  hsc card failed:", e)
        time.sleep(4)
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
    # positionless: every NHL skater with 20+ GP is in the same pool (Mark, 9/23)
    grp = lambda r: int(r["GP"]) >= 20
    g_by = {norm(r["Player"]) + r["Team"]: r for r in g_rows}
    def g_for(rx): return g_by.get(norm(rx["Player"]) + rx["Team"]) or eh_row(g_rows, rx["Player"], rx["Team"])
    def blended(rx):
        """This season only, no regression: the point estimate is the reliability-weighted blend of
        sustainable (xGAR) and results (GAR) as delivered. Shrinkage sets only the likely range."""
        toi = f(rx["TOI_All"]); rg = g_for(rx)
        vx = sum(f(rx[c]) for c in XK.values()); vg = sum(f(rg[c]) for c in GK.values()) if rg else vx
        rel = composite(rx, XK, toi)[1]
        return BLEND["sustainable"] * vx + BLEND["results"] * vg, vx, vg, rel
    ranked = sorted(((blended(r)[0], r["Player"], r["Team"], int(r["GP"]), r["Position"]) for r in xg_rows if grp(r)), key=lambda t: -t[0])
    x_pool = [t[0] for t in ranked]
    xs_pool = [sum(f(r[c]) for c in XK.values()) for r in xg_rows if grp(r)]
    g_pool = [sum(f(r[c]) for c in GK.values()) for r in g_rows if grp(r)]
    me_x = eh_row(xg_rows, name, "DET"); me_g = g_for(me_x)
    if me_x is None: raise SystemExit(f"{name}: no Evolving-Hockey row for {EH_SEASON}")
    if me_g is None: me_g = me_x
    toi = f(me_x["TOI_All"])
    vb, vx, vg, rel = blended(me_x)
    sd = (sum((v - sum(x_pool) / len(x_pool)) ** 2 for v in x_pool) / max(1, len(x_pool) - 1)) ** 0.5
    se = sd * math.sqrt(max(0.0, 1 - rel))
    score = {
        "value": qbr(x_pool, vb), "low": qbr(x_pool, vb - Z80 * se), "high": qbr(x_pool, vb + Z80 * se),
        "sustainable": qbr(xs_pool, vx), "results": qbr(g_pool, vg), "percentile": percentile(x_pool, vb),
        "goalsBlended": round(vb, 1), "goalsSustainable": round(vx, 1), "goalsResults": round(vg, 1),
        "blend": {k: round(v, 2) for k, v in BLEND.items()}, "blendMeasured": {k: round(v, 2) for k, v in BLEND_MEASURED.items()}, "k": K, "repeatability": REPEAT,
        "reliability": round(rel, 3), "pool": len(x_pool), "group": "skaters", "position": group,
        "components": [
            {"key": c, "label": {"EVO": "Even-strength offense", "EVD": "Even-strength defense", "PPO": "Power play", "SHD": "Penalty kill", "Pens": "Penalties drawn minus taken"}[c],
             "sustainable": f(me_x[XK[c]]), "results": f(me_g[GK[c]]), "shrink": round(shrink(toi, K[c]), 2), "repeat": REPEAT[c],
             "counted": round(BLEND["sustainable"] * f(me_x[XK[c]]) + BLEND["results"] * f(me_g[GK[c]]), 1)} for c in XK],
        "raw": {"xGAR": f(me_x["xGAR"]), "GAR": f(me_g["GAR"]), "WAR": f(me_g["WAR"]), "xWAR": f(me_x["xWAR"]), "toiAll": toi},
        "rapm": {k: f(v) for k, v in rapm.get(name, {}).items() if k not in ("Player", "Season", "Team", "Position")},
        "rank": (next((i + 1 for i, t in enumerate(ranked) if norm(t[1]) == norm(name)), None)),
        "neighbours": (lambda mi: [
            {"rank": i + 1, "name": t[1], "team": t[2], "gp": t[3], "pos": t[4], "value": qbr(x_pool, t[0]), "goals": round(t[0], 1), "isMe": norm(t[1]) == norm(name)}
            for i, t in enumerate(ranked) if abs(i - mi) <= 2] if mi is not None else [])(next((j for j, u in enumerate(ranked) if norm(u[1]) == norm(name)), None)),
        "method": "A 0-100 rating, not a percentile, positionless: 50 is the average NHL skater (20+ GP, forwards and defensemen together) and each standard deviation of value is about 23 points, on a shrunken goals-above-replacement composite. Components: Evolving-Hockey xGAR (sustainable) or GAR (results): EV offense, EV defense, power play, penalty kill, penalties. The likely range uses each component's measured year-over-year repeatability at the player's minutes; the headline itself is not shrunk. Likely range = the reliability standard error (pool SD × sqrt(1 − mean reliability)) at 80%, mapped through the same scale.",
    }

    # ---- isolated impact map: every skater's even-strength RAPM impact this season
    rapm_rows = eh_rows("rapm_ev_rates_all_seasons.csv")
    gp_by = {r["Player"]: int(r["GP"]) for r in xg_rows}
    impact = [{"name": r["Player"], "team": r["Team"], "pos": r["Position"], "off": f(r["xGF/60"]), "def": -f(r["xGA/60"]),
               "toi": round(f(r["TOI"])), "det": r["Team"] == "DET", "me": norm(r["Player"]) == norm(name)}
              for r in rapm_rows if gp_by.get(r["Player"], 0) >= 20]
    if not any(d["me"] for d in impact):  # under 20 GP: still plot him
        rm = eh_row(rapm_rows, name, "DET")
        if rm: impact.append({"name": rm["Player"], "team": rm["Team"], "pos": rm["Position"], "off": f(rm["xGF/60"]), "def": -f(rm["xGA/60"]), "toi": round(f(rm["TOI"])), "det": True, "me": True})

    # ---- career arc: this player's value by season, blended per component
    def season_rows(fn):
        out = {}
        for r in csv.DictReader((EH / fn).open()):
            if norm(r["Player"]) == norm(name) and (r["Season"] not in out or r["Team"] == "DET"): out[r["Season"]] = r
        return out
    cx, cg = season_rows("xgar_all_seasons.csv"), season_rows("gar_all_seasons.csv")
    career = []
    for sn in sorted(cx):
        rx, rg = cx[sn], cg.get(sn)
        comps = {c: round(BLEND["sustainable"] * f(rx[XK[c]]) + BLEND["results"] * f(rg[GK[c]]) if rg else f(rx[XK[c]]), 1) for c in XK}
        career.append({"season": sn, "gp": int(rx["GP"]), "toi": round(f(rx["TOI_All"])), "components": comps,
                       "total": round(sum(comps.values()), 1), "xGAR": f(rx["xGAR"]), "GAR": f(rg["GAR"]) if rg else None})

    # ---- player comps: nearest three same-position skaters on the standardized component profile
    def profile(rx):
        rg = g_for(rx)
        return [BLEND["sustainable"] * f(rx[XK[c]]) + BLEND["results"] * f(rg[GK[c]]) if rg else f(rx[XK[c]]) for c in XK]
    pool_rows = [r for r in xg_rows if grp(r) and (("D" if r["Position"] == "D" else "F") == group)]
    profs = {r["Player"]: profile(r) for r in pool_rows}
    n = len(XK); means = [sum(v[i] for v in profs.values()) / len(profs) for i in range(n)]
    sds = [max(1e-6, (sum((v[i] - means[i]) ** 2 for v in profs.values()) / max(1, len(profs) - 1)) ** 0.5) for i in range(n)]
    mine = profs.get(me_x["Player"]) or profile(me_x)
    def dist(v): return sum(((v[i] - mine[i]) / sds[i]) ** 2 for i in range(n)) ** 0.5
    near = sorted((dist(v), pn) for pn, v in profs.items() if norm(pn) != norm(name))[:3]
    by_name = {r["Player"]: r for r in pool_rows}
    comps = []
    for d, pn in near:
        r = by_name[pn]; v = profs[pn]
        comps.append({"name": pn, "team": r["Team"], "pos": r["Position"], "gp": int(r["GP"]), "distance": round(d, 2),
                      "value": qbr(x_pool, sum(v)), "goals": round(sum(v), 1),
                      "components": {c: round(v[i], 1) for i, c in enumerate(XK)}})
    my_components = {c: round(mine[i], 1) for i, c in enumerate(XK)}

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
    # team context for the game-score tiles (data/site/team_gamescores.json, 20+ GP skaters)
    tg_path = ROOT / "data" / "site" / "team_gamescores.json"
    team_gs = None
    if tg_path.exists():
        tp = json.load(tg_path.open())["players"]
        by_date = {g["date"][5:]: g for g in games}
        def game_ref(mmdd):
            g = by_date.get(mmdd); return {"date": g["date"], "gameId": g["gameId"], "opponent": g["opponent"], "home": g["home"]} if g else {"date": mmdd}
        ordered = sorted(tp, key=lambda r: -r["average"])
        best = max(tp, key=lambda r: r["best"]["value"]); worst = min(tp, key=lambda r: r["worst"]["value"])
        most2 = sorted(tp, key=lambda r: -r["above2"])
        team_gs = {"players": len(tp), "minGames": json.load(tg_path.open())["minGames"],
                   "avgRank": (1 + [r["playerId"] for r in ordered].index(pid)) if any(r["playerId"] == pid for r in ordered) else None,
                   "best": {"name": best["name"], "playerId": best["playerId"], "value": best["best"]["value"], **game_ref(best["best"]["date"])},
                   "worst": {"name": worst["name"], "playerId": worst["playerId"], "value": worst["worst"]["value"], **game_ref(worst["worst"]["date"])},
                   "most2": {"name": most2[0]["name"], "playerId": most2[0]["playerId"], "above2": most2[0]["above2"], "below0": most2[0]["below0"]},
                   "next2": {"name": most2[1]["name"], "above2": most2[1]["above2"]} if len(most2) > 1 else None}
    gs = [g["gameScore"] for g in games if g["gameScore"] is not None]
    scored = [g for g in games if g["gameScore"] is not None] or games
    best = max(scored, key=lambda g: g["gameScore"] if g["gameScore"] is not None else -99); worst = min(scored, key=lambda g: g["gameScore"] if g["gameScore"] is not None else 99)
    fs = land.get("featuredStats", {}).get("regularSeason", {}).get("subSeason", {}) or {}
    out = {
        "playerId": pid, "name": name, "slug": re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()).strip("-"), "season": SEASON, "seasonLabel": f"{SEASON[:4]}-{SEASON[6:]}",
        "bio": {"number": land.get("sweaterNumber"), "position": pos, "shoots": land.get("shootsCatches"), "heightIn": land.get("heightInInches"),
                "weightLb": land.get("weightInPounds"), "birthDate": land.get("birthDate"), "birthplace": f"{land.get('birthCity', {}).get('default', '')}, {land.get('birthCountry', '')}",
                "draft": land.get("draftDetails"), "headshot": land.get("headshot"), "silhouette": f"/players/{pid}.png"},
        "seasonLine": {"gp": fs.get("gamesPlayed"), "goals": fs.get("goals"), "assists": fs.get("assists"), "points": fs.get("points"), "plusMinus": fs.get("plusMinus"),
                       "pim": fs.get("pim"), "shots": fs.get("shots"), "shootingPct": fs.get("shootingPctg"), "toiPerGame": fs.get("avgToi"), "ppPoints": fs.get("powerPlayPoints")},
        "moneypuck": sk, "hsc": hsc_card.get("ratings", {}), "score": score,
        "impact": impact, "career": career, "comps": comps, "myComponents": my_components,
        "gameLog": games,
        "teamGameScore": team_gs,
        "gameScore": {"average": round(sum(gs) / max(1, len(gs)), 2), "games": len(gs), "best": {"date": best["date"], "opponent": best["opponent"], "value": best["gameScore"] or 0},
                      "worst": {"date": worst["date"], "opponent": worst["opponent"], "value": worst["gameScore"] or 0}, "above2": sum(1 for v in gs if v >= 2), "below0": sum(1 for v in gs if v < 0)},
    }
    dest = ROOT / "data" / "site" / "players"; dest.mkdir(parents=True, exist_ok=True)
    (dest / f"{pid}.json").write_text(json.dumps(out, indent=1))
    print(f"site/players/{pid}.json written: {name} value {score['value']} ({score['low']}-{score['high']}) sustainable {score['sustainable']} results {score['results']} rank {score['rank']}/{score['pool']} · K={K} blend={score['blend']}")


if __name__ == "__main__":
    if sys.argv[1] == "--roster":
        roster = json.load((ROOT / "data" / "raw" / "players" / "roster_pages.json").open())
        for r in roster:
            if r["position"] == "G": print("skip goalie:", r["name"]); continue
            try: build(r["playerId"], fetch="--fetch" in sys.argv)
            except SystemExit as e: print("SKIP", e)
    else:
        build(int(sys.argv[1]), fetch="--fetch" in sys.argv)
