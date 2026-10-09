"""Live US Google SERPs: hockey-intent share of top 10, SERP features, who ranks."""
import os, json, base64, re, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor

AUTH = base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode()
OUT = os.path.dirname(os.path.abspath(__file__))
HOCKEY = re.compile(r"hockey|nhl|puck|goalie|goaltend|icing|skater|stanley|corsi|fenwick|moneypuck|natural ?stat|evolving|rink|ahl|ohl|capfriendly|puckpedia|capwages|red wings|maple leafs|oilers|bruins|rangers|penguins|canadiens|flyers|blackhawks|avalanche", re.I)
HOCKEY_DOMAINS = {"nhl.com", "moneypuck.com", "naturalstattrick.com", "evolving-hockey.com", "hockey-reference.com",
                  "thehockeywriters.com", "hockey-graphs.com", "puckpedia.com", "capwages.com", "hockeyviz.com",
                  "dailyfaceoff.com", "hockeyfights.com", "usahockey.com", "hockeycanada.ca", "eliteprospects.com",
                  "hockeymonkey.com", "puremhockey.com", "prohockeyrumors.com", "thehockeynews.com", "si.com/hockey",
                  "allaboutthejersey.com", "hockeyfeed.com", "hockeyanswered.com", "hockeyworld.blog"}


def post(path, payload):
    req = urllib.request.Request("https://api.dataforseo.com/v3/" + path, data=json.dumps(payload).encode(),
                                 headers={"Authorization": "Basic " + AUTH, "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=300))


def serp(kw):
    import time
    for attempt in range(5):
        d = post("serp/google/organic/live/advanced",
             [{"keyword": kw, "location_code": 2840, "language_code": "en", "device": "desktop", "depth": 10}])
        if d.get("tasks") and d["tasks"][0].get("status_code") == 20000: break
        print("retry", kw, d.get("status_message"), (d.get("tasks") or [{}])[0].get("status_message"), file=sys.stderr); time.sleep(5 * (attempt + 1))
    res = (d["tasks"][0].get("result") or [{}])[0]
    items = res.get("items") or []
    types = sorted({i["type"] for i in items})
    org = [i for i in items if i["type"] == "organic"][:10]
    top = []
    for i in org:
        dom = (i.get("domain") or "").replace("www.", "")
        txt = f"{i.get('title','')} {i.get('description','')} {i.get('url','')}"
        top.append({"rank": i.get("rank_group"), "domain": dom, "title": i.get("title"), "url": i.get("url"),
                    "hockey": bool(HOCKEY.search(txt)) or dom in HOCKEY_DOMAINS})
    fs = next((i for i in items if i["type"] == "featured_snippet"), None)
    aio = next((i for i in items if i["type"] == "ai_overview"), None)
    return {"keyword": kw, "types": types, "hockey_share": sum(t["hockey"] for t in top) / max(len(top), 1),
            "featured_snippet": (fs or {}).get("domain"), "ai_overview": aio is not None, "top": top}


if __name__ == "__main__":
    kws = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    with ThreadPoolExecutor(10) as ex:
        res = list(ex.map(serp, kws))
    json.dump(res, open(os.path.join(OUT, sys.argv[2]), "w"), indent=1)
    for r in res:
        doms = ", ".join(t["domain"] + ("" if t["hockey"] else "*") for t in r["top"][:7])
        print(f"{r['keyword'][:38]:38} hk={r['hockey_share']:.0%} aio={'Y' if r['ai_overview'] else '-'} fs={r['featured_snippet'] or '-':18} | {doms}")
