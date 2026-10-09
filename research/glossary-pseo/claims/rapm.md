# Claims register: rapm.json

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | RAPM is a regression estimating each player's impact on shot attempts, xG and goals, controlling for teammates, opponents, zone starts and score; reported per 60 against a league-average zero | EH RAPM glossary (targets GF/60, CF/60, xGF/60; "contribution (per 60 minutes) to the league scoring rate"); Hockey-Graphs RAPM article (predictor list) | SUPPORTED |
| 2 | A building block of public WAR models | Hockey-Graphs WAR Parts 2-3 (long-term RAPM is the SPM target); HockeyStats WAR methodology (weighted ridge regression / RAPM) | SUPPORTED |
| 3 | Plus-minus gives everyone on the ice equal credit; the site uses RAPM for the isolated-impact chart on player pages | NHL glossary plus-minus definition; src/pages/players/[slug].astro "Isolated impact" section (EH RAPM) | SUPPORTED |
| 4 | Dan Rosenbaum, 82games.com, April 2004, building on Sagarin and Winston's WINVAL | Rosenbaum, "Measuring How NBA Players Help Their Teams Win", Apr 30, 2004 | SUPPORTED |
| 5 | Joseph Sill, MIT Sloan conference, March 2010; regularization (ridge regression) nearly doubled APM's accuracy out of sample | Sill, SSAC 2010 paper ("nearly doubles its accuracy", "a.k.a. ridge regression", out-of-sample testing) | SUPPORTED |
| 6 | Macdonald's first hockey APM posted June 2010, JQAS 2011, weighted least squares on even-strength goals | arXiv 1006.4310; DOI 10.2202/1559-0410.1284 | SUPPORTED |
| 7 | Macdonald 2012: ridge regression on goals, shots, Fenwick and Corsi; estimates independent of teammates, opponents and the zone a shift begins | arXiv 1201.0317 (JQAS 8(3), Oct 2012) | SUPPORTED |
| 8 | Robert Gramacy, Matthew Taddy and Shane Jensen, regularized logistic version, 2013 | arXiv 1209.5026 (authors Robert B. Gramacy, Matthew A. Taddy, Shane T. Jensen); JQAS 9(1), 2013 | SUPPORTED |
| 9 | EH revived it at Hockey-Graphs on January 14, 2019; it sits under EH WAR's even-strength components | Hockey-Graphs RAPM article; WAR Parts 2-3 | SUPPORTED |
| 10 | The site plots EH's single-season even-strength export for every skater with 20 games | pipeline/build_player.py (rapm_ev_rates, gp ≥ 20) | SUPPORTED |
| 11 | Each stint (no substitutions) is one observation weighted by length; separate regressions per target | Hockey-Graphs RAPM article ("weights = length_shift"); EH RAPM glossary | SUPPORTED |
| 12 | 2017-18 demo: 293,009 shifts averaging 12.94 seconds, 586,018 rows | Hockey-Graphs RAPM article | SUPPORTED |
| 13 | Predictors: offense skaters, defense skaters, score state, strength state, zone-start faceoff in the stint, back-to-back, home ice | Hockey-Graphs RAPM article (full list); EH RAPM glossary (zone start = stint included a faceoff in that zone) | SUPPORTED |
| 14 | Worked example | Invented round numbers, labelled | SUPPORTED (illustrative) |
| 15 | Ridge pulls toward zero (league average), never exactly zero; strength set by cross-validation; players under ~100-150 EV minutes regressed to the mean | Hockey-Graphs RAPM article | SUPPORTED |
| 16 | Each season run separately with players split by team; multi-season versions weighted by TOI | EH GAR/RAPM glossary; Hockey-Graphs RAPM article (3-year models) | SUPPORTED |
| 17 | 2025-26 net xG impact among skaters with 20+ GP: −0.58 to +0.53; middle 80% −0.19 to +0.21 | W&W calc, EH RAPM EV export (795 skater-team rows) | SUPPORTED (computed) |
| 18 | Seider +0.53 led, ahead of Fox (+0.50) and Spence (+0.50); +0.24 offense, 0.30 fewer xGA/60 | Same file | SUPPORTED (computed) |
| 19 | Seider's 1,640 EV minutes × 0.533 ÷ 60 ≈ 14.6 expected goals | Same file | SUPPORTED (computed) |
| 20 | DeBrincat 50th (+0.26); Larkin 542nd (−0.08, below average both ends); Chiarot 774th of 795 (−0.30, xGA +0.21) | Same file | SUPPORTED (computed) |
| 21 | Only four skaters cleared +0.20 at both ends (Seider, Cozens, Kyrou, Malinski) | Same file | SUPPORTED (computed) |
| 22 | Kasper 0.93 5v5 P/60, 354th of 385 forwards (500+ min); RAPM +0.17 net, 115th; +0.12 xGF/60 | MoneyPuck 2025-26 skater file (5on5); EH RAPM export | SUPPORTED (computed) |
| 23 | EH uses long-term RAPM because single-season multicollinearity is still an issue | Hockey-Graphs WAR Part 2 | SUPPORTED |
| 24 | Goalies enter only the GF/60 regression (so xG versions carry no goalie term); shift length is not a predictor | EH RAPM glossary; predictor list | SUPPORTED |
| 25 | The model is linear and additive | Ridge regression structure (Hockey-Graphs RAPM article) | SUPPORTED |
| 26 | FAQ: Relative Corsi = on-ice minus off-ice | Natural Stat Trick glossary ("Rel - Difference between the team's stat with that player on the ice and ... off the ice") | SUPPORTED |

Computed rows: Evolving-Hockey RAPM EV export `research/rasmussen/raw/eh/rapm_ev_rates_all_seasons.csv` (downloaded 2026-09-08), 2025-26 rows whose player played 20+ games (GP from the xGAR export); MoneyPuck `raw/mp_skaters_2025.csv` (downloaded 2026-10-09).

## Voice metrics (running prose, `--target barnwell_lean`)

1,199 words. Sentence mean 19.3, SD 10.6; short 10%, long 13%; 57 words per paragraph; one-sentence paragraphs 10%; contractions 31.7/1k; I 0.0; you 4.2; questions 1.7; parentheses 5.0; intensifiers 0.8; transition openers 0%; numbers 51.7/1k; hedges 0.0. Every metric in range. ai-content-detection: no contrast frames, colon pivots or unicode artifacts; hints are uniform_paragraph_structure and repeated_ngrams.
