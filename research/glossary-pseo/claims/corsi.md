# Claims register: corsi.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/mp_teams_2025.csv`, `mp_skaters_2025.csv`
(MoneyPuck season "2025" = 2025-26) and `mp_team_games_5on5_2023-2025_extract.csv` (five-on-five rows for 2023-24
through 2025-26 cut from MoneyPuck's 32 team game-by-game files plus ARI.csv), all downloaded 2026-10-09. NHL rows
come from `nhl_stats_glossary_2026-10-09.json`, `nhl_team_percentages_20252026.json` and
`nhl_team_summary_20252026_corsi-family.json`, downloaded the same day.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Corsi counts every shot attempt (on goal, missed, blocked) for and against a team or while a player is on the ice | NHL glossary SAT entry; MoneyPuck glossary (Corsi, Shot Attempt, On Ice); NST glossary (Wayback capture, raw `nst_glossary_players_wayback_20250109.html`) | SUPPORTED |
| 2 | CF% is the share; 50% is break-even | NHL glossary SAT% ("over 50% is above average"); NST CF*100/(CF+CA) | SUPPORTED |
| 3 | The NHL calls it SAT, for shot attempts | NHL glossary SAT ("also known as Corsi"); SI, Feb 20 2015 | SUPPORTED |
| 4 | 2025-26 five-on-five league totals 121,106 attempts, 5,367 goals, about 23 per goal | W&W calc, sum of 32 teams' shotAttemptsFor and goalsFor at 5on5, MoneyPuck teams file (121,106 / 5,367 = 22.6) | SUPPORTED (computed) |
| 5 | Larger sample than goals is the main reason to use SAT | NHL glossary SAT ("take advantage of the much larger sample size of shot attempts than goals") | SUPPORTED |
| 6 | Tim Barnes, a Chicago financial analyst, blogged as Vic Ferrari at Irreverent Oiler Fans | Wikipedia Corsi (statistic) citing McKenzie/TSN 2014-10-06; RMNB 2014-10-11 (Barnes "also goes by the name Vic Ferrari", ran Irreverent Oilers Fans, lived in Chicago, finance) | SUPPORTED |
| 7 | Ferrari heard Darcy Regier talk about shot attempts on the radio; considered "Regier" then "Ruff" number; chose Jim Corsi's photo on the Sabres website; "I just liked his moustache" | McKenzie excerpt (Hockey Confidential) quoted by Die By The Blade, 2014-10-06; Wikipedia | SUPPORTED |
| 8 | Jim Corsi was the Sabres' longtime goaltending coach | McKenzie excerpt ("long-time Buffalo Sabre goalie coach"); NBC Sports 2010-04-30 | SUPPORTED |
| 9 | Corsi added shots on goal, missed shots and blocked shots to measure goalie workload, since shots on goal alone left part of it out; explained to NBC Sports | NBC Sports 2010-04-30 (quotes Corsi on goalie workload and shots against); McKenzie excerpt | SUPPORTED |
| 10 | Ferrari didn't know about Corsi's workload count until McKenzie told him in a 2014 interview | McKenzie excerpt via Die By The Blade ("had no idea ... until I told him"; interview in April 2014) | SUPPORTED |
| 11 | Jim Corsi played 26 games in goal for the Oilers in 1979-80 | Hockey-Reference player page (raw `hockeyref_jim_corsi_player_page_dl2026-10-09.html`) | SUPPORTED |
| 12 | The stat was born on an Oilers blog | Irreverent Oiler Fans is an Oilers fan blog (RMNB; CNS Maryland 2017-02-03) | SUPPORTED |
| 13 | Corsi in use on the Alberta blogs by November 2007, when Matt Fenwick proposed dropping blocked shots | Battle of Alberta, "Flames thru 20", Nov 2007, posted by Matt (raw `battleofalberta_2007-11_archive_fetched_2026-10-09.html`; discusses "the two versions of the Corsi +/-"); Pension Plan Puppets 2012-07-25 identifies Matt Fenwick of Battle of Alberta | SUPPORTED |
| 14 | Washington hired Barnes as an analytics consultant in October 2014 | RMNB 2014-10-11 | SUPPORTED |
| 15 | In February 2015 NHL.com launched enhanced stats and renamed Corsi SAT | SI (Allan Muir) 2015-02-20 | SUPPORTED |
| 16 | League stats site still files it as SAT, with numbers back to 2009-10 | NHL stats API glossary ("SAT is available since 2009-10"); team percentages report field `satPct` (2026-10-09) | SUPPORTED |
| 17 | NST, MoneyPuck, Evolving-Hockey and Hockey-Reference publish Corsi | NST glossary; MoneyPuck glossary; Evolving-Hockey General Terms; Hockey-Reference analytics page ("Corsi (EV)" columns) | SUPPORTED |
| 18 | Built from the NHL play-by-play feed | Schuckers and Macdonald (RTSS events in public play-by-play files) | SUPPORTED |
| 19 | NHL counts only five-on-five for SAT | NHL glossary SAT ("Only 5-on-5 shot attempts are currently counted") | SUPPORTED |
| 20 | Missed shots include posts and crossbars; blocked attempts count for the shooting team | NHL glossary MsS and BkS entries | SUPPORTED |
| 21 | Goals count (every goal is a shot on goal); shootout attempts excluded | NST glossary (Corsi = goals, shots on net, misses and blocks, outside the shootout); MoneyPuck data (shotsOnGoalFor = saved + goals, checked) | SUPPORTED |
| 22 | Outside five-on-five excluded, so power plays and pulled-goalie (6-on-5) stretches are out | NHL glossary 5-on-5 only (a pulled goalie is not 5-on-5) | SUPPORTED |
| 23 | iCF keeps only a player's own attempts | NHL glossary iSAT/60 (player's own shot attempts) | SUPPORTED |
| 24 | Worked example 45 ÷ 85 = 52.9%, differential plus-five (invented, labelled) | arithmetic | SUPPORTED |
| 25 | NHL glossary: SAT a common proxy for puck possession, doesn't measure possession time | NHL glossary SAT and Puck possession entries | SUPPORTED |
| 26 | 2025-26 5v5 CF%: Carolina 59.8 (1st), Toronto 44.8 (last), Detroit 48.8 (21st) | W&W calc CF/(CF+CA) from attempt counts, MoneyPuck teams file | SUPPORTED (computed) |
| 27 | Detroit about two more attempts against than for a night | (3,959 − 3,775) / 82 = 2.2, MoneyPuck teams file | SUPPORTED (computed) |
| 28 | 598 skaters with 500+ 5v5 min: median on-ice CF% 49.6, top tenth ≥ 55.3, bottom tenth ≤ 45.1; K'Andre Miller 61.9 led; 20 of top 50 Hurricanes | W&W calc OnIce_F/A_shotAttempts, MoneyPuck skaters file 5on5 | SUPPORTED (computed) |
| 29 | Split-season test, 96 team-seasons 2023-24 to 2025-26: first-half CF% to second-half CF% r = 0.81; GF% to GF% 0.56 | W&W calc, game-by-game extract, first 41 vs last 41 games by date, Pearson r | SUPPORTED (computed) |
| 30 | NHL glossary credits possession with high correlation with winning and predicting future performance | NHL glossary Puck possession entry | SUPPORTED |
| 31 | First-half metric to second-half GF%: CF% 0.42, score-adjusted CF% 0.47, xGF% 0.52, GF% 0.56 | W&W calc, same extract | SUPPORTED (computed) |
| 32 | Corsi, with or without score adjustment, is the most stable number in the family | Same test: score-adjusted CF% 0.812, CF% 0.806, FF% 0.766, xGF% 0.723, SF% 0.696, GF% 0.559, PDO 0.364 | SUPPORTED (computed) |
| 33 | Detroit 2025-26: CF% 48.8 (21st), xGF% 48.8 (21st), GF% 45.5 (26th), shooting 8.1% on shots on goal, 30th of 32 | W&W calc, MoneyPuck teams file 5on5 (sh% = GF/SOG = 142/1,761) | SUPPORTED (computed) |
| 34 | Seider on-ice CF% 53.0, best among Detroit regulars (500+ min); off-ice 46.2; relative Corsi ranked 12th of 598 (plus-6.7) | W&W calc, MoneyPuck skaters file (OnIce and OffIce shot attempts) | SUPPORTED (computed) |
| 35 | Chiarot second among Detroit defensemen in 5v5 minutes (1,491 behind Seider's 1,612); 46.3 on, 50.4 off | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 36 | Trailing teams take more attempts and leading teams fewer; NHL calls it score effects | NHL glossary Score effects entry; MoneyPuck glossary (leading teams "sit back") | SUPPORTED |
| 37 | Detroit SAT% 53.5 trailing, 42.9 leading; league team average 52.4 and 47.4 | NHL team percentages report 2025-26 (satPctBehind, satPctAhead; mean of 32 teams) | SUPPORTED (computed) |
| 38 | NST and Evolving-Hockey both use McCurdy's score-adjustment method | NST glossary ("method created by Micah Blake McCurdy"); Evolving-Hockey General Terms | SUPPORTED |
| 39 | Score-adjusted Corsi held up better than raw in the split test | Rows 29 and 31 (0.812 vs 0.806 repeat; 0.47 vs 0.42 forecast) | SUPPORTED (computed) |
| 40 | xG beat raw Corsi as a forecast of second-half goal share, 0.52 to 0.42 | Row 31 | SUPPORTED (computed) |
| 41 | Rink effects 2007-08 through 2012-13 (six seasons): blocked shots 15 rinks, missed shots 9, shots on goal 2 | Schuckers and Macdonald, arXiv 1412.1035, Table 19 (raw PDF saved) | SUPPORTED |
| 42 | On-ice CF% correlated 0.74 with team CF% (598 skaters) | W&W calc, MoneyPuck skaters + teams files | SUPPORTED (computed) |
| 43 | Players with more offensive-zone starts should expect a slight bump in SAT% | NHL glossary OZ Start% entry | SUPPORTED |
| 44 | 2025-26, 32 teams: 5v5 GF% r = 0.86 with points %, CF% r = 0.57 | W&W calc, MoneyPuck teams file + NHL team summary pointPct | SUPPORTED (computed) |
| 45 | Live slot: team.json situations.5on5.corsiPct + leagueRanks.corsiPct_5on5, situations.all.corsiPct, dashboard xg_share_5v5, skaters fiveOnFive.onIceCorsiPct | TEMPLATE.md fields available today | SUPPORTED |
| 46 | Small-sample note: Corsi steadies faster than goals | Split test, first 10 games vs rest: CF% 0.68, GF% 0.36 | SUPPORTED (computed) |

Correction to the family brief: the man who named Corsi is Tim **Barnes** (Vic Ferrari), not "Tim Barnwell". No
reputable source ties a Barnwell to the name.

## Voice metrics (running prose, `--target barnwell_lean`)

Running prose, 1,267 words.

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 17.8 / 10.1 | 17-21 / ≥ 10 |
| Short / long sentences | 14% / 14% | 6-15% / ≤ 20% |
| Words per paragraph | 63 | 55-85 |
| One-sentence paragraphs | 10% | 5-12% |
| Contractions per 1k | 28.4 | ≥ 28 |
| I / you per 1k | 0.8 / 3.2 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.6 / 3.9 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 54.5 | 30-55 |
