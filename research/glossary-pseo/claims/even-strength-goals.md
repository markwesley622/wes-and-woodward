# Claims register: even-strength-goals.json

Raw files (downloaded 2026-10-09, `research/glossary-pseo/raw/`): `nhl_skater_summary_20252026.json`,
`nhl_skater_summary_20242025.json`, `nhl_skater_powerplay_20252026.json`, `nhl_team_summary_20252026.json`,
`nhl_team_powerplay_20252026.json`, `nhl_team_penaltykill_20252026.json`, `nhl_team_goalsforbystrength_20252026.json`,
`nhl_team_goalsagainstbystrength_20252026.json`, `nhl_records_season_evg_20261009.json`, `nhl_records_career_evg_20261009.json`,
`nhl_records_det_season_evg_20261009.json`, `nhl_stats_glossary_20261009.json`, `nhl_rulebook_2025-26_downloaded_20261009.pdf`,
`mp_teams_2025.csv`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | EVG = goal scored with the same number of players on each side, at 5-on-5, 4-on-4 or 3-on-3; EVP adds assists | NHL glossary even-strength stats ("equal numbers of players... includes 5-on-5, 4-on-4, and 3-on-3"), EVG, EVP | SUPPORTED |
| 2 | Even-strength column is where to read a scorer without his PP time | NHL glossary: comparing at even strength or 5-on-5 means totals "will not be skewed by differing amounts of special teams (particularly power play) time" | SUPPORTED |
| 3 | 77.7% of goals at even strength in 2025-26 (6,286 of 8,086) | W&W calc, NHL skater summary (evGoals sum) | SUPPORTED (computed) |
| 4 | 66.3% of all goals at 5-on-5 (5,362) | NHL team goals-for-by-strength (goalsFor5On5 sum) | SUPPORTED (computed) |
| 5 | Covers 5v5/4v4/3v3 plus most empty-net goals | Row 1; row 20 calc | SUPPORTED (computed) |
| 6 | MacKinnon led EVG (42) and EVP (97) | NHL skater summary 2025-26 | SUPPORTED (computed) |
| 7 | Median forward 12 EVG and 30 EVP among 327 with 60+ GP | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 8 | Detroit 180 EV goals, 23rd; league median 197 | W&W calc: goalsFor − PPG − SHG per team (team summary, power-play, penalty-kill reports) | SUPPORTED (computed) |
| 9 | Stats database files every goal as EV, PP or SH, back as far as its PP records (1933-34) | NHL glossary EVG/PPG/SHG firstSeasonForStat 19331934; evGoals + ppGoals + shGoals = goals in 2025-26 | SUPPORTED |
| 10 | Gretzky 68 EVG in 1981-82 single-season record; 617 career leader ahead of Ovechkin (593) and Howe (566) | NHL API season and career queries sorted by evGoals | SUPPORTED |
| 11 | Yzerman 45 EVG in 1988-89 Detroit season record | NHL API franchiseId=12 season query | SUPPORTED |
| 12 | Even strength = same number of players, nobody in the box or both sides lost the same number | NHL glossary even-strength stats | SUPPORTED |
| 13 | Coincidental minors don't make either team shorthanded (Rule 16.2); regular-season OT is 3-on-3 (Rule 84.1) | NHL Official Rules 2025-26 | SUPPORTED |
| 14 | Analysts mostly work at 5-on-5; glossary explains the skew; 5-on-5 excludes goalie-pulled time | NHL glossary 5-on-5 stats ("Many enhanced stats concentrate on 5-on-5 play"; goalie pulled doesn't qualify) | SUPPORTED |
| 15 | MoneyPuck files carry a 5on5 bucket and the site uses it for most team numbers | MoneyPuck files; `data/site/team.json` situations.5on5, `dashboard.json` tiles | SUPPORTED |
| 16 | A goal with a goalie pulled for an extra attacker counts as EV when nobody's in the box | W&W calc (row 20) + NHL glossary definition | SUPPORTED (computed) |
| 17 | EVG = goals − PPG − SHG; EV GF% = EV GF ÷ (EV GF + EV GA) | NHL glossary (EV GF%); 2025-26 sums reconcile exactly | SUPPORTED |
| 18 | EVP tracked back to 1933-34; on-ice EV GF/GA back to 2009-10 | NHL glossary firstSeasonForStat | SUPPORTED |
| 19 | 2025-26: 5,362 EV goals at 5v5, 178 at 3v3, 82 at 4v4 | NHL team goals-for-by-strength report | SUPPORTED (computed) |
| 20 | The other 664 came with a net empty, an extra attacker on, or on a penalty shot (about a seventh of the column) | W&W calc: 6,286 − 5,622 = 664; empty-net 508 + extra-attacker 211 + penalty-shot 6 = 725, minus 30 PP and 31 SH | SUPPORTED (computed) |
| 21 | Detroit's first unit got 3+ PP minutes a night, its fourth line almost none | NHL skater power-play report (top five 3:11-3:20; Rasmussen 0:14, Appleton 0:04) | SUPPORTED (computed) |
| 22 | DeBrincat 62 EVP ranked 9th, 26 EVG tied 21st; 15 of his 41 goals on the PP | NHL skater summary | SUPPORTED (computed) |
| 23 | Detroit 142 at 5v5, third-fewest | NHL team goals-for-by-strength | SUPPORTED (computed) |
| 24 | EV share of Detroit goals 75.3%, smaller than all but eight teams | W&W calc: 180 / 239; rank 24 of 32 | SUPPORTED (computed) |
| 25 | Special teams made back only part of the EV deficit | EV goal differential −21 vs special-teams net +6 (56 PPG + 3 SHG − 48 PPGA − 5 SHGA); total −15 | SUPPORTED (computed) |
| 26 | Year-to-year (379 skaters, 60+ GP both seasons): EVP 0.77, EVG 0.71, points 0.86, goals 0.80 | W&W calc (Pearson), NHL skater summaries 2024-25 and 2025-26 | SUPPORTED (computed) |
| 27 | Hockey-Graphs study: after about 20 games (about a quarter of a season), a team's xG beats its goals at forecasting future goals | Hockey-Graphs 2015-10-01 (same finding as expected-goals register row 8) | SUPPORTED |
| 28 | Raymond nine points behind DeBrincat (76 vs 85); EV gap 13 (62 vs 49); Raymond 27 PPP vs 23; Raymond 36% of points on PP vs DeBrincat 27% | NHL skater summary | SUPPORTED (computed) |
| 29 | MoneyPuck had Detroit at 161.1 5v5 xGF, 19.1 short; scoring those puts 180 at the median of 197 | MoneyPuck teams file 5on5 (expected-goals register row 20); 180 + 19.1 = 199.1 | SUPPORTED (computed) |
| 30 | Seider 60 points tied 11th among D; 28 PPP tied 4th; 32 EVP vs D median 22; Bouchard 60 EVP | NHL skater summary (161 D with 60+ GP for the median) | SUPPORTED (computed) |
| 31 | 924 of 6,286 EV goals weren't scored at 5v5 | 6,286 − 5,362 | SUPPORTED (computed) |
| 32 | 508 empty-net goals; the NHL counted most as EV | NHL goals-for-by-strength (508); at most 61 of the 725 EN/EA/PS goals were PP or SH, so at least 447 EN goals were EV | SUPPORTED (computed) |
| 33 | EVG credits the scorer, EVP the passers; other skaters get nothing | NHL glossary EVG/EVP (player's own) vs EV GF (on-ice) | SUPPORTED |
| 34 | NHL publishes EV TOI back to 1997-98 | NHL glossary EV TOI ("available since 1997-98") | SUPPORTED |
| 35 | MoneyPuck warns one season of finishing carries a lot of luck | MoneyPuck about, shooting talent section (expected-goals register row 22) | SUPPORTED |
| 36 | FAQ: OT is 3-on-3; a penalty in OT gives the other team a fourth skater, so that goal is a PPG | Rule 84.1 ("If a team is penalized in overtime, teams play 4 on 3") | SUPPORTED |
| 37 | FAQ: the NHL skater summary report carries EVG and EVP for every season back to 1933-34 | NHL stats API skater summary fields evGoals/evPoints; 1933-34 populated | SUPPORTED |
| 38 | Live slot: 5v5 tiles from MoneyPuck; leaders table goals/points/GP from the NHL API, 5v5 columns from MoneyPuck | `data/site/team.json`, `skaters.json`; lead's 10/9 note on NHL API fields | SUPPORTED |

Worked example uses invented round numbers and says so.

## Voice metrics (running prose, `--target barnwell_lean`)

1,271 words. Sentence mean 19.6 / SD 10.5; short 14% / long 20%; 58 words per paragraph; one-sentence paragraphs 9%;
contractions 39.3/1k; I 0.0; you 3.1; questions 2.4; parentheses 3.1; intensifiers 0.0; transition openers 0%;
numbers 53.5/1k; hedges 0.0. All in range (long sentences at the 20% ceiling). ai-content-detection: no contrast frames,
payoff colons, unicode artifacts or negation pivots; hints `uniform_paragraph_structure`, `repeated_ngrams`.

Proposed hover short: Goals (EVG) and points (EVP) scored when neither team is shorthanded by a penalty, including 4-on-4, 3-on-3 and most empty-net goals. Most scoring happens here.

(Reason: "the same number of skaters on each side" misses goalie-pulled 6-on-5 goals, which the NHL files as even strength; 664 such goals in 2025-26.)
