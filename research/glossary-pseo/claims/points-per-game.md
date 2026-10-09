# Claims register: points-per-game.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`nhl_skater_summary_20252026_scoringbasics.json`, `nhl_skater_summary_20242025_scoringbasics.json`,
`nhl_point_per_game_players_by_season_scoringbasics.json`, `nhl_goals_per_team_game_select_seasons_scoringbasics.json`,
`nhl_skater_season_top_pointsPerGame_thru20252026_scoringbasics.json` (40-game minimum). Glossary text:
`nhl_stats_glossary_api_20261009_scoringbasics.json`. Hockey-Reference pages read 2026-10-09.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | P/GP = points ÷ games played; levels players who missed time | NHL glossary P/GP | SUPPORTED |
| 2 | A point a game marks a star in the current NHL | Row 9 (35 of 488 regulars, 7%) | SUPPORTED (computed) |
| 3 | 35 of 488 regulars reached a point a game; only one was a Red Wing | W&W calc, 60+ GP (DeBrincat only) | SUPPORTED (computed) |
| 4 | NHL glossary carries P/GP back to the first season; describes it as points ÷ GP for missed games / partial NHL seasons | NHL glossary P/GP (firstSeasonForStat 19171918) | SUPPORTED |
| 5 | Malone 48 points in 20 games = 2.40, most of them goals | NHL skater summary 1917-18 (44 G, 4 A, 20 GP) | SUPPORTED |
| 6 | Gretzky career 1.921 best among 500-point players, Lemieux 1.883 | Hockey-Reference career P/GP leaders; rate requirement 500 points | SUPPORTED |
| 7 | Gretzky 1983-84: 205 in 74 = 2.77, best full season; 1983-84 teams averaged 3.94 goals a game, 3.08 in 2025-26 | NHL stats API season leaders (40+ GP); team summaries | SUPPORTED (computed) |
| 8 | Hockey-Reference: 0.625 points per scheduled game (about 52 over an 82-game schedule), 500 career points; a points minimum | Hockey-Reference Rate Statistic Requirements (0.625 × 82 = 51.25) | SUPPORTED |
| 9 | This site uses a 60-game floor | W&W method | SUPPORTED |
| 10 | GP counts any game with at least one shift or a shootout appearance | NHL glossary GP | SUPPORTED |
| 11 | Worked example (60 in 60 = 1.00; 68 in 80 = 0.85) | Invented round numbers, labelled | SUPPORTED (illustrative) |
| 12 | Glossary flags that the rate ignores ice time and special-teams time | NHL glossary P/GP | SUPPORTED |
| 13 | Most repeatable of the basic scoring rates: P/GP r = 0.88, G/GP 0.74 (260 forwards) | W&W calc, skater summaries 2024-25 and 2025-26 (A/GP 0.86, A1/GP 0.80, A2/GP 0.73, primary points 0.86) | SUPPORTED (computed) |
| 14 | Median regular forward 0.51, defenseman 0.34 | W&W calc, 60+ GP | SUPPORTED (computed) |
| 15 | Kucherov led at 1.71, McDavid just behind; Draisaitl fourth by rate, ninth in points (97 in 65 GP) | NHL skater summary, 60+ GP | SUPPORTED |
| 16 | Kucherov's edge came from games; McDavid had eight more points | 130 in 76 vs 138 in 82 | SUPPORTED |
| 17 | 2014-15: 2.66 goals a team game; eight regulars at a point a game; 2025-26: 35 | NHL team and skater summaries | SUPPORTED (computed) |
| 18 | 0.95 rate: 43 other regulars at or above it in 2025-26 (44 total), one of 11 in 2014-15 | W&W calc, 60+ GP | SUPPORTED (computed) |
| 19 | DeBrincat 1.04 ranked 31st of 488; Raymond and Larkin close behind (0.95, 0.91) | W&W calc | SUPPORTED (computed) |
| 20 | Seider 0.73, 16th of 161 regular defensemen; Detroit 22nd in goals | W&W calc; NHL team summary | SUPPORTED (computed) |
| 21 | Draisaitl 97 vs Scheifele 103 (82 GP): 1.49 vs 1.26 | NHL skater summary | SUPPORTED |
| 22 | Larkin missed eight games; 74-point full-season pace, seven above his 67 | 74 GP of 82; 0.905 × 82 = 74.2 | SUPPORTED (computed) |
| 23 | Raymond's rate = 78-point full season; DeBrincat never missed a game | 0.95 × 82 = 77.9; DeBrincat 82 GP | SUPPORTED (computed) |
| 24 | Gretzky 2.77 vs McDavid 1.68; eight to 35 point-a-game regulars in barely a decade | Rows 7, 15, 17 | SUPPORTED |
| 25 | Martone 10 points in nine games (1.11) would've ranked 20th among regulars | NHL skater summary (19 regulars above 1.111) | SUPPORTED (computed) |
| 26 | Seider 25.7 minutes, DeBrincat 18.5; per-minute gap nearly double | W&W calc (3.36 vs 1.71 per hour; 1.04 vs 0.73 per game) | SUPPORTED (computed) |
| 27 | PPP were 21% of skater points | W&W calc: 4,640 ÷ 21,741 | SUPPORTED (computed) |
| 28 | NHL.com uses PPG for power-play goals | NHL glossary PPG | SUPPORTED |
| 29 | FAQ: NHL.com and Hockey-Reference keep regular-season and playoff stats separately | NHL stats game-type split (gameTypeId 2 vs 3); Hockey-Reference separate playoff tables | SUPPORTED |
| 30 | Facts: medians 0.51 / 0.34; Kucherov 1.71 (130 in 76); DeBrincat 1.04; Gretzky 1.921 | Rows 6, 14, 15, 19 | SUPPORTED |

Cut for lack of verification: any official NHL minimum for per-game leaderboards; claims about what other sites
abbreviate as PPG; Lemieux's distance from Gretzky's 2.77 (first draft's "within a tenth" was wrong and came out).
Per the 10/9 CBA note, no evergreen "82" remains: the hero says "every game", the pace formula uses "games on the
schedule", and 82 appears only tied to 2025-26.

## Voice metrics (running prose, `--target barnwell_lean`, 1,168 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.8 / 10.0 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 19% | 6-15% / ≤ 20% |
| Words per paragraph | 58 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 41.1 | ≥ 28 |
| I / you per 1k | 0 / 3.4 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.7 / 3.4 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 52.2 | 30-55 |

ai-content-detection: no contrast frames, payoff colons or unicode artifacts. Remaining hint (`repeated_ngrams`)
comes from the stat's name ("point a game", "points per game").

Proposed hover short: Points divided by games played. It puts a player who missed time on the same footing as one who played every game, and a point a game marks a star.

(The current short says "one who played all 82"; 2026-27 is an 84-game season, so the number won't stay evergreen.)
