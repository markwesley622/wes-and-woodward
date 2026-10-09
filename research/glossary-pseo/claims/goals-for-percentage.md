# Claims register: goals-for-percentage.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/mp_teams_2025.csv`, `mp_skaters_2025.csv`,
`mp_skaters_2024.csv` (MoneyPuck season "2025" = 2025-26, "2024" = 2024-25) and
`mp_team_games_5on5_2023-2025_extract.csv`, downloaded 2026-10-09. NHL rows come from
`nhl_stats_glossary_2026-10-09.json`, `nhl_team_percentages_20252026.json` and
`nhl_team_summary_20252026_corsi-family.json`, same day.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | GF% = share of goals in a team's games or a player's minutes, usually 5v5; 50% break-even | NHL glossary Goals % ("generally at 5-on-5"); NST GF% (GF*100/(GF+GA)) | SUPPORTED |
| 2 | It's the result CF% and xGF% try to predict | Hover short; NHL glossary (compare Goals % with SAT%/USAT%) | SUPPORTED |
| 3 | Detroit 2025-26 5v5 GF% 45.5% (26th; 142 for, 170 against); CF% and xGF% both 48.8% | W&W calc, MoneyPuck teams file; NHL team percentages goalsForPct 0.4566 agrees within a goal | SUPPORTED (computed) |
| 4 | NHL glossary: plus-minus "hockey's first enhanced stat", official since 1959-60, goal differential on ice, power-play goals excluded | NHL glossary +/- entry; NHL skater summary 1959-60 carries plus-minus (raw `nhl_skater_summary_19591960_plusminus_check.json`), 1958-59 doesn't | SUPPORTED |
| 5 | NHL files it as goals for percentage, numbers back to 2009-10; skater version generally 5v5; compare with SAT% and USAT% | NHL glossary Goals % (firstSeasonForStat 2009-10) | SUPPORTED |
| 6 | EV GF% entry: goal samples build up much more slowly than shot samples | NHL glossary EV GF% | SUPPORTED |
| 7 | NST publishes GF% for teams and skaters; MoneyPuck carries on-ice GF/GA; NHL team percentages report lists 5v5 GF% for every club | NST glossary (Wayback capture); MoneyPuck skaters columns OnIce_F_goals/OnIce_A_goals; NHL team percentages goalsForPct (Colorado 0.6279 = 216/344, the 5v5 split) | SUPPORTED |
| 8 | Built from the goals in the league's play-by-play with the on-ice skaters | NST and MoneyPuck on-ice definitions | SUPPORTED |
| 9 | Goals outside 5v5 were about a third of league scoring in 2025-26 | W&W calc: 5,367 of 8,086 goals at 5on5 (66.4%), MoneyPuck teams file | SUPPORTED (computed) |
| 10 | Worked example (invented): 40 for, 30 against = 57.1%, plus-10; half the goals each way, same share | arithmetic | SUPPORTED |
| 11 | Every skater on the ice gets the goal in his column; same rule as plus-minus | NST GF definition; NHL glossary +/- ("All the skaters on the ice receive a plus or minus") | SUPPORTED |
| 12 | 32 teams 2025-26: 5v5 GF% r = 0.86 with points %, CF% 0.57 | W&W calc, MoneyPuck teams file + NHL team summary pointPct | SUPPORTED (computed) |
| 13 | Colorado 62.8% (1st), Vancouver 38.4% (last) | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |
| 14 | 598 skaters: median 50.0%, top tenth ≥ 59.5%, bottom tenth ≤ 39.3%; SD 7.6 points vs 4.0 for CF% (nearly twice) | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 15 | DeBrincat 56.2% topped Detroit regulars | W&W calc | SUPPORTED (computed) |
| 16 | First 20 games to rest of season: GF% 0.37, xGF% 0.51, score-adjusted CF% 0.42 (96 team-seasons) | W&W calc, game-by-game extract | SUPPORTED (computed) |
| 17 | First half to second half: GF% 0.56, the best single forecast in the sample, xGF% 0.52 | W&W calc, first 41 vs last 41 of each 82-game season | SUPPORTED (computed) |
| 18 | Had Detroit's goal share matched its chance share, the 312 goals would have split about 152 to 160; actual 142 to 170 | 312 × 0.488 = 152.3, MoneyPuck teams file | SUPPORTED (computed) |
| 19 | Most of the gap traces to shooting | Detroit 142 GF on 161.1 xGF, 170 GA on 169.2 xGA; 5v5 shooting 8.1%, 30th (see pdo register) | SUPPORTED (computed) |
| 20 | MacKinnon 70.4% on a 57.6% xG share (5v5); Kasper 38.2% GF on 50.3% xGF, near the bottom (552nd of 598) | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 21 | Detroit all-situations goal share 48.5% (239 for, 254 against), about three points above 5v5; outscored opponents 54 to 47 on the power play and penalty kill combined | MoneyPuck teams file (5on4 51-4, 4on5 3-43); NHL team summary (239, 254) | SUPPORTED (computed) |
| 22 | Plus-minus includes shorthanded and empty-net goals | NHL glossary +/- | SUPPORTED |
| 23 | Detroit 5v5 season: 312 goals, 7,734 attempts; each goal moves GF% about 25 times as far as one attempt moves CF% | W&W calc: 7,734 / 312 = 24.8 (marginal effect ratio about 26 given each share's distance from 100%) | SUPPORTED (computed) |
| 24 | PDO is shooting plus save percentage and drifts back toward 100 | pdo register rows 1-3, 21-23 | SUPPORTED |
| 25 | On-ice GF% vs team GF% r = 0.53 (598 skaters) | W&W calc | SUPPORTED (computed) |
| 26 | 501 skaters with 500+ min both seasons: on-ice GF% y/y r 0.30; CF% 0.63 | W&W calc, MoneyPuck skaters 2024 and 2025 | SUPPORTED (computed) |

Live slot: omitted. The pipeline carries `team.situations.5on5.goalsFor` and `goalsAgainst`, so count tiles are
possible today, but there's no share or rank. Wanted: `team.situations.5on5.goalsPct` with
`leagueRanks.goalsPct_5on5`, and `skaters.fiveOnFive.onIceGoalsPct`.

## Voice metrics (running prose, `--target barnwell_lean`)

Running prose, 1,111 words.

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.2 / 10.5 | 17-21 / ≥ 10 |
| Short / long sentences | 14% / 19% | 6-15% / ≤ 20% |
| Words per paragraph | 58 | 55-85 |
| One-sentence paragraphs | 11% | 5-12% |
| Contractions per 1k | 31.5 | ≥ 28 |
| I / you per 1k | 0.0 / 5.4 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 5.4 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 51.3 | 30-55 |

ai-content-detection: no contrast frames, payoff colons or unicode artifacts. A ", never" frame in the dek was cut.
Hardest metrics: sentence SD against the short/long and one-sentence-paragraph caps (they pull in opposite
directions on a page this size) and numbers per 1k (first draft 72).

Hover short: the current `short` agrees with the page. No change proposed.
