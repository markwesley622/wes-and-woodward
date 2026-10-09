# Claims register: on-ice-shooting-and-save-percentage.json

Reviewed 2026-10-09. Computed rows use MoneyPuck regular-season files: 2025-26 team and skater files
(`research/glossary-pseo/raw/mp_teams_2025.csv`, `mp_skaters_2025.csv`, downloaded 2026-10-09) and the 2024-25 skater
and team files (`research/rasmussen/raw/mp/skaters_2024.csv`, `teams_2024.csv`, downloaded 2026-09-08). All on-ice
figures are five-on-five; samples are skaters with ≥500 five-on-five minutes. MoneyPuck shotsOnGoal includes goals
(DET 5on5: 1,761 = 1,619 saved + 142 goals).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | oiSH% and oiSV% = team shooting and save percentage while a player is on the ice; sum is PDO | Hockey-Reference column tips ("Team On-Ice Shooting Percentage", "Team On-Ice Save Percentage", "PDO: Shooting % + Save %"); NST player glossary | SUPPORTED |
| 2 | Both swing with luck year over year | Rows 15-16 (r = 0.35 / 0.06 forwards); Hohl 2014 | SUPPORTED (computed) |
| 3 | On-ice stats date to 2007, when the NHL began logging events and shifts | Evolving-Hockey General Terms: "This method became available in 2007 when the NHL began tracking events and shifts at a play-by-play level" | SUPPORTED |
| 4 | PDO came out of the Irreverent Oilers blog; War-on-Ice wrote the parts OSh% and OSv%; league PDO is 100 by construction | War-on-Ice Annotated Glossary (2015-11-26): OSh%, OSv%, "PDO ... League average is 100 by construction. Origins: Irreverent Oilers" | SUPPORTED |
| 5 | Hohl 2014: 575 samples of a defenseman's two-season relative SV% vs the next two seasons; R² 2.6%; worst tenth had no impact after; best tenth kept <20%; defensemen lack substantial, sustainable control | Hockey-Graphs, Garret Hohl, 2014-07-07, verbatim figures and title | SUPPORTED |
| 6 | Hockey-Reference (oiSH%, oiSV%), NST, Evolving-Hockey publish them; NHL.com carries on-ice shooting % in its puck-possession report | H-R 2025-26 advanced table; NST glossary; EH on-ice tables (Sh%, Sv% columns, `research/soderblom/raw/eh/std_onice_5v5_2025.csv` header); NHL stats API skater/puckPossessions field `onIceShootingPct` | SUPPORTED |
| 7 | Power play inflates shooting: teams shot about 50% better at 5v4 in 2025-26 (14.42% vs 9.51%); PK drags save % down (85.6%) | W&W calc goalsFor ÷ shotsOnGoalFor by situation, MoneyPuck teams file | SUPPORTED (computed) |
| 8 | Inputs: on-ice goals and shots on goal for and against; shots on goal include goals; blocked and missed attempts excluded | NST formulas GF/SF, GA/SA; NST "Shots - Any shot attempt on net (goals and shots on net)" | SUPPORTED |
| 9 | Worked example (invented): 400 SOG each way, 36 goals each → 9.0%, 91.0%, PDO 100; +8 goals → 11.0% | Labelled invented; arithmetic | SUPPORTED |
| 10 | A defenseman's oiSH% includes his forwards' shots; a forward's oiSV% is his goalie's save % during his shifts | Definition (row 1) | SUPPORTED |
| 11 | League 5v5 2025-26: 9.51% shooting, 90.49% saves, sum 100 | W&W calc 5,367 goals / 56,451 SOG | SUPPORTED (computed) |
| 12 | 385 forwards: median oiSH 9.52%, middle 80% 7.0% to 12.1% (6.99, 12.14); Utah 4.47% with Brandon Tanev, Montreal 17.26% with Alex Newhook (extremes); oiSV spread narrower (88.38 to 92.67) | W&W calc OnIce_F_goals ÷ OnIce_F_shotsOnGoal etc. | SUPPORTED (computed) |
| 13 | Detroit team 5v5 shooting 8.06%, 30th; only Calgary (7.86) and New Jersey (7.22) lower; save % 90.48%, 17th | W&W calc teams file | SUPPORTED (computed) |
| 14 | Among Wings with 900 5v5 minutes: Raymond best on-ice shooting 10.23%, Kasper worst 5.91% | W&W calc skaters file (NST's own figure for Kasper: 5.92%) | SUPPORTED (computed) |
| 15 | 324 forwards with 500 min in both 2024-25 and 2025-26: oiSH r = 0.35, oiSV r = 0.06, CF% r = 0.64 | W&W calc, Pearson r, MoneyPuck 2024 and 2025 skater files | SUPPORTED (computed) |
| 16 | 177 defensemen: oiSH r = 0.16, oiSV r = 0.04 | Same | SUPPORTED (computed) |
| 17 | Kasper: DET had 50.3% of xG and 38.2% of goals with him on (26 GF, 42 GA); oiSV 90.41%; 26 goals on 440 shots; at 9.51% ≈ 42 goals | W&W calc (xGF 40.41, xGA 39.93; 440 × 0.0951 = 41.8) | SUPPORTED (computed) |
| 18 | Bernard-Docker oiSV 93.77% (24 GA / 385 SA), Sandin-Pellikka 88.49% (48 / 417); xGA/60 2.39 vs 2.83; GA/60 1.73 vs 3.07 (gap ~3x as wide) | W&W calc | SUPPORTED (computed) |
| 19 | Top-10 oiSH forwards of 2024-25 (500 min both years): 12.87% → 10.75%; bottom 10: 5.19% → 8.72%; league rate 8.95% → 9.51% | W&W calc 2024 and 2025 files | SUPPORTED (computed) |
| 20 | RAPM splits ice time to credit individuals | Evolving-Hockey RAPM glossary (controls for teammates, opponents) | SUPPORTED |
| 21 | Detroit's eight forwards with 900 5v5 min were on for 440 to 604 shots on goal; with 440, one goal moves Kasper's oiSH% ~0.23 points | W&W calc (Finnie/Kasper 440 ... DeBrincat 604); 1/440 | SUPPORTED (computed) |
| 22 | Larkin's on-ice SH% is 11.2% at Hockey-Reference and 8.1% in MoneyPuck 5v5 | `raw/hr_skaters_advanced_2025-26_downloaded_2026-10-09.html`; W&W calc 37/458 | SUPPORTED |
| 23 | FAQ: NST defines 5v5 as five skaters and a goalie each side, so empty nets aren't 5v5 | NST team glossary "5v5" definition | SUPPORTED |

Not claimed: which game state Hockey-Reference's oiSH% uses (its table header doesn't say), so the page only says the
two sites count different game states.

## Voice metrics

Running prose: 1266 words (extract_prose.py → style_metrics.py --target barnwell_lean).

| Metric | Page | Target |
|---|---|---|
| sent_mean | 17.8 | 17-21 |
| sent_sd | 10.0 | >=10 |
| pct_short_le6 | 11 | 6-15 |
| pct_long_ge30 | 11 | <=20 |
| para_words | 60 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 32.4 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 7.1 | 3-8 |
| q_per_k | 1.6 | 1-5 |
| paren_per_k | 3.2 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 51.3 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

ai-content-detection analyze_text.py: unicode artifacts 0, em dashes 0, contrast frames 0, payoff colons 0, question fragments 0, sentence-negation flags 0. Remaining n-gram hints are metric names ("five on five", "on the ice").

Hover short: the current `short` agrees with the page. No change proposed.
