# Claims register: per-60-rates.json

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | A per-60 rate divides a count by ice time and scales it to 60 minutes; written /60 | Natural Stat Trick glossary ("/60 - Rate per 60 minutes of play. Stat*60/TOI"); MoneyPuck glossary | SUPPORTED |
| 2 | Larkin outscored Kane by ten points (67 to 57) but Kane produced more per minute at 5v5 (2.00 vs 1.41 P/60) | W&W calc, MoneyPuck 2025-26 skater file (all and 5on5) | SUPPORTED (computed) |
| 3 | GAA = goals allowed × 60 ÷ minutes; NHL glossary carries it back to 1917-18, the league's first season | NHL stats glossary API (GAA, firstSeasonForStat 19171918) | SUPPORTED |
| 4 | Skater ice-time records start in 1997-98 | NHL stats glossary (TOI firstSeasonForStat 19971998; "EV TOI is available since 1997-98", "PP TOI is available since 1997-98") | SUPPORTED |
| 5 | NHL glossary: points per game "does not account for varying time on ice and varying special teams time" | NHL stats glossary (P/GP) | SUPPORTED |
| 6 | By the end of the 2000s writers cited Gabe Desjardins' Behind the Net for even-strength scoring adjusted for ice time; two years later the Globe and Mail quoted its rate stats | Canucks Army (Jonathan Willis), Apr 8, 2009; Globe and Mail (James Mirtle), Apr 13, 2011 ("EVGA per 60 minutes" from Behind the Net) | SUPPORTED |
| 7 | NHL.com runs a Scoring per 60 report at 5v5 with data back to 2009-10 | NHL.com stats report "Scoring per 60 (5v5, since 2009-10)"; glossary P/60 (5-on-5) firstSeasonForStat 20092010 | SUPPORTED |
| 8 | NST defines rates the same way; MoneyPuck explains with 2 goals in 120 minutes = 1 per 60 | NST glossary; MoneyPuck glossary | SUPPORTED |
| 9 | NHL.com's analytics primer calls per 60 the most common rate scale in hockey | NHL.com, Alison Lukan, Sep 6, 2022 | SUPPORTED |
| 10 | Forwards score at more than 2.5× their 5v5 pace on the power play (4.37 vs 1.63 P/60, pooled) | W&W calc, MoneyPuck 2025-26 skater file, all forwards pooled by situation | SUPPORTED (computed) |
| 11 | Worked example | Invented round numbers, labelled | SUPPORTED (illustrative) |
| 12 | MoneyPuck files and the NHL stats API report ice time in seconds | MoneyPuck `icetime` column; NHL API avgTimeOnIcePerGame (data/site/skaters.json toiPerGame 1234.7 s) | SUPPORTED |
| 13 | Forwards with 60+ GP: busiest averaged 23.0 min/night, lightest 7.2 (all situations) | W&W calc, MoneyPuck 2025-26, 327 forwards | SUPPORTED (computed) |
| 14 | Median forward (500+ 5v5 min, 385) 1.60 P/60; top 10% ≥ 2.31; defensemen median 0.83 (213) | W&W calc, MoneyPuck 2025-26 5on5 | SUPPORTED (computed) |
| 15 | DeBrincat 2.31, 39th of 385; Kane 2.00 and Raymond 1.94 (both > 1.9); Larkin 1.41 | Same | SUPPORTED (computed) |
| 16 | Year-to-year (324 forwards, 500+ 5v5 min both seasons): iCF/60 0.85, ixG/60 0.65, P/60 0.53, G/60 0.42 | W&W calc, MoneyPuck 2024-25 and 2025-26 skater files | SUPPORTED (computed) |
| 17 | Larkin 67 points, third on the team; 25 at 5v5, 255th of 385 (bottom half); 42 in other states | Same file (DeBrincat 85, Raymond 76, Larkin 67) | SUPPORTED (computed) |
| 18 | van Riemsdyk 1.74 P/60 in 690 5v5 minutes, under two-thirds of Larkin's 1,065 | Same file | SUPPORTED (computed) |
| 19 | Seider 25 of 60 points at 5on4 in 254 minutes, about a sixth of his 1,612 5v5 minutes | Same file | SUPPORTED (computed) |
| 20 | Kevin Rooney (UTA) one 5v5 point in 9.7 minutes = 6.16 P/60, ~70% above Kucherov's 3.64 (top among 500+ min forwards) | Same file | SUPPORTED (computed) |
| 21 | NST lets users set a minimum TOI | NST glossary ("Min TOI - Set a minimum amount of ice time...") | SUPPORTED |
| 22 | Site percentiles need 300 5v5 minutes for a skater | pipeline/build_site_data.py MIN_SKATER_5V5_SECONDS = 300 × 60 | SUPPORTED |
| 23 | At 300 minutes one point = 0.20 per 60, an eighth of the 1.60 median | Arithmetic (60/300; 0.20/1.60) | SUPPORTED (computed) |
| 24 | EH RAPM controls for teammates, opponents and zone starts and reports impact per 60 | EH RAPM glossary; Hockey-Graphs RAPM article | SUPPORTED |
| 25 | Live tiles pp_xgf60 and pk_xga60; leaders on fiveOnFive.ixgPer60 | src/lib/glossary.js, data/site/dashboard.json, data/site/skaters.json | SUPPORTED |

Computed rows: `research/glossary-pseo/raw/mp_skaters_2025.csv` (MoneyPuck 2025-26, downloaded 2026-10-09) and `raw/mp_skaters_2024_repeatability.csv` (MoneyPuck 2024-25, downloaded 2026-10-09 for this page family).

## Voice metrics (running prose, `--target barnwell_lean`)

1,096 words. Sentence mean 18.3, SD 10.6; short 12%, long 15%; 58 words per paragraph; one-sentence paragraphs 11%; contractions 40.1/1k; I 0.0; you 6.4; questions 1.8; parentheses 3.6; intensifiers 0.9; transition openers 0%; numbers 54.7/1k; hedges 0.0. Every metric in range. Numbers per 1k was the hard one: the stat's own name is a number, so every "per 60" counts, and the first drafts ran 87-107/1k. ai-content-detection: no contrast frames, colon pivots or unicode artifacts; hints are uniform_paragraph_structure and repeated_ngrams.
