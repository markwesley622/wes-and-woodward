# Claims register: score-adjusted-stats.json

Reviewed 2026-10-09. Score-state rows use MoneyPuck shot-by-shot files for 2018-19 through 2025-26
(`research/rasmussen/raw/mp/shots_2018.csv` … `shots_2025.csv`, downloaded 2026-09-08): regular season, five-on-five
(5 skaters each side), both goalies in, score before the shot (verified: the first goal of a game carries 0-0),
capped at ±3. Team and player raw-versus-adjusted rows use `research/glossary-pseo/raw/mp_teams_2025.csv` and
`mp_skaters_2025.csv` (downloaded 2026-10-09). McCurdy's article saved as
`raw/hockeyviz_mccurdy_score_adjusted_fenwick_2014_dl20261009.html`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Score-adjusted stats reweight attempts and xG for the score; trailing teams push, leading teams sit back; unadjusted, leaders look worse and trailers better | MoneyPuck glossary ("leading 'sit back' but aren't actually playing poorly"; more credit to teams with big leads); Evolving-Hockey General Terms (leading teams play more defensively, trailing teams press) | SUPPORTED |
| 2 | Teams with a lead took under half of 5v5 unblocked attempts in each of the last eight seasons (44.6% to 48.9%) | W&W calc by season 2018-19…2025-26: 44.9, 45.4, 48.8, 46.8, 48.9, 47.2, 44.6, 46.3 | SUPPORTED (computed) |
| 3 | McCurdy: "Teams that are losing get more of the puck" | HockeyViz, "Better Way to Compute Score-Adjusted Fenwick" (originally senstats.ca, October 2014), verbatim | SUPPORTED |
| 4 | Score close, pioneered by Tore Purdy (JLikens): within a goal in periods 1-2, tied in the 3rd | War-on-Ice Annotated Glossary; McCurdy 2014 | SUPPORTED |
| 5 | Tulsky's January 2012 Broad Street Hockey piece kept every event and weighted by score state using time in each state | McCurdy 2014 (formula, minutes-per-state weights, "2012 article at Broad Street Hockey"); War-on-Ice glossary link dated 2012/1/23 | SUPPORTED |
| 6 | McCurdy's version published October 2014; used by NST and Evolving-Hockey | HockeyViz header; NST glossary ("using the method created by Micah Blake McCurdy"); EH Score Adjustments page | SUPPORTED |
| 7 | It dropped time weights, split home and away, capped at three goals | McCurdy 2014 | SUPPORTED |
| 8 | Split 40-game samples: halves matched with R² 0.530 (McCurdy), 0.488 (Tulsky), 0.428 (score close); his version best at predicting goals and wins; score close last on every test | McCurdy 2014 tables (goal % 0.113/0.108/0.0857; win % 0.0559/0.0483/0.0388; 5-game test 0.330/0.249/0.242) | SUPPORTED |
| 9 | War-on-Ice built its own score/period/rink model; MoneyPuck publishes score-adjusted shot attempts and score- and venue-adjusted xG; glossary goal = more credit to away teams and big leads | War-on-Ice glossary; MoneyPuck file columns (scoreAdjustedShotsAttemptsFor, scoreVenueAdjustedxGoalsFor); MoneyPuck glossary | SUPPORTED |
| 10 | Method needs only event counts; weight × team's events = average of both teams' events | McCurdy 2014 ("no need for any measurement of times"; coefficient rule verbatim) | SUPPORTED |
| 11 | Separate weights by game state and event type (Corsi, Fenwick, shots, goals, xG) | Evolving-Hockey Score Adjustments page | SUPPORTED |
| 12 | Worked example (invented): 1,000 vs 1,100 → weights 1.05 and 0.95 | Labelled invented; arithmetic | SUPPORTED |
| 13 | 2025-26, home team up one at 5v5: home 7,736 unblocked attempts, visitors 8,497 → weights 1.049 and 0.955; McCurdy's 2007-2014 weights 1.026 and 0.975 | W&W calc shots_2025.csv; McCurdy 2014 table | SUPPORTED (computed) |
| 14 | Home teams take a bigger share than visitors in the same score state | W&W calc 2025-26 (home lead +1 47.7% vs away lead +1 46.5%; tied 51.4%; etc.) | SUPPORTED (computed) |
| 15 | MoneyPuck's fully adjusted xG also discounts rebound flurries | MoneyPuck glossary "Flurry Adjusted"; file column flurryScoreVenueAdjustedxGoalsFor | SUPPORTED |
| 16 | 2025-26 5v5: leader by one 47.1%, by two 45.8%, by three+ 44.7%; tied, home 51.4% | W&W calc shots_2025.csv | SUPPORTED (computed) |
| 17 | Team 5v5 CF%: adjustment moved the average team 0.44 points, max 1.25; raw vs adjusted r = 0.99; Colorado 56.7 → 57.9 (largest gain), Vancouver 46.5 → 45.2 (largest drop) | W&W calc shotAttempts vs scoreAdjustedShotsAttempts, teams file | SUPPORTED (computed) |
| 18 | Detroit CF% 48.8% raw (21st) → 48.6% adjusted (23rd); xGF% 48.8% → 48.6% | W&W calc (48.81 → 48.56; xG 48.79 → 48.65 score-and-venue adjusted) | SUPPORTED (computed) |
| 19 | Sandin-Pellikka on-ice CF% 50.2% → 49.6%, largest drop among Wings with 900 5v5 min | W&W calc OnIce_F/A_shotAttempts vs scoreAdjusted, skaters file | SUPPORTED (computed) |
| 20 | Gain grows as sample shrinks (5-game test: 0.330 vs 0.249 vs 0.242) | McCurdy 2014 ("greater predictivity at all sample sizes, especially smaller sample sizes") | SUPPORTED |
| 21 | Team page shows Detroit's xG share raw and adjusted every night | `src/pages/team.astro` renders all `dashboard.tiles`, incl. xg_share_5v5 and xg_share_5v5_adj | SUPPORTED |
| 22 | Four biggest gainers included Carolina and Colorado (1st and 2nd in raw CF%); biggest losers included Vancouver and Toronto (29th and 32nd) | W&W calc | SUPPORTED (computed) |
| 23 | 598 skaters with 500 5v5 min: mean change 0.46 points; biggest drop Noah Juulsen (PHI) 45.3 → 43.7 | W&W calc skaters file | SUPPORTED (computed) |
| 24 | EH score-adjusts every on-ice and relative number | Evolving-Hockey Score Adjustments ("All on-ice and relative to teammate metrics ... are score adjusted") | SUPPORTED |
| 25 | Limits: league-average weights; sites use different weights; older work used score close; adjustment leaves shooting/save luck | Rows 6, 9, 4, 8; definition | SUPPORTED |
| 26 | FAQ: EH weights for 5v5, 4v4, 3v3 and special teams; NST's adjusted filter is 5v5 only | EH Score Adjustments page; NST glossary ("5v5 Score & Venue Adjusted") | SUPPORTED |
| 27 | Live tiles: dashboard keys xg_share_5v5 and xg_share_5v5_adj (flurry, score and venue adjusted) and team.json situations.5on5.corsiPct | `pipeline/build_site_data.py` adj_share (flurryScoreVenueAdjusted); `data/site/team.json` | SUPPORTED |

Cut: that most sites use McCurdy's method (only NST and EH confirmed); that the effect "points the same way every
season" (one season of team reorders checked).

## Voice metrics

Running prose: 1180 words (extract_prose.py → style_metrics.py --target barnwell_lean).

| Metric | Page | Target |
|---|---|---|
| sent_mean | 19.7 | 17-21 |
| sent_sd | 10.3 | >=10 |
| pct_short_le6 | 10 | 6-15 |
| pct_long_ge30 | 18 | <=20 |
| para_words | 56 | 55-85 |
| one_sent_paras | 10 | 5-12 |
| contractions_per_k | 29.7 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 4.2 | 3-8 |
| q_per_k | 1.7 | 1-5 |
| paren_per_k | 4.2 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 47.5 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

ai-content-detection analyze_text.py: unicode artifacts 0, em dashes 0, contrast frames 0, payoff colons 0, question fragments 0, sentence-negation flags 0. Remaining n-gram hints are metric names ("five on five", "on the ice").

Hover short: the current `short` agrees with the page. No change proposed.
