# Claims register: shots-on-goal.json

Raw files (all downloaded 2026-10-09, in `research/glossary-pseo/raw/`): `mp_teams_2025.csv` (MoneyPuck 2025-26 teams),
`nhl_team_summary_20252026_sogfamily.json`, `nhl_skater_summary_20252026_sogfamily.json`,
`nhl_skater_summary_20242025_sogfamily.json`, `nhl_skater_summary_career_through20252026_DET2526_sogfamily.json`,
`nhl_goalie_summary_20252026_sogfamily.json`, `nhl_goalie_summary_20252026_DETonly_sogfamily.json`,
`nhl_stats_glossary_api_20261009.json` (NHL stats glossary, api.nhle.com/stats/rest/en/glossary),
`nhl_boxscore_2025020001_sogfamily.json` (NHL gamecenter box score sample).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | SOG = shots that go in or force a save; posts, crossbar, misses and blocks don't count | NHL stats glossary: S ("Attempts blocked and missed shots are not included"), S% ("only shots that were saved by the goalie or scored a goal"), Sv% ("Hitting the post or the crossbar ... does not count as a shot on goal, but as a missed shot") | SUPPORTED |
| 2 | Every goal is a shot on goal, and so is every save | NHL glossary S% definition (goals and saved shots are the shots on goal) | SUPPORTED |
| 3 | NHL box-score column is S; also called SOG; the NHL's oldest official shot count | NHL glossary S: "Shots are also called shots on goal, or SOG" | SUPPORTED |
| 4 | Official for teams since 1955-56, skaters since 1959-60 | NHL glossary S | SUPPORTED |
| 5 | Save percentage official 1955-56, shooting percentage 1959-60, both with SOG as denominator | NHL glossary Sv% ("began officially tracking save percentage in 1955-56", Sv% = SV/SA) and S% ("1959-60", goals divided by shots) | SUPPORTED |
| 6 | For four decades SOG was the only shot the official record kept | Missed shots first tracked 1997-98, blocked shots 2002-03 (NHL glossary MsS, BkS); 1955-56 to 1997-98 = 42 seasons | SUPPORTED |
| 7 | Missed shots = wide, over, short, post, crossbar (and failed bank attempts); since 1997-98; blocked shots since 2002-03 | NHL glossary MsS and BkS | SUPPORTED |
| 8 | SAT and USAT (Corsi and Fenwick) start in 2009-10 | NHL glossary SAT ("also known as Corsi", "available since 2009-10"), USAT ("also known as Fenwick") | SUPPORTED |
| 9 | NHL game box score lists SOG for every player with no column for missed or blocked attempts | NHL gamecenter boxscore feed, player fields: goals, assists, points, plusMinus, pim, hits, powerPlayGoals, sog, faceoffWinningPctg, toi, blockedShots (blocks made), shifts, giveaways, takeaways | SUPPORTED |
| 10 | Rule 36 (2025-26 rulebook): Real Time Scorers electronically record all official statistics; 3 stats-entry scorers, a time-on-ice scorer, an event analyst, overseen by a scoring system manager; reports during the 1st and 2nd intermissions and post-game | NHL Official Rules 2025-26, Rule 36.1-36.3 (media.nhl.com 2025-26Rules.pdf) | SUPPORTED |
| 11 | Whether a puck grazing the pad is a save or miss is the scorers' judgment | Rule 36.1 (Real Time Scorers record all official statistics) + glossary definitions | SUPPORTED (inference from the rule) |
| 12 | Worked example: 10 attempts, 3 blocked, 2 wide, 1 post, 4 on goal, 1 goal; Corsi 10, Fenwick 7 | Arithmetic from the glossary definitions (post = missed shot = in USAT) | SUPPORTED (invented, labelled) |
| 13 | Goalie doesn't have to defend a shot that misses the frame; post counted as miss | NHL glossary Sv% | SUPPORTED |
| 14 | 2025-26: 152,961 attempts; 40,865 blocked; 39,036 missed; 73,060 SOG (47.8%); 8,086 goals; ~1 in 9 SOG and ~1 in 19 attempts scored | W&W calc, MoneyPuck teams file, all situations, 32 teams (8,086/73,060 = 11.1%; 8,086/152,961 = 5.3%) | SUPPORTED (computed) |
| 15 | Average team 27.8 SOG/game; Colorado 33.7 (1st), Chicago 24.6 (32nd); Detroit 28.2, allowed 27.7, differential +0.5 (14th) | W&W calc, NHL team summary 2025-26 (shotsForPerGame, shotsAgainstPerGame; league = 73,032 / 2,624 team games) | SUPPORTED (computed) |
| 16 | 327 forwards with 60+ GP, median 131 SOG; 161 defensemen with 60+ GP, median 93 | W&W calc, NHL skater summary 2025-26 | SUPPORTED (computed) |
| 17 | MacKinnon led with 350; DeBrincat tied Celebrini for 4th at 287 (behind MacKinnon 350, McDavid 306, Robertson 294); 287 is more than twice 131; Larkin 229 ranked 20th among 60+ GP forwards; Seider 187 ranked 10th among 325 defensemen | W&W calc, NHL skater summary 2025-26 | SUPPORTED (computed) |
| 18 | 189 forwards with 100+ SOG in both 2024-25 and 2025-26; shots/GP year-to-year r = 0.80, S% r = 0.35 | W&W calc, NHL skater summaries 2024-25 and 2025-26, Pearson r | SUPPORTED (computed) |
| 19 | DeBrincat 41 goals on 287 shots; league S% 11.1% → ~32 goals; 14.3% vs 14.2% career | W&W calc: league 8,086 / 73,022 skater shots = 11.07%; 287 × 0.1107 = 31.8; DeBrincat career 294/2,064 = 14.2% (NHL career aggregate) | SUPPORTED (computed) |
| 20 | Hypothetical 41 goals on 180 shots = almost 23% | 41/180 = 22.8% | SUPPORTED (computed) |
| 21 | Dallas 25.3 SOG/game (30th), 273 goals (9th), 13.2% (best); Calgary 28.1 SOG/game (above 27.8 average), 208 goals (fewest), 9.0% | W&W calc, NHL team summary + MoneyPuck teams file (goals/SOG, all situations) | SUPPORTED (computed) |
| 22 | Gibson faced 1,461 SOG for Detroit, saved 1,317, .901; league .896 | NHL goalie summary 2025-26 (Detroit-only split; league = 64,976 saves / 72,530 shots against) | SUPPORTED (computed) |
| 23 | This site grades goalies on goals saved above expected | `data/site/dashboard.json` gsax tile; expected-goals.json claim 24 | SUPPORTED |
| 24 | Average unblocked attempt worth 0.073 goals in MoneyPuck's model | W&W calc, 8,222 xG / 112,096 unblocked attempts, MoneyPuck teams file | SUPPORTED (computed) |
| 25 | More than half of attempts blocked or missed | (40,865 + 39,036) / 152,961 = 52.2% | SUPPORTED (computed) |
| 26 | Schuckers and Macdonald: six seasons (2007-08 to 2012-13) of RTSS data; shots steadiest event; only Florida (1.030) and St. Louis (0.955) persistent shot effects; persistent rink effects for hits 12, giveaways 18, missed shots 9 | arXiv 1412.1035, rink-effect results and Table 19 | SUPPORTED |
| 27 | FAQ: record is Phil Esposito 550 in 1970-71; Ovechkin 528 in 2008-09 next (3rd is 446); 350 is far outside the top 20 (20th is 393) | Hockey-Reference single-season shots leaders | SUPPORTED |

## Voice metrics (extract_prose.py → style_metrics.py --target barnwell_lean)

1,323 words. Sentence mean 18.1 / SD 10.9; short 8%; long 16%; words per paragraph 66; one-sentence paragraphs 10%;
contractions 30.2/1k; I 0; you 5.3/1k; questions 1.5/1k; parentheses 3.8/1k; intensifiers 0; transition openers 0%;
numbers 53.7/1k; hedges 0. All in range. Numbers per 1k was the binding constraint (first draft 86.5); seasons were
rewritten as "last season" where the year wasn't needed.

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, balanced negation or unicode artifacts.
Remaining hints `uniform_paragraph_structure` (meaning paragraphs) and `repeated_ngrams` ("shots on goal",
"off the post"), the metric-name pattern TEMPLATE.md expects.

No hover-short change proposed; the current `short` agrees with the page.
