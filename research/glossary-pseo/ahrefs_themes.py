"""Step 4: one keyword theme per stat, scored on Ahrefs KE (US) instead of DataForSEO Labs.

Same gates as growth:keyword-research theme.py (imported, not re-derived): MIN_VOLUME 10, cap 10 by
volume, sort volume desc -> difficulty asc (Ahrefs KD stands in for median dofollow RDs) -> CPC desc
-> alpha, supporting keywords need >=30% overlap with the primary's top-10 SERP domains (live
DataForSEO serp/organic/live/regular, the skill's own DFS.serp), theme needs >=2 keywords.
"""
import csv, importlib.util, json, os, re, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
THEME_PY = os.path.expanduser("~/.claude/plugins/cache/daydream-growth-skills/growth/c4ba71121068/"
                              "skills/growth/keyword-research/scripts/theme.py")
spec = importlib.util.spec_from_file_location("theme", THEME_PY)
theme = importlib.util.module_from_spec(spec)
spec.loader.exec_module(theme)
sys.path.insert(0, HERE)
from stats import STATS


def num(s):
    s = (s or "").strip().replace("$", "")
    if s in ("", "N/A") or "–" in s:
        return None
    m = re.match(r"^([\d.]+)([KM]?)$", s)
    if not m:
        return None
    return float(m.group(1)) * {"": 1, "K": 1_000, "M": 1_000_000}[m.group(2)]


ahrefs = {}
for r in csv.DictReader(open(os.path.join(HERE, "ahrefs_ke_us.tsv")), delimiter="\t"):
    ahrefs[r["KW"]] = {"search_volume": int(num(r["SV"]) or 0), "kd": num(r["KD"]), "cpc": num(r["CPC"]) or 0,
                       "traffic_potential": num(r["TP"]), "parent_topic": None if r["PARENT"] == "N/A" else r["PARENT"]}

dfs = theme.DFS(os.environ["DATAFORSEO_LOGIN"], os.environ["DATAFORSEO_PASSWORD"], 2840, "en")
cache_path = os.path.join(HERE, "serp_cache.json")
serp_cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}

plans = []
for sid, cat, label, names in STATS:
    raw = [k for k in open(os.path.join(HERE, "theme_inputs", f"{sid}.txt")).read().split("\n") if k]
    cands = [{"keyword": k, **ahrefs[k]} for k in raw if k in ahrefs]
    cands = theme.dedupe(cands)
    cands = [c for c in cands if c["search_volume"] >= theme.MIN_VOLUME]
    cands = theme.cap_candidates(cands)
    plans.append((sid, cat, label, cands))

need = sorted({c["keyword"] for *_, cands in plans for c in cands if len(cands) >= 2} - set(serp_cache))
print(len(need), "SERPs to pull")
with ThreadPoolExecutor(8) as ex:
    for k, urls in zip(need, ex.map(lambda k: dfs.serp(k, 10), need)):
        serp_cache[k] = urls
json.dump(serp_cache, open(cache_path, "w"), indent=1)

# Gate 3 (Mark's keyword gates): the primary's top 10 must be explainer pages, not leaderboards,
# standings or a different entity (Fenwick Friars, youth "SHG" leagues). If the sort-determined
# primary fails, the highest-volume candidate that passes becomes primary; the swap is recorded.
DATA = re.compile(r"/stats|standings|leaders|/players?/|/player/|/team/|/teams/|statmuse\.com|naturalstattrick\.com|"
                  r"moneypuck\.com|hockey-reference\.com/(leagues|players|teams)|espn\.com/nhl/(stats|standings|team|player)|"
                  r"nhl\.com/(stats|standings|player)|capfriendly|puckpedia\.com/(player|team)|evolving-hockey\.com/?$|"
                  r"hockeystats\.com|quanthockey|dailyfaceoff|records\.nhl\.com|/scores|/schedule|fenwickfriar|fenwickfriars|"
                  r"maxpreps|eliteprospects|youthhockey\.com|sportngin\.com|myhockeyrankings", re.I)
EXPLAINER_MIN = 0.50


def explainer_share(urls):
    return 1 - sum(bool(DATA.search(u)) for u in urls) / max(len(urls), 1)


out = []
for sid, cat, label, cands in plans:
    rec = {"stat": sid, "category": cat, "label": label, "candidates": len(cands)}
    if not cands:
        rec["status"] = "no_volume"
    elif len(cands) == 1:
        rec.update(status="single_keyword", primary=cands[0], supporting=[], rejected={})
    else:
        for c in cands:
            c["median_dofollow_rds"] = c["kd"]   # theme.sort_theme's difficulty column
        cands = theme.sort_theme(cands)
        override = None
        if explainer_share(serp_cache[cands[0]["keyword"]]) < EXPLAINER_MIN:
            ok = [c for c in cands if explainer_share(serp_cache[c["keyword"]]) >= EXPLAINER_MIN]
            if ok:
                override = {"from": cands[0]["keyword"], "to": ok[0]["keyword"],
                            "reason": f"sort primary's top 10 is {1 - explainer_share(serp_cache[cands[0]['keyword']]):.0%} "
                                      "leaderboards/standings/other entity"}
                cands = [ok[0]] + [c for c in cands if c is not ok[0]]
            else:
                override = {"from": cands[0]["keyword"], "to": None, "reason": "no candidate has an explainer SERP"}
        primary = cands[0]
        pdom = theme.domains_of(serp_cache[primary["keyword"]])
        sup, rej = [], {}
        for c in cands[1:]:
            ov = theme.serp_overlap(pdom, theme.domains_of(serp_cache[c["keyword"]]))
            (sup.append({**c, "serp_overlap": round(ov, 2)}) if ov >= theme.OVERLAP_THRESHOLD
             else rej.__setitem__(c["keyword"], round(ov, 2)))
        rec.update(status="theme" if sup else "no_serp_overlap", primary=primary, supporting=sup, rejected=rej,
                   primary_top10=serp_cache[primary["keyword"]], primary_override=override,
                   primary_explainer_share=round(explainer_share(serp_cache[primary["keyword"]]), 2))
    out.append(rec)

json.dump(out, open(os.path.join(HERE, "stat_themes.json"), "w"), indent=1)
print(f"DataForSEO SERP cost this run: ${dfs.cost:.3f}")
for r in out:
    p = r.get("primary")
    head = f"{p['keyword']} ({p['search_volume']}, KD {p['kd']})" if p else "-"
    sup = ", ".join(f"{s['keyword']} ({s['search_volume']}, {s['serp_overlap']:.0%})" for s in r.get("supporting", []))
    if r.get("primary_override"): print("   OVERRIDE", r["primary_override"])
    print(f"{r['category']:8} {r['stat']:16} {r['status']:16} {head}\n{'':26}+ {sup}\n{'':26}x {r.get('rejected')}")
