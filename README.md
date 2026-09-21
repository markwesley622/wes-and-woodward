# Wes & Woodward

wesandwoodward.com — a Detroit Red Wings advanced-analytics publication. "Woodward" is
Woodward Avenue, where Little Caesars Arena sits. Professional-publication register.
Personal project. Hosting: GitHub -> Astro (GitHub Actions/Pages), NOT Vercel.
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
- HockeyStatCards (`hockeystatcards.com` — plural; the singular domain does not resolve) —
  free, no key, no login. Server-rendered TanStack Start app: `/players/<nhlPlayerId>` is the
  skater card (Luszczyszyn Game Score ratings + percentiles), `/players/<nhlPlayerId>?tab=logs`
  is the game-by-game log with per-game on-ice xGF/xGA/GF/GA. Underlying data is Natural Stat
  Trick. This is the cheapest per-game on-ice xG source we have — MoneyPuck's season files
  can't do it and NST needs a browser. Fetcher:
  `research/sandin-pellikka/raw/hsc/fetch_hsc.py`. Rate-limits hard (429); back off between pulls.
- Evolving Hockey (subscriber, Mark's personal Chrome — the OTHER connected Chrome is not signed
  in). League-wide GAR/xGAR/RAPM/QoT/QoC exports live in `research/rasmussen/raw/eh/` and already
  cover 2025-26. Its player selectors are Shiny `selectInput`s with server-side options, so
  typing into the box does nothing — drive them from the query string
  (`?_inputs_&sglog_player="First Last"&sglog_table="Zones"&...`) and click Download. The
  QoT/QoC table is SEASON-ONLY; there is no date filter anywhere on it.
- (Later, optional) Natural Stat Trick scrapes for anything MoneyPuck lacks.

## Gotchas

- macOS Python needs certifi for SSL (`ssl.create_default_context(cafile=certifi.where())`
  is already baked into both fetchers). Plain urllib without it fails cert verification.
- MoneyPuck `lines.csv` is 5on5-only, `position` is `line` or `pairing`.
- NHL shift charts (`api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId=X`) reconstruct
  who was on the ice each second, which is how we build quality of competition by date when EH
  can't. `typeCode == 517` are shifts (505 are events); goalies arrive in the same feed and are
  stripped via the goalie `bios` endpoint. Both endpoints need `urllib.parse.urlencode` — a raw
  space in `cayenneExp` raises `InvalidURL`. Reference implementation:
  `research/sandin-pellikka/raw/build_qoc_by_date.py` (validates against EH 5v5 TOI exactly).
- MoneyPuck's season `skaters.csv` lists a midseason-traded player ONCE, under his final team,
  with his whole-season totals. Justin Faulk's 2025-26 row reads `DET, 78 GP` but is St. Louis
  plus Detroit combined. For team-scoped numbers on a traded player use the team `lines_*.csv`
  file (correctly scoped) or MoneyPuck's shot-by-shot files, never the season row.
- Skater percentiles are computed among league regulars (>=300 min 5v5), split F vs D;
  entries carry `qualifiesForPercentiles` so small samples can be visually flagged.
- GSAx = MoneyPuck `xGoals - goals` against, all situations.

## Editorial model (decided 2026-08-26)

1. Living dashboards — auto-refresh nightly from this pipeline.
2. Weekly columns — Mark writes; pipeline will generate a "what the numbers say this
   week" draft-assist starting point (not built yet).
3. Evergreen interactives — trade trees (~/Documents/debrincat-trade-tree) and NHL
   redraft port in as launch content.
