# Claims register: pdo.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/mp_teams_2025.csv`, `mp_teams_2024.csv`,
`mp_skaters_2025.csv`, `mp_skaters_2024.csv` (MoneyPuck season "2025" = 2025-26, "2024" = 2024-25) and
`mp_team_games_5on5_2023-2025_extract.csv`, all downloaded 2026-10-09. NHL rows come from
`nhl_stats_glossary_2026-10-09.json` and `nhl_team_percentages_20252026.json`, same day.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | PDO = shooting percentage plus save percentage, usually at five-on-five, team or on-ice for a player | NHL glossary On-ice S%+Sv%; NST glossary PDO; Hockey-Reference "PDO: Shooting % + Save %" | SUPPORTED |
| 2 | League as a whole always lands at exactly 100 | Arithmetic (league GF = GA and SF = SA, so league Sh% + Sv% = 1); CNS ("on average, a team will have a PDO rating of 100"); Hockey-Graphs 2014 (average 1000) | SUPPORTED |
| 3 | Teams far from 100 tend to drift back | NHL glossary ("A low value frequently portends future improvement ... and vice versa"); W&W split test (rows 17-18) | SUPPORTED |
| 4 | Letters don't stand for anything | CNS Maryland 2017-02-03 ("not an acronym and stands for nothing"); Grantland 2015-02-20 | SUPPORTED |
| 5 | Detroit 2025-26 5v5 PDO 98.5, 25th of 32; shooting 8.1%, 30th (third-lowest); save % at the league median (90.48, 17th) | W&W calc, MoneyPuck teams file 5on5; NHL team percentages (shootingPlusSavePct5v5 98.58, 25th) agrees | SUPPORTED (computed) |
| 6 | Brian King, Edmonton native and Oilers fan, frequented Irreverent Oiler Fans in the mid-2000s; PDO was his username there and his Counter-Strike handle | CNS Maryland 2017; Grantland 2015 | SUPPORTED |
| 7 | Same blog where Vic Ferrari named Corsi | RMNB 2014-10-11 (Barnes/Ferrari ran Irreverent Oilers Fans); McKenzie excerpt | SUPPORTED |
| 8 | Ferrari posted each Oiler's on-ice goals, shooting % and save %; King added the two percentages | CNS Maryland 2017 | SUPPORTED |
| 9 | King quotes: "incredibly lucky", "just couldn't score to save their lives", "you can do everything absolutely perfect, and the puck ends up in your net" | CNS Maryland 2017, verbatim | SUPPORTED |
| 10 | King designed it as a player stat and prefers that use; smaller sample, more variance | CNS Maryland 2017 | SUPPORTED |
| 11 | NHL picked it up in February 2015 as SPSV% | SI (Allan Muir) 2015-02-20 | SUPPORTED |
| 12 | NHL glossary: also known as PDO, credited to Tim Barnes; purpose estimating "puck luck" at 5-on-5; low value portends improvement | NHL glossary On-ice S%+Sv% entry | SUPPORTED |
| 13 | Tim Barnes is Ferrari's real name; his blog published the numbers | RMNB 2014-10-11; CNS 2017 | SUPPORTED |
| 14 | NST and Hockey-Reference print it as PDO; league stats feed carries five-on-five shooting plus save percentage | NST glossary (Wayback capture); Hockey-Reference skaters-advanced 2025-26 (raw saved); NHL team percentages field shootingPlusSavePct5v5 | SUPPORTED |
| 15 | NHL and Hockey-Reference print around 100; Hockey-Graphs and older writing used 1000 (decimal dropped) | NHL glossary ("well over 100.0"); Hockey-Reference values (e.g., 99.5); Hockey-Graphs (Wendorf) 2014-02-04 | SUPPORTED |
| 16 | Worked example (invented): 90/1,000 and 80/1,000 gives 9.0% + 92.0% = 101; opponents 99 | arithmetic | SUPPORTED |
| 17 | Empty-net goals fall outside five-on-five (6-on-5) | Definition of 5on5 (MoneyPuck situation split; NHL 5-on-5 entries) | SUPPORTED |
| 18 | 2025-26: Dallas 102.4 (1st), New Jersey 97.1 (last); Boston second | W&W calc, MoneyPuck teams file 5on5 | SUPPORTED (computed) |
| 19 | Five of every six team-seasons 2023-24 to 2025-26 between 98 and 102 (80 of 96) | W&W calc, game-by-game extract | SUPPORTED (computed) |
| 20 | 598 skaters (500+ 5v5 min): four in five between 96.8 and 103.3 (10th/90th percentiles); extremes 93.4 and 107.7 | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 21 | First-half to second-half PDO r = 0.36 vs CF% 0.81 (96 team-seasons) | W&W calc, first 41 vs last 41 | SUPPORTED (computed) |
| 22 | Teams at 101.5+ at halfway (16) averaged 102.6 then 101.1; teams at 98.5 or worse (20) 98.0 then 98.8 | W&W calc, same split | SUPPORTED (computed) |
| 23 | 56 skaters with 2024-25 PDO ≥ 103 (500+ min both seasons) averaged 103.8, then 101.0 in 2025-26 | W&W calc, MoneyPuck skaters files 2024 and 2025 | SUPPORTED (computed) |
| 24 | Dallas: 47.5% CF%, 50.8% xGF%, 55.2% GF%; Boston same pattern (47.3% xGF%, 55.0% GF%) | W&W calc, MoneyPuck teams file 5on5 | SUPPORTED (computed) |
| 25 | Detroit 5v5 GF% 45.5 vs CF% and xGF% 48.8; median shooting 9.6% on Detroit's 1,761 shots ≈ 168 goals vs 142 scored | W&W calc (1,761 × 0.0957 = 168.5) | SUPPORTED (computed) |
| 26 | Kasper on ice for 26 GF, 42 GA (38.2%), 49.6% of attempts, 50.3% of xG; on-ice PDO 96.3, 558th of 598; on-ice Sh% 5.9%; 99.8 in 2024-25 (1,026 min) | W&W calc, MoneyPuck skaters files | SUPPORTED (computed) |
| 27 | First-20-games PDO to rest-of-season PDO r = 0.21; shot and chance shares carry over far better (CF% 0.75, xGF% 0.64) | W&W calc, game-by-game extract | SUPPORTED (computed) |
| 28 | This site leans on expected goals | expected-goals.json dek; Team page | SUPPORTED |
| 29 | King: a team with Carey Price or Henrik Lundqvist "is going to be a PDO leader" | CNS Maryland 2017, verbatim | SUPPORTED |
| 30 | Wendorf (Hockey-Graphs, 2014): a single goaltender can outperform expectations by a wide margin | Hockey-Graphs 2014-02-04 ("a single goaltender can quite significantly outperform expectations") | SUPPORTED |
| 31 | MoneyPuck publishes a shooting-talent-adjusted xG version | MoneyPuck about (see expected-goals register row 26) | SUPPORTED |
| 32 | NHL glossary: a handful of elite players consistently over 100 on-ice | NHL glossary On-ice S%+Sv% | SUPPORTED |
| 33 | A season of one player's minutes covers a few hundred shots each way | On-ice SF for the 598 skaters runs 158 to 816, MoneyPuck skaters file | SUPPORTED (computed) |

Live slot: omitted. Wanted: `team.situations.5on5.shotsOnGoalFor` / `shotsOnGoalAgainst` (or a computed
`pdo`) with `leagueRanks.pdo_5on5`, and `skaters.fiveOnFive.onIceShPct`, `onIceSvPct`, `onIcePdo`.

## Voice metrics (running prose, `--target barnwell_lean`)

Running prose, 1,219 words.

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 18.2 / 10.3 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 10% | 6-15% / ≤ 20% |
| Words per paragraph | 64 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 28.7 | ≥ 28 |
| I / you per 1k | 0.0 / 4.9 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.6 / 3.3 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 54.1 | 30-55 |
