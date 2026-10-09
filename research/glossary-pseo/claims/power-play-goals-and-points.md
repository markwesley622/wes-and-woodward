# Claims register: power-play-goals-and-points.json

Raw files (all downloaded 2026-10-09, `research/glossary-pseo/raw/`): `nhl_skater_summary_20252026.json`,
`nhl_skater_powerplay_20252026.json`, `nhl_skater_penalties_20252026.json`, `nhl_team_summary_20252026.json`,
`nhl_team_powerplay_20252026.json`, `nhl_team_goalsforbystrength_20252026.json`, `nhl_skater_summary_19331934_ppg_check.json`,
`nhl_records_season_ppg_20261009.json`, `nhl_records_career_ppg_20261009.json`, `nhl_records_det_season_ppg_20261009.json`,
`nhl_records_det_career_ppg_20261009.json`, `nhl_stats_glossary_20261009.json`, `nhl_rulebook_2025-26_downloaded_20261009.pdf`,
`mp_skaters_2025.csv` / `mp_teams_2025.csv` (situation list).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | PPG = goal scored while the other team is shorthanded by a penalty (5-on-4, 5-on-3, 4-on-3); PPP adds the assists | NHL stats glossary (PPG, PPP, PP TOI "man advantage", PP GF); team goals-for-by-strength columns 5On4/5On3/4On3 | SUPPORTED |
| 2 | 1,595 of 8,086 goals on the power play in 2025-26 (19.7%, about one in five) | W&W calc: sum ppGoals / sum goals, NHL skater summary 2025-26 (team summary goalsFor also sums to 8,086) | SUPPORTED (computed) |
| 3 | About 61% of Detroit's skater power-play time went to its top five | W&W calc: 1,249.5 PP min for DeBrincat/Seider/Raymond/Larkin/Kane ÷ (5 × 407.2 team PP min), NHL skater + team power-play reports | SUPPORTED (computed) |
| 4 | Tracked since 1933-34 (PPG, PPP, PPA) | NHL glossary firstSeasonForStat 19331934; API 1932-33 ppGoals null, 1933-34 populated | SUPPORTED |
| 5 | 2025-26 league PP% 21.1% = 1,595 goals on 7,555 power plays | W&W calc, NHL team power-play report | SUPPORTED (computed) |
| 6 | Most PPG 2025-26 Wyatt Johnston (DAL) 27, seven clear of Dorofeyev (20); most PPP McDavid 54 | NHL skater summary 2025-26 | SUPPORTED (computed) |
| 7 | Median forward 7 PPP / 3 PPG among 327 forwards with 60+ GP; top 10% cleared 10 PPG and 24 PPP; 61 had zero PPP | W&W calc, NHL skater summary (90th-percentile value) | SUPPORTED (computed) |
| 8 | Detroit 56 PPG, tied for 7th of 32 | NHL team power-play report | SUPPORTED (computed) |
| 9 | 1933-34: John Sorrell 10 PPG of 21 goals, four more than anyone; Ebbie Goodfellow (DET) tied second with six | NHL API 1933-34 skater summary sorted by ppGoals (Sorrell 10, Cook 6, Goodfellow 6) | SUPPORTED |
| 10 | Nov. 5, 1955 Béliveau three PPG on the same penalty in 44 seconds vs Boston; penalized player served full minor then; rule changed for 1956-57 | NHL.com "This date in NHL history, November 5" | SUPPORTED |
| 11 | Rule 16.2: when a team scores against an opponent shorthanded by a minor, the first minor ends | NHL Official Rules 2025-26, Rule 16.2 | SUPPORTED |
| 12 | A major doesn't end on a goal (Rule 20.2) | Rule 20.2 | SUPPORTED |
| 13 | NHL.com publishes PPG, PPP and PPA back to 1933-34; Hockey-Reference lists PP goals as "PP" | NHL glossary (PPA firstSeasonForStat 19331934); Hockey-Reference glossary | SUPPORTED |
| 14 | MoneyPuck's 5-on-4 bucket leaves out 5-on-3 and 4-on-3, which fall under "other" | MoneyPuck 2025-26 files: situation values are all/5on5/5on4/4on5/other only | SUPPORTED |
| 15 | Kerr 34 PPG in 1985-86 single-season record; Ovechkin 331 career leader | NHL API season and career queries sorted by ppGoals | SUPPORTED |
| 16 | Detroit season record 21 shared by Redmond (1973-74) and Ciccarelli (1992-93); Howe 209 franchise career high | NHL API franchiseId=12 queries (Shanahan's 20 in 1996-97 is HFD+DET combined, below 21) | SUPPORTED |
| 17 | NHL defines PP time as time with a man advantage; the advantage has to come from a penalty | NHL glossary PP TOI and even-strength definition ("no one is in the penalty box or both teams have been penalized equally") | SUPPORTED |
| 18 | A goalie pulled for an extra attacker leaves teams even in the league's books; a 6-on-5 goal is even strength | NHL glossary even strength = equal numbers of players; W&W calc: of 725 empty-net/extra-attacker/penalty-shot goals only 30 were PPG and 31 SHG, the other 664 are in evGoals | SUPPORTED (computed) |
| 19 | 2025-26: 1,444 PPG at 5-on-4, 87 at 5-on-3, 34 at 4-on-3; the other 30 in empty-net/extra-attacker/penalty-shot columns | NHL team goals-for-by-strength report; 1,595 − 1,565 = 30 | SUPPORTED (computed) |
| 20 | PPA split into PPA1/PPA2 back to 1997-98; PPP/60 back to 2009-10 | NHL glossary firstSeasonForStat | SUPPORTED |
| 21 | Four goals in five happen somewhere other than the power play | Row 2 | SUPPORTED (computed) |
| 22 | DeBrincat 15 PPG tied 7th; Larkin 14 tied 10th | NHL skater summary 2025-26 ranks | SUPPORTED (computed) |
| 23 | 161 D with 60+ GP: median 1 PPP, 71 at zero, top 10% 18; Seider 28 tied 4th behind Hughes 34, Bouchard 33, Makar 29; 47% of his 60 points | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 24 | Detroit converted 22.6% (12th); 142 goals at 5v5 third-fewest; PP produced 23.4% of DET goals, fifth-highest share | NHL team power-play, team summary, goals-for-by-strength reports | SUPPORTED (computed) |
| 25 | Top five each averaged 3:11-3:20 PP a night; nobody else who spent the full year in Detroit topped 1:51 (van Riemsdyk) | NHL skater power-play report, ppTimeOnIcePerGame, teamAbbrevs = DET only | SUPPORTED (computed) |
| 26 | Those five put up 121 PPP; no other Red Wing had more than 11 | NHL skater summary (van Riemsdyk 11; Faulk 9 and Perron 8 combined with other teams) | SUPPORTED (computed) |
| 27 | Seider 6.41 PPP/60 vs DeBrincat 5.06; Seider had a point on more PP goals (28 vs 23), DeBrincat finished more (15 vs 3) | NHL skater power-play report | SUPPORTED (computed) |
| 28 | DeBrincat 27% of points on PP, Raymond 36%, Seider 47%; median forward with 60 GP 19% | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 29 | Second-unit forward gets about half the minutes; Copp 107 PP minutes | NHL skater power-play report (Copp 1:21/GP vs top unit 3:11-3:20; 107 min) | SUPPORTED (computed) |
| 30 | Raymond drew 26 penalties, the team high | NHL skater penalties report | SUPPORTED (computed) |
| 31 | 87 goals at 5-on-3 sit in the same column as 1,444 at 5-on-4 | Row 19 | SUPPORTED (computed) |
| 32 | DeBrincat played 273 PP minutes, less than five full games of ice | NHL skater power-play report (16,386 s); 273 / 60 = 4.6 | SUPPORTED (computed) |
| 33 | Live slot: MoneyPuck 5-on-4 numbers exclude 5-on-3 time | MoneyPuck situation definitions (row 14) | SUPPORTED |
| 34 | FAQ: NHL glossary keeps PPG for power-play goals and writes points per game as P/GP | NHL glossary entries PPG and P/GP | SUPPORTED |
| 35 | FAQ: a delayed minor isn't imposed if the other team scores on the play; majors and match penalties still are | Rule 15.2 | SUPPORTED |

Worked example uses invented round numbers and says so.

## Voice metrics (running prose, `--target barnwell_lean`)

1,370 words. Sentence mean 19.0 / SD 10.4; short 10% / long 15%; 60 words per paragraph; one-sentence paragraphs 9%;
contractions 38.0/1k; I 0.0; you 3.6; questions 1.5; parentheses 3.6; intensifiers 0.0; transition openers 1%;
numbers 53.3/1k; hedges 0.0. All in range. ai-content-detection: no contrast frames, payoff colons, unicode artifacts or
negation pivots; remaining hints `uniform_paragraph_structure`, `repeated_ngrams` (template + metric names).

Proposed hover short: Goals (PPG) and points (PPP) scored while the other team is shorthanded by a penalty. They show who a coach trusts with the man advantage.

(Reason: the current "more skaters on the ice than its opponent" also describes a 6-on-5 with the goalie pulled, which the NHL files as even strength.)
