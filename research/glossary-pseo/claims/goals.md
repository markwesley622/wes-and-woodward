# Claims register: goals.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`nhl_skater_summary_20252026_scoringbasics.json`, `nhl_skater_summary_20242025_scoringbasics.json`,
`nhl_skater_realtime_20252026_scoringbasics.json`, `nhl_team_summary_20252026_scoringbasics.json`,
`nhl_standings_20260417_final_scoringbasics.json`, `nhl_goals_per_team_game_select_seasons_scoringbasics.json`,
`nhl_skater_assists_per_goal_all_seasons_scoringbasics.json`, `nhl_skater_season_top_goals_thru20252026_scoringbasics.json`,
`nhl_det_franchise_career_goals_thru20252026_scoringbasics.json`, `nhl_roster_DET_20252026_positioncodes_scoringbasics.json`,
`mp_skaters_2025.csv` (MoneyPuck season "2025" = 2025-26). Rule text: `nhl_rulebook_2025-26_excerpts_rules6_33_78_84_scoringbasics.txt`
(from the 2025-26 rulebook PDF; Rules 6, 33, 78 and 84 checked unchanged in the 2026-27 edition).
Glossary text: `nhl_stats_glossary_api_20261009_scoringbasics.json` (the API behind nhl.com/stats/glossary).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | A goal is credited to the last player on the scoring team to touch the puck before it crosses the goal line | Rule 33.2 ("A goal is awarded to the last player on the scoring team to touch the puck prior to the puck entering the net"); NHL glossary G | SUPPORTED |
| 2 | Each goal counts as one point in the player's record | Rule 78.2 | SUPPORTED |
| 3 | G means goalie in a roster's position column | NHL roster API positionCode "G" for goalies (C, L, R, D, G) | SUPPORTED |
| 4 | Average NHL team scored 3.08 goals a game in 2025-26 | W&W calc: 8,086 goals ÷ 2,624 team games, NHL team summary | SUPPORTED (computed) |
| 5 | The In-Arena Scorer decides who gets credit | Rule 78.1, Rule 33.2 | SUPPORTED |
| 6 | NHL database counts goals back to 1917-18 | NHL glossary G, firstSeasonForStat 19171918; skater summary 1917-18 | SUPPORTED |
| 7 | Joe Malone scored 44 goals in 20 games for the Canadiens in 1917-18 | NHL skater summary 1917-18 (Malone, MTL, 44 G, 4 A, 20 GP) | SUPPORTED |
| 8 | 1917-18: fewer than half as many assists as goals; goals were 70% of points | W&W calc: 145 assists, 342 goals (0.42), 342 ÷ 487 = 70.2% | SUPPORTED (computed) |
| 9 | Rule 78.1 makes the scorer's decision final over the referee's | Rule 78.1 ("final, notwithstanding the report of the Referee") | SUPPORTED |
| 10 | Rule 78.2 quote "propelled the puck into the opponent's goal" | Rule 78.2 | SUPPORTED |
| 11 | A shot that deflects in off a teammate is the teammate's goal | Rule 33.2 last-touch rule | SUPPORTED |
| 12 | Own goal goes to the last attacker to touch the puck | Rule 78.4; NHL glossary G | SUPPORTED |
| 13 | Scorer uses video replay; teams have 24 hours to request a change; League Official Scorer appointed by Hockey Operations rules, final | Rule 33.2 | SUPPORTED |
| 14 | Rocket Richard Trophy donated by the Canadiens in 1999, to the regular season's top goal scorer; Selanne won the first | Hockey Hall of Fame trophy page | SUPPORTED |
| 15 | MacKinnon won 2025-26 with 53 | NHL skater summary 2025-26 (goals leader 53); trophy goes to the leader | SUPPORTED |
| 16 | NHL.com, Hockey-Reference, MoneyPuck publish goals from official scoring | Hockey-Reference data credits (official NHL data via Sportradar); MoneyPuck data page | SUPPORTED |
| 17 | MoneyPuck's 2025-26 skater file is two goals short of the NHL's count | W&W calc: MoneyPuck all-situations I_F_goals 8,084 vs NHL 8,086 | SUPPORTED (computed) |
| 18 | Season G = EVG + PPG + SHG | NHL skater summary: 6,286 + 1,595 + 205 = 8,086 | SUPPORTED (computed) |
| 19 | Worked example (200 shots, 10%, 20 goals, 80 games) | Invented round numbers, labelled | SUPPORTED (illustrative) |
| 20 | Shootout goals don't count for players; winning team gets one extra goal; losing goalie not charged | Rule 84.4 | SUPPORTED |
| 21 | Stats pages and standings disagree on 2025-26 league goals by 119, one per shootout | W&W calc: standings goalFor sum 8,205 − 8,086 = 119 = winsInShootout sum; NHL glossary GF note | SUPPORTED (computed) |
| 22 | The rulebook awards every game to the team with more goals | Rule 78.1 | SUPPORTED |
| 23 | Detroit scored 2.91 goals a game in 2025-26, 22nd | NHL team summary (239 GF, 2.91/GP; 21 teams higher) | SUPPORTED |
| 24 | 327 forwards with 60+ GP: median 16, top tenth 32+ | W&W calc, NHL skater summary (33rd-highest = 32) | SUPPORTED (computed) |
| 25 | Defensemen with 60+ GP (161): median 5 | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 26 | 15 players reached 40; only MacKinnon (53) and Caufield (51) reached 50 | NHL skater summary 2025-26 | SUPPORTED |
| 27 | DeBrincat 41, tied for 11th; Larkin 34; nobody else on Detroit reached 30; Raymond next with 25 | NHL skater summary (10 players above 41; Gauthier also 41) | SUPPORTED |
| 28 | YoY (260 forwards, 60+ GP both seasons): G/GP r = 0.74, P/GP 0.88, shots/GP 0.89, SH% 0.37 | W&W calc, NHL skater summaries 2024-25 and 2025-26 | SUPPORTED (computed) |
| 29 | About one goal in five came on the power play in 2025-26 | 1,595 ÷ 8,086 = 19.7% | SUPPORTED (computed) |
| 30 | DeBrincat 15 of 41 PPG, Larkin 14 of 34, close to double the league rate | NHL skater summary (37%, 41% vs 19.7%) | SUPPORTED (computed) |
| 31 | Raymond 25 goals on 19.5 ixG (+5.5); Larkin 34 on 33.8 | MoneyPuck skaters file, all situations (I_F_xGoals 19.49, 33.76) | SUPPORTED (computed) |
| 32 | MoneyPuck warns one season of finishing carries a lot of luck | MoneyPuck about, shooting talent section (same as expected-goals row 22) | SUPPORTED |
| 33 | MacKinnon led with 350 shots, 15.1%; Caufield 51 on 258 (19.8%); league 11.1% | NHL skater summary (8,086 ÷ 73,022 shots) | SUPPORTED (computed) |
| 34 | DeBrincat 14.3% was the lowest of the 15 40-goal scorers | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 35 | 508 empty-net goals in 2025-26, 6.3% of goals; DeBrincat and Larkin four each | NHL skater realtime report (emptyNetGoals) | SUPPORTED (computed) |
| 36 | Teams can appeal within 24 hours, so the next morning's box score can differ from the one announced | Rule 33.2 (announced twice; changes reviewed by League Official Scorer) | SUPPORTED |
| 37 | FAQ: Ovechkin 929 regular-season goals through 2025-26; Gretzky 894; Gretzky single-season record 92 | NHL stats API career aggregate through 2025-26; season leaders (Gretzky 92, 1981-82) | SUPPORTED |
| 38 | FAQ: Howe's 786 for Detroit are the franchise record; Yzerman second (692) | NHL stats API franchise aggregate (franchiseId 12) | SUPPORTED |
| 39 | Facts: median forward 16; MacKinnon 53; DeBrincat 41 tied 11th | Rows 24, 26, 27 | SUPPORTED |

Cut for lack of verification: the date Ovechkin passed Gretzky; any claim about how often scoring changes happen;
why MoneyPuck's count differs from the NHL's by two goals.

## Voice metrics (running prose, `--target barnwell_lean`, 1,196 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 18.1 / 10.0 | 17-21 / ≥ 10 |
| Short / long sentences | 14% / 18% | 6-15% / ≤ 20% |
| Words per paragraph | 57 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 41.8 | ≥ 28 |
| I / you per 1k | 0 / 5.9 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.7 / 5.0 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 2% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 53.5 | 30-55 |

ai-content-detection: no contrast frames, payoff colons or unicode artifacts. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and the rule's own wording.
