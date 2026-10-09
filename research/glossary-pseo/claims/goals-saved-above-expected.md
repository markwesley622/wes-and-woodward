# Claims register: goals-saved-above-expected.json

Reviewed 2026-10-09. Raw files in `research/glossary-pseo/raw/`, all downloaded 2026-10-09.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | GSAx = expected goals a goalie faced minus goals he allowed; positive = stopped more than an average goalie on the same shots | MoneyPuck glossary (GSAx: xGA − goals, "a positive number means the goalie is stopping more goals than an average goalie would"); Evolving-Hockey Standard Goalie Tables (GSAx = xGA − GA) | SUPPORTED |
| 2 | Site uses GSAx on the Team page goalie table, the team radar's goaltending axis and each goalie's player-page rating | `src/pages/team.astro` (GSAx column + 600-minute percentile note), `data/site/dashboard.json` radar "goaltending: goals saved above expected", `pipeline/build_player.py` build_goalie (0-100 rating on GSAx) | SUPPORTED |
| 3 | Gibson +11.7, Talbot −13.1 GSAx for Detroit in 2025-26 | W&W calc, xGoals − goals, `mp_goalies_2025.csv` situation=all (155.73 − 144; 79.89 − 93) | SUPPORTED (computed) |
| 4 | Ryder's 2004 *Shot Quality* (the paper that started hockey xG) called save percentage "a murky statistic" because goalies don't face the same shots; quote "to measure goaltending, it is necessary to neutralize shot quality" | Ryder PDF (`raw/ryder_shot_quality_2004_dl2026-10-09.pdf`): "Save Percentage (SV) also a murky statistic... this assumption is just plain false"; "To measure goaltending, it is necessary to neutralize shot quality." xG page row 7 for the origin | SUPPORTED |
| 5 | Ryder built a shot-quality-neutral save percentage for every team in 2002-03; Minnesota first either way; Detroit moved from eighth to seventh | Ryder PDF table "Shot Quality Neutral Save Percentage 2002-03": MIN SV rank 1, SQNSV rank 1; DET SV rank 8, SQNSV rank 7 | SUPPORTED |
| 6 | Eight years later (2012) Macdonald, Lennon and Sturdivant priced shots with a regression model and subtracted goals allowed from expected goals against; quote "the number of goals that a goalie saved above what is expected" | arXiv 1205.1746 v1 (8 May 2012), §5 text and Table 4 (`raw/macdonald_lennon_sturdivant_2012_weighted_shots_arxiv1205.1746.pdf`): "logistic regression model"; quote verbatim | SUPPORTED |
| 7 | Tim Thomas led 2010-11, 103 goals allowed on 145 expected | arXiv 1205.1746 Table 4, "top 5 goalies in goals prevented in 2010-2011": Thomas ExpGA 145, GA 103, DiffGA 42, first row | SUPPORTED |
| 8 | MoneyPuck and Evolving-Hockey publish GSAx, each as xGA − GA on its own xG model | MoneyPuck glossary; Evolving-Hockey glossary; each site's own model write-up (xG page rows 10-11, 29) | SUPPORTED |
| 9 | NHL.com's Seattle Kraken analytics column explained GSAx for fans in 2021 | Alison Lukan, "Analytics with Alison: Sizing up Goaltending," NHL.com, Oct 28, 2021 | SUPPORTED |
| 10 | MoneyPuck prices every unblocked attempt a goalie faces and sums them into xGA; inputs location, shot type, play before, skaters on ice | MoneyPuck glossary ("Expected Goals Against: the sum of all expected goals from the unblocked shot attempts taken on the goalie"); MoneyPuck about (inputs; xG page row 15) | SUPPORTED |
| 11 | Worked example (30 attempts: 20 × 0.03 + 8 × 0.15 + 2 × 0.40 = 2.6; two goals = +0.6; 30 × 0.03 = 0.9, two goals = −1.1) | Arithmetic, labelled invented | SUPPORTED |
| 12 | Misses count on the expected side; xG is the chance an unblocked attempt becomes a goal, so each value includes the odds it misses | MoneyPuck glossary (xGoals = "the chance of an unblocked shot attempt being a goal"; Fenwick = shots on goal plus misses) | SUPPORTED |
| 13 | Blocked attempts aren't counted; empty-net goals go against the team, never a goalie | MoneyPuck glossary ("blocked attempts valued at 0 xGoals"); goalie file sums vs team file (DET goalies 237 GA, team 254 in MoneyPuck's team file; the 17 difference are empty-net goals); GAA page row on empty nets | SUPPORTED |
| 14 | Variants: dFSv% = FSv% − xFSv% = GSAx ÷ unblocked attempts; MoneyPuck "Save % Above Expected" = SV% − expected SV%; GSAA prices every shot at league SV%; team GSAx includes empty nets | Evolving-Hockey Standard Goalie Tables (FSv%, xFSv%, dFSv% formulas; algebra); MoneyPuck glossary; NST/Vollman GSAA definition; `pipeline/build_site_data.py` gsax tile = team xGoalsAgainst − goalsAgainst | SUPPORTED |
| 15 | League total not zero: 98 goalies allowed 7,575 on 7,646.4 expected (+71.4) | W&W calc, `mp_goalies_2025.csv` all situations | SUPPORTED (computed) |
| 16 | Median among 51 goalies with 30+ GP +4.2; median of all 98 −1.0 | W&W calc (4.23; −0.98) | SUPPORTED (computed) |
| 17 | Thompson led at +29.3 (WSH); Swayman +28.8 and Sorokin +25.3 close behind; top five all above +23; Binnington last at −22.4 (30+ GP pool) | W&W calc, 30+ GP pool of 51 | SUPPORTED (computed) |
| 18 | Gibson 12th of 51 (top quarter); Talbot 47th | W&W calc (12/51 = 23.5%) | SUPPORTED (computed) |
| 19 | Gibson + Talbot net −1.4; team figure −1.6, 21st; −0.8 at five-on-five | W&W calc: 11.73 − 13.11 = −1.38; `mp_teams_2025.csv` DET all 252.38 − 254 = −1.62 (21st of 32); 5on5 169.16 − 170 = −0.84 (matches xG page row 20) | SUPPORTED (computed) |
| 20 | 39 goalies with 1,500+ minutes in both 2024-25 and 2025-26; year-to-year correlation of GSAx per unblocked attempt 0.21 | W&W calc, Pearson, `mp_goalies_2025.csv` + `mp_goalies_2024_for_gsax_repeatability_dl2026-10-09.csv` | SUPPORTED (computed) |
| 21 | Talbot +12.8 in 47 games for Detroit in 2024-25 | `mp_goalies_2024_for_gsax_repeatability_dl2026-10-09.csv` (team DET, GP 47, xGoals − goals) | SUPPORTED (computed) |
| 22 | Site's goalie ratings trust a season's GSAx halfway at 1,500 minutes | `pipeline/build_player.py`: `rel = mins / (mins + 1500)`, comment "half-trust at 1,500 minutes" | SUPPORTED |
| 23 | Talbot's unblocked attempts averaged 0.047 xG, Gibson's 0.048; Gibson 144 on 155.7, Talbot 93 on 79.9 | W&W calc (79.89/1,716; 155.73/3,217) | SUPPORTED (computed) |
| 24 | Wedgewood led regulars in SV% at .921 and was fifth in GSAx; Colorado gave him one of the gentler shot mixes (10th-gentlest xFSv% of 51) | NHL stats API goalie summary (.9213, best among 30+ GP; save-percentage page agrees); W&W calc on MoneyPuck file (GSAx rank 5; xFSv% rank 10) | SUPPORTED (computed) |
| 25 | Thompson's .912 trailed Wedgewood's; he faced 1,100+ more unblocked attempts and harder ones (xFSv% .9511 vs .9527); finished first | NHL API (.9118); MoneyPuck file (3,461 vs 2,307 attempts) | SUPPORTED (computed) |
| 26 | Team page shows GSAx and a percentile among 600+ minute goalies; player page 0-100 rating where 50 is the average 600-minute goalie, band tightens with minutes | `src/pages/team.astro` note; `pipeline/build_site_data.py` MIN_GOALIE_SECONDS pool; `pipeline/build_player.py` method string and se/rel band | SUPPORTED |
| 27 | Public models don't see pre-shot passes; neither MoneyPuck's nor EH's published inputs include screens or goalie position | Evolving-Hockey xG write-up; MoneyPuck about (xG page rows 25, 28) | SUPPORTED |
| 28 | r = 0.21 explains about 4% of the spread; Talbot's swing of almost 26 goals came with the same team | 0.21² = 0.044; 12.8 − (−13.1) = 25.9; DET both seasons | SUPPORTED (computed) |
| 29 | A rebound a goalie allows becomes another shot against him and adds to his xGA; MoneyPuck publishes a flurry-adjusted version giving less credit to rebound chances | MoneyPuck glossary ("Flurry Adjusted: gives teams less credit for rebound shot opportunities than initial shots"; xGA = sum over unblocked attempts on the goalie) | SUPPORTED |
| 30 | MoneyPuck and EH train different models; this page uses MoneyPuck's 2025-26 file as published at review | Each site's methodology; download date | SUPPORTED |
| 31 | FAQ: MoneyPuck publishes separate regular-season and playoff files; page uses regular season | MoneyPuck data URLs `seasonSummary/2025/regular/goalies.csv` and `.../2025/playoffs/goalies.csv` (both HTTP 200, 2026-10-09) | SUPPORTED |
| 32 | Live intro: rebuilt nightly from MoneyPuck and the NHL's club stats | `pipeline/build_site_data.py` build_goalies (NHL club_stats + MoneyPuck goalies.csv) | SUPPORTED |

## Voice metrics (`style_metrics.py --target barnwell_lean`, running prose, 1,240 words)

| Metric | Value | Target |
|---|---|---|
| Sentence mean / SD | 20.0 / 10.7 | 17-21 / ≥ 10 |
| Short / long sentences | 6% / 19% | 6-15% / ≤ 20% |
| Words per paragraph | 62 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 41.1 | ≥ 28 |
| I / you per 1k | 0.0 / 4.0 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.6 / 3.2 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 50.8 | 30-55 |

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, unicode artifacts, question fragments or false ranges. Remaining hints `uniform_paragraph_structure` and `repeated_ngrams` (metric names) come from the template.

Hover short in `glossary-terms.json` agrees with the page; no change proposed.
