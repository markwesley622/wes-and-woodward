# Claims register: shorthanded-goals-and-points.json

Raw files (downloaded 2026-10-09, `research/glossary-pseo/raw/`): `nhl_skater_summary_20252026.json`,
`nhl_skater_summary_20242025.json`, `nhl_skater_penaltykill_20252026.json`, `nhl_team_penaltykill_20252026.json`,
`nhl_team_powerplay_20252026.json`, `nhl_team_goalsforbystrength_20252026.json`, `nhl_records_season_shg_20261009.json`,
`nhl_records_career_shg_20261009.json`, `nhl_records_det_season_shg_20261009.json`, `nhl_records_det_career_shg_20261009.json`,
`nhl_stats_glossary_20261009.json`, `nhl_rulebook_2025-26_downloaded_20261009.pdf`, `mp_teams_2025.csv`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | SHG = goal scored by a team that's a man down to a penalty; SHP adds the assists | NHL glossary (SHG, SHP, SH GF); Rule 16.2 short-handed definition | SUPPORTED |
| 2 | Rarest goals by game state, about one in 40 last season | W&W calc: 205 SHG / 8,086 goals = 2.5% (vs 1,595 PP, 6,286 EV), NHL skater summary | SUPPORTED (computed) |
| 3 | NHL glossary notes shorthanded shots often come on breakaways and odd-man rushes | NHL glossary, SH Sv% entry | SUPPORTED |
| 4 | A shorthanded goal doesn't end the penalty; the power play keeps going | Rule 16.2 (only a goal by the opposing team terminates a minor) | SUPPORTED |
| 5 | Spelled short-handed in the rulebook | Rule 16.2 text | SUPPORTED |
| 6 | Tracked since 1933-34 | NHL glossary SHG/SHP/SHA firstSeasonForStat 19331934 | SUPPORTED |
| 7 | 36.9 power plays per shorthanded goal in 2025-26 | W&W calc: 7,555 PP opportunities / 205, NHL team power-play report | SUPPORTED (computed) |
| 8 | Most SHG Ryan McLeod (BUF) 5, on 10 SH shots; most SHP Jean-Gabriel Pageau (NYI) 7 | NHL skater summary + penalty-kill report | SUPPORTED (computed) |
| 9 | Carolina 12 SHG most by a team; Colorado, Boston, Seattle 2 each | NHL team penalty-kill report | SUPPORTED (computed) |
| 10 | Detroit 3 SHG (tied fourth-fewest), 5 allowed on its own PP; median team allowed 6 | NHL team penalty-kill and power-play reports | SUPPORTED (computed) |
| 11 | Lemieux 13 SHG in 1988-89 single-season record; Gretzky 73 career leader; Yzerman third with 50, all for Detroit; Dionne 10 in 1974-75 Detroit season record | NHL API season, career and franchiseId=12 queries (Yzerman's career and Detroit totals are both 50) | SUPPORTED |
| 12 | The record holders are all centers | Lemieux, Gretzky, Yzerman, Dionne (all C in the NHL API positionCode) | SUPPORTED |
| 13 | NHL.com publishes SHG, SHP, SHA back to 1933-34; Hockey-Reference lists SH goals as "SH" | NHL glossary; Hockey-Reference glossary | SUPPORTED |
| 14 | Net PP% subtracts SH goals against; Net PK% credits SH goals for | NHL glossary Net PP%, Net PK% | SUPPORTED |
| 15 | MoneyPuck files carry a 4-on-5 bucket | MoneyPuck 2025-26 files, situation 4on5 | SUPPORTED |
| 16 | Example: all four SH skaters get a plus, the five PP skaters a minus | NHL glossary +/- ("All the skaters on the ice receive a plus or minus when an even-strength goal or shorthanded goal is scored") | SUPPORTED |
| 17 | 2025-26: 173 SHG at 4-on-5, 1 at 3-on-4, other 31 in empty-net/extra-attacker/penalty-shot columns | NHL team goals-for-by-strength report (174 by manpower; 205 − 174 = 31) | SUPPORTED (computed) |
| 18 | SHA1/SHA2 back to 1997-98; SHP/60 back to 2009-10 | NHL glossary firstSeasonForStat | SUPPORTED |
| 19 | PP teams outscored PK teams nearly eight to one (1,595 vs 205) | NHL skater summary sums; 1,595 / 205 = 7.8 | SUPPORTED (computed) |
| 20 | 222 of 327 forwards with 60+ GP had zero SHG; 13 skaters had three or more | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 21 | Average team scored one about every 13 games | W&W calc: 2,624 team games (32 × 82, 2025-26) / 205 = 12.8 | SUPPORTED (computed) |
| 22 | Larkin, Rasmussen, A. Johansson one SHG each; Johansson's two SHP led Detroit | NHL skater summary (DET rows) | SUPPORTED (computed) |
| 23 | Detroit PK 77.1%, 23rd; gave up 48 PP goals | NHL team penalty-kill report | SUPPORTED (computed) |
| 24 | 379 skaters with 60+ GP in both 2024-25 and 2025-26: year-to-year correlation SHG 0.44, PPG 0.74, goals 0.80 | W&W calc (Pearson), NHL skater summaries 2024-25 and 2025-26 | SUPPORTED (computed) |
| 25 | Colorado allowed 13 SHG (most); PP% 17.1% (27th) to net 12.2% (31st) | NHL team power-play report (powerPlayPct, powerPlayNetPct) | SUPPORTED (computed) |
| 26 | Detroit PP% 22.6% to net 20.6% | NHL team power-play report | SUPPORTED (computed) |
| 27 | Carolina PK 80.5% (11th) to net 85.7% (3rd), an eight-spot climb; Detroit 77.1% to net 78.6% | NHL team penalty-kill report (penaltyKillPct, penaltyKillNetPct) | SUPPORTED (computed) |
| 28 | Detroit's heaviest PK minutes: Chiarot 146, Seider 130, Compher 126, none with an SHP; Johansson two SHP in 111 minutes | NHL skater penalty-kill report | SUPPORTED (computed) |
| 29 | 190 of 327 regular forwards had zero SHP | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 30 | Two SHG put a player in the league's top 45 | W&W calc: 45 skaters with 2+ SHG | SUPPORTED (computed) |
| 31 | PP GA/60 measures penalty-killing effectiveness | NHL glossary PP GA/60 | SUPPORTED |
| 32 | Penalty killers took 1,998 SH shots on goal, about one per four power plays; no skater took more than 23 (Backlund) | NHL skater penalty-kill report (shShots); 7,555 / 1,998 = 3.8 | SUPPORTED (computed) |
| 33 | An empty-net goal against a PP that pulled its goalie counts as an SHG | Row 17 (31 SHG outside the manpower columns) + Rule 16.2 definition | SUPPORTED (computed) |
| 34 | NHL glossary calls SH save percentage volatile because goalies face so few SH shots | NHL glossary SH Sv% | SUPPORTED |
| 35 | FAQ: coincidental minors don't make either side short-handed; a 4-on-4 goal is even strength | Rule 16.2; NHL glossary even-strength stats (includes 4-on-4) | SUPPORTED |
| 36 | Live slot: MoneyPuck 4-on-5 numbers | `data/site/team.json` situations.4on5; MoneyPuck files | SUPPORTED |

Worked example uses invented round numbers and says so.

## Voice metrics (running prose, `--target barnwell_lean`)

1,202 words. Sentence mean 17.7 / SD 10.0; short 12% / long 16%; 57 words per paragraph; one-sentence paragraphs 5%;
contractions 30.8/1k; I 0.0; you 3.3; questions 1.7; parentheses 6.7; intensifiers 0.0; transition openers 0%;
numbers 51.6/1k; hedges 0.0. All in range (SD and one-sentence paragraphs sit at the edge). ai-content-detection: no
contrast frames, payoff colons, unicode artifacts or negation pivots; hints `uniform_paragraph_structure`, `repeated_ngrams`.

Proposed hover short: Goals (SHG) and points (SHP) scored while a player's own team is shorthanded by a penalty. They're rare and swing a lot from one season to the next.

(Reason: "fewer skaters on the ice than its opponent" also covers a team facing a pulled goalie, which the NHL files as even strength; "usually on a penalty kill" undersells it, since an SHG is always scored while killing a penalty.)
