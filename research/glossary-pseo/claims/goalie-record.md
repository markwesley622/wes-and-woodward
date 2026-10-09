# Claims register: goalie-record.json

Reviewed 2026-10-09. All NHL API files downloaded 2026-10-09 to `research/glossary-pseo/raw/`. "W&W calc" = computed by the writer from the named file.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Record = W, regulation L, OT/SO losses; decision to the goalie of record when the deciding goal is scored | Hockey-Reference glossary (hockey-reference.com/about/glossary.html) W, L, OL; Sports Illustrated 2011-12-08 ('goalie of record when the winning goal was scored') | SUPPORTED |
| 2 | OTL worth one standings point to a win's two (since 2005-06); ties before 2005-06 | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) 'P (Standings)' | SUPPORTED |
| 3 | Kuemper led with 15 OTL (LAK) | raw/nhl_goalie_summary_20252026.json | SUPPORTED |
| 4 | NHL glossary carries goalie W and L (and ties) to 1917-18 | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) GS W, GS L, GS T first season 19171918 | SUPPORTED |
| 5 | Shootout arrived 2005-06 | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) S/O Win, SO G first season 20052006 | SUPPORTED |
| 6 | Before the OTL column an OT loss was a plain L in NHL goalie stats; 2003-04 goalies W = L (1,060 each) with 340 ties; OTL column starts 2005-06 | W&W calc, raw/nhl_goalie_summary_20032004.json, raw/nhl_goalie_summary_19992000.json, raw/nhl_goalie_summary_20052006.json | SUPPORTED (computed) |
| 7 | Hockey-Reference's T/O = ties plus OT/SO losses; OL = OT/SO losses | Hockey-Reference glossary (hockey-reference.com/about/glossary.html); raw/hr_goalies_2025-26_downloaded_2026-10-09.html column tip | SUPPORTED |
| 8 | Brodeur 691 career wins; season record 48 shared by Brodeur (2006-07) and Holtby (2015-16) | raw/nhl_goalie_records_career_wins_top10_2026-10-09.json; raw/nhl_goalie_records_season_wins_top10_2026-10-09.json | SUPPORTED |
| 9 | Detroit franchise: Sawchuk 350 wins, Osgood 317, nobody else 250+ (Howard 246) | raw/nhl_goalie_records_det_franchise_career_wins_2026-10-09.json | SUPPORTED |
| 10 | GWG = goal that gives the winner one more than the loser's final total, whenever scored | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) GWG | SUPPORTED |
| 11 | Worked example (invented): 4-3 comeback, 4th goal is GWG, backup in net gets W, starter no decision | Applies the GWG rule above | SUPPORTED |
| 12 | Talbot won in relief of Gibson vs ANA (Nov 13) and NSH (Mar 2); Gibson 57 GP, 55 decisions | raw/nhl_goalie_games_20252026.json | SUPPORTED |
| 13 | Murphy, Dec 2011: loss vs Calgary without allowing a goal; came on in relief, pulled for extra attacker, goalie of record for Iginla's empty-net GWG; 7-6 | Sports Illustrated, 2011-12-08 | SUPPORTED |
| 14 | League goalies 1,312 W, 986 L, 326 OTL = team totals | W&W calc, raw/nhl_goalie_summary_20252026.json vs raw/nhl_team_summary_20252026_goalie-pages.json | SUPPORTED (computed) |
| 15 | Vasilevskiy led with 39 W; Gibson 29-22-4, Talbot 12-9-6 (team 41-31-10); Talbot .883 near bottom of 51 regulars | raw/nhl_goalie_summary_20252026.json; raw/nhl_team_summary_20252026_goalie-pages.json | SUPPORTED |
| 16 | Bussi 31-6-2 .895; Hellebuyck 23-23-11 .895; GF/60 3.63 vs 2.65; Bussi ≈4 fewer SA/60 (23.2 vs 27.3) | raw/nhl_goalie_summary_20252026.json; raw/nhl_goalie_advanced_20252026.json (goalsForAverage, shotsAgainstPer60) | SUPPORTED (computed) |
| 17 | Hellebuyck 2024-25: 47 W, .925; win total −24, SV% −30 points; goal support thinned (3.38 → 2.65 GF/60) | raw/nhl_goalie_summary_20242025.json; raw/nhl_goalie_advanced_20242025.json; raw/nhl_goalie_advanced_20252026.json | SUPPORTED (computed) |
| 18 | Gibson 57 starts, 48 complete; Talbot 9 relief + 25 starts; 2 of Talbot's 12 W in relief; Gibson's W in the Mar 8 combined shutout after leaving hurt in the 2nd | raw/nhl_goalie_advanced_20252026.json (completeGames); raw/nhl_goalie_startedVsRelieved_20252026.json; raw/nhl_goalie_games_20252026.json; AP recap via CBS Sports, 2026-03-08 (cbssports.com/nhl/gametracker/recap/NHL_20260308_DET@NJ) | SUPPORTED |
| 19 | Knight and Hellebuyck 11 OTL each; Detroit 10 OTL of 92 points | raw/nhl_goalie_summary_20252026.json; raw/nhl_team_summary_20252026_goalie-pages.json | SUPPORTED |
| 20 | NHL publishes ROL = regulation + OT losses (no shootouts) | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) ROL | SUPPORTED |
| 21 | NHL publishes GF while goalie on ice, akin to run support; Gibson 2.85, Talbot 2.81 GF/60; win share 53% vs 44% | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) GF (goalie); raw/nhl_goalie_advanced_20252026.json; W ÷ decisions | SUPPORTED (computed) |
| 22 | Gibson 40 min vs ANA (Nov) no decision; ~31 min vs PHI (Apr 9) win | raw/nhl_goalie_games_20252026.json (TOI 40.0 / 30.7) | SUPPORTED |
| 23 | Regular-season OT is 3-on-3 (since 2015-16) | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) OTG / OT TOI notes | SUPPORTED |
| 24 | Live tiles: team record and points; two per win, one per OT loss | pipeline team.json record; NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) P (Standings) | SUPPORTED |

## Voice metrics (`extract_prose.py goalie-record` + `style_metrics.py --target barnwell_lean`)

| Metric | Page | Target |
|---|---|---|
| Words (running prose) | 1138 | |
| sent_mean | 19.6 | 17-21 |
| sent_sd | 10.8 | >=10 |
| pct_short_le6 | 10 | 6-15 |
| pct_long_ge30 | 17 | <=20 |
| para_words | 60 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 35.1 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 3.5 | 3-8 |
| q_per_k | 1.8 | 1-5 |
| paren_per_k | 4.4 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 53.6 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

Every metric is inside the target. ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, negation pivots or unicode artifacts; remaining hints are `uniform_paragraph_structure` and `repeated_ngrams` (fixed template + metric names).

Proposed hover short: none (the current `short` in glossary-terms.json agrees with the page).
