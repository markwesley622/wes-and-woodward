# Glossary pSEO keyword validation (2026-10-09)

Google Ads search volume (DataForSEO `keywords_data/google_ads/search_volume/live`), US (2840) + Canada (2124),
for 4,015 variants built from `terms.py` (term names x 17 phrasing templates + hub queries). Live US desktop SERPs for
40 representative keywords in `serps.json`.

- `volumes.json` every variant with US/CA volume + 12 monthly values (most recent first, Aug 2026 back to Sep 2025)
- `glossary_terms.csv` one row per candidate page: hockey-qualified variants only, close variants deduped by identical
  monthly series. `cluster_us` is an upper bound (Google groups close variants, so sums overlap).
- `serps.json` top 10, hockey share of the top 10, AI Overview presence

Rerun: `export SSL_CERT_FILE="$(python3 -c 'import certifi;print(certifi.where())')"; python3 -I pull_volume.py; python3 -I serp.py serp_kws.txt serps.json`
