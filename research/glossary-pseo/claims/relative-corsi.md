# Claims register: relative-corsi.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/mp_skaters_2025.csv`,
`mp_skaters_2024.csv` and `mp_teams_2025.csv` (MoneyPuck season "2025" = 2025-26, "2024" = 2024-25), downloaded
2026-10-09. On-ice and off-ice CF% are computed from `OnIce_F/A_shotAttempts` and `OffIce_F/A_shotAttempts` at
5on5 (they match MoneyPuck's rounded `onIce_corsiPercentage` / `offIce_corsiPercentage` within 0.005).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Rel CF% = on-ice CF% minus team's CF% with him off the ice, usually 5v5; positive = team better with him | NHL glossary SAT% Relative; MoneyPuck glossary ("Relative: on ice metric minus their off ice metric"); Hockey-Reference ("CF% - CFoff%") | SUPPORTED |
| 2 | 20 of the top 50 on-ice CF% skaters (500+ 5v5 min) played for Carolina; Seider 126th on raw CF% | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 3 | Seider sixth among 213 defensemen with 500+ min by Rel CF%; 12th of 598 skaters at plus-6.7; Edvinsson 18th of 213 D at plus-5.0 | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 4 | EvolvingWild (Hockey-Graphs, 2018) couldn't find where the approach first originated | Hockey-Graphs 2018-02-21, "Revisiting Relative Shot Metrics, Part 1" ("I actually couldn't find where this approach first originated") | SUPPORTED |
| 5 | NHL stats site: SAT% Relative, defined as player SAT% minus team SAT% while not on the ice, since 2009-10; USAT% Relative built the same way | NHL glossary entries 1236 and 1237 (firstSeasonForStat 2009-10) | SUPPORTED |
| 6 | MoneyPuck publishes on-ice and off-ice Corsi and defines relative as on minus off | MoneyPuck glossary; skaters file columns onIce_/offIce_corsiPercentage | SUPPORTED |
| 7 | Hockey-Reference prints CF% rel for even strength | Hockey-Reference skaters-advanced 2025-26 header tooltip (raw saved) | SUPPORTED |
| 8 | NST relative view compares with the team's numbers while the player is dressed but not on the ice | NST player glossary, Wayback capture (raw `nst_glossary_players_wayback_20250109.html`) | SUPPORTED |
| 9 | David Johnson's HockeyAnalysis and Puckalytics made Rel TM public; it weights teammates by shared TOI | Hockey-Graphs 2018-02-21 | SUPPORTED |
| 10 | Unqualified Rel CF% means the team version | NHL, MoneyPuck, Hockey-Reference and NST definitions (all on-minus-off team versions) | SUPPORTED |
| 11 | Both splits cover only games the player dressed for | NST definition (row 8); MoneyPuck data check: Larkin (74 GP) on-ice + off-ice CF = 3,426 of Detroit's 3,775 | SUPPORTED (computed) |
| 12 | Worked example (invented): 550/450 on (55.0%), 900/1,100 off (45.0%), Rel plus-10.0 | arithmetic | SUPPORTED |
| 13 | Seider: Detroit allowed 10.6 fewer attempts per 60 with him on (52.0 vs 62.6) and generated 4.8 more (58.6 vs 53.8) | W&W calc; off-ice minutes = team 5v5 minutes 4,065.4 − Seider's 1,612.1 (he dressed for all 82) | SUPPORTED (computed) |
| 14 | On-ice CF% vs team CF% r = 0.74; Rel CF% vs team CF% r = 0.00 (−0.001), 598 skaters | W&W calc | SUPPORTED (computed) |
| 15 | All 20 Carolina regulars at 57.5%+ on-ice; 11 below zero relative | W&W calc | SUPPORTED (computed) |
| 16 | Median skater about zero (+0.03); forwards +0.24, defensemen −0.55; top and bottom tenths beyond ±4.4 | W&W calc | SUPPORTED (computed) |
| 17 | Jordan Spence (OTT, D) led at plus-11.2; Erik Gudbranson (CBJ) last at minus-14.5; Adam Fox (NYR) second among D at plus-9.9 | W&W calc | SUPPORTED (computed) |
| 18 | Rasmussen minus-4.8 (551st of 598) | W&W calc | SUPPORTED (computed) |
| 19 | 501 skaters with 500+ min both seasons: raw CF% y/y r 0.69 for 387 who stayed, 0.43 for 114 who moved; Rel CF% 0.51 and 0.50 | W&W calc, MoneyPuck skaters 2024 and 2025 | SUPPORTED (computed) |
| 20 | Seider on-ice 53.0%; Wings 46.2% without him | W&W calc | SUPPORTED (computed) |
| 21 | Chiarot (−4.0), Bernard-Docker (−3.9), Johansson (−3.3) below zero; Chiarot's on/off CF/60 55.2 vs 56.0 and CA/60 64.0 vs 55.2 (8.8 more allowed) | W&W calc (Chiarot dressed for all 82) | SUPPORTED (computed) |
| 22 | Faulk: St. Louis 2024-25 Rel CF% −3.6; Detroit 2025-26 −1.3 | W&W calc, MoneyPuck skaters 2024 (team STL) and 2025 (team DET) | SUPPORTED (computed) |
| 23 | Team-relative version is pulled by linemates; the reason Rel TM exists | Hockey-Graphs 2018-02-21 | SUPPORTED |
| 24 | More OZ starts, slight bump in SAT%; more DZ starts, slight decrease | NHL glossary OZ Start% and DZ Start% | SUPPORTED |
| 25 | Seider played about 40% of Detroit's 5v5 minutes (1,612 of 4,065); Detroit's most-used defenseman | W&W calc, MoneyPuck skaters + teams files | SUPPORTED (computed) |
| 26 | Hockey-Reference (even strength) has Seider at 53.1% and plus-6.9 | Hockey-Reference skaters-advanced 2025-26 (raw `hockeyref_skaters_advanced_2025-26_dl2026-10-09_corsi-family.html`) | SUPPORTED |

Live slot: omitted. Wanted: `skaters.fiveOnFive.offIceCorsiPct` and `relCorsiPct` (MoneyPuck carries
`offIce_corsiPercentage`), so the table can sort Red Wings skaters by Rel CF%.

## Voice metrics (running prose, `--target barnwell_lean`)

Running prose, 1,153 words.

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.5 / 10.3 | 17-21 / ≥ 10 |
| Short / long sentences | 14% / 19% | 6-15% / ≤ 20% |
| Words per paragraph | 61 | 55-85 |
| One-sentence paragraphs | 11% | 5-12% |
| Contractions per 1k | 44.2 | ≥ 28 |
| I / you per 1k | 0.0 / 6.1 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.7 / 4.3 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 52.9 | 30-55 |
