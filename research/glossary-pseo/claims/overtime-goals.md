# Claims register: overtime-goals.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`nhl_skater_summary_20252026_scoringbasics.json`, `nhl_skater_summary_20242025_scoringbasics.json`,
`nhl_team_summary_20252026_scoringbasics.json`, `nhl_standings_20260417_final_scoringbasics.json`,
`nhl_team_overtime_outcomes_by_season_scoringbasics.json` (2009-10, 2014-15, 2015-16, 2018-19, 2024-25, 2025-26),
`nhl_overtime_format_history_check_scoringbasics.json` (1982-83, 1983-84, 1998-99, 1999-2000, 2005-06),
`nhl_skater_career_otgoals_thru20252026_scoringbasics.json`, `nhl_det_franchise_career_otGoals_thru20252026_scoringbasics.json`,
`hr_playoff_overtime_goals_20261009.html` (Hockey-Reference playoff OT goal list). Rule text:
`nhl_rulebook_2025-26_excerpts_rules6_33_78_84_scoringbasics.txt` (Rule 84 unchanged in 2026-27).
Glossary text: `nhl_stats_glossary_api_20261009_scoringbasics.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | An overtime goal ends the game; regular-season OT is five minutes of three-on-three, then a shootout; playoff OT is 20-minute periods at five-on-five | Rules 84.1, 84.4, 84.5 | SUPPORTED |
| 2 | 326 of 1,312 games went past regulation; 207 ended on an overtime goal | NHL standings (otLosses 326); W&W calc OT wins = ROW − RW = 207 | SUPPORTED (computed) |
| 3 | Every overtime goal counts as a game-winner | NHL glossary GWG definition; skater OTG sum 207 within GWG | SUPPORTED |
| 4 | Changed shape three times since the five-minute, five-on-five period for 1983-84 | The Hockey News (Titus, Dec. 28, 2023: "five-minute five-man overtime was introduced for the 1983-84 season"); changes in rows 6-8 | SUPPORTED |
| 5 | League records show 54 OT wins in 1983-84 and none in 1982-83 | NHL team summary (regulationAndOtWins − winsInRegulation) | SUPPORTED (computed) |
| 6 | Losing in OT cost the tie point until 1999-2000, when the league went to four-on-four and gave the loser a point | The Hockey News (5-on-5 to 4-on-4 and the loser point together); NHL team summary (otLosses 0 in 1998-99, 114 in 1999-2000) | SUPPORTED |
| 7 | 162 of 222 OT games still ended in ties the season before the change (1998-99) | The Hockey News; NHL team summary 1998-99 (162 ties + 60 OT wins) | SUPPORTED |
| 8 | Shootout arrived in 2005-06 and ended ties; three-on-three replaced four-on-four a decade later (2015-16) | AP via Fox Sports (Oct. 6, 2025); NHL glossary OTG (4-on-4 through 2014-15, 3-on-3 from 2015-16); NHL team summary 2005-06 (0 ties, 145 shootouts) | SUPPORTED |
| 9 | Share of OT games settled before a shootout: 44% in 2014-15, 61% in 2015-16 | W&W calc, NHL team summaries (136/306, 168/275) | SUPPORTED (computed) |
| 10 | AP: shootouts decided 15% of games at their 2009-10 peak, 5.9% in 2024-25 | AP via Fox Sports; matches W&W calc (184/1,230; 77/1,312) | SUPPORTED |
| 11 | Climbed back to 9.1% in 2025-26 | W&W calc: 119 ÷ 1,312 | SUPPORTED (computed) |
| 12 | Rule 84.1: ice shoveled, teams change ends, three skaters a side, up to five minutes, first goal wins with the extra point | Rule 84.1 | SUPPORTED |
| 13 | Team can pull its goalie; under 84.2 it forfeits the overtime point if it loses with the net empty | Rule 84.2 | SUPPORTED |
| 14 | Penalties add skaters; a minor makes it four-on-three | Rule 84.3 | SUPPORTED |
| 15 | Playoffs: no shootout, 15-minute intermission, full 20-minute periods, change ends, first goal wins | Rule 84.5 | SUPPORTED |
| 16 | Longest game in league history went to Detroit: Bruneteau at 116:30 of OT, sixth extra period, beat the Maroons in a 1936 semifinal | Hockey-Reference playoff OT goals (1936-03-24, SF G1, DET 1-0 MTM, 6 OTs, 116:30; longest OT time on the list) | SUPPORTED |
| 17 | Worked example (Detroit-Boston, three-on-three goal) | Invented game, labelled | SUPPORTED (illustrative) |
| 18 | Shootout goals aren't overtime goals; winning team gets one goal; nobody's goal total changes | Rule 84.4 | SUPPORTED |
| 19 | One per overtime game at most; worth a standings point | Rule 84.1 | SUPPORTED |
| 20 | 144 players scored one, 42 two or more, 15 three or more | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 21 | Caufield led with five; Kaprizov, Keller, Kempe, Larkin four | NHL skater summary 2025-26 | SUPPORTED |
| 22 | Defensemen scored about 20% of OT goals (41 of 207) vs 15% of all goals | W&W calc | SUPPORTED (computed) |
| 23 | Detroit 9-6 in OT, 2-4 in shootouts, 21 games past regulation | NHL standings (ROW 39 − RW 30 = 9; otLosses 10 − shootoutLosses 4 = 6; shootoutWins 2, shootoutLosses 4) | SUPPORTED (computed) |
| 24 | Larkin four of nine OT winners; DeBrincat two; Seider, Copp, Edvinsson one each | NHL skater summary OTG | SUPPORTED |
| 25 | Larkin's 13 career OT goals are the franchise record, one ahead of Fedorov | NHL stats API franchise aggregate (Larkin 13, Fedorov 12, Shanahan 9, Yzerman 9) | SUPPORTED |
| 26 | Ovechkin's 27 lead the league through 2025-26 | NHL stats API career aggregate | SUPPORTED |
| 27 | A team's OT wins equal its OT goals; Minnesota led with 11; Detroit's nine tied for sixth | W&W calc, NHL team summary (MIN 11; SJS, MTL, NYI, UTA 10) | SUPPORTED (computed) |
| 28 | Detroit lost four of six shootouts | NHL standings | SUPPORTED |
| 29 | Draisaitl led with six OT goals in 2024-25 and scored one in 2025-26 | NHL skater summaries | SUPPORTED |
| 30 | Only two Stanley Cup Final Game 7s decided in OT, both Detroit: Babando double OT vs Rangers 1950, Leswick vs Montreal 1954 | Hockey-Reference playoff OT goals (only Final Game 7 entries; through the 2026 playoffs) | SUPPORTED |
| 31 | Sakic's eight career playoff OT goals are the record | Hockey-Reference playoff OT goals leader table | SUPPORTED |
| 32 | League leader has five or six in a season; OTG YoY r = 0.33 (260 forwards); 2024-25's top three combined for four in 2025-26 | NHL skater summaries (Draisaitl 6→1, Aho 5→2, Suzuki 5→1); W&W calc | SUPPORTED (computed) |
| 33 | Career totals mix five-on-five, four-on-four and three-on-three; 44% vs 63.5% decided in OT | Rows 4-9; W&W calc 207/326 | SUPPORTED (computed) |
| 34 | League keeps regular-season and playoff OT goals separately | NHL stats game types; Hockey-Reference separate playoff list | SUPPORTED |
| 35 | Facts: three-on-three since 2015-16; 24.8%; 63.5%; Caufield 5; Larkin 4 tied second; Larkin 13; Sakic 8 | Rows 2, 8, 21, 25, 31 | SUPPORTED |

Cut for lack of verification: regular-season overtime's removal in 1942 (Wikipedia only); the league's stated
reason for three-on-three (the NHL.com approval story wouldn't load); the June 2015 Board of Governors date;
any explanation of why defensemen score more of the overtime goals.

## Voice metrics (running prose, `--target barnwell_lean`, 1,113 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 18.9 / 10.1 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 17% | 6-15% / ≤ 20% |
| Words per paragraph | 59 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 28.8 | ≥ 28 |
| I / you per 1k | 0 / 5.4 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 3.6 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 49.4 | 30-55 |

ai-content-detection: no contrast frames, payoff colons or unicode artifacts. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and format names. Formats are spelled
out in prose ("three-on-three") because "3-on-3" counts as two numbers and pushed the page past 100 per 1k.
