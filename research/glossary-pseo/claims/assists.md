# Claims register: assists.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`nhl_skater_summary_20252026_scoringbasics.json`, `nhl_skater_scoringpergame_20252026_scoringbasics.json`
(primary and secondary assists), `nhl_skater_scoringpergame_20242025_scoringbasics.json`,
`nhl_goalie_summary_20252026_scoringbasics_assists.json`, `nhl_skater_assists_per_goal_all_seasons_scoringbasics.json`
(every season 1917-18 through 2025-26, skaters only), `nhl_skater_season_top_assists_thru20252026_scoringbasics.json`,
`nhl_det_franchise_career_assists_thru20252026_scoringbasics.json`, `nhl_det_franchise_season_assists_thru20252026_scoringbasics.json`,
`mp_skaters_2025.csv` (MoneyPuck season "2025" = 2025-26). Rule text: `nhl_rulebook_2025-26_excerpts_rules6_33_78_84_scoringbasics.txt`
(Rules 6, 33, 78 and 84 unchanged in the 2026-27 edition). Glossary text: `nhl_stats_glossary_api_20261009_scoringbasics.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Assist = credit for the last one or two scoring-team players to touch the puck before the scorer, unless an opponent plays or controls it in between | Rule 78.3; NHL glossary A ("provided the opposing team has not controlled the puck between...") | SUPPORTED |
| 2 | Touch right before the scorer = primary, the one before = secondary | NHL glossary A1, A2 | SUPPORTED |
| 3 | On a sweater, A marks an alternate captain | Rule 6.2 ("Alternate Captains shall wear the letter 'A'"); Rule 33.1 | SUPPORTED |
| 4 | Skaters credited with about 1.7 assists per goal in 2025-26 | W&W calc: 13,655 ÷ 8,086 = 1.69 | SUPPORTED (computed) |
| 5 | Rule 78.3 quote "the player or players (maximum two) who touch the puck prior to the goal scorer"; only one point to any player on a goal | Rule 78.3 | SUPPORTED |
| 6 | So a defenseman who starts and finishes a rush gets the goal and nothing more | Rule 78.2 and 78.3 (one point per player per goal); NHL glossary P | SUPPORTED |
| 7 | Scorer calls it from video replay, records assisting players with each scorer; 24 hours to appeal | Rule 33.1, 33.2 | SUPPORTED |
| 8 | NHL records show no secondary assists in the first five seasons (1917-18 to 1921-22) | NHL scoring-per-game report, totalSecondaryAssists = 0 every season 1917-18 to 1921-22 | SUPPORTED (computed) |
| 9 | Skaters averaged under one assist per goal every season until 1931-32 | W&W calc, all-seasons series (first season ≥ 1.0 is 1931-32) | SUPPORTED (computed) |
| 10 | Between 1.61 and 1.74 every season since 1960-61; 1.69 in 2025-26 | W&W calc, all-seasons series (min 1.605 in 1971-72, max 1.741 in 2006-07) | SUPPORTED (computed) |
| 11 | NHL glossary defines primary/secondary and calls G + A1 primary points | NHL glossary A1 ("The sum of goals and primary assists is often called primary points") | SUPPORTED |
| 12 | Game Score introduced by Dom Luszczyszyn at Hockey-Graphs in 2016; weights G 0.75, A1 0.7, A2 0.55 | Hockey-Graphs, July 13, 2016 (byline omgitsdomi, formula); Hockey-Graphs NWHL Game Score, March 22, 2018 ("In July of 2016, Dom Luszczyszyn released a metric called Game Score") | SUPPORTED |
| 13 | NHL stats pages and MoneyPuck files both carry the primary/secondary split | NHL scoring-per-game report fields; MoneyPuck I_F_primaryAssists / I_F_secondaryAssists | SUPPORTED |
| 14 | Worked example (defenseman, center, winger; poke-check makes it unassisted) | Invented play, labelled; logic per Rule 78.3 | SUPPORTED (illustrative) |
| 15 | Roughly three goals in four carried two assists; about 6% unassisted | W&W calc: 6,082 skater secondaries ÷ 8,086 = 75.2% (≤ 75.9% with goalies' 58); 8,086 − 7,573 skater primaries = 513 (6.3%, ≥ 5.6% with goalies) | SUPPORTED (computed) |
| 16 | Regulars (60+ GP): median forward 21 assists, median defenseman 20, top tenth of forwards 43+ | W&W calc, NHL skater summary (327 F, 161 D; 33rd-highest F = 43) | SUPPORTED (computed) |
| 17 | McDavid led with 90 | NHL skater summary 2025-26 | SUPPORTED |
| 18 | Raymond led Detroit with 51, 34 primary | NHL scoring-per-game report | SUPPORTED |
| 19 | Seider 50, tied for ninth among defensemen, near-even split (26/24) | NHL skater summary (8 defensemen above 50; McAvoy also 50); scoring-per-game | SUPPORTED |
| 20 | DeBrincat 44 assists, a little more than half primary (24), team-leading 41 goals | NHL skater summary, scoring-per-game | SUPPORTED |
| 21 | Regulars: forwards' assists 59% primary, defensemen's 48% | W&W calc, scoring-per-game, 60+ GP | SUPPORTED (computed) |
| 22 | Eight most secondary-heavy of the 66 players with 40+ assists were all defensemen; Pastrnak 57 of 71 primary | W&W calc, scoring-per-game (Sergachev, Fox, Heiskanen, Sanderson, Bouchard, Karlsson, Josi, Hutson) | SUPPORTED (computed) |
| 23 | YoY: forwards A1/GP r = 0.80, A2/GP 0.73; defensemen 0.71 and 0.70 | W&W calc, scoring-per-game 2024-25 and 2025-26, 60+ GP both (260 F, 119 D) | SUPPORTED (computed) |
| 24 | Primary points: DeBrincat 85 → 65; Raymond 76 → 59 and Larkin 67 → 50 (similar share); Seider 60 → 36, the biggest relative drop | W&W calc (76%, 78%, 75%, 60% retained) | SUPPORTED (computed) |
| 25 | IPP: DeBrincat and Raymond 69%, Larkin 65%, Seider 43% | W&W calc: points ÷ MoneyPuck all-situations OnIce_F_goals (85/123, 76/110, 67/103, 60/140) | SUPPORTED (computed) |
| 26 | Defensemen scored 15% of the league's goals | W&W calc: 1,226 ÷ 8,086 | SUPPORTED (computed) |
| 27 | Power-play goals carried 1.91 assists apiece, even-strength goals 1.66 | W&W calc: (4,640 PPP − 1,595 PPG) ÷ 1,595; (16,697 EVP − 6,286 EVG) ÷ 6,286 | SUPPORTED (computed) |
| 28 | Seider's 28 power-play points were the most on Detroit; 32 at even strength | NHL skater summary (Raymond 27, Larkin 24, DeBrincat 23) | SUPPORTED |
| 29 | The league's event feed records shots and goals but not passes | Evolving-Hockey xG write-up (same as expected-goals row 25) | SUPPORTED |
| 30 | Wingers shooting 8% vs 14% example | Hypothetical, framed as arithmetic | SUPPORTED (illustrative) |
| 31 | Teams have 24 hours to ask the league to change an award | Rule 33.2 | SUPPORTED |
| 32 | FAQ: goalies can get assists; goalies had 58 in 2025-26; Markstrom led with four | Rule 78.3 ("player or players"); NHL goalie summary 2025-26 | SUPPORTED |
| 33 | FAQ: Gretzky 1,963 career, single-season record 163 | NHL stats API career aggregate; season leaders (163, 1985-86) | SUPPORTED |
| 34 | FAQ: Yzerman's 1,063 are the Red Wings record; his 1988-89 (90) is the franchise's best season | NHL stats API franchise aggregates | SUPPORTED |
| 35 | Facts: Rule 78.3 maximum two; 1.69 per goal; median forward 21; McDavid 90; Raymond 51 (34 primary) | Rows 4, 5, 16-18 | SUPPORTED |

Cut for lack of verification: a 1930s three-assist limit and a one-assist 1945-46 season (crowd-sourced only); any
claim that assists change on appeal more often than goals; "usually" claims about how goalies earn assists; any
repeatability figures from outside sources (computed here instead).

## Voice metrics (running prose, `--target barnwell_lean`, 1,251 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.2 / 10.5 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 17% | 6-15% / ≤ 20% |
| Words per paragraph | 57 | 55-85 |
| One-sentence paragraphs | 9% | 5-12% |
| Contractions per 1k | 33.6 | ≥ 28 |
| I / you per 1k | 0 / 3.2 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.6 / 4.8 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 44.8 | 30-55 |

ai-content-detection: no contrast frames, payoff colons or unicode artifacts. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and the rule's own wording
("who touched the puck", "primary assist").
