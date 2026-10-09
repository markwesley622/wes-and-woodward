# Claims register: goals-against-average.json

Reviewed 2026-10-09. All NHL API files downloaded 2026-10-09 to `research/glossary-pseo/raw/`. "W&W calc" = computed by the writer from the named file.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | GAA = goals against × 60 ÷ minutes played; ignores shots faced and their danger | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) GAA (GA*60/TOI); Hockey-Reference glossary (hockey-reference.com/about/glossary.html) GAA | SUPPORTED |
| 2 | Oldest goalie rate stat; NHL glossary carries GAA to 1917-18, the first season; SA not official until 1955-56 (nearly four decades) | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) GAA firstSeasonForStat 19171918; SA/Sv% 1955-56 | SUPPORTED |
| 3 | Hainsworth 0.92 GAA, Montreal 1928-29, 43 GA in 44 GP, lowest ever (25+ GP) | NHL API season query sorted by GAA, raw/nhl_goalie_records_season_gaa_low_min25gp_2026-10-09.json | SUPPORTED (computed) |
| 4 | Overtime and partial games count at real length; relief charged only for his minutes | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) GAA uses TOI; Hockey-Reference glossary (hockey-reference.com/about/glossary.html) minutes played | SUPPORTED |
| 5 | NHL.com and Hockey-Reference publish GAA; Hockey-Reference runs an adjusted GAA | raw/hr_goalies_2025-26_downloaded_2026-10-09.html (GAA and GAA/A 'Adjusted Goals Against Average' columns) | SUPPORTED |
| 6 | Empty-net and shootout goals not charged to the goalie | W&W calc: raw/nhl_team_summary_20252026_goalie-pages.json GA 8,086 vs raw/nhl_goalie_summary_20252026.json GA 7,578 = 508 = raw/nhl_skater_realtime_20252026.json emptyNetGoals; 0-0 shootout game 2025-11-23 in raw/nhl_goalie_games_20252026.json (0 GA charged) | SUPPORTED (computed) |
| 7 | Worked example 140 × 60 ÷ 3,000 = 2.80; 3 GA in 20 min = 9.00 (invented) | Arithmetic | SUPPORTED (computed) |
| 8 | GAA = SA/60 × (1 − SV%); Gibson 27.6 SA/60 × 9.9% = 2.72 | Identity; raw/nhl_goalie_advanced_20252026.json shotsAgainstPer60 27.56, raw/nhl_goalie_summary_20252026.json SV% .9014, GAA 2.716 | SUPPORTED (computed) |
| 9 | League goalie GAA 2.88 (7,578 GA × 3,600 ÷ 9,476,127 s); team GA 3.08 per game, gap = 508 empty-net goals | W&W calc, raw/nhl_goalie_summary_20252026.json, raw/nhl_team_summary_20252026_goalie-pages.json, raw/nhl_skater_realtime_20252026.json | SUPPORTED (computed) |
| 10 | 51 goalies 30+ GP: median 2.76; Wedgewood 2.02 best, Lankinen 3.70 worst; Gibson 2.72 22nd; Talbot 3.19 (45th); >3.00 = 18 of 51 (roughly bottom third) | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 11 | Woll .899 SV%, 3.34 GAA (48th), most SA/60 of the 51 (32.8); Ersson .870 (worst), 3.12 GAA, 23.9 SA/60 | W&W calc, raw/nhl_goalie_summary_20252026.json + raw/nhl_goalie_advanced_20252026.json | SUPPORTED (computed) |
| 12 | YoY GAA correlation 0.27 vs SV% 0.28, 35 goalies with 30+ GP both seasons | W&W calc, raw/nhl_goalie_summary_20242025.json + raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 13 | Bussi 2.47 GAA (6th) on .895 (32nd); fewest SA/60 of the 51 (23.2); CAR fewest team SA (23.9/game); at league 27.6 SA/60 his .895 → ≈2.90 | W&W calc, raw/nhl_goalie_summary_20252026.json, raw/nhl_goalie_advanced_20252026.json, raw/nhl_team_summary_20252026_goalie-pages.json; league SA/60 = 72,530 ÷ 2,632.3 h | SUPPORTED (computed) |
| 14 | Detroit 254 GA (20th-fewest per game); Gibson 144, Talbot 93, 17 empty-net; SA/GP 16th fewest | W&W calc, raw/nhl_team_summary_20252026_goalie-pages.json, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 15 | At 27.6 SA/60, ten SV% points = 0.28 goals/game ≈ 23 per full season; Gibson's 18-point edge on Talbot ≈ half a goal a game | W&W calc, raw/nhl_goalie_advanced_20252026.json, raw/nhl_goalie_summary_20252026.json (.9014 − .8833 = .0181 × 27.56 = 0.50) | SUPPORTED (computed) |
| 16 | SA/60 is the NHL's workload measure | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) SA/60 goalie | SUPPORTED |
| 17 | GA/GP includes empty-net goals | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) GA/GP | SUPPORTED |
| 18 | Talbot made 9 of 34 appearances in relief | raw/nhl_goalie_startedVsRelieved_20252026.json | SUPPORTED |
| 19 | League GAA 3.84 in 1983-84, 2.46 in 2003-04 (low since 1983-84), 2.88 in 2025-26 | W&W calc, raw/nhl_league_goalie_totals_by_season_1983-2026.json | SUPPORTED (computed) |
| 20 | Live intro: GAA, SV%, record from NHL club stats | pipeline/build_site_data.py | SUPPORTED |

## Voice metrics (`extract_prose.py goals-against-average` + `style_metrics.py --target barnwell_lean`)

| Metric | Page | Target |
|---|---|---|
| Words (running prose) | 1204 | |
| sent_mean | 19.7 | 17-21 |
| sent_sd | 10.1 | >=10 |
| pct_short_le6 | 11 | 6-15 |
| pct_long_ge30 | 18 | <=20 |
| para_words | 60 | 55-85 |
| one_sent_paras | 10 | 5-12 |
| contractions_per_k | 32.4 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 5.0 | 3-8 |
| q_per_k | 1.7 | 1-5 |
| paren_per_k | 4.2 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 52.3 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

Every metric is inside the target. ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, negation pivots or unicode artifacts; remaining hints are `uniform_paragraph_structure` and `repeated_ngrams` (fixed template + metric names).

Proposed hover short: none (the current `short` in glossary-terms.json agrees with the page).
