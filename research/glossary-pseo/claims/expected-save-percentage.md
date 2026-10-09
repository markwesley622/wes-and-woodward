# Claims register: expected-save-percentage.json

Reviewed 2026-10-09. Raw files in `research/glossary-pseo/raw/`, all downloaded 2026-10-09.

Definition check (brief asked to verify xSV%/dSV%): Evolving-Hockey defines xFSv% = 1 − xGA/FA, FSv% = 1 − GA/FA, dFSv% = FSv% − xFSv% (Standard Goalie Tables). MoneyPuck defines Expected Save Percentage as "the save percentage an average NHL goalie would have based on the quality of the shots the goalie has faced" and "Save % Above Expected" as actual minus expected (glossary; it doesn't state the denominator, so the page doesn't attribute a formula to MoneyPuck). Macdonald, Lennon and Sturdivant (2012) define ExpSv% = 1 − EGA/ShotA on shots on goal. Natural Stat Trick's archived goalie glossary (January 2025) lists no expected save percentage, so the page doesn't attribute one to NST.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | xSV% = the save percentage an average goalie would post on the shots a goalie faced, built from expected goals; real minus expected = dSV%; it's GSAx as a rate | MoneyPuck glossary (Expected Save Percentage; Save % Above Expected); Evolving-Hockey (dFSv% = FSv% − xFSv% = GSAx ÷ FA by algebra) | SUPPORTED |
| 2 | Talbot faced one of the gentlest shot mixes and finished near the bottom | W&W calc, `mp_goalies_2025.csv`: xFSv% rank 6 of 51 (gentlest = highest), dFSv% rank 49 of 51 | SUPPORTED (computed) |
| 3 | Ryder's 2004 paper estimated each team's shot quality against and backed out a shot-quality-neutral save percentage; quote "the save percentage one would expect with no variation in shot quality from team to team" | Ryder PDF (`raw/ryder_shot_quality_2004_dl2026-10-09.pdf`), quote verbatim | SUPPORTED |
| 4 | His 2002-03 table lifted Florida's goaltending (basically Roberto Luongo, Ryder noted) seven places, into second | Ryder PDF: "Florida's goaltending, basically Roberto Luongo, jumps 7 positions into second place"; table FLA SV rank 9, SQNSV rank 2 | SUPPORTED |
| 5 | Macdonald, Lennon and Sturdivant (2012): ExpSv% = 1 − expected goals against ÷ shots against; adjusted SV% = league average plus (Sv% − ExpSv%) | arXiv 1205.1746, §5 ("ExpSv% = 1 − EGA/ShotA"; "By adjusted save percentage we mean the league average save percentage plus DiffSv%, the difference in Sv% and ExpSv%") | SUPPORTED |
| 6 | Tim Thomas .940 in 2010-11 on shots that called for .915 | arXiv 1205.1746 Table 4 (Sv% .940, ExpSv% .915) | SUPPORTED |
| 7 | They found some evidence the adjusted number predicted a goalie's future better than plain save percentage and called it "far from overwhelming" | arXiv 1205.1746 summary of findings ("some evidence that adjusted save percentage ... is a better predictor of future performance than save percentage ... However, the evidence is far from overwhelming") | SUPPORTED |
| 8 | Evolving-Hockey publishes xFSv% on unblocked attempts and dFSv%; MoneyPuck defines expected save percentage and "Save % Above Expected" | Evolving-Hockey Standard Goalie Tables; MoneyPuck glossary | SUPPORTED |
| 9 | NHL.com's Seattle Kraken column explained the delta (dFSv%) in 2021 | Lukan, "Analytics with Alison: Sizing up Goaltending," NHL.com, Oct 28, 2021 | SUPPORTED |
| 10 | Public xG models price unblocked attempts, misses included | MoneyPuck glossary (xG on unblocked attempts; Fenwick includes misses); Evolving-Hockey (xGA = xG of all Fenwick shots against) | SUPPORTED |
| 11 | Worked example (100 xG on 2,000 attempts = .950; 90 allowed = .955; +0.5 points = 10 goals of GSAx) | Arithmetic, labelled invented | SUPPORTED |
| 12 | Misses count as stops in the Fenwick version, so numbers sit near .950 vs box-score near .900; league expected and real Fenwick rates .9495 and .9500 | W&W calc, MoneyPuck file: 1 − 7,646.4/151,555 = .9495; 1 − 7,575/151,555 = .9500; NHL SV% .896 | SUPPORTED (computed) |
| 13 | Range among 51 regulars: Wallstedt .9559 (MIN) gentlest, Andersen .9402 (CAR) toughest; MIN's two goalies 1-2, SEA's two 3-4, CAR's two 50-51 | W&W calc, xFSv% (Wallstedt, Gustavsson, Grubauer, Daccord, ... Bussi, Andersen) | SUPPORTED (computed) |
| 14 | Talbot .9534 (sixth-gentlest), Gibson .9516; Gibson dFSv% +0.36, Talbot −0.76, ahead of only Ersson and Binnington | W&W calc (Talbot rank 49 of 51 in dFSv%) | SUPPORTED (computed) |
| 15 | On the box-score scale Talbot's shots called for about .900, he posted .883 | W&W calc 1 − 79.89/796 = .8996; NHL API SV% .8833 | SUPPORTED (computed) |
| 16 | Wedgewood led dFSv% at +1.00, Binnington trailed at −1.10, median +0.17; regulars fit inside about two percentage points | W&W calc | SUPPORTED (computed) |
| 17 | 39 goalies with 1,500+ minutes in both seasons: dFSv% r 0.21, xFSv% r 0.04; no better (0.02) for the 31 who stayed with the same team | W&W calc, Pearson, MoneyPuck 2025-26 + `mp_goalies_2024_for_gsax_repeatability_dl2026-10-09.csv` | SUPPORTED (computed) |
| 18 | Talbot's xFSv% .9477 in 2024-25, .9534 in 2025-26, same club | MoneyPuck files (team DET both seasons) | SUPPORTED (computed) |
| 19 | Wallstedt's .916 was second-best SV% among regulars; gentlest mix; dFSv% +0.29 ranked 22nd of 51 | NHL API (.9157, second to Wedgewood among 30+ GP); W&W calc | SUPPORTED (computed) |
| 20 | Cooley's +0.98 (CGY) second only to Wedgewood, on 1,758 attempts; Thompson +0.85 on 3,461 and GSAx leader | W&W calc, MoneyPuck file | SUPPORTED (computed) |
| 21 | Public models don't see pre-shot passes, screens or goalie position; cross-crease feeds priced like other shots from the spot | Evolving-Hockey xG write-up; MoneyPuck about (xG page rows 25, 28) | SUPPORTED |
| 22 | League near .950 on unblocked attempts and near .895 on shots on goal | W&W calc (.9495; 1 − 7,646.4/72,520 = .8946) | SUPPORTED (computed) |
| 23 | r 0.21 means most of a goalie's gap doesn't repeat; Talbot's delta was +0.47 the season before his −0.76 | 0.21² = 0.044; MoneyPuck 2024-25 file (12.8 GSAx / unblocked attempts = +0.47) | SUPPORTED (computed) |
| 24 | Rebounds a goalie allows become new shots against him and lower his xSV%; MoneyPuck's flurry adjustment gives less credit for rebound chances | MoneyPuck glossary (xGA sums attempts on the goalie; Flurry Adjusted definition) | SUPPORTED |

## Voice metrics (`style_metrics.py --target barnwell_lean`, running prose, 1,025 words)

| Metric | Value | Target |
|---|---|---|
| Sentence mean / SD | 19.0 / 10.9 | 17-21 / ≥ 10 |
| Short / long sentences | 13% / 11% | 6-15% / ≤ 20% |
| Words per paragraph | 57 | 55-85 |
| One-sentence paragraphs | 6% | 5-12% |
| Contractions per 1k | 41.0 | ≥ 28 |
| I / you per 1k | 0.0 / 5.9 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 2.0 / 5.9 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 52.7 | 30-55 |

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, unicode artifacts, question fragments or false ranges. Remaining hint `repeated_ngrams` (metric names).

Hover short in `glossary-terms.json` agrees with the page; no change proposed.
