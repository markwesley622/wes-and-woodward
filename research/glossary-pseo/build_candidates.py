"""Step 1: Google Ads US volume for every stat-name x modifier variant (discovery + intent filter)."""
import os, json, base64, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stats import STATS, MODIFIERS, GENERIC_NAMES, Q_TEMPLATES

AUTH = base64.b64encode(f"{os.environ['DATAFORSEO_LOGIN']}:{os.environ['DATAFORSEO_PASSWORD']}".encode()).decode()
OUT = os.path.dirname(os.path.abspath(__file__))


def post(path, payload):
    req = urllib.request.Request("https://api.dataforseo.com/v3/" + path, data=json.dumps(payload).encode(),
                                 headers={"Authorization": "Basic " + AUTH, "Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=300))


def clean(k):
    k = k.lower().replace("+/-", "plus minus").replace("%", " percentage")
    k = re.sub(r"[%/+]|(?<=\w)-(?=\w)", " ", k.lower())
    k = re.sub(r"[^a-z0-9 ]", "", k)
    return re.sub(r"\s+", " ", k).strip()


meta = {}
for sid, cat, label, names in STATS:
    for n in names:
        short = len(re.sub(r"[^a-z0-9]", "", n.lower())) <= 2 or n in GENERIC_NAMES
        for m in (Q_TEMPLATES if short else MODIFIERS):
            k = clean(m.format(n=n))
            if not k or len(k.split()) > 10:
                continue
            qualified = bool(re.search(r"\b(hockey|nhl)\b", k))
            meta.setdefault(k, []).append({"stat": sid, "name": n, "modifier": m, "qualified": qualified})

kws = sorted(meta)
print(len(kws), "variants")


def run(chunk):
    for _ in range(4):
        try:
            d = post("keywords_data/google_ads/search_volume/live",
                     [{"keywords": chunk, "location_code": 2840, "language_code": "en"}])
            t = d["tasks"][0]
            if t["status_code"] == 20000:
                return t["result"] or []
            print(t["status_code"], t["status_message"]); time.sleep(15)
        except Exception as e:
            print("err", e); time.sleep(15)
    return None


chunks = [kws[i:i + 1000] for i in range(0, len(kws), 1000)]
vol = {}
with ThreadPoolExecutor(4) as ex:
    for i, res in enumerate(ex.map(run, chunks)):
        if res is None:
            print("CHUNK FAILED", i)
            continue
        for r in res:
            vol[r["keyword"]] = {"us": r.get("search_volume"), "cpc": r.get("cpc"),
                                 "monthly": [m["search_volume"] for m in (r.get("monthly_searches") or [])]}
rows = []
for k in kws:
    v = vol.get(k) or {}
    for m in meta[k]:
        rows.append({"keyword": k, **m, "us": v.get("us"), "monthly": v.get("monthly")})
json.dump(rows, open(os.path.join(OUT, "stat_variants.json"), "w"), indent=1)
print("with volume:", len({r["keyword"] for r in rows if (r["us"] or 0) > 0}))
