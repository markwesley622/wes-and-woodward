# Claims register: penalty-kill-percentage.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/nhl_team_penaltykill_20252026_pkpct_page.json`
(NHL stats API team penalty-kill report, 2025-26), `nhl_team_penaltykill_allseasons_to_20252026.json`,
`nhl_team_powerplay_allseasons_to_20252026.json` and `mp_teams_2025.csv` (MoneyPuck season "2025" = 2025-26), all
downloaded 2026-10-09. Rules from the NHL's Official Rules 2025-2026 PDF, fetched the same day.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | PK% = share of opponents' power plays killed without a goal = (times shorthanded − PPGA) ÷ times shorthanded; mirror image of PP% | NHL.com hockey glossary (power plays killed ÷ shorthanded situations); Hockey-Reference glossary ((PPOA − PPA) ÷ PPOA) | SUPPORTED |
| 2 | Detroit's 23rd-ranked kill allowed fewer PP goals (48) than 18 other teams | Penalty-kill report (12 teams fewer, CGY tied, 18 more) | SUPPORTED (computed) |
| 3 | Before 1956-57 a team stayed short-handed for the full minor; Béliveau's three PP goals in 44 seconds vs Boston, November 1955, led to the change the next season | NHL.com This Date in NHL History, Nov. 5 (1955) | SUPPORTED |
| 4 | Rule 16.2 ends the minor with the least time left when a short-handed team is scored on; worst case on a single minor is one goal | NHL Official Rules 2025-2026, Rule 16.2 | SUPPORTED |
| 5 | Database carries kill rates every season from 1977-78 | All-seasons report (continuous timesShorthanded from 19771978) | SUPPORTED (computed) |
| 6 | New Jersey 89.6% in 2011-12 (27 PPGA in 259) best on record (48+ GP) | All-seasons report | SUPPORTED (computed) |
| 7 | League-wide kills peaked in the late 1990s (84.9%, 1997-98) and were 78.9% in 2025-26; power plays scoring more since | All-seasons reports (league PP% 15.1% in 1997-98, 21.1% in 2025-26) | SUPPORTED (computed) |
| 8 | NHL stats site publishes a net version crediting shorthanded goals | Penalty-kill report column penaltyKillNetPct = (TSH − PPGA + SHGF) ÷ TSH for all 32 teams | SUPPORTED (computed) |
| 9 | Worked example (invented): 240 TSH, 48 PPGA → 192 kills, 80.0%; +8 SHG → 83.3% net; 200 TSH at 80% → 40 goals | arithmetic | SUPPORTED |
| 10 | League PP% 21.1% and PK% 78.9% sum to exactly 100 (1,595 goals; 7,555 chances on both sides) | Power-play and penalty-kill reports (totals identical) | SUPPORTED (computed) |
| 11 | Median kill 79.6%; Colorado 84.6% (36/234) best; Vancouver 71.5% (65/228) last; gap ≈ 31 goals over 236 TSH | Penalty-kill report; (0.846 − 0.715) × 236 = 30.9 | SUPPORTED (computed) |
| 12 | PP gap between best and worst is the same order (≈ 35 goals) | Power-play page row 13 | SUPPORTED (computed) |
| 13 | Detroit 77.1% (23rd), up from 70.1% (32nd, 55/184) in 2024-25; 210 TSH third-fewest (VGK 204, NJD 208); 48 PPGA tied 13th-fewest | Penalty-kill reports | SUPPORTED (computed) |
| 14 | Detroit 28th in 4v5 xGA per 60 (8.00); 43 4v5 goals on 43.7 xGA (goaltending about average) | W&W calc, MoneyPuck teams file 4on5 | SUPPORTED (computed) |
| 15 | PK% year-to-year r = 0.26 vs PP% 0.37 over the last ten seasons (310 pairs); times shorthanded per game r = 0.51 | W&W calc, all-seasons reports, same franchise ID | SUPPORTED (computed) |
| 16 | Boston 278 TSH (most), 64 PPGA, 77.0%; Detroit almost the same rate with 48; 16-goal gap from penalties taken | Penalty-kill report | SUPPORTED (computed) |
| 17 | PK% vs 4v5 xGA/60 r = −0.46 (PP pair 0.72) | W&W calc, penalty-kill report + MoneyPuck 4on5 | SUPPORTED (computed) |
| 18 | Chicago last in 5v5 xG share, second-best kill (83.6%), 36 4v5 goals on 46.5 xGA | Penalty-kill report; MoneyPuck 4on5; xG page register row 4 (Chicago 42.4%, last) | SUPPORTED (computed) |
| 19 | Carolina 12 SHG (most), 80.5% → 85.7% net; Buffalo 11 SHG, best net rate (86.6%); Detroit 3 SHG, 77.1% → 78.6% | Penalty-kill report | SUPPORTED (computed) |
| 20 | Ottawa lowest 4v5 xGA/60 (6.09), 29th in PK% (75.7%), 48 goals on 37.3 xGA | MoneyPuck 4on5; penalty-kill report | SUPPORTED (computed) |
| 21 | ~235 TSH a season (median 236); two goals ≈ 0.85 points | Penalty-kill report | SUPPORTED (computed) |

Live slot: dashboard tile `pk_xga60`, `situations.4on5.goalsAgainst` and `situations.4on5.xGoalsAgainst`, all
MoneyPuck, default credit. No leaderboard. Wanted: the NHL's team `penaltyKillPct`, `timesShorthanded`,
`ppGoalsAgainst`, `penaltyKillNetPct` (team penalty-kill report) with league ranks, and a 4on5 xGA rank in
`leagueRanks`.

## Voice metrics (running prose, `--target barnwell_lean`, 1,043 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.3 / 10.3 | 17-21 / ≥ 10 |
| Short / long sentences | 7% / 17% | 6-15% / ≤ 20% |
| Words per paragraph | 58 | 55-85 |
| One-sentence paragraphs | 11% | 5-12% |
| Contractions per 1k | 28.8 | ≥ 28 |
| I / you per 1k | 0.0 / 4.8 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.9 / 4.8 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 54.7 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts, question fragments, sentence-negation
pivots or false ranges. Remaining hints (`uniform_paragraph_structure`, `repeated_ngrams`) come from the fixed
template and metric names. `gate_glossary.py penalty-kill-percentage`: PASS. JSON parses.
Hardest metric: numbers per 1k (first draft 72); the 1977-78 to 2025-26 records paragraph alone carried 15 numbers, so the worst-ever and season-by-season detail moved to the facts tiles and the claims register.

Hover short: the current `short` agrees with the page. No change proposed.
