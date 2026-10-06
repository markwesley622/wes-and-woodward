#!/usr/bin/env python3
"""Wes & Woodward prospect system. Builds data/site/prospects.json (ranked pipeline) and
data/site/prospects/<nhlId>.json (one block per prospect, read by the player page templates).

Decided with Mark 2026-10-06. Four layers, every one computed WITHIN POSITION (F / D / G):

  1. League strength    published Network NHLe coefficient (hockeystats.com, Patrick Bacon), cited.
  2. Performance        skaters: points per game percentile among same-league, same-position,
                        same-birth-year skaters. Goalies: save percentage percentile among same-league,
                        same-birth-year goalies. (EliteProspects league tables; exact birth-year cohorts
                        by set difference of EP's cumulative age buckets.)
  3. Ceiling            cohort match: drafted players 2008-2019 at the same position and age with a
                        similar production feature (skaters: NHLe points per game; goalies: save
                        percentage above the league-season average, in a league of similar strength)
                        and, while pedigree still counts, a similar draft slot. Outcome = each one's peak
                        NHL season as a percentile among NHL regulars at the position (skaters: points per
                        game; goalies: save percentage); busts count as 0. Expected = mean, ceiling = 75th
                        percentile. Tier words match the NHL page value score.
  4. Trajectory         change in the production feature between the last two full seasons.

  Draft pedigree (same cohort, by pick band) enters with DIMINISHING RETURNS (Mark, 10/6): it is
  strongest in the draft year and neutral by draft+2. w = 0.5 in the draft year (and for a pre-draft
  anchor season), 0.25 at draft+1, 0 from draft+2. The headline expected peak blends the pick-band
  prior and the cohort mean by w, and the comparable search weights draft slot by 2w (so at draft+2
  comparables are chosen on production alone).

Prospect = rookie-eligible AND inside draft+4 where the draft year is year one (2021 -> through
2025-26). NHL-roster players who meet that rule (Brandsegg-Nygård, Johansson) are ranked too; their one
page keeps the NHL template while they are up, and that page is canonical.

Inputs: data/raw/ep/{player,draft,league,system}/*.json (EliteProspects, pulled by ep_worker.js via
ep_receiver.py), data/raw/nhl_seasons/{skaters,goalies}_*.json (NHL API), data/raw/nhle/hockeystats_nhle.json.
"""
import datetime as dt, json, math, pathlib, re, ssl, statistics, sys, time, unicodedata, urllib.parse, urllib.request
import certifi

ROOT = pathlib.Path(__file__).resolve().parents[1]
EP = ROOT / "data" / "raw" / "ep"
CFG = json.loads((ROOT / "pipeline" / "config.json").read_text())
SEASON = CFG["nhl_season"]                      # 20262027
YR = int(SEASON[:4])                            # 2026
CUR = f"{YR}-{YR + 1}"; PREV = f"{YR - 1}-{YR}"; PREV2 = f"{YR - 2}-{YR - 1}"
COHORT_YEARS = range(2008, 2020)
K_NEIGHBOURS = 50
CTX = ssl.create_default_context(cafile=certifi.where())
NHLE = json.loads((ROOT / "data" / "raw" / "nhle" / "hockeystats_nhle.json").read_text())
sys.path.insert(0, str(ROOT / "pipeline"))
from build_player import prospect_status, rookie_eligible, nhl_roster_ids, slug_of   # noqa  (same rule as the page builder)

# EP league name -> hockeystats table name. Anything not here (and not matched by normalisation)
# carries no coefficient and is skipped as a primary line.
ALIASES = {"hockeyallsvenskan": "Allsvenskan", "nl": "NLA", "u20 nationell": "Superelit", "j20 superelit": "Superelit", "j20 nationell": "Superelit",
           "u20 sm-sarja": "U20 SM-Liiga", "jr. a sm-liiga": "U20 SM-Liiga", "czechia": "Czech", "extraliga": "Czech", "czechia2": "Czech2", "ntdp": "USDP",
           "usdp": "USDP", "u18 sm-sarja": "U18 SM-Sarja", "j18 allsvenskan": "J18 Allsvenskan", "j18 elit": "J18-Elit", "u18 regional": "J18-Elit",
           "wjc-20": "WJC-20", "wjc-18": "WJC-18", "slovakia": "Slovakia", "ohl": "OHL", "whl": "WHL", "qmjhl": "QMJHL", "ushl": "USHL", "ncaa": "NCAA",
           "ahl": "AHL", "nhl": "NHL", "khl": "KHL", "vhl": "VHL", "mhl": "MHL", "shl": "SHL", "liiga": "Liiga", "del": "DEL", "del2": "DEL2", "echl": "ECHL",
           "bchl": "BCHL", "ajhl": "AJHL", "nahl": "NAHL", "ushs-prep": "USHS-Prep", "mestis": "Mestis", "sl": "NLB", "norway": "Norway", "denmark": "Denmark",
           "czech u20": "Czech-U20", "u20 elit": "U20-Elit", "ice hockey league": "EBEL", "icehl": "EBEL", "ebel": "EBEL", "belarus": "Belarus", "usports": "Usports",
           "u sports": "Usports", "usphl premier": "USPHL-Premier", "ojhl": "OJHL", "sjhl": "SJHL", "mjhl": "MJHL", "cchl": "CCHL", "gojhl": "GOJHL", "u18 aaa": "16U-AAA",
           "18u aaa": "16U-AAA", "16u aaa": "16U-AAA", "russia u18": "Russia-U18", "russia u17": "Russia-U17", "czech u18": "Czech U18", "slovakia u20": "Slovakia-U20",
           "slovakia u18": "Slovakia-U18", "u16 sm-sarja": "U16 SM-Sarja", "u18 elit": "J18-Elit", "u18 nationell": "J18 Allsvenskan",
           "u18 region": "J18-Elit", "ushs-mn": "USHS-MN", "nmhl": "NMHL", "dnl": "DNL", "division 1": "Division-1", "hockeyettan": "Division-1", "latvia": None,
           "elitserien": "SHL", "sm-liiga": "Liiga", "u20 sm-liiga": "U20 SM-Liiga", "czechia u20": "Czech-U20", "czechia u18": "Czech U18", "cis": "Usports",
           "ligue magnus": "France", "alpshl": "ALPSHL", "division 2": "Division-2", "czechia u16": "Czech U16", "j20 elit": "J20-Elit",
           "sphl": None, "cjhl": None, "opjhl": "OJHL", "nla": "NLA", "t1ehl 18u": "USPHL-18U", "t1ehl 16u": "HPHL-16U", "umhsehl": "USHS-MN",
           "international": None, "international-jr": None, "wc": None, "olympics": None, "wjac-19": None, "hlinka gretzky cup": None, "whc-17": None, "wjc-20 d1a": None}
TABLE_NORM = {re.sub(r"[^a-z0-9]", "", k.lower()): k for k in NHLE["coefficients"]}
TIERS = [(88, "elite"), (73, "top-line"), (50, "above average"), (27, "below average"), (0, "replacement level")]
BANDS = [(1, 5), (6, 15), (16, 32), (33, 64), (65, 120), (121, 300)]


def coef_for(league):
    if not league: return None, None
    key = league.lower().strip()
    if key in ALIASES:
        name = ALIASES[key]
        return (name, NHLE["coefficients"].get(name)) if name else (None, None)
    n = re.sub(r"[^a-z0-9]", "", key)
    if n in TABLE_NORM: return TABLE_NORM[n], NHLE["coefficients"][TABLE_NORM[n]]
    return None, None


def norm_name(s):
    return re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower())


def age_at(season, dob):
    """Hockey age: whole years on Sept 15 of the season's first year."""
    y = int(season[:4])
    return (dt.date(y, 9, 15) - dt.date.fromisoformat(dob)).days // 365.25


def pos_group(p):
    pos = (p.get("position") or "").upper()
    if pos == "G": return "G"
    if pos == "D": return "D"
    dp = [x.upper() for x in (p.get("detailedPosition") or [])]
    return "D" if dp and all(x == "D" for x in dp) else "F"


def svpct(reg):
    svs, ga = reg.get("SVS") or 0, reg.get("GA") or 0
    return svs / (svs + ga) if (svs + ga) > 0 else None


def tier(v):
    if v is None: return "did not stick"
    return next(t for cut, t in TIERS if v >= cut)


def pedigree_weight(n, group="F"):
    """Diminishing returns on draft pedigree: 0.5 in the draft year (n <= 0), falling linearly to 0 at the
    horizon. Skaters: neutral by draft+2 (Mark, 10/6). Goalies: neutral by draft+4, because the cohort
    says the slot keeps predicting for goalies long after it stops for skaters (2008-2019 drafted goalies:
    picks 33-64 became NHL regulars 61% of the time, picks 121+ 16%; goalies are drafted and develop later,
    so draft+2 for a goalie is where draft+0 is for a skater)."""
    if n is None: return 0.0
    horizon = 4 if group == "G" else 2
    return 0.5 * max(0.0, 1 - max(0, n) / horizon)


def pct(vals, v):
    if not vals: return None
    lo = 0; hi = len(vals)
    while lo < hi:
        mid = (lo + hi) // 2
        if vals[mid] < v: lo = mid + 1
        else: hi = mid
    return round(100 * lo / len(vals), 1)


# ---------------------------------------------------------------- NHL outcome pools (per season, per position)
def nhl_pools():
    pools = {}
    for f in sorted((ROOT / "data" / "raw" / "nhl_seasons").glob("skaters_*.json")):
        rows = json.load(f.open()).get("data", [])
        sid = f.stem.split("_")[1]; season = f"{sid[:4]}-{sid[4:]}"
        mx = max((r.get("gamesPlayed") or 0) for r in rows) if rows else 82
        thr = max(20, int(round(0.5 * mx)))
        for g in ("F", "D"):
            vals = sorted((r["points"] / r["gamesPlayed"]) for r in rows if (r.get("gamesPlayed") or 0) >= thr and (("D" if r.get("positionCode") == "D" else "F") == g))
            pools[(season, g)] = {"vals": vals, "threshold": thr, "n": len(vals)}
    for f in sorted((ROOT / "data" / "raw" / "nhl_seasons").glob("goalies_*.json")):
        rows = json.load(f.open()).get("data", [])
        sid = f.stem.split("_")[1]; season = f"{sid[:4]}-{sid[4:]}"
        mx = max((r.get("gamesPlayed") or 0) for r in rows) if rows else 82
        thr = max(10, int(round(0.25 * mx)))                   # a quarter of the schedule: tandem goalies count
        vals = sorted(r["savePct"] for r in rows if (r.get("gamesPlayed") or 0) >= thr and r.get("savePct") is not None)
        pools[(season, "G")] = {"vals": vals, "threshold": thr, "n": len(vals)}
    return pools


def nhl_outcome(rec, group, pools):
    """Peak NHL season as a percentile within position (skaters: points per game, seasons with at least
    half the games; goalies: save percentage, at least a quarter), from the player's own EP NHL season
    lines. peak None = never a qualifying season."""
    peak = None; gp_total = 0; seasons = 0; best = None
    for s in rec["seasons"]:
        if s.get("league") != "NHL" or not s.get("team") or not s.get("reg"): continue
        gp = s["reg"].get("GP") or 0; gp_total += gp
        pool = pools.get((s["season"], group))
        if not pool or gp < pool["threshold"]: continue
        v = svpct(s["reg"]) if group == "G" else (s["reg"].get("PTS") or 0) / gp
        if v is None: continue
        seasons += 1
        p = pct(pool["vals"], v)
        if peak is None or p > peak: peak, best = p, s["season"]
    return {"peak": peak, "peakSeason": best, "nhlGp": gp_total, "qualifyingSeasons": seasons}


# ---------------------------------------------------------------- league tables
def load_league_tables():
    """(league, season, pos, ageBucket) -> {playerId: row}. A traded player has one row per team: summed."""
    tabs = {}
    for f in (EP / "league").glob("*.json"):
        d = json.load(f.open())
        lg, se, pos, age, _ = f.stem.rsplit("_", 4)
        t = tabs.setdefault((lg, se, pos, age), {})
        for r in d.get("rows", []):
            if not r.get("playerId") or not r.get("reg"): continue
            cur = t.get(r["playerId"])
            keys = ("GP", "SVS", "GA") if pos == "G" else ("GP", "G", "A", "PTS")
            if cur is None: t[r["playerId"]] = {"playerId": r["playerId"], "name": r["name"], "reg": {k: (r["reg"].get(k) or 0) for k in keys}}
            else:
                for k in keys: cur["reg"][k] += (r["reg"].get(k) or 0)
    return tabs


def league_goalie_avg(tabs, slug, season, min_gp=10):
    """League-season save percentage of goalies with min_gp+ games (all-ages goalie table), save-weighted."""
    t = tabs.get((slug, season, "G", "all"))
    if not t: return None
    svs = sum(r["reg"]["SVS"] for r in t.values() if r["reg"]["GP"] >= min_gp); ga = sum(r["reg"]["GA"] for r in t.values() if r["reg"]["GP"] >= min_gp)
    n = sum(1 for r in t.values() if r["reg"]["GP"] >= min_gp)
    return {"svp": svs / (svs + ga), "n": n} if (svs + ga) > 0 and n >= 4 else None


# ---------------------------------------------------------------- season features
def primary_line(rec, season, group, tabs=None):
    """The season's main line. Skaters: NHLe blends every coefficient-bearing line weighted by games
    (a junior split between the SHL and the J20 isn't judged on 12 scoreless SHL games); "league" names
    the line with the most games. Goalies: the single line with the most games, feature = save
    percentage minus that league-season's average (needs the all-ages goalie table)."""
    best = None; wsum = 0.0; gsum = 0; lines = []
    for s in rec["seasons"]:
        if s.get("season") != season or not s.get("team") or not s.get("reg"): continue
        name, c = coef_for(s.get("league"))
        if c is None: continue
        gp = s["reg"].get("GP") or 0
        if gp <= 0: continue
        slug = (s.get("leaguePath") or "").split("/")[-1]
        if group == "G":
            sv = svpct(s["reg"])
            if sv is None: continue
            if best is None or gp > best["gp"]:
                best = {"league": s["league"], "leagueSlug": slug, "table": name, "coef": c, "team": s["team"], "gp": gp, "lineGp": gp, "svp": round(sv, 4),
                        "gaa": s["reg"].get("GAA"), "w": s["reg"].get("W"), "l": s["reg"].get("L"), "so": s["reg"].get("SO")}
            continue
        pts = s["reg"].get("PTS") or 0
        wsum += pts * c; gsum += gp; lines.append(s["league"])
        if best is None or gp > best["gp"]:
            best = {"league": s["league"], "leagueSlug": slug, "table": name, "coef": c, "team": s["team"], "gp": gp,
                    "g": s["reg"].get("G") or 0, "a": s["reg"].get("A") or 0, "pts": pts}
    if not best: return None
    if group == "G":
        avg = league_goalie_avg(tabs or {}, best["leagueSlug"], season)
        if not avg: return None                                   # no league average on file: not a usable season
        best["leagueSvp"] = round(avg["svp"], 4); best["leagueN"] = avg["n"]; best["svDelta"] = round(best["svp"] - avg["svp"], 4)
        best["feature"] = best["svDelta"]
    else:
        best["pgp"] = round(best["pts"] / best["gp"], 3); best["lineGp"] = best["gp"]; best["gp"] = gsum
        best["nhle"] = round(wsum / gsum, 3); best["nhle82"] = round(best["nhle"] * 82, 1); best["lines"] = lines
        best["feature"] = best["nhle"]
    return best


def all_lines(rec, season):
    out = []
    for s in rec["seasons"]:
        if s.get("season") != season or not s.get("team") or not s.get("reg"): continue
        name, c = coef_for(s.get("league"))
        r = s["reg"]
        out.append({"league": s["league"], "team": s["team"], "gp": r.get("GP"), "g": r.get("G"), "a": r.get("A"), "pts": r.get("PTS"), "pm": r.get("PM"), "pim": r.get("PIM"),
                    "gaa": r.get("GAA"), "svp": r.get("SVP"), "w": r.get("W"), "l": r.get("L"), "so": r.get("SO"), "coef": c, "status": s.get("status")})
    return sorted(out, key=lambda l: -(l["gp"] or 0))


def seasons_since_draft(rec, draft_year):
    """Where he played: every season from the draft year forward (draft year = year one). Undrafted: the
    last three seasons. Newest first."""
    seasons = sorted({s["season"] for s in rec["seasons"] if s.get("season") and s.get("team") and s.get("reg")}, reverse=True)
    if draft_year: seasons = [s for s in seasons if int(s[:4]) >= draft_year]
    else: seasons = seasons[:3]
    return [{"season": s, "lines": all_lines(rec, s)} for s in seasons]


# ---------------------------------------------------------------- cohort
def load_cohort(pools, tabs):
    picks = {}
    for y in COHORT_YEARS:
        f = EP / "draft" / f"{y}.json"
        if not f.exists(): continue
        for p in json.load(f.open())["picks"]:
            if p.get("playerId"): picks[p["playerId"]] = p
    rows = []
    for pid, p in picks.items():
        f = EP / "player" / f"{pid}.json"
        if not f.exists(): continue
        rec = json.load(f.open()); pl = rec["player"]
        if not pl or not pl.get("dateOfBirth"): continue
        g = pos_group(pl)
        out = nhl_outcome(rec, g, pools)
        for s in sorted({s["season"] for s in rec["seasons"] if s.get("season")}):
            if int(s[:4]) > p["year"] + 4 or int(s[:4]) < p["year"] - 3: continue     # draft-3 .. draft+4 seasons only
            line = primary_line(rec, s, g, tabs)
            if not line or line["lineGp"] < 10 or line["league"] == "NHL": continue
            rows.append({"pid": pid, "name": pl["name"], "group": g, "age": int(age_at(s, pl["dateOfBirth"])), "season": s, "league": line["league"], "coef": line["coef"],
                         "feature": line["feature"], "gp": line["lineGp"], "pick": p["overall"], "year": p["year"], "peak": out["peak"], "nhlGp": out["nhlGp"], "regular": out["peak"] is not None})
    # goalies: one season of save percentage is noise; the feature is the two-season average when the
    # season before is on file (same treatment as the current prospects in main())
    by = {}
    for r in rows:
        if r["group"] == "G": by.setdefault(r["pid"], {})[r["season"]] = r
    for seasons in by.values():
        for s, r in seasons.items():
            prev = seasons.get(f"{int(s[:4]) - 1}-{int(s[:4])}")
            r["feature1"] = r["feature"]
            if prev: r["feature"] = round((r["feature1"] + prev.get("feature1", prev["feature"])) / 2, 4)
    return rows


def summarise(nbrs):
    peaks = [n["peak"] if n["peak"] is not None else 0.0 for n in nbrs]
    if not peaks: return None
    ps = sorted(peaks)
    q = lambda f: ps[min(len(ps) - 1, int(f * len(ps)))]
    return {"n": len(nbrs), "expected": round(sum(peaks) / len(peaks), 1), "median": round(q(0.5), 1), "p75": round(q(0.75), 1), "p90": round(q(0.9), 1),
            "pRegular": round(sum(1 for n in nbrs if n["regular"]) / len(nbrs), 2), "pTopLine": round(sum(1 for n in nbrs if (n["peak"] or 0) >= 73) / len(nbrs), 2),
            "pAboveAvg": round(sum(1 for n in nbrs if (n["peak"] or 0) >= 50) / len(nbrs), 2), "pElite": round(sum(1 for n in nbrs if (n["peak"] or 0) >= 88) / len(nbrs), 2)}


def ceiling(cohort, group, age, feature, coef, pick, pick_w):
    """Nearest K cohort rows at the same position and age. Distance = |Δfeature| in cohort SDs, plus
    pick_w x |Δ log pick| in SDs (pick_w = 2 x pedigree weight, so 1.0 in the draft year and 0 from
    draft+2), plus for goalies 0.5 x |Δ log league coefficient| so comparables come from leagues of
    similar strength (save percentage above league average means more in a stronger league)."""
    pool = [r for r in cohort if r["group"] == group and r["age"] == age]
    if len(pool) < 20: return None
    sd_f = statistics.pstdev([r["feature"] for r in pool]) or 1.0
    lp = [math.log(r["pick"]) for r in pool]; sd_p = statistics.pstdev(lp) or 1.0
    lc = [math.log(r["coef"]) for r in pool]; sd_c = statistics.pstdev(lc) or 1.0
    lpick = math.log(pick) if pick else statistics.median(lp)
    for r in pool:
        r["_d"] = abs(r["feature"] - feature) / sd_f + pick_w * abs(math.log(r["pick"]) - lpick) / sd_p + (0.5 * abs(math.log(r["coef"]) - math.log(coef)) / sd_c if group == "G" else 0.0)
    pool.sort(key=lambda r: r["_d"])
    nbrs = pool[:K_NEIGHBOURS]
    s = summarise(nbrs)
    t = tier(s["p75"])
    # share of the comparables who reached the ceiling tier or better, so "elite" never reads as the forecast
    s.update({"poolN": len(pool), "group": group, "age": age, "pickWeight": pick_w, "tier": t,
              "pCeiling": {"elite": s["pElite"], "top-line": s["pTopLine"], "above average": s["pAboveAvg"], "below average": round(sum(1 for n in nbrs if (n["peak"] or 0) >= 27) / len(nbrs), 2), "replacement level": s["pRegular"], "did not stick": 1.0}[t],
              "featureBand": [round(min(n["feature"] for n in nbrs), 3), round(max(n["feature"] for n in nbrs), 3)],
              "examples": [{"name": n["name"], "year": n["year"], "pick": n["pick"], "league": n["league"], "feature": n["feature"], "peak": n["peak"], "tier": tier(n["peak"]), "nhlGp": n["nhlGp"]} for n in nbrs[:8]]})
    return s


def pedigree(cohort, group, pick):
    if not pick: return None
    lo, hi = next(b for b in BANDS if b[0] <= pick <= b[1])
    seen = {}
    for r in cohort:
        if r["group"] == group and lo <= r["pick"] <= hi: seen[r["pid"]] = r
    s = summarise(list(seen.values()))
    if s: s.update({"band": f"{lo}-{hi}", "group": group})
    return s


# ---------------------------------------------------------------- age-relative performance
def performance(tabs, pid, slug, season, group, min_gp):
    buckets = sorted({k[3] for k in tabs if k[0] == slug and k[1] == season and k[2] == group and k[3] != "all"}, key=lambda a: int(a[1:]))
    mine = None
    for a in buckets:
        if pid in tabs[(slug, season, group, a)]: mine = a; break
    if mine is None: return None
    i = buckets.index(mine)
    rows = dict(tabs[(slug, season, group, mine)])
    if i > 0:
        for k in tabs[(slug, season, group, buckets[i - 1])]: rows.pop(k, None)
    me = rows.get(pid)
    if not me or not me.get("reg"): return None
    val = (lambda r: svpct(r["reg"])) if group == "G" else (lambda r: (r["reg"]["PTS"] or 0) / r["reg"]["GP"])
    pool = [val(r) for r in rows.values() if r.get("reg") and (r["reg"].get("GP") or 0) >= min_gp and val(r) is not None]
    gp = me["reg"].get("GP") or 0
    if gp < min_gp or len(pool) < 6: return {"league": slug, "season": season, "ageBucket": mine, "cohortN": len(pool), "gp": gp, "percentile": None, "note": "sample too small"}
    v = val(me)
    allpool = [val(r) for a in buckets for r in tabs[(slug, season, group, a)].values() if r.get("reg") and (r["reg"].get("GP") or 0) >= min_gp and val(r) is not None]
    return {"league": slug, "season": season, "ageBucket": mine, "cohortN": len(pool), "gp": gp, "value": round(v, 4), "percentile": pct(sorted(pool), v),
            "percentileAllAges": pct(sorted(allpool), v), "allAgesN": len(allpool)}


# ---------------------------------------------------------------- EP -> NHL id map
def nhl_search(name):
    u = "https://search.d3.nhle.com/api/v1/search/player?culture=en-us&limit=20&q=" + urllib.parse.quote(name)
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "wes-and-woodward/0.1"}), context=CTX, timeout=30))


def landing(nhl_id, fetch=True):
    d = ROOT / "data" / "raw" / "players" / str(nhl_id); d.mkdir(parents=True, exist_ok=True)
    f = d / "landing.json"
    if not f.exists() and fetch:
        f.write_text(json.dumps(json.load(urllib.request.urlopen(urllib.request.Request(f"https://api-web.nhle.com/v1/player/{nhl_id}/landing", headers={"User-Agent": "wes-and-woodward/0.1"}), context=CTX, timeout=30)), indent=1))
        time.sleep(0.5)
    return json.load(f.open()) if f.exists() else None


def id_map(system):
    f = EP / "idmap.json"
    m = json.load(f.open()) if f.exists() else {}
    for p in system:
        if p["id"] in m: continue
        rec = json.load((EP / "player" / f"{p['id']}.json").open()); pl = rec["player"]
        dob = pl.get("dateOfBirth"); found = None
        try:
            cands = nhl_search(pl["name"]) + (nhl_search(pl["alternativeName"]) if pl.get("alternativeName") else [])
            if "-" in pl["name"]: cands += nhl_search(pl["name"].replace("-", " "))     # NHL spells Dower-Nilsson without the hyphen
            if not cands: cands = [c for c in nhl_search(pl["name"].split()[-1]) if c.get("teamAbbrev") == "DET"]
        except Exception as e:
            print("  search failed", pl["name"], e); continue
        cands = sorted(cands, key=lambda c: (c.get("teamAbbrev") != "DET", norm_name(c.get("name")) != norm_name(pl["name"])))
        for c in cands[:6]:
            if norm_name(c.get("name")) not in (norm_name(pl["name"]), norm_name(pl.get("alternativeName") or "")) and c.get("teamAbbrev") != "DET": continue
            try: land = landing(c["playerId"])
            except Exception: continue
            if land and land.get("birthDate") == dob: found = int(c["playerId"]); break
        m[p["id"]] = found
        print(f"  idmap {pl['name']}: {found}")
        time.sleep(0.4)
    f.write_text(json.dumps(m, indent=1))
    return m


def roster_prospects(draft_by_ep, idm):
    """NHL-roster players who are prospects under the rule but absent from EP's system list (it only
    lists players off the NHL roster): matched to their EP draft record by name + draft year."""
    out = []
    by_name = {}
    for epid, p in draft_by_ep.items(): by_name.setdefault((norm_name(p["name"]), p["year"]), epid)
    for pid in sorted(nhl_roster_ids()):
        land = landing(pid, fetch=False)
        if not land or not prospect_status(land)["prospect"]: continue
        dr = land.get("draftDetails") or {}
        epid = by_name.get((norm_name(f"{land['firstName']['default']} {land['lastName']['default']}"), dr.get("year")))
        if not epid or not (EP / "player" / f"{epid}.json").exists():
            print(f"  roster prospect without an EP page: {land['firstName']['default']} {land['lastName']['default']} (pull /player/{epid or '?'})"); continue
        idm[epid] = pid
        rec = json.load((EP / "player" / f"{epid}.json").open())
        out.append({"id": epid, "name": rec["player"]["name"], "pos": "/".join(rec["player"].get("detailedPosition") or []), "lines": []})
    return out


# ---------------------------------------------------------------- main
def main():
    pools = nhl_pools()
    tabs = load_league_tables()
    print("NHL pools:", len(pools), "· league tables:", len(tabs))
    cohort = load_cohort(pools, tabs)
    print("cohort rows:", len(cohort), "players:", len({r['pid'] for r in cohort}), "goalie rows:", sum(1 for r in cohort if r["group"] == "G"))
    system = json.load((EP / "system" / "DET.json").open())
    players = [p for p in system["skaters"] + system["goalies"] if (EP / "player" / f"{p['id']}.json").exists()]
    idm = id_map(players)
    draft_by_ep = {}
    for f in (EP / "draft").glob("*.json"):
        for p in json.load(f.open())["picks"]:
            if p.get("playerId"): draft_by_ep[p["playerId"]] = p
    have = {p["id"] for p in players}
    players += [p for p in roster_prospects(draft_by_ep, idm) if p["id"] not in have]
    (EP / "idmap.json").write_text(json.dumps(idm, indent=1))
    roster = nhl_roster_ids()

    prospects, excluded = [], []
    for p in players:
        rec = json.load((EP / "player" / f"{p['id']}.json").open()); pl = rec["player"]
        nhl_id = idm.get(p["id"]); land = landing(nhl_id, fetch=False) if nhl_id else None
        g = pos_group(pl); dob = pl.get("dateOfBirth"); dr = draft_by_ep.get(p["id"])
        if land:
            st = prospect_status(land)
        else:   # no NHL id found: fall back to EP draft year + age window, flagged
            yr_d = dr["year"] if dr else None
            st = {"prospect": (yr_d is not None and YR <= yr_d + 4) or (yr_d is None and age_at(CUR, dob) < 23), "rookieEligible": None, "inWindow": True, "window": f"draft+{YR - yr_d}" if yr_d else "undrafted", "draftYear": yr_d, "note": "no NHL id; eligibility unverified"}
        slug = slug_of(f"{land['firstName']['default']} {land['lastName']['default']}") if land else slug_of(pl["name"])
        base = {"epId": p["id"], "nhlId": nhl_id, "name": pl["name"], "slug": slug,
                "group": g, "position": "/".join(pl.get("detailedPosition") or []) or pl.get("position"), "birthDate": dob, "age": int(age_at(CUR, dob)) if dob else None,
                "height": (pl.get("height") or {}).get("imperial"), "weight": (pl.get("weight") or {}).get("imperial"), "shoots": pl.get("shoots"), "catches": pl.get("catches"), "contract": pl.get("contract"),
                "rights": (pl.get("nhlRights") or {}).get("rights"), "draft": ({"year": dr["year"], "overall": dr["overall"], "round": dr["round"]} if dr else None),
                "status": {**st, "onNhlRoster": bool(nhl_id and nhl_id in roster)}, "scouting": re.sub(r"<[^>]+>", "", pl.get("profileDescriptionAsHTML") or "").strip() or None,
                "currentLines": all_lines(rec, CUR), "lastLines": all_lines(rec, PREV), "seasons": seasons_since_draft(rec, dr["year"] if dr else None)}
        if not st["prospect"]:
            excluded.append({**base, "reason": ("past draft+4" if st.get("draftYear") else "past the undrafted age window") if st.get("rookieEligible") else "lost rookie eligibility"}); continue
        cur = primary_line(rec, CUR, g, tabs); prev = primary_line(rec, PREV, g, tabs); prev2 = primary_line(rec, PREV2, g, tabs)
        anchor = cur if (cur and cur["lineGp"] >= 10) else prev
        anchor_season = CUR if anchor is cur else PREV
        n_since = (int(anchor_season[:4]) - dr["year"]) if (dr and anchor) else None
        w = pedigree_weight(n_since, g) if dr else 0.0
        if anchor and g == "G":   # two-season save-percentage feature, matching the cohort treatment
            before = prev2 if anchor is prev else prev
            anchor["feature1"] = anchor["feature"]
            if before: anchor["feature"] = round((anchor["feature"] + before["feature"]) / 2, 4); anchor["featureSeasons"] = 2
            else: anchor["featureSeasons"] = 1
        perf_prev = performance(tabs, p["id"], prev["leagueSlug"], PREV, g, 10) if prev else None
        perf_cur = performance(tabs, p["id"], cur["leagueSlug"], CUR, g, 3) if cur else None
        ceil = ceiling(cohort, g, int(age_at(anchor_season, dob)), anchor["feature"], anchor["coef"], dr["overall"] if dr else None, 2 * w) if anchor else None
        ped = pedigree(cohort, g, dr["overall"] if dr else None)
        traj = None
        if prev and prev2:
            traj = {"from": {"season": PREV2, "league": prev2["league"], "feature": prev2["feature"], "gp": prev2["lineGp"]}, "to": {"season": PREV, "league": prev["league"], "feature": prev["feature"], "gp": prev["lineGp"]}, "delta": round(prev["feature"] - prev2["feature"], 4)}
        nhl_sample = None
        if land:
            rows = [t for t in land.get("seasonTotals", []) if t.get("leagueAbbrev") == "NHL" and t.get("gameTypeId") == 2]
            if rows:
                nhl_sample = {"gp": sum(t.get("gamesPlayed") or 0 for t in rows), "pts": sum(t.get("points") or 0 for t in rows), "seasons": sorted({t["season"] for t in rows}),
                              "thisSeason": next(({"gp": t.get("gamesPlayed"), "pts": t.get("points"), "toi": t.get("avgToi"), "savePct": t.get("savePctg")} for t in rows if t.get("season") == int(SEASON)), None)}
        blend = None; score = None
        if ceil:
            score = ceil["expected"]
            if ped and w > 0:
                score = round(w * ped["expected"] + (1 - w) * ceil["expected"], 1)
            blend = {"w": w, "sinceDraft": n_since, "pedigreeExpected": ped["expected"] if ped else None, "cohortExpected": ceil["expected"], "expected": score, "tier": tier(score) if ceil["pRegular"] > 0 else "did not stick"}
        prospects.append({**base, "anchor": {"season": anchor_season, **anchor} if anchor else None, "league": ({"name": anchor["league"], "table": anchor["table"], "coef": anchor["coef"], "source": NHLE["source"]} if anchor else None),
                          "performance": {"last": perf_prev, "current": perf_cur}, "ceiling": ceil, "pedigree": ped, "blend": blend, "trajectory": traj, "nhlSample": nhl_sample,
                          "availability": {"gp": anchor["lineGp"], "season": anchor_season} if anchor else None, "rank": None, "score": score})
    prospects.sort(key=lambda x: (-(x["score"] if x["score"] is not None else -1), -((x["ceiling"] or {}).get("p75") or 0)))
    for i, x in enumerate(prospects): x["rank"] = i + 1

    out = {"season": SEASON, "built": dt.date.today().isoformat(), "cohort": {"years": [COHORT_YEARS.start, COHORT_YEARS.stop - 1], "rows": len(cohort), "players": len({r['pid'] for r in cohort}), "k": K_NEIGHBOURS},
           "nhle": {"source": NHLE["source"], "retrieved": NHLE["retrieved"]}, "prospects": prospects, "excluded": excluded,
           "method": {"prospect": "Rookie-eligible and inside draft+4 (draft year = year one). Undrafted: under 23 on Sept 15. NHL-roster players who qualify are ranked; their page keeps the NHL template while they are up.",
                      "league": "Network NHLe points coefficient per league, hockeystats.com (Patrick Bacon). Skaters: applied to points per game. Goalies: used to keep comparables in leagues of similar strength.",
                      "performance": "Skaters: points per game percentile among skaters of the same position born the same year, same league and season. Goalies: save percentage percentile among goalies born the same year, same league and season. (EliteProspects tables.) Full season needs 10+ GP; the current season 3+.",
                      "ceiling": f"Nearest {K_NEIGHBOURS} drafted players (2008-2019 classes) at the same position and age. Skaters matched on NHLe points per game; goalies on save percentage above the league-season average and league strength. Draft slot enters with weight 2w (w below). Outcome = each one's peak NHL season as a percentile within position (skaters: points per game over seasons with at least half the games; goalies: save percentage over seasons with at least a quarter); busts count as 0. Cohort expected = mean, ceiling = 75th percentile. Tiers: elite 88+, top-line 73+, above average 50+, below average 27+.",
                      "pedigree": "Diminishing returns: w = 0.5 in the draft year (or a pre-draft anchor season), 0.25 at draft+1, 0 from draft+2. Expected peak = w x pick-band prior + (1 - w) x cohort mean.",
                      "trajectory": "Change in the production feature between the two most recent full seasons (skaters NHLe points per game; goalies save percentage above league average).",
                      "ranking": "By expected peak (the pedigree-blended cohort mean), then by the cohort 75th percentile."}}
    site = ROOT / "data" / "site"; (site / "prospects").mkdir(parents=True, exist_ok=True)
    (site / "prospects.json").write_text(json.dumps(out, indent=1))
    for x in prospects + excluded:
        if x.get("nhlId"): (site / "prospects" / f"{x['nhlId']}.json").write_text(json.dumps(x, indent=1))
    print(f"prospects: {len(prospects)} ranked, {len(excluded)} excluded")
    for x in prospects:
        c = x["ceiling"] or {}; pf = (x["performance"]["last"] or {}); b = x["blend"] or {}
        feat = x["anchor"]["feature"] if x["anchor"] else "-"
        print(f"{x['rank']:>2} {x['name']:<26} {x['group']} age {x['age']} {x['anchor']['league'] if x['anchor'] else '-':<12} feat {feat:<8} perf {pf.get('percentile')} cohort {c.get('expected')} ped {b.get('pedigreeExpected')} w {b.get('w')} -> {x['score']} p75 {c.get('p75')} pReg {c.get('pRegular')} {c.get('tier')}")


if __name__ == "__main__":
    main()
