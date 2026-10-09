# Claims register: shutouts.json

Reviewed 2026-10-09. All NHL API files downloaded 2026-10-09 to `research/glossary-pseo/raw/`. "W&W calc" = computed by the writer from the named file.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | SO = shutout: opponent scores zero before any shootout; a goalie gets it only as his team's lone goalie; combined shutouts go to the team | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) 'SO shutout'; W&W calc raw/nhl_team_games_20252026.json vs raw/nhl_goalie_games_20252026.json (113 team shutouts, 111 goalie, 2 combined credited to neither); The Hockey Writers 2025-01-08 (Skinner not credited after Pickard briefly played) | SUPPORTED |
| 2 | On NHL shootout reports SO marks shootout stats (SO G, SO S) | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) SO G, SO S | SUPPORTED |
| 3 | One shutout about every 24 starts (111 / 2,624) | W&W calc, raw/nhl_goalie_summary_20252026.json, raw/nhl_goalie_games_20252026.json | SUPPORTED (computed) |
| 4 | Hainsworth 22 in 1928-29 (44-game schedule, MTL); none above 15 since; Esposito 15 in 1969-70 closest | raw/nhl_goalie_records_season_shutouts_top10_2026-10-09.json | SUPPORTED |
| 5 | Brodeur 125 career; Sawchuk second with 103; Sawchuk 85 with Detroit is franchise record | raw/nhl_goalie_records_career_shutouts_top10_2026-10-09.json; raw/nhl_goalie_records_det_franchise_career_shutouts_2026-10-09.json | SUPPORTED |
| 6 | 191 goalie shutouts in 2003-04 (30 teams, 2,460 team games = 7.8%) vs 111 in 2025-26 (4.2%); league GAA rose 2.46 → 2.88 | W&W calc, raw/nhl_league_goalie_totals_by_season_1983-2026.json | SUPPORTED (computed) |
| 7 | NHL.com and Hockey-Reference publish goalie shutouts; NHL team reports carry team shutouts incl. shared ones | Hockey-Reference glossary (hockey-reference.com/about/glossary.html) SO; raw/nhl_team_summary_20252026_goalie-pages.json teamShutouts (sum 113) | SUPPORTED |
| 8 | Mar 8, 2026 DET 3-0 at NJ: Gibson 21 saves, hurt late in 2nd; Talbot 10 in 3rd; first Detroit combined shutout since 2014; neither credited | AP recap via CBS Sports, 2026-03-08 (cbssports.com/nhl/gametracker/recap/NHL_20260308_DET@NJ); raw/nhl_goalie_games_20252026.json (shutouts = 0 for both) | SUPPORTED |
| 9 | NYI-SEA 0-0 shootout in Nov 2025: Rittich and Daccord each credited; Daccord's with an OTL | raw/nhl_goalie_games_20252026.json 2025-11-23 | SUPPORTED (computed) |
| 10 | 52 of 98 goalies had a shutout; 14 of 51 with 30+ GP had none, incl. Hellebuyck (57 starts of 82, > two-thirds) | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 11 | Sorokin 7 led; NYI 9 team shutouts led; Hofer 6; Gibson's 4 tied with six others for third; ANA, WPG, SJS, PHI had none | W&W calc, raw/nhl_goalie_summary_20252026.json, raw/nhl_team_summary_20252026_goalie-pages.json | SUPPORTED (computed) |
| 12 | Sorokin .906 vs Hellebuyck .895 (11 points) | raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 13 | COL and MIN had the best team SV% and 8 team shutouts each; Detroit's 5 tied for sixth, league median 3 | W&W calc, raw/nhl_goalie_games_20252026.json by team; raw/nhl_team_summary_20252026_goalie-pages.json | SUPPORTED (computed) |
| 14 | Sawchuk 12 in a season three times for Detroit (67-70 GP) and Hall 12 in 1955-56; Osgood second with 39; nobody else 30+ | raw/nhl_goalie_records_det_franchise_season_shutouts_2026-10-09.json; raw/nhl_goalie_records_det_franchise_career_shutouts_2026-10-09.json (Lumley 26 third) | SUPPORTED |
| 15 | Gibson's four: 39 saves vs VAN (Dec 8), 27 vs MTL, 26 vs CHI, 21 vs COL (Feb 2) | raw/nhl_goalie_games_20252026.json | SUPPORTED |
| 16 | Coin-flip: .905^22 ≈ 11%, .905^35 ≈ 3% (labelled idealized) | Arithmetic | SUPPORTED (computed) |
| 17 | Most regulars land between 0 and 4 (49 of 51 with 30+ GP) | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 18 | Live intro: shutouts, SV%, GAA from NHL club stats | pipeline/build_site_data.py | SUPPORTED |

## Voice metrics (`extract_prose.py shutouts` + `style_metrics.py --target barnwell_lean`)

| Metric | Page | Target |
|---|---|---|
| Words (running prose) | 1086 | |
| sent_mean | 19.1 | 17-21 |
| sent_sd | 10.6 | >=10 |
| pct_short_le6 | 11 | 6-15 |
| pct_long_ge30 | 14 | <=20 |
| para_words | 57 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 38.7 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 6.4 | 3-8 |
| q_per_k | 1.8 | 1-5 |
| paren_per_k | 3.7 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 54.3 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

Every metric is inside the target. ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, negation pivots or unicode artifacts; remaining hints are `uniform_paragraph_structure` and `repeated_ngrams` (fixed template + metric names).

Proposed hover short: none (the current `short` in glossary-terms.json agrees with the page).
