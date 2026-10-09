# Claims register: shot-share.json

Reviewed 2026-10-09. Five-on-five rows come from `research/glossary-pseo/raw/mp_teams_2025.csv`,
`mp_skaters_2025.csv` and `mp_team_games_5on5_2023-2025_extract.csv` (MoneyPuck, downloaded 2026-10-09). Historical
all-situations shares come from `nhl_team_summary_allseasons_to_20252026.json` (NHL stats API team summary, every
team-season with shots, 1959-60 through 2025-26; downloaded 2026-10-09 by the family's shared pull) and 2025-26
points percentage from `nhl_team_summary_20252026_corsi-family.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | SF% = team's share of shots on goal in its games or in a player's minutes, usually 5v5; 50% break-even | NST glossary SF% (SF*100/(SF+SA)); NHL glossary Shots | SUPPORTED |
| 2 | Misses and blocks don't count | NHL glossary Shots ("Attempts blocked and missed shots are not included") | SUPPORTED |
| 3 | NHL has tracked team shots officially since 1955-56 (skaters since 1959-60); missed shots dated to 1997-98, blocked shots to 2002-03 | NHL glossary S, MsS, BkS entries | SUPPORTED |
| 4 | Last season SF% tracked the standings more closely than Corsi (points % r 0.70 vs 0.57; xGF% 0.74) | W&W calc, MoneyPuck teams file 5on5 + NHL pointPct, 32 teams | SUPPORTED (computed) |
| 5 | Jim Corsi added missed and blocked shots because shots against left part of the workload out; bloggers applied the count to skaters in the 2000s | NBC Sports 2010-04-30; McKenzie excerpt; Battle of Alberta Nov 2007 | SUPPORTED |
| 6 | NHL stats site lists shots for/against per game and shot differential (SD/GP) | NHL team summary fields shotsForPerGame / shotsAgainstPerGame; NHL glossary SD/GP | SUPPORTED |
| 7 | NST publishes SF% for teams and players, goals counted as shots on goal | NST team and player glossary (Wayback capture) | SUPPORTED |
| 8 | Shot on goal = went in or would have without the save; post = miss | NHL.com hockey glossary (Shot on Goal); NHL stats glossary MsS (posts and crossbars) | SUPPORTED |
| 9 | SF = FF − missed shots | Definitions (Fenwick = shots on goal + missed shots) | SUPPORTED |
| 10 | Worked example (invented): 20 of 45 vs 25 of 40, SF% 44.4% | arithmetic | SUPPORTED |
| 11 | 2025-26 5v5: 47% of attempts on goal, about a quarter missed, rest blocked | W&W calc: 56,451 / 121,106 = 46.6%; misses 25.6%; blocked 27.8% | SUPPORTED (computed) |
| 12 | 2025-26 5v5 SF%: Carolina 57.7 (1st), Chicago 44.4 (last), Detroit 49.7 (18th; 1,761 for, 1,785 against) | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |
| 13 | Colorado league-high 32.9 SF/60; Detroit at the median, about 26 (25.99 vs 26.13) | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |
| 14 | 598 skaters: median on-ice SF% 49.9, top tenth ≥ 55.5, bottom tenth ≤ 44.8; Seider 55.9 led Detroit regulars, Rasmussen lowest 44.5 | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 15 | SF% above CF% means blocking more of the opponent's attempts or missing less (or both); Detroit's gap came from blocking | Definitions; Detroit blocked 1,179 opponent attempts (tied 1st) with its own blocked attempts at the median; FF% 49.69 vs SF% 49.66, so misses add nothing and the CF%-to-FF% gap is blocks, MoneyPuck teams file | SUPPORTED (computed) |
| 16 | Split test (96 team-seasons): first-half SF% to second-half GF% 0.47 vs CF% 0.42; repeat CF% 0.81, SF% 0.70 | W&W calc, game-by-game extract | SUPPORTED (computed) |
| 17 | Detroit all-situations 2025-26 shot share 50.4%, 14th | NHL team summary (shotsForPerGame / (for + against)) | SUPPORTED (computed) |
| 18 | NHL stats feed carries team shots back to 1959-60 (66 seasons through 2025-26) | NHL team summary all seasons (first season with shot data 1959-60) | SUPPORTED |
| 19 | 2007-08 Red Wings 59.4% all-situations shot share, highest in those 66 seasons; won the Stanley Cup | W&W calc, NHL team summary; Hockey-Reference 2007-08 DET page ("Won Stanley Cup Final (4-2) over Pittsburgh"), raw saved | SUPPORTED (computed) |
| 20 | Detroit led the league in shot share eight times, four straight from 2005-06; only Montreal (11) more | W&W calc, NHL team summary (Boston also 8) | SUPPORTED (computed) |
| 21 | Rink effects 2007-08 through 2012-13: shots on goal 2 rinks, blocks 15, misses 9 | Schuckers and Macdonald, arXiv 1412.1035, Table 19 | SUPPORTED |
| 22 | On-ice SF% correlated 0.72 with team SF% (598 skaters) | W&W calc | SUPPORTED (computed) |
| 23 | Counts come from the Real Time Scoring System, logged into the public play-by-play files | Schuckers and Macdonald, arXiv 1412.1035 (abstract) | SUPPORTED |
| 24 | Every shot on goal ends as a goal or a save; save percentage = saves ÷ shots on goal faced | NHL.com hockey glossary (Save Percentage, Shot on Goal) | SUPPORTED |

Live slot: omitted. Wanted: `team.situations.5on5.shotsOnGoalFor` and `shotsOnGoalAgainst` (or a computed
`shotsPct`) with `leagueRanks.shotsPct_5on5`, and `skaters.fiveOnFive.onIceShotsPct`.

## Voice metrics (running prose, `--target barnwell_lean`)

Running prose, 1,090 words.

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 18.2 / 10.7 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 18% | 6-15% / ≤ 20% |
| Words per paragraph | 57 | 55-85 |
| One-sentence paragraphs | 11% | 5-12% |
| Contractions per 1k | 33.9 | ≥ 28 |
| I / you per 1k | 0.0 / 3.7 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 2.8 / 4.6 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 51.4 | 30-55 |
