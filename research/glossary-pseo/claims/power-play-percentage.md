# Claims register: power-play-percentage.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/nhl_team_powerplay_20252026_ppct_page.json`
(NHL stats API team power-play report, 2025-26), `nhl_team_powerplay_allseasons_to_20252026.json` (every regular
season), `nhl_team_summary_20252026_pp_pk_gd.json` and `mp_teams_2025.csv` (MoneyPuck season "2025" = 2025-26),
all downloaded 2026-10-09. Rules from the NHL's Official Rules 2025-2026 PDF (media.nhl.com), fetched the same day.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | PP% = power-play goals ÷ power-play opportunities | NHL.com hockey glossary ("Total number of power-play goals divided by total number of power-play opportunities"); Hockey-Reference glossary | SUPPORTED |
| 2 | League PP% 21.1% in 2025-26 (1,595 goals on 7,555 opportunities); median team 21.0% ("a hair lower") | W&W calc, NHL power-play report | SUPPORTED (computed) |
| 3 | About one goal in five came on the power play (19.7%: 1,595 of 8,086) | W&W calc, power-play report + team summary goals | SUPPORTED (computed) |
| 4 | Detroit fell from 27.0% (2024-25, 4th) to 22.6% (2025-26, 12th); ~11 goals at last season's 248 opportunities | All-seasons report (64/237; 56/248); 0.270 × 248 − 56 = 11.0 | SUPPORTED (computed) |
| 5 | Béliveau, Nov. 5, 1955: three power-play goals vs Boston in 44 seconds, all on the same penalty; NHL changed the rule for 1956-57 so a penalized player returns when a goal is scored | NHL.com This Date in NHL History, Nov. 5 (1955 entry) | SUPPORTED |
| 6 | Before the change a penalized player served his full minor regardless of goals | Implied by the NHL entry (rule change "allowing a penalized player to return ... if a goal is scored") | SUPPORTED |
| 7 | Today's rulebook ends the minor with the least time left when the short-handed team is scored on (Rule 16.2); majors don't end on a goal (Rule 20.2); coincidental minors don't make either side short-handed (16.2) | NHL Official Rules 2025-2026, Rules 16.2, 20.2 | SUPPORTED |
| 8 | NHL stats database carries PP opportunities for every team from 1977-78 on | All-seasons report (continuous non-null ppOpportunities from 19771978) | SUPPORTED (computed) |
| 9 | Montreal 1977-78 31.9% stood until Edmonton 2022-23 32.4% (89 of 275) | All-seasons report (19771978 MTL 73/229; 20222023 EDM 89/275) | SUPPORTED (computed) |
| 10 | Only five of 1,282 team seasons since 1977-78 (48+ GP) cleared 30%; Edmonton's 30.6% in 2025-26 is one | All-seasons report | SUPPORTED (computed) |
| 11 | NHL stats site publishes a net version subtracting shorthanded goals allowed | Power-play report column powerPlayNetPct = (PPG − SHGA) ÷ PPO for all 32 teams | SUPPORTED (computed) |
| 12 | Worked example (invented): 55/250 = 22.0%; net (55 − 5)/250 = 20.0%; 200 × 22% = 44, eleven fewer | arithmetic | SUPPORTED |
| 13 | Edmonton best 30.6% (68/222), Dallas 28.6%, Philadelphia last 15.7% (37/235); gap ≈ 35 goals over 236 opportunities | Power-play report; (0.306 − 0.157) × 236 = 35.1 | SUPPORTED (computed) |
| 14 | League scored 7.32 goals per 60 at 5v4 vs 2.48 per team at 5v5 (about three times) | W&W calc, MoneyPuck teams file (5on4, 5on5) | SUPPORTED (computed) |
| 15 | Average team spent under five minutes a game on the power play (4.74) | Power-play report, ppTimeOnIcePerGame × GP summed ÷ 2,624 team-games | SUPPORTED (computed) |
| 16 | Detroit 22.6% (12th); 248 opportunities tied 7th-most; 56 PPG tied 7th; seventh in 5v4 xGF/60 (8.18) | Power-play report; MoneyPuck teams file 5on4 | SUPPORTED (computed) |
| 17 | PP% year-to-year r = 0.37 over the last ten seasons (310 team pairs, 2015-16 to 2025-26) | W&W calc, all-seasons report, same franchise ID | SUPPORTED (computed) |
| 18 | Toronto fewest PPO (197) at 21.3%, 42 PPG; Florida most (266) at 19.5%, 52 PPG | Power-play report | SUPPORTED (computed) |
| 19 | PP% vs 5v4 xGF/60 r = 0.72 across 32 teams | W&W calc, power-play report + MoneyPuck 5on4 | SUPPORTED (computed) |
| 20 | Colorado, best 5v5 team by xG share, 17.1% (27th); 40 5v4 goals on 50.1 xG | Power-play report; MoneyPuck 5on4; xG page register row 4 (Colorado 56.9%, 1st) | SUPPORTED (computed) |
| 21 | Colorado 13 SHGA (most), net 12.2%; Detroit 5 SHGA, net 20.6%; Washington 17.8% (25th) → 13.3% net (29th) | Power-play report | SUPPORTED (computed) |
| 22 | Same rate, 266 vs 197 opportunities ≈ 15 goals apart (at 21.1%) | 0.211 × 69 = 14.6 | SUPPORTED (computed) |
| 23 | Colorado's gross and net rates almost five points apart (17.1 vs 12.2) | Power-play report | SUPPORTED (computed) |
| 24 | ~240 power plays a season; two or three goals ≈ one point; middle third (ranks 11-21) within about four points (23.1 to 19.5) | Power-play report (median 236) | SUPPORTED (computed) |
| 25 | Edmonton 63 5v4 goals on 52.0 expected, 11 above | MoneyPuck teams file 5on4 | SUPPORTED (computed) |
| 26 | FAQ: minor two minutes, double minor four, major five; a goal ends the earliest-expiring minor; a major runs its full five | NHL Official Rules 2025-2026, Rules 16.1, 16.2, 18.1, 20.1, 20.2 | SUPPORTED |
| 27 | FAQ: average power play lasted about 1:39 in 2025-26 | 12,442 PP minutes ÷ 7,555 opportunities = 1.65 min (power-play report) | SUPPORTED (computed) |

Live slot: dashboard tile `pp_xgf60`, `situations.5on4.goalsFor` and `situations.5on4.xGoalsFor` (rank
`leagueRanks.xGoalsFor_5on4`), all MoneyPuck, default credit. No leaderboard. Wanted: the NHL's team
`powerPlayPct`, `ppOpportunities`, `powerPlayGoalsFor`, `powerPlayNetPct` (team power-play report) with league ranks,
and skater `ppGoals`/`ppPoints`/`ppTimeOnIce` for a Red Wings leaderboard.

## Voice metrics (running prose, `--target barnwell_lean`, 1,159 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19 / 10.1 | 17-21 / ≥ 10 |
| Short / long sentences | 11% / 16% | 6-15% / ≤ 20% |
| Words per paragraph | 58 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 34.5 | ≥ 28 |
| I / you per 1k | 0.0 / 3.5 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.7 / 4.3 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 54.4 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts, question fragments, sentence-negation
pivots or false ranges. Remaining hints (`uniform_paragraph_structure`, `repeated_ngrams`) come from the fixed
template and metric names. `gate_glossary.py power-play-percentage`: PASS. JSON parses.
Hardest metric: numbers per 1k (first draft 81), then sentence-length variety; season ranges and per-60 labels each count as numbers, so benchmarks moved into words.

Hover short: the current `short` agrees with the page. No change proposed.
