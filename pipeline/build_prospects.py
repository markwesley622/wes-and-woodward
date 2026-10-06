#!/usr/bin/env python3
"""Wes & Woodward prospect system. Builds data/site/prospects.json (ranked pipeline) and
data/site/prospects/<nhlId>.json (one block per prospect, read by the prospect page template).

Decided with Mark 2026-10-06. Four layers, every one computed WITHIN POSITION (F / D; goalies are
listed but not modelled):

  1. League strength    published Network NHLe coefficient (hockeystats.com, Patrick Bacon), cited.
  2. Performance        points per game percentile among same-league, same-position, SAME-AGE skaters
                        (EliteProspects league tables, exact age by set difference of EP's cumulative
                        age buckets).
  3. Ceiling            cohort match: drafted skaters 2008-2019 at the same position and the same age
                        with a similar NHLe and a similar draft slot; where their NHL peak landed as a
                        points-per-game percentile among NHL regulars at that position. Reported as the
                        expected peak (busts count as 0), the median, the 75th percentile (the ceiling)
                        and P(NHL regular). Tier words match the NHL page value score.
  4. Trajectory         change in NHLe points per game between the last two full seasons.
  plus draft pedigree (same cohort by pick band), deployment (TOI / PP from EP game logs where the
  league reports them), availability (GP), the NHL sample where one exists, and the games every
  number rests on.

Prospect = rookie-eligible AND inside draft+4 where the draft year is year one (2021 -> through
2025-26). The template a player gets follows his CURRENT roster status (build_player.py).

Inputs: data/raw/ep/{player,draft,league,system}/*.json (EliteProspects, pulled by ep_worker.js via
ep_receiver.py), data/raw/nhl_seasons/skaters_*.json (NHL API), data/raw/nhle/hockeystats_nhle.json.
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
           "slovakia u18": "Slovakia-U18", "u16 sm-sarja": "U16 SM-Sarja", "u20 elit": "U20-Elit", "u18 elit": "J18-Elit", "u18 nationell": "J18 Allsvenskan",
           "u18 region": "J18-Elit", "ushs-mn": "USHS-MN", "nmhl": "NMHL", "dnl": "DNL", "division 1": "Division-1", "hockeyettan": "Division-1", "latvia": None,
           "elitserien": "SHL", "sm-liiga": "Liiga", "u20 sm-liiga": "U20 SM-Liiga", "czechia u20": "Czech-U20", "czechia u18": "Czech U18", "cis": "Usports",
           "ligue magnus": "France", "alpshl": "ALPSHL", "division 2": "Division-2", "czechia u16": "Czech U16", "j20 elit": "J20-Elit", "u20 elit": "U20-Elit",
           "sphl": None, "cjhl": None, "opjhl": "OJHL", "nla": "NLA", "u18 aaa": "16U-AAA", "t1ehl 18u": "USPHL-18U", "t1ehl 16u": "HPHL-16U", "umhsehl": "USHS-MN",
           "international": None, "international-jr": None, "wc": None, "olympics": None, "wjac-19": None, "hlinka gretzky cup": None, "whc-17": None, "wjc-20 d1a": None}
TABLE_NORM = {re.sub(r"[^a-z0-9]", "", k.lower()): k for k in NHLE["coefficients"]}


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
    return pools


def pct(vals, v):
    if not vals: return None
    lo = 0; hi = len(vals)
    while lo < hi:
        mid = (lo + hi) // 2
        if vals[mid] < v: lo = mid + 1
        else: hi = mid
    return round(100 * lo / len(vals), 1)


def nhl_outcome(rec, group, pools):
    """Peak NHL points-per-game percentile within position over qualifying seasons (GP at or above half
    the season), from the player's own EP NHL season lines. None = never a qualifying season."""
    peak = None; gp_total = 0; seasons = 0; best = None
    for s in rec["seasons"]:
        if s.get("league") != "NHL" or not s.get("team") or not s.get("reg"): continue
        gp = s["reg"].get("GP") or 0; gp_total += gp
        pool = pools.get((s["season"], group))
        if not pool or gp < pool["threshold"]: continue
        seasons += 1
        p = pct(pool["vals"], (s["reg"].get("PTS") or 0) / gp)
        if peak is None or p > peak: peak, best = p, s["season"]
    return {"peak": peak, "peakSeason": best, "nhlGp": gp_total, "qualifyingSeasons": seasons}


# ---------------------------------------------------------------- season features
def primary_line(rec, season):
    """The season's main line: most GP among leagues with a coefficient; team-less EP pace rows and
    tournaments are ignored. Returns None when nothing usable (GP < 10)."""
    best = None; wsum = 0.0; gsum = 0; lines = []
    for s in rec["seasons"]:
        if s.get("season") != season or not s.get("team") or not s.get("reg"): continue
        name, c = coef_for(s.get("league"))
        if c is None: continue
        gp = s["reg"].get("GP") or 0
        if gp <= 0: continue
        pts = s["reg"].get("PTS") or 0
        wsum += pts * c; gsum += gp; lines.append(s["league"])
        if best is None or gp > best["gp"]:
            best = {"league": s["league"], "leagueSlug": (s.get("leaguePath") or "").split("/")[-1], "table": name, "coef": c, "team": s["team"], "gp": gp,
                    "g": s["reg"].get("G") or 0, "a": s["reg"].get("A") or 0, "pts": pts}
    if best:
        # NHLe for the season blends every coefficient-bearing line, weighted by games, so a junior split
        # between the SHL and the J20 isn't judged on his 12 scoreless SHL games alone. "league" names the
        # line with the most games; "gp" is the season's games across those lines.
        best["pgp"] = round(best["pts"] / best["gp"], 3); best["lineGp"] = best["gp"]; best["gp"] = gsum
        best["nhle"] = round(wsum / gsum, 3); best["nhle82"] = round(best["nhle"] * 82, 1); best["lines"] = lines
    return best


def all_lines(rec, season):
    out = []
    for s in rec["seasons"]:
        if s.get("season") != season or not s.get("team") or not s.get("reg"): continue
        name, c = coef_for(s.get("league"))
        out.append({"league": s["league"], "team": s["team"], "gp": s["reg"].get("GP"), "g": s["reg"].get("G"), "a": s["reg"].get("A"), "pts": s["reg"].get("PTS"),
                    "pm": s["reg"].get("PM"), "pim": s["reg"].get("PIM"), "coef": c, "status": s.get("status")})
    return sorted(out, key=lambda l: -(l["gp"] or 0))


# ---------------------------------------------------------------- cohort
def load_cohort(pools):
    picks = {}
    for y in COHORT_YEARS:
        f = EP / "draft" / f"{y}.json"
        if not f.exists(): continue
        for p in json.load(f.open())["picks"]:
            if p.get("playerId") and p.get("pos") != "G": picks[p["playerId"]] = p
    rows = []
    for pid, p in picks.items():
        f = EP / "player" / f"{pid}.json"
        if not f.exists(): continue
        rec = json.load(f.open()); pl = rec["player"]
        if not pl or not pl.get("dateOfBirth"): continue
        g = pos_group(pl)
        if g == "G": continue
        out = nhl_outcome(rec, g, pools)
        for s in sorted({s["season"] for s in rec["seasons"] if s.get("season")}):
            if int(s[:4]) > p["year"] + 4 or int(s[:4]) < p["year"] - 3: continue     # draft-3 .. draft+4 seasons only
            line = primary_line(rec, s)
            if not line or line["gp"] < 10 or line["league"] == "NHL": continue
            rows.append({"pid": pid, "name": pl["name"], "group": g, "age": int(age_at(s, pl["dateOfBirth"])), "season": s, "league": line["league"], "nhle": line["nhle"], "gp": line["gp"],
                         "pick": p["overall"], "year": p["year"], "peak": out["peak"], "nhlGp": out["nhlGp"], "regular": out["peak"] is not None})
    return rows


TIERS = [(88, "elite"), (73, "top-line"), (50, "above average"), (27, "below average"), (0, "replacement level")]


def tier(v):
    if v is None: return "did not stick"
    return next(t for cut, t in TIERS if v >= cut)


def summarise(nbrs):
    peaks = [n["peak"] if n["peak"] is not None else 0.0 for n in nbrs]
    if not peaks: return None
    ps = sorted(peaks)
    q = lambda f: ps[min(len(ps) - 1, int(f * len(ps)))]
    return {"n": len(nbrs), "expected": round(sum(peaks) / len(peaks), 1), "median": round(q(0.5), 1), "p75": round(q(0.75), 1), "p90": round(q(0.9), 1),
            "pRegular": round(sum(1 for n in nbrs if n["regular"]) / len(nbrs), 2), "pTopLine": round(sum(1 for n in nbrs if (n["peak"] or 0) >= 73) / len(nbrs), 2),
            "pAboveAvg": round(sum(1 for n in nbrs if (n["peak"] or 0) >= 50) / len(nbrs), 2)}


def ceiling(cohort, group, age, nhle, pick):
    pool = [r for r in cohort if r["group"] == group and r["age"] == age]
    if len(pool) < 20: return None
    sd_n = statistics.pstdev([r["nhle"] for r in pool]) or 1.0
    lp = [math.log(r["pick"]) for r in pool]; sd_p = statistics.pstdev(lp) or 1.0
    lpick = math.log(pick) if pick else statistics.median(lp)
    for r in pool:
        r["_d"] = abs(r["nhle"] - nhle) / sd_n + 0.5 * abs(math.log(r["pick"]) - lpick) / sd_p
    pool.sort(key=lambda r: r["_d"])
    nbrs = pool[:K_NEIGHBOURS]
    s = summarise(nbrs)
    s.update({"poolN": len(pool), "group": group, "age": age, "tier": tier(s["p75"]), "expectedTier": tier(s["expected"]) if s["pRegular"] > 0 else "did not stick",
              "nhleBand": [round(min(n["nhle"] for n in nbrs), 2), round(max(n["nhle"] for n in nbrs), 2)],
              "examples": [{"name": n["name"], "year": n["year"], "pick": n["pick"], "league": n["league"], "nhle": n["nhle"], "peak": n["peak"], "tier": tier(n["peak"]), "nhlGp": n["nhlGp"]} for n in nbrs[:8]]})
    return s


def pedigree(cohort, group, pick):
    if not pick: return None
    bands = [(1, 5), (6, 15), (16, 32), (33, 64), (65, 120), (121, 300)]
    lo, hi = next(b for b in bands if b[0] <= pick <= b[1])
    seen = {}
    for r in cohort:
        if r["group"] == group and lo <= r["pick"] <= hi: seen[r["pid"]] = r
    rows = list(seen.values())
    s = summarise(rows)
    if s: s.update({"band": f"{lo}-{hi}", "group": group})
    return s


# ---------------------------------------------------------------- league tables (age-relative percentile)
def load_league_tables():
    tabs = {}
    for f in (EP / "league").glob("*.json"):
        d = json.load(f.open())
        lg, se, pos, age, _ = f.stem.rsplit("_", 4)
        t = tabs.setdefault((lg, se, pos, age), {})
        for r in d.get("rows", []):     # a traded player has one row per team: sum them
            if not r.get("playerId") or not r.get("reg"): continue
            cur = t.get(r["playerId"])
            if cur is None: t[r["playerId"]] = {"playerId": r["playerId"], "name": r["name"], "reg": {k: (r["reg"].get(k) or 0) for k in ("GP", "G", "A", "PTS")}}
            else:
                for k in ("GP", "G", "A", "PTS"): cur["reg"][k] += (r["reg"].get(k) or 0)
    return tabs


def performance(tabs, pid, slug, season, group, min_gp):
    buckets = sorted({k[3] for k in tabs if k[0] == slug and k[1] == season and k[2] == group}, key=lambda a: int(a[1:]))
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
    pool = [(r["reg"]["PTS"] or 0) / r["reg"]["GP"] for r in rows.values() if r.get("reg") and (r["reg"].get("GP") or 0) >= min_gp]
    gp = me["reg"].get("GP") or 0
    if gp < min_gp or len(pool) < 8: return {"league": slug, "season": season, "ageBucket": mine, "cohortN": len(pool), "gp": gp, "percentile": None, "note": "sample too small"}
    v = (me["reg"].get("PTS") or 0) / gp
    allpool = [(r["reg"]["PTS"] or 0) / r["reg"]["GP"] for a in buckets for r in tabs[(slug, season, group, a)].values() if r.get("reg") and (r["reg"].get("GP") or 0) >= min_gp]
    return {"league": slug, "season": season, "ageBucket": mine, "exactAge": int(mine[1:]) - 1, "cohortN": len(pool), "gp": gp, "pgp": round(v, 3), "percentile": pct(sorted(pool), v),
            "percentileAllAges": pct(sorted(set(allpool)) and sorted(allpool), v), "allAgesN": len(set(allpool)) and len(allpool)}


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
            if not cands and "-" in pl["name"]: cands = nhl_search(pl["name"].replace("-", " "))
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


# ---------------------------------------------------------------- deployment from EP game logs
def deployment(rec):
    games = (rec.get("gameLog") or {}).get("games") or []
    tois = []; ppg = 0; g = 0
    for x in games:
        t = x.get("TOI") or x.get("toi") or (x.get("stats") or {}).get("TOI")
        if isinstance(t, str) and ":" in t:
            mm, ss = t.split(":")[:2]; tois.append(int(mm) + int(ss) / 60)
        ppg += (x.get("PPG") or (x.get("stats") or {}).get("PPG") or 0) or 0; g += (x.get("G") or (x.get("stats") or {}).get("G") or 0) or 0
    if not games: return None
    return {"season": (rec.get("gameLog") or {}).get("season"), "games": len(games), "toiPerGame": round(sum(tois) / len(tois), 1) if tois else None, "ppGoals": ppg, "goals": g}


# ---------------------------------------------------------------- main
def main():
    pools = nhl_pools()
    print("NHL pools:", len(pools), "seasons x positions")
    cohort = load_cohort(pools)
    print("cohort rows:", len(cohort), "players:", len({r['pid'] for r in cohort}))
    tabs = load_league_tables()
    print("league tables:", len(tabs))
    system = json.load((EP / "system" / "DET.json").open())
    skaters = [p for p in system["skaters"] if (EP / "player" / f"{p['id']}.json").exists()]
    goalies = [p for p in system["goalies"] if (EP / "player" / f"{p['id']}.json").exists()]
    idm = id_map(skaters + goalies)
    from build_player import prospect_status, rookie_eligible, nhl_roster_ids, slug_of   # noqa  (same rule as the page builder)
    roster = nhl_roster_ids()
    draft_by_ep = {}
    for f in (EP / "draft").glob("*.json"):
        for p in json.load(f.open())["picks"]:
            if p.get("playerId"): draft_by_ep[p["playerId"]] = p

    prospects, excluded = [], []
    for p in skaters:
        rec = json.load((EP / "player" / f"{p['id']}.json").open()); pl = rec["player"]
        nhl_id = idm.get(p["id"]); land = landing(nhl_id, fetch=False) if nhl_id else None
        g = pos_group(pl); dob = pl.get("dateOfBirth"); dr = draft_by_ep.get(p["id"])
        if land:
            st = prospect_status(land)
        else:   # no NHL id found: fall back to EP draft year + age window, flagged
            yr_d = dr["year"] if dr else None
            st = {"prospect": (yr_d is not None and YR <= yr_d + 4) or (yr_d is None and age_at(CUR, dob) < 23), "rookieEligible": None, "inWindow": True, "window": f"draft+{YR - yr_d}" if yr_d else "undrafted", "draftYear": yr_d, "note": "no NHL id; eligibility unverified"}
        # slug must match the player page (build_player.slug_of on the NHL API name: "JP Hurlbert" -> jp-hurlbert, not EP's "J.P.")
        slug = slug_of(f"{land['firstName']['default']} {land['lastName']['default']}") if land else slug_of(pl["name"])
        base = {"epId": p["id"], "nhlId": nhl_id, "name": pl["name"], "slug": slug,
                "group": g, "position": "/".join(pl.get("detailedPosition") or []) or pl.get("position"), "birthDate": dob, "age": int(age_at(CUR, dob)) if dob else None,
                "height": (pl.get("height") or {}).get("imperial"), "weight": (pl.get("weight") or {}).get("imperial"), "shoots": pl.get("shoots"), "contract": pl.get("contract"),
                "rights": (pl.get("nhlRights") or {}).get("rights"), "draft": ({"year": dr["year"], "overall": dr["overall"], "round": dr["round"]} if dr else None),
                "status": {**st, "onNhlRoster": bool(nhl_id and nhl_id in roster)}, "scouting": re.sub(r"<[^>]+>", "", pl.get("profileDescriptionAsHTML") or "").strip() or None,
                "currentLines": all_lines(rec, CUR), "lastLines": all_lines(rec, PREV)}
        if not st["prospect"]:
            excluded.append({**base, "reason": ("past draft+4" if st.get("draftYear") else "past the undrafted age window") if st.get("rookieEligible") else "lost rookie eligibility"}); continue
        cur = primary_line(rec, CUR); prev = primary_line(rec, PREV); prev2 = primary_line(rec, PREV2)
        anchor = cur if (cur and cur["gp"] >= 10) else prev
        anchor_season = CUR if anchor is cur else PREV
        perf_prev = performance(tabs, p["id"], prev["leagueSlug"], PREV, g, 10) if prev else None
        perf_cur = performance(tabs, p["id"], cur["leagueSlug"], CUR, g, 3) if cur else None
        ceil = ceiling(cohort, g, int(age_at(anchor_season, dob)), anchor["nhle"], dr["overall"] if dr else None) if anchor else None
        ped = pedigree(cohort, g, dr["overall"] if dr else None)
        traj = None
        if prev and prev2:
            traj = {"from": {"season": PREV2, "league": prev2["league"], "nhle": prev2["nhle"], "gp": prev2["gp"]}, "to": {"season": PREV, "league": prev["league"], "nhle": prev["nhle"], "gp": prev["gp"]}, "delta": round(prev["nhle"] - prev2["nhle"], 3)}
        nhl_sample = None
        if land:
            rows = [t for t in land.get("seasonTotals", []) if t.get("leagueAbbrev") == "NHL" and t.get("gameTypeId") == 2]
            if rows:
                nhl_sample = {"gp": sum(t.get("gamesPlayed") or 0 for t in rows), "pts": sum(t.get("points") or 0 for t in rows), "seasons": sorted({t["season"] for t in rows}),
                              "thisSeason": next(({"gp": t.get("gamesPlayed"), "pts": t.get("points"), "toi": t.get("avgToi")} for t in rows if t.get("season") == int(SEASON)), None)}
        score = (ceil or {}).get("expected")
        prospects.append({**base, "anchor": {"season": anchor_season, **anchor} if anchor else None, "league": ({"name": anchor["league"], "table": anchor["table"], "coef": anchor["coef"], "source": NHLE["source"]} if anchor else None),
                          "performance": {"last": perf_prev, "current": perf_cur}, "ceiling": ceil, "pedigree": ped, "trajectory": traj, "deployment": deployment(rec), "nhlSample": nhl_sample,
                          "availability": {"gp": anchor["gp"], "season": anchor_season} if anchor else None, "rank": None, "score": score})
    prospects.sort(key=lambda x: (-(x["score"] if x["score"] is not None else -1), -((x["ceiling"] or {}).get("p75") or 0)))
    for i, x in enumerate(prospects): x["rank"] = i + 1

    goalie_rows = []
    for p in goalies:
        rec = json.load((EP / "player" / f"{p['id']}.json").open()); pl = rec["player"]; dr = draft_by_ep.get(p["id"]); nhl_id = idm.get(p["id"])
        goalie_rows.append({"epId": p["id"], "nhlId": nhl_id, "name": pl["name"], "birthDate": pl.get("dateOfBirth"), "age": int(age_at(CUR, pl["dateOfBirth"])) if pl.get("dateOfBirth") else None,
                            "draft": ({"year": dr["year"], "overall": dr["overall"], "round": dr["round"]} if dr else None), "currentLines": all_lines(rec, CUR), "lastLines": all_lines(rec, PREV)})

    out = {"season": SEASON, "built": dt.date.today().isoformat(), "cohort": {"years": [COHORT_YEARS.start, COHORT_YEARS.stop - 1], "rows": len(cohort), "players": len({r['pid'] for r in cohort}), "k": K_NEIGHBOURS},
           "nhle": {"source": NHLE["source"], "retrieved": NHLE["retrieved"]}, "prospects": prospects, "excluded": excluded, "goalies": goalie_rows,
           "method": {"prospect": "Rookie-eligible and inside draft+4 (draft year = year one). Undrafted: under 23 on Sept 15.",
                      "league": "Network NHLe points coefficient per league, hockeystats.com (Patrick Bacon). Applied to points per game.",
                      "performance": "Points per game percentile among skaters of the same position and the same age in the same league and season (EliteProspects league tables; exact age by set difference of EP's cumulative age filter). Full season needs 10+ GP; the current season 3+.",
                      "ceiling": f"Nearest {K_NEIGHBOURS} drafted skaters (2008-2019 classes) at the same position and age by NHLe (weight 1) and log draft slot (weight 0.5). Outcome = each one's peak NHL points-per-game percentile within position over seasons with at least half the games; busts count as 0. Expected = mean, ceiling = 75th percentile of the neighbours. Tiers: elite 88+, top-line 73+, above average 50+, below average 27+.",
                      "trajectory": "NHLe points per game, last full season minus the one before, league change noted.",
                      "ranking": "By expected peak percentile (the cohort mean), then by the 75th percentile."}}
    site = ROOT / "data" / "site"; (site / "prospects").mkdir(parents=True, exist_ok=True)
    (site / "prospects.json").write_text(json.dumps(out, indent=1))
    for x in prospects + excluded:
        if x.get("nhlId"): (site / "prospects" / f"{x['nhlId']}.json").write_text(json.dumps(x, indent=1))
    print(f"prospects: {len(prospects)} ranked, {len(excluded)} excluded, {len(goalie_rows)} goalies")
    for x in prospects:
        c = x["ceiling"] or {}; pf = (x["performance"]["last"] or {})
        print(f"{x['rank']:>2} {x['name']:<26} {x['group']} age {x['age']} {x['anchor']['league'] if x['anchor'] else '-':<10} nhle {x['anchor']['nhle'] if x['anchor'] else '-':<6} perf {pf.get('percentile')} ceiling exp {c.get('expected')} p75 {c.get('p75')} pReg {c.get('pRegular')} n {c.get('n')} {c.get('tier')}")


if __name__ == "__main__":
    main()
