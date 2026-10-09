"""Step 3: per-stat candidate lists for theme.py --file (hockey intent only, close variants collapsed)."""
import json, os, re, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats import STATS

rows = json.load(open("stat_variants.json"))
share = json.load(open("unq_hockey_share.json"))
HOCKEY_MIN = 0.60   # unqualified variants need >=60% hockey results in the US top 10

by_stat = collections.defaultdict(dict)
for r in rows:
    if (r["us"] or 0) < 10:
        continue
    if not r["qualified"] and share.get(r["keyword"], 0) < HOCKEY_MIN:
        continue
    by_stat[r["stat"]][r["keyword"]] = r


def key(k):  # word order and "in" don't change the query for Google Ads
    return frozenset(t for t in k.split() if t != "in")


def pref(k):
    toks = k.split()
    return (not ("what" in toks and "in" in toks), toks[0] in ("hockey", "nhl"), -len(k))


os.makedirs("theme_inputs", exist_ok=True)
summary = []
for sid, cat, label, names in STATS:
    groups = collections.defaultdict(list)
    for k, r in by_stat.get(sid, {}).items():
        groups[(key(k), r["us"], tuple(r["monthly"] or []))].append(k)
    reps = []
    for g, ks in groups.items():
        rep = sorted(ks, key=pref)[0]
        reps.append({"keyword": rep, "us": by_stat[sid][rep]["us"], "collapsed": sorted(set(ks) - {rep})})
    reps.sort(key=lambda x: -x["us"])
    with open(f"theme_inputs/{sid}.txt", "w") as f:
        f.write("\n".join(x["keyword"] for x in reps) + ("\n" if reps else ""))
    summary.append({"stat": sid, "category": cat, "label": label, "n": len(reps),
                    "top": reps[:3], "variants": reps})
json.dump(summary, open("theme_inputs/summary.json", "w"), indent=1)
for s in summary:
    print(f"{s['category']:9} {s['stat']:16} n={s['n']:>3}  " + "; ".join(f"{x['keyword']} ({x['us']})" for x in s['top']))
