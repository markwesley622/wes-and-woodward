# Claims register: save-percentage.json

Reviewed 2026-10-09. All NHL API files downloaded 2026-10-09 to `research/glossary-pseo/raw/`. "W&W calc" = computed by the writer from the named file.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | SV% = saves ÷ shots on goal faced; standard on NHL stat lines | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) Sv%; Hockey-Reference glossary (hockey-reference.com/about/glossary.html) SV% | SUPPORTED |
| 2 | Treats a point shot and a tap-in the same; expected-goals stats grade more fairly | Definition (every shot weighted 1); MoneyPuck GSAx built on xG per attempt (moneypuck.com/glossary.htm) | SUPPORTED |
| 3 | League SV% .896 in 2025-26 (64,976 saves / 72,530 SA), lowest since 1993-94 (.895) | W&W calc, raw/nhl_goalie_summary_20252026.json; raw/nhl_league_goalie_totals_by_season_1983-2026.json | SUPPORTED (computed) |
| 4 | League SV% peaked at .915 in 2015-16, highest since at least 1983-84 | W&W calc, raw/nhl_league_goalie_totals_by_season_1983-2026.json (2015-16 .9149, 2014-15 .9147) | SUPPORTED (computed) |
| 5 | NHL glossary dates official SV% tracking to 1955-56, when shots against began being counted (teams) | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) Sv% and SA entries | SUPPORTED |
| 6 | First 38 seasons (1917-18 to 1954-55) before SV%; formula SV/SA in NHL and Hockey-Reference glossaries | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) (GAA first season 1917-18; Sv% 1955-56); Hockey-Reference glossary (hockey-reference.com/about/glossary.html) | SUPPORTED |
| 7 | Shots logged rink by rink through the Real Time Scoring System | Schuckers & Macdonald, arXiv 1412.1035 (data 2007-08 to 2012-13) | SUPPORTED |
| 8 | Blocked and missed attempts excluded; post/crossbar = missed shot | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) SA and Sv% entries | SUPPORTED |
| 9 | NHL skaters hit 2,137 posts and 691 crossbars in 2025-26 | W&W calc, raw/nhl_skater_realtime_20252026.json (missedShotGoalpost, missedShotCrossbar) | SUPPORTED (computed) |
| 10 | NHL splits SV% by strength since 1997-98 (EV/PP/SH) | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) EV Sv%, PP Sv%, SH Sv% | SUPPORTED |
| 11 | Hockey-Reference publishes SV% next to its GSAA | raw/hr_goalies_2025-26_downloaded_2026-10-09.html (SV% and GSAA columns) | SUPPORTED |
| 12 | MoneyPuck prices each attempt a goalie faces (xG on unblocked attempts) | MoneyPuck about/glossary; raw/mp_goalies_2025.csv (xGoals, unblocked_shot_attempts) | SUPPORTED |
| 13 | Worked example 27/30 = .900, 28/30 = .933 (invented); Gibson 1,461 SA, each save ≈ .0007 (1/1,461) | Arithmetic; raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 14 | Teams allowed 8,086 goals, goalies charged 7,578; gap = exactly the 508 empty-net goals | W&W calc, raw/nhl_team_summary_20252026_goalie-pages.json vs raw/nhl_goalie_summary_20252026.json vs raw/nhl_skater_realtime_20252026.json (emptyNetGoals sum 508) | SUPPORTED (computed) |
| 15 | NYI beat SEA in a shootout after 0-0 in November 2025; Rittich and Daccord each credited a shutout and 0 GA; Daccord took the OTL | raw/nhl_goalie_games_20252026.json + raw/nhl_team_games_20252026.json, game 2025-11-23 | SUPPORTED (computed) |
| 16 | 51 goalies with 30+ GP: median .899, Wedgewood .921 (COL) best, Ersson .870 (PHI) worst; Gibson .901 21st; Talbot .883 (43rd, near the bottom) | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 17 | Detroit goalies combined .895 (2,021 / 2,258), as close to league average as a team gets (17th of 32) | W&W calc, raw/nhl_goalie_games_20252026.json summed by team | SUPPORTED (computed) |
| 18 | Saros led with 1,700 SA; ten points = 1 goal per 100 shots ≈ 17 goals for him | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 19 | Gibson +8.2 goals vs a .896 goalie on 1,461 shots; Talbot −10.0 on 797 ('about half the shots'); tandem ≈ −2 net | W&W calc, (SV% − .8959) × SA, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 20 | Year-to-year SV% correlation 0.28 for the 35 goalies with 30+ GP in 2024-25 and 2025-26 (r² < 0.1) | W&W calc, raw/nhl_goalie_summary_20242025.json and raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 21 | GSAA = (SV% − league SV%) × SA, published by Hockey-Reference for every goalie | raw/hr_goalies_2025-26_downloaded_2026-10-09.html GSAA tooltip | SUPPORTED |
| 22 | League EV SV% .903, PP SV% .853 in 2025-26; NHL glossary attributes lower PP SV% to higher-quality shots | W&W calc, raw/nhl_goalie_savesByStrength_20252026.json; NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) PP Sv% | SUPPORTED (computed) |
| 23 | Gibson faced 202 of 1,461 shots on the PK (13.8% vs 14.9% league); EV .912, PP .837 | W&W calc, raw/nhl_goalie_savesByStrength_20252026.json | SUPPORTED (computed) |
| 24 | MoneyPuck: Gibson faced 155.7 xG, allowed 144, GSAx +11.7; Talbot −13.1 | W&W calc, raw/mp_goalies_2025.csv (all situations, xGoals − goals) | SUPPORTED (computed) |
| 25 | Hellebuyck .925 in 2024-25, .895 in 2025-26, both WPG (30-point drop) | raw/nhl_goalie_summary_20242025.json; raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 26 | Schuckers & Macdonald: shots the most consistently recorded of the events studied; only Florida's and St. Louis's rinks significantly off the league rate | Schuckers & Macdonald, arXiv 1412.1035 (data 2007-08 to 2012-13) | SUPPORTED |
| 27 | FAQ: Hockey-Reference prints .897-style decimals; NHL API stores 0.91233 for Vasilevskiy 2025-26 | raw/hr_goalies_2025-26_downloaded_2026-10-09.html; raw/nhl_goalie_summary_20252026.json | SUPPORTED |
| 28 | Live intro: SV%, GAA and record from NHL club stats, GSAx from MoneyPuck | pipeline/build_site_data.py (club_stats.json goalies; MoneyPuck xGoals − goals) | SUPPORTED |

## Voice metrics (`extract_prose.py save-percentage` + `style_metrics.py --target barnwell_lean`)

| Metric | Page | Target |
|---|---|---|
| Words (running prose) | 1307 | |
| sent_mean | 18.9 | 17-21 |
| sent_sd | 10.3 | >=10 |
| pct_short_le6 | 7 | 6-15 |
| pct_long_ge30 | 16 | <=20 |
| para_words | 65 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 42.8 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 3.8 | 3-8 |
| q_per_k | 1.5 | 1-5 |
| paren_per_k | 5.4 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 54.3 | 30-55 |
| hedge_narrow_per_k | 0.8 | <=3 |

Every metric is inside the target. ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, negation pivots or unicode artifacts; remaining hints are `uniform_paragraph_structure` and `repeated_ngrams` (fixed template + metric names).

Proposed hover short: none (the current `short` in glossary-terms.json agrees with the page).
