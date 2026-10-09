"""Google Ads search volume for every glossary variant, US + Canada."""
import os, json, base64, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(__file__))
from terms import TERMS, HUB, TEMPLATES

AUTH = base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode()
OUT = os.path.dirname(os.path.abspath(__file__))


def post(path, payload):
    req = urllib.request.Request("https://api.dataforseo.com/v3/" + path, data=json.dumps(payload).encode(),
                                 headers={"Authorization": "Basic " + AUTH, "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=300))


kw_meta = {}  # keyword -> (term_id, category, name, template)
for tid, cat, names in TERMS:
    for n in names:
        for t in TEMPLATES:
            k = re.sub(r"\s+", " ", t.format(n=n)).strip().lower()
            kw_meta.setdefault(k, (tid, cat, n, t))
for k in HUB:
    kw_meta.setdefault(k.lower(), ("hub", "hub", k, "{n}"))

kws = sorted(kw_meta)
print(len(kws), "keywords")
chunks = [kws[i:i + 1000] for i in range(0, len(kws), 1000)]


def run(args):
    loc, chunk = args
    for attempt in range(3):
        try:
            d = post("keywords_data/google_ads/search_volume/live",
                     [{"keywords": chunk, "location_code": loc, "language_code": "en"}])
            t = d["tasks"][0]
            if t["status_code"] != 20000:
                print(loc, t["status_code"], t["status_message"]); time.sleep(10); continue
            return loc, t["result"] or []
        except Exception as e:
            print("err", loc, e); time.sleep(10)
    return loc, []


jobs = [(loc, c) for loc in (2840, 2124) for c in chunks]
vol = {}
with ThreadPoolExecutor(4) as ex:
    for loc, res in ex.map(run, jobs):
        for r in res:
            vol.setdefault(r["keyword"], {})[loc] = {
                "sv": r.get("search_volume"), "cpc": r.get("cpc"), "comp": r.get("competition"),
                "monthly": [m["search_volume"] for m in (r.get("monthly_searches") or [])][:12]}

rows = []
for k in kws:
    tid, cat, n, t = kw_meta[k]
    v = vol.get(k, {})
    rows.append({"keyword": k, "term": tid, "category": cat, "name": n, "template": t,
                 "us": (v.get(2840) or {}).get("sv"), "ca": (v.get(2124) or {}).get("sv"),
                 "us_monthly": (v.get(2840) or {}).get("monthly")})
json.dump(rows, open(os.path.join(OUT, "volumes.json"), "w"), indent=1)
print("returned", sum(1 for r in rows if r["us"] is not None), "us /", sum(1 for r in rows if r["ca"] is not None), "ca")
