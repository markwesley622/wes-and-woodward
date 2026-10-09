# Claims register: individual-points-percentage.json

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | IPP = share of on-ice goals for that a player scored or assisted on; points ÷ on-ice goals for | Natural Stat Trick glossary ("the percentage of goals for that player's team while that player is on the ice that the player earned a point on. Total Points/Goals For") | SUPPORTED |
| 2 | Usually at five-on-five; NST computes it in whatever game state is filtered | NST glossary ("All player statistics are presented within the scope of the selected filters"); TSN (Yost) used 5v5 data | SUPPORTED |
| 3 | No one is credited with inventing IPP | Searches of Hockey-Graphs, Vollman, Behind the Net turned up no coiner; the earliest publisher found was stats.hockeyanalysis.com | SUPPORTED (by absence; worded as "doesn't have a famous inventor") |
| 4 | By 2015 TSN explained it; Yost: forwards ~68%, defensemen ~30%; Crosby 84.8% and Karlsson 49.4% lead career IPP in his data | Travis Yost, TSN, Aug 25, 2015 (Wayback copy) | SUPPORTED |
| 5 | Yost: IPP "regresses substantially towards league averages"; deviations from league and career norms; a GM can sell after favourable variance | Same | SUPPORTED |
| 6 | The norms "still roughly hold" | W&W calc: 2025-26 medians 65.4% (F) and 34.8% (D) vs Yost's 68% / 30% | SUPPORTED (computed) |
| 7 | Primary and secondary assists count the same in IPP | Definition (total points) | SUPPORTED |
| 8 | Worked example (26 of 40 = 65%; minus three = 57.5%, just above the bottom fifth) | Invented numbers; bottom-fifth line = 56.0% (20th percentile, 385 forwards, 2025-26) | SUPPORTED (illustrative + computed) |
| 9 | IPP tops out at 100%; 2025-26 5v5 goals carried 2.68 points (1.68 assists) with five skaters on, so the average skater's IPP ≈ 54% (53.7%) | W&W calc: 5,366 5v5 goals, 9,028 assists; on-ice GF sum = 5.0 × goals; MoneyPuck 2025-26 | SUPPORTED (computed) |
| 10 | Forwards (385, 500+ 5v5 min): median 65.4%, top 10% ≥ 76.9%; defensemen (213) median 34.8% | Same file | SUPPORTED (computed) |
| 11 | DeBrincat 45 of 59 (76.3%, 43rd); Raymond 37 of 49 (75.5%, 51st); van Riemsdyk 20 of 23 (87.0%), 3rd of 385 | Same file | SUPPORTED (computed) |
| 12 | Year-to-year IPP r = 0.21 (forwards, 324), shooting % 0.25, iCF/60 0.85; defensemen 0.36 (177) | W&W calc, MoneyPuck 2024-25 and 2025-26 files, 500+ 5v5 min in both | SUPPORTED (computed) |
| 13 | Median forward on ice for 38 5v5 goals; one goal ≈ 2.6 points of IPP; three ≈ 8 | Same file; arithmetic | SUPPORTED (computed) |
| 14 | Finnie, rookie, 20 points on 38 on-ice goals, 52.6%, 336th of 385 | Same file | SUPPORTED (computed) |
| 15 | A season far below a player's career IPP is a better bet to recover; Yost's regression-flag and trade logic | Yost, TSN 2015; r = 0.21 (row 12) | SUPPORTED |
| 16 | Seider on ice for 71 5v5 goals (most on Detroit), 24 points, 33.8%, near the 34.8% defense median | Same file | SUPPORTED (computed) |
| 17 | Copp 26 of 42 (61.9%, a little under the 65.4% median); 12 secondary assists, 4 goals; primary IPP 33% vs DeBrincat 52.5% | Same file | SUPPORTED (computed) |
| 18 | A four-goal swing on 40 goals = 10 points, close to the median-to-top-10% gap (11.5) | Arithmetic, row 10 | SUPPORTED (computed) |
| 19 | Secondary assists per 60 repeat at 0.22, primary at 0.38 (forwards, year to year) | W&W calc, MoneyPuck 2024-25 and 2025-26, 324 forwards | SUPPORTED (computed) |
| 20 | IPP only counts goals, so it pairs with expected goals; it depends on linemates' finishing | Definition | SUPPORTED |

Computed rows: `research/glossary-pseo/raw/mp_skaters_2025.csv` (MoneyPuck 2025-26, downloaded 2026-10-09) and `raw/mp_skaters_2024_repeatability.csv` (MoneyPuck 2024-25, downloaded 2026-10-09). IPP = five-on-five I_F_points ÷ OnIce_F_goals.

## Voice metrics (running prose, `--target barnwell_lean`)

1,152 words. Sentence mean 19.5, SD 10.7; short 14%, long 17%; 58 words per paragraph; one-sentence paragraphs 10%; contractions 28.6/1k; I 0.0; you 4.3; questions 1.7; parentheses 3.5; intensifiers 0.0; transition openers 0%; numbers 46.9/1k; hedges 0.0. Every metric in range; contractions were the tightest (a stat about percentages leaves few natural spots for them). ai-content-detection: no contrast frames, colon pivots or unicode artifacts; hints are repeated_ngrams.
