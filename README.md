# Red Wings Analytics (working title)

Data warehouse + (eventually) Astro site for a Detroit Red Wings advanced-analytics
publication. Personal project. Hosting: GitHub -> Astro (GitHub Actions/Pages), NOT Vercel.
GitHub account: markwesley622.

## Layout

- `pipeline/config.json` — season + team config. Bump `nhl_season` (20262027) and
  `mp_season` (2026) when the new season starts; set `standings_date` to `now` in-season.
- `pipeline/fetch_nhl.py` — official NHL API: roster, club stats, schedule/results, standings.
- `pipeline/fetch_moneypuck.py` — MoneyPuck season CSVs (skaters/goalies/lines/teams),
  full-league files + `_det` filtered copies. League files are kept for percentile context.
- `pipeline/build_site_data.py` — merges raw pulls into `data/site/*.json`, the contract
  the Astro site will consume: team.json, skaters.json, goalies.json, lines.json, results.json.
- `refresh.sh` — runs all three in order.

## Data sources

- NHL API (`api-web.nhle.com`) — free, no key.
- MoneyPuck season summaries — free CSV downloads, xG model.
- (Later, optional) Natural Stat Trick scrapes for anything MoneyPuck lacks.

## Gotchas

- macOS Python needs certifi for SSL (`ssl.create_default_context(cafile=certifi.where())`
  is already baked into both fetchers). Plain urllib without it fails cert verification.
- MoneyPuck `lines.csv` is 5on5-only, `position` is `line` or `pairing`.
- Skater percentiles are computed among league regulars (>=300 min 5v5), split F vs D;
  entries carry `qualifiesForPercentiles` so small samples can be visually flagged.
- GSAx = MoneyPuck `xGoals - goals` against, all situations.

## Editorial model (decided 2026-08-26)

1. Living dashboards — auto-refresh nightly from this pipeline.
2. Weekly columns — Mark writes; pipeline will generate a "what the numbers say this
   week" draft-assist starting point (not built yet).
3. Evergreen interactives — trade trees (~/Documents/debrincat-trade-tree) and NHL
   redraft port in as launch content.
