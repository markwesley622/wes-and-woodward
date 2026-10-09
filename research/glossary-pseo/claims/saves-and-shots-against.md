# Claims register: saves-and-shots-against.json

Reviewed 2026-10-09. All NHL API files downloaded 2026-10-09 to `research/glossary-pseo/raw/`. "W&W calc" = computed by the writer from the named file.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | SA = shots on goal faced, GA = goals in, SV = the rest; SA − GA = SV; SV% = SV/SA | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) SA, Sv, Sv%; Hockey-Reference glossary (hockey-reference.com/about/glossary.html) SV | SUPPORTED |
| 2 | League goalies faced 72,530 SA in 2025-26, 27.6 per team game (÷ 2,624) | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 3 | Save leader is usually the busiest goalie (Saros 1,519 saves on 1,700 SA, .894, 35th of 51) | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 4 | Team SA officially tracked since 1955-56; SV% starts same season | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) SA, Sv% | SUPPORTED |
| 5 | NHL.com and Hockey-Reference print SV% beside SA/SV/GA | raw/hr_goalies_2025-26_downloaded_2026-10-09.html; raw/nhl_goalie_summary_20252026.json | SUPPORTED |
| 6 | Shots logged rink by rink via the Real Time Scoring System | Schuckers & Macdonald, arXiv 1412.1035 (data 2007-08 to 2012-13) | SUPPORTED |
| 7 | Blocked/missed excluded; post or crossbar = missed shot; 2,137 posts and 691 crossbars in 2025-26 | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json); W&W calc raw/nhl_skater_realtime_20252026.json | SUPPORTED (computed) |
| 8 | NHL.com splits SA/saves by strength since 1997-98 | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) EV SA, PP SA, SH SA | SUPPORTED |
| 9 | MoneyPuck logs every unblocked attempt (151,555 against goalies) and builds xG on them; its SOG tally 72,520 within 10 of the NHL's 72,530 | W&W calc, raw/mp_goalies_2025.csv (unblocked_shot_attempts, ongoal) | SUPPORTED (computed) |
| 10 | Worked example (invented): 29/32 = .906 | Arithmetic | SUPPORTED (computed) |
| 11 | Gibson 1,461 SA, 144 GA, 1,317 SV | raw/nhl_goalie_summary_20252026.json | SUPPORTED |
| 12 | 8,086 team GA vs 7,578 goalie GA = 508 empty-net goals; shootout attempts separate columns, never in SA/SV/GA | W&W calc, raw/nhl_team_summary_20252026_goalie-pages.json, raw/nhl_goalie_summary_20252026.json, raw/nhl_skater_realtime_20252026.json; NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) S/O SA, S/O Saves; raw/nhl_goalie_games_20252026.json 2025-11-23 | SUPPORTED (computed) |
| 13 | 64,976 saves; median start 24 saves; 40+ saves in 39 of 2,624 starts | W&W calc, raw/nhl_goalie_games_20252026.json | SUPPORTED (computed) |
| 14 | Woll most SA/60 (32.8), Bussi fewest (23.2) among 51 with 30+ GP, gap nearly ten | W&W calc, raw/nhl_goalie_advanced_20252026.json | SUPPORTED (computed) |
| 15 | Detroit goalies 2,258 SA, 27.5/game, 15th-lowest of 32; 2,021 saves; Gibson 27.6 SA/60 = league average (27.55) | W&W calc, raw/nhl_goalie_games_20252026.json by team; raw/nhl_goalie_advanced_20252026.json | SUPPORTED (computed) |
| 16 | Merzlikins 48 saves on 52, CBJ vs MIN, Oct 11 2025; four others reached 46 (Tarasov 47 for FLA in March); nobody did it twice | raw/nhl_goalie_games_20252026.json | SUPPORTED |
| 17 | At .896 an average goalie stops ≈1,309 of Gibson's 1,461; Gibson +8.2 | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 18 | CAR goalies 23.8 SA/game fewest, TOR 32.2 most | W&W calc, raw/nhl_goalie_games_20252026.json by team ÷ 82 (2025-26) | SUPPORTED (computed) |
| 19 | 14.9% of SA came shorthanded; PP SV% .853 vs EV .903; Gibson 13.8% | W&W calc, raw/nhl_goalie_savesByStrength_20252026.json | SUPPORTED (computed) |
| 20 | Schuckers & Macdonald: shots most consistently recorded; FLA and STL rinks off | Schuckers & Macdonald, arXiv 1412.1035 (data 2007-08 to 2012-13) | SUPPORTED |
| 21 | More than half of MoneyPuck's 151,555 unblocked attempts missed the net (79,035) | W&W calc, raw/mp_goalies_2025.csv | SUPPORTED (computed) |
| 22 | SA/60 is the NHL's workload measure | NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) SA/60 goalie | SUPPORTED |

## Voice metrics (`extract_prose.py saves-and-shots-against` + `style_metrics.py --target barnwell_lean`)

| Metric | Page | Target |
|---|---|---|
| Words (running prose) | 1069 | |
| sent_mean | 18.8 | 17-21 |
| sent_sd | 10.9 | >=10 |
| pct_short_le6 | 12 | 6-15 |
| pct_long_ge30 | 19 | <=20 |
| para_words | 56 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 42.1 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 5.6 | 3-8 |
| q_per_k | 1.9 | 1-5 |
| paren_per_k | 5.6 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 54.3 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

Every metric is inside the target. ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, negation pivots or unicode artifacts; remaining hints are `uniform_paragraph_structure` and `repeated_ngrams` (fixed template + metric names).

Live slot omitted: the pipeline's goalies.json doesn't carry shotsAgainst, saves or goalsAgainst yet.

Proposed hover short: none (the current `short` in glossary-terms.json agrees with the page).
