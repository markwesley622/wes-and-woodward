# Claims register: game-score.json

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Game score is a single-game rating of goals, assists, shots, blocks, penalties, faceoffs and on-ice shot and goal results | Luszczyszyn, Hockey-Graphs, Jul 13, 2016 (formula) | SUPPORTED |
| 2 | Luszczyszyn built the hockey version in 2016, weighted so a season lands close to a player's points | Same ("scale the weights down by 75 percent in order to make Game Score roughly equal to points") | SUPPORTED |
| 3 | The site averages MoneyPuck's and HockeyStatCards' versions; a game gets a score only once both have posted | pipeline/build_player.py (blend(); comment "A game only gets a score once both sources have it") | SUPPORTED |
| 4 | Bill James created the baseball version, John Hollinger the basketball one, credited by Luszczyszyn | Hockey-Graphs 2016 ("originally a baseball stat created by Bill James, but the basketball version was created by John Hollinger") | SUPPORTED |
| 5 | Title "Measuring Single Game Productivity", July 13, 2016 | Hockey-Graphs URL and dateline | SUPPORTED |
| 6 | Weights by frequency relative to goals, scaled down 75%; Corsi, blocks and faceoffs not scaled further; goalie formula on goals allowed and saves | Hockey-Graphs 2016 | SUPPORTED |
| 7 | The article listed the only games since 2007-08 above 5; Sam Gagner's eight-point night in 2012 = 7.1 | Hockey-Graphs 2016 ("Sam Gagner's eight point night back in 2012"; "worth a Game Score of 7.1") | SUPPORTED |
| 8 | Expected goals added in 2019; NHL.com described the current version as using "advanced measures of shot quality for and against" | All About The Jersey primer, Dec 28, 2020 (xG added June 2019); NHL.com Kraken, Nov 13, 2021 | SUPPORTED |
| 9 | GSVA at The Athletic built on the same idea | All About The Jersey primer ("same Game Score concept ... translated into wins"); The Athletic snippet | SUPPORTED |
| 10 | MoneyPuck data dictionary: gameScore "as designed by @domluszczyszyn" | MoneyPuckDataDictionaryForPlayers.csv | SUPPORTED |
| 11 | HockeyStatCards publishes a game score per game in its logs, with xG columns, linking to the 2016 article and the 2019 model | hockeystatcards.com player logs (column headers; "What is Game Score?" and "Learn the Model" links) | SUPPORTED |
| 12 | Skater formula weights (13 counts) and goalie formula as printed | Hockey-Graphs 2016 | SUPPORTED |
| 13 | Worked example = 1.72; goal + assist = 1.30, more than three-quarters | Invented inputs, labelled; arithmetic with the 2016 weights | SUPPORTED (illustrative) |
| 14 | MoneyPuck applies box-score terms to all situations and on-ice terms to 5v5; rebuilding its 2025-26 gameScore that way lands within 0.01 for 923 of 940 skaters | W&W calc, MoneyPuck 2025-26 skater file | SUPPORTED (computed) |
| 15 | HSC's numbers don't match MoneyPuck's game for game | Player JSON gameScoreParts (moneypuck vs hockeystatcards differ per game); HSC links the 2019 model | SUPPORTED (stated without 2026-27 numbers) |
| 16 | DeBrincat 87.4 game score vs 85 points | W&W calc, MoneyPuck 2025-26 | SUPPORTED (computed) |
| 17 | Per game: median forward (327, 60+ GP) 0.53, top 10% ≥ 1.02; defensemen median 0.36 (about a third lower) | Same | SUPPORTED (computed) |
| 18 | MacKinnon led at 1.86 per game, ahead of Kucherov (1.68) and McDavid (1.66) | Same | SUPPORTED (computed) |
| 19 | DeBrincat 1.07, 32nd of 488 skaters with 60+ GP; Larkin 0.90, Seider 0.87, Raymond 0.87; Detroit regulars between 0.04 and 1.07 | Same | SUPPORTED (computed) |
| 20 | Year to year (260 forwards, 60+ GP both seasons): GS per game r = 0.86, points per game 0.88 | W&W calc, MoneyPuck 2024-25 and 2025-26 | SUPPORTED (computed) |
| 21 | Luszczyszyn called it fairly repeatable | Hockey-Graphs 2016 ("fairly repeatable from year-to-year") | SUPPORTED |
| 22 | Player pages: per-game score, 2.0 strong, below zero poor, ten-game rolling average, bars colored by sign | src/pages/players/[slug].astro (chart label "red above zero, black below · line is the ten-game average"; note "2.0 is a strong night and below zero is a poor one") | SUPPORTED |
| 23 | Before EH data exists, the W-Value is replaced by a cumulative game-score stand-in on the same 0-100 scale among every skater who has played | pipeline/build_player.py stand_in_skater method string ("Stand-in until the W-Value is computable") | SUPPORTED |
| 24 | Seider 71.6 and Raymond 69.5 game score on 60 and 76 points; Seider's 180 blocks = 9.0, 5v5 CF−CA +176 = 8.8; Chiarot 15 points, 9.3 GS, 5v5 CF−CA −218 | W&W calc, MoneyPuck 2025-26 with 2016 weights | SUPPORTED (computed) |
| 25 | Goals and assists = 68% of game score for forwards with 60+ GP | Same | SUPPORTED (computed) |
| 26 | DeBrincat's 287 shots on goal = 21.5 of 87.4, about a quarter | Same | SUPPORTED (computed) |
| 27 | Live slot ranks skaters.json gameScore, MoneyPuck's own season total, all situations | pipeline/build_site_data.py (entry["gameScore"] = MoneyPuck all-situations gameScore) | SUPPORTED |

Computed rows: `research/glossary-pseo/raw/mp_skaters_2025.csv` (MoneyPuck 2025-26, downloaded 2026-10-09) and `raw/mp_skaters_2024_repeatability.csv` (MoneyPuck 2024-25, downloaded 2026-10-09). Per-game = season gameScore ÷ games_played, all situations.

## Voice metrics (running prose, `--target barnwell_lean`)

1,123 words. Sentence mean 19.4, SD 11.1; short 12%, long 17%; 59 words per paragraph; one-sentence paragraphs 11%; contractions 35.6/1k; I 0.0; you 4.5; questions 1.8; parentheses 3.6; intensifiers 0.9; transition openers 0%; numbers 50.8/1k; hedges 0.9 ("likely" is not used; the hit is "fairly", inside Luszczyszyn's own "fairly repeatable"). Every metric in range. Hardest: numbers per 1k (the first draft ran 80/1k because of the formula-heavy worked example, now written in words). ai-content-detection: no contrast frames, colon pivots or unicode artifacts; the one question_fragments hit ("Does it repeat? About as well...") was rewritten to a full sentence.
