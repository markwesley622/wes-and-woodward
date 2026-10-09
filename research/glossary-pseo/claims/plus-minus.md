# Claims register: plus-minus.json

Raw files (downloaded 2026-10-09, `research/glossary-pseo/raw/`): `nhl_skater_summary_20252026.json`,
`nhl_skater_summary_20242025.json`, `nhl_team_summary_20252026.json`, `nhl_team_powerplay_20252026.json`,
`nhl_team_penaltykill_20252026.json`, `nhl_skater_summary_19581959_plusminus_check.json`,
`nhl_skater_summary_19591960_plusminus_check.json`, `nhl_skater_summary_19821983_plusminus_check.json`,
`nhl_skater_summary_20072008_plusminus_check.json`, `nhl_skater_howe_seasons_check.json`,
`nhl_team_summary_19951996_det_check.json`, `nhl_records_season_pm_top_20261009.json`, `nhl_records_career_pm_20261009.json`,
`nhl_records_det_season_pm_20261009.json`, `nhl_records_det_career_pm_20261009.json`, `nhl_stats_glossary_20261009.json`,
`mp_skaters_2025.csv`, `mp_teams_2025.csv`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | +/- = on-ice goal differential counting EV and SH goals, leaving out PP goals; plus when his team scores, minus when the other does; it can't tell who caused the goal | NHL glossary +/- ("excluding power play goals for and against but including empty net situations"; all skaters on ice get a plus or minus on EV or SH goals) | SUPPORTED |
| 2 | It carries teammates' and goalie's results | EH RAPM glossary (raw on-ice ratings impacted by teammates/opponents); NHL glossary PP GA/60 warning (teammates and goalie save percentage) | SUPPORTED |
| 3 | Oldest on-ice number in the NHL's books | NHL glossary: +/- first season 1959-60, "hockey's first enhanced stat"; EV GF/GA and other on-ice splits start 2009-10 | SUPPORTED |
| 4 | Official since 1959-60 per the NHL's stats glossary | NHL glossary +/- ("becoming an official NHL statistic in 1959-60"). Note: some secondary sources (The Hockey Writers 2013) say 1967-68; the page follows the NHL | SUPPORTED |
| 5 | First season in the database is 1959-60; Doug Harvey (MTL) led at +37 | NHL API: 1958-59 plusMinus null; 1959-60 leader Harvey +37 | SUPPORTED |
| 6 | Gordie Howe's first 13 seasons (1946-47 to 1958-59) predate the stat; his record starts in his 14th | NHL API Howe season rows (plusMinus null through 1958-59, 16 in 1959-60) | SUPPORTED |
| 7 | NHL plus-minus award 1982-83 through 2007-08; Charlie Huddy first, Pavel Datsyuk last | The Hockey News, "Winners of NHL awards that faded into history" (first winner 1983, last 2008) | SUPPORTED |
| 8 | Huddy played for Edmonton | NHL API 1982-83 (Huddy EDM) | SUPPORTED |
| 9 | Datsyuk won at +41, one ahead of teammate Lidstrom (+40) | NHL API 2007-08 plus-minus leaders | SUPPORTED |
| 10 | Orr +124 in 1970-71 single-season record; Robinson +722 career leader | NHL API season and career queries | SUPPORTED |
| 11 | Konstantinov +60 in 1995-96 Detroit record; Lidstrom +450 over a career entirely in Detroit, eighth all-time | NHL API franchise queries; career query (Lidstrom 8th; career GP 1,564 equals Detroit GP 1,564) | SUPPORTED |
| 12 | Evolving-Hockey's RAPM controls for teammates, opponents, zone starts and score | EH RAPM glossary ("control for all teammates, opponents, score state, zone starts, etc.") | SUPPORTED |
| 13 | Empty-net goals count; goalies don't get a rating | NHL glossary +/- | SUPPORTED |
| 14 | An SHG against is a minus for each skater on the power play | NHL glossary +/-; Hockey-Reference glossary (minus for goals allowed at EV or on the PP) | SUPPORTED |
| 15 | EV GF% = EV GF ÷ (EV GF + EV GA); EV GF/GA published back to 2009-10 | NHL glossary | SUPPORTED |
| 16 | A penalty killer never takes a minus for a PP goal against; a PP skater takes one for every SHG against | NHL glossary + Hockey-Reference definition | SUPPORTED |
| 17 | Median forward (327, 60+ GP) exactly 0; median defenseman (161) +2; range MacKinnon +57 to Boeser −48 | W&W calc, NHL skater summary 2025-26 | SUPPORTED (computed) |
| 18 | Five of the top 11 were Colorado (MacKinnon, Necas, Malinski, Manson, Toews) | NHL skater summary (Toews +37 tied 10th) | SUPPORTED (computed) |
| 19 | Colorado best EV goal differential +103; Vancouver worst −93 | W&W calc: (GF − PPG − SHG) − (GA − PPGA − SHGA), NHL team reports | SUPPORTED (computed) |
| 20 | Boeser and DeBrusk (VAN) two of the bottom seven | NHL skater summary (−48 and −31; seventh-lowest is −31) | SUPPORTED (computed) |
| 21 | Detroit spread Seider +15 to −20 for Sandin-Pellikka and Kasper | NHL skater summary | SUPPORTED (computed) |
| 22 | Seider at 5v5: on ice for 71 GF, 57 GA; xG 70.2 to 56.8 | MoneyPuck skaters file, situation 5on5 | SUPPORTED (computed) |
| 23 | Year-to-year (379 skaters, 60+ GP both seasons): +/- 0.35, points 0.86, PIM 0.77 | W&W calc (Pearson), NHL skater summaries 2024-25 and 2025-26 | SUPPORTED (computed) |
| 24 | Kasper at 5v5: 26 GF, 42 GA, xG 40.4 to 39.9; Detroit shot 5.9% with him on the ice vs 9.5% league | MoneyPuck skaters file (OnIce_F_goals/shotsOnGoal) and teams file (5,367 / 56,451 at 5on5) | SUPPORTED (computed) |
| 25 | Seider (+15) and Chiarot (−9) played every game in 2025-26; 24-goal gap; MoneyPuck 5v5 xG differential +13.4 and −12.3 | NHL skater summary (82 GP each); MoneyPuck skaters file 5on5 | SUPPORTED (computed) |
| 26 | NHL on-ice goal splits start in 2009-10; plus-minus back to 1959-60 | NHL glossary firstSeasonForStat (EV GF 20092010; +/- 19591960) | SUPPORTED |
| 27 | Konstantinov's +60 came on a Detroit team that won 62 games; Fedorov +49 on the same roster | NHL API 1995-96 team summary (62 W, 131 pts); franchise season query (Fedorov +49 in 1995-96) | SUPPORTED |
| 28 | A fifth of the league's goals sit outside the stat | 19.7% PP goals (PPG register row 2) | SUPPORTED (computed) |
| 29 | Hockey-Reference's definition spells out the asymmetry | Hockey-Reference glossary +/- | SUPPORTED |
| 30 | Gramacy, Taddy and Jensen describe plus-minus as an aggregate measure that averages over teammates' and opponents' contributions | arXiv 1209.5026 introduction ("an aggregate measure that averages over the contributions of opponents and teammates") | SUPPORTED |
| 31 | NHL glossary calls on-ice PP goals against heavily influenced by teammates and goalie save percentage | NHL glossary PP GA/60 | SUPPORTED |
| 32 | A late empty-netter is a minus for every skater on the trailing team, extra attacker included | NHL glossary +/- (empty net included, all skaters on ice) | SUPPORTED |
| 33 | FAQ: league skaters combined −507 in 2025-26; SH goal = four pluses, five minuses; EN goal vs a pulled goalie = five pluses, six minuses | W&W calc: sum of plusMinus, NHL skater summary; arithmetic from the NHL definition | SUPPORTED (computed) |

Cut for lack of a reputable primary source: the common story that the Montreal Canadiens first tracked plus-minus in the
1950s and that Emile Francis popularized it (only Wikipedia citing LiveAbout, a fan wiki and a 2013 Hockey Writers post);
the 1967-68 "official" date (conflicts with NHL.com's 1959-60).

Worked example uses invented round numbers and says so.

## Voice metrics (running prose, `--target barnwell_lean`)

1,177 words. Sentence mean 18.4 / SD 10.3; short 12% / long 17%; 56 words per paragraph; one-sentence paragraphs 5%;
contractions 46.7/1k; I 0.0; you 5.1; questions 1.7; parentheses 5.1; intensifiers 0.0; transition openers 0%;
numbers 54.4/1k; hedges 0.0. All in range. ai-content-detection: no contrast frames, payoff colons, unicode artifacts or
negation pivots; hints `uniform_paragraph_structure`, `repeated_ngrams`.

The current hover short agrees with the page; no change proposed.
