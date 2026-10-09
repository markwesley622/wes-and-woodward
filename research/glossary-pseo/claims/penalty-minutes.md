# Claims register: penalty-minutes.json

Raw files (downloaded 2026-10-09, `research/glossary-pseo/raw/`): `nhl_skater_penalties_20252026.json`,
`nhl_skater_summary_20252026.json`, `nhl_skater_summary_20242025.json`, `nhl_team_penalties_20252026.json`,
`nhl_team_penaltykill_20252026.json`, `nhl_team_powerplay_20252026.json`, `nhl_records_season_pim_20261009.json`,
`nhl_records_det_season_pim_20261009.json`, `nhl_records_det_career_pim_20261009.json`, `nhl_stats_glossary_20261009.json`,
`nhl_rulebook_2025-26_downloaded_20261009.pdf`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Minor 2, double minor 4, major 5, misconduct 10, game misconduct 10 | Rules 16.1, 18.1, 20.1, 22.1, 23.1 ("Ten minutes are applied in the league records") | SUPPORTED |
| 2 | Every penalty counts whether or not it put the team shorthanded; penalties drawn don't offset | NHL glossary PIM ("whether those penalties caused an opposition power play or not"); Pen Drawn tracked separately | SUPPORTED |
| 3 | Misconducts cost nothing on the ice (no shorthanded time) | Rule 22.3 | SUPPORTED |
| 4 | Hockey-Reference: PIM = penalties in minutes | Hockey-Reference glossary | SUPPORTED |
| 5 | Fights are majors | NHL glossary Major ("Fighting also results in a major penalty") | SUPPORTED |
| 6 | Match penalty recorded as 15 (five on the clock plus 10 for removal) | Rule 21.2 | SUPPORTED |
| 7 | Zadorov (BOS) 152 led 2025-26 | NHL skater penalties report | SUPPORTED (computed) |
| 8 | Median forward 28 PIM (327, 60+ GP); top 10% 62; median D 34 (161) | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 9 | Detroit 629 team PIM, fifth-fewest | NHL team penalties report | SUPPORTED (computed) |
| 10 | PIM tracked since 1917-18, the NHL's first season | NHL glossary PIM firstSeasonForStat 19171918 | SUPPORTED |
| 11 | Schultz 472 (PHI, 1974-75) single-season record | NHL API season query | SUPPORTED |
| 12 | Probert 398 in 1987-88, sixth all-time, Detroit record; most PIM as a Red Wing (2,090) | NHL API season and franchise queries | SUPPORTED |
| 13 | NHL glossary: fighting majors almost always coincidental, rarely change manpower | NHL glossary Major | SUPPORTED |
| 14 | A game misconduct goes into the records as 10 even though the player's gone for the night | Rule 23.1 | SUPPORTED |
| 15 | NHL definition quote | NHL glossary PIM, verbatim | SUPPORTED |
| 16 | Penalties taken and drawn published as counts since 2009-10; public WAR models put a goal value on them | NHL glossary Pen Taken/Pen Drawn firstSeasonForStat 20092010; EH GAR glossary (Take, Draw) | SUPPORTED |
| 17 | PIM/GP back to 1997-98 | NHL glossary | SUPPORTED |
| 18 | Example: substitute allowed during a misconduct | Rule 22.1 | SUPPORTED |
| 19 | Penalties-taken column counts a hook and a misconduct as one penalty each | NHL glossary Pen Taken ("Number of penalties... All penalty types") | SUPPORTED |
| 20 | 2025-26 teams charged 23,596 PIM on 9,656 penalties; 8,490 minors; rest bench minors, majors, misconducts, game misconducts, match penalties | NHL team penalties report sums (minors 8,490, bench 266, majors 632, misconducts 232, GM 32, match 4; these sum to 9,656) | SUPPORTED (computed) |
| 21 | Kastelic 140, second; 25 minors, 10 majors, 4 misconducts, so 40 minutes from misconducts | NHL skater penalties report (25×2 + 10×5 + 4×10 = 140) | SUPPORTED (computed) |
| 22 | Zadorov 152 mostly minors, 41, most in the league | NHL skater penalties report | SUPPORTED (computed) |
| 23 | Detroit 11 majors tied second-fewest; shorthanded 210 times, third-fewest; Edvinsson and Chiarot 75 each led the team | NHL team penalties and penalty-kill reports; skater penalties | SUPPORTED (computed) |
| 24 | Year-to-year PIM 0.77 (379 skaters), points 0.86, plus-minus 0.35 | W&W calc (Pearson), NHL skater summaries 2024-25 and 2025-26 | SUPPORTED (computed) |
| 25 | Across 32 teams, r(PIM, times shorthanded) = 0.72; r(minors, times shorthanded) = 0.86 | W&W calc (Pearson), NHL team penalties + penalty-kill reports | SUPPORTED (computed) |
| 26 | Tampa Bay 1,207 PIM, 229 more than anyone; Boston and Florida shorthanded more often (278, 273 vs 258) | NHL team penalties + penalty-kill reports | SUPPORTED (computed) |
| 27 | Ross Johnston (ANA) and Mathieu Olivier (CBJ) led with 11 majors each | NHL skater penalties report | SUPPORTED (computed) |
| 28 | Zadorov took 51, drew 26, net −25 worst; Chiarot took 31, drew 10, −21 fifth-worst | NHL skater penalties report | SUPPORTED (computed) |
| 29 | Finnie 6 PIM, drew 22, net +19 tied third | NHL skater penalties report | SUPPORTED (computed) |
| 30 | A delayed minor washed out by a goal is never imposed, so never in PIM | Rule 15.2 | SUPPORTED |
| 31 | EH: 5v5 minor 0.182 goals; minor 30 s into an opponent's 5v4 0.419 | Evolving-Hockey, Penalty Goals (2019) | SUPPORTED |
| 32 | FAQ: coincidental penalties count toward PIM | NHL glossary PIM (all penalty minutes, whether or not they caused a power play) | SUPPORTED |

Worked example uses invented round numbers and says so.

## Voice metrics (running prose, `--target barnwell_lean`)

1,191 words. Sentence mean 18.6 / SD 10.8; short 14% / long 17%; 60 words per paragraph; one-sentence paragraphs 5%;
contractions 35.3/1k; I 0.0; you 5.0; questions 1.7; parentheses 3.4; intensifiers 0.0; transition openers 0%;
numbers 52.1/1k; hedges 0.0. All in range. ai-content-detection: no contrast frames, payoff colons, unicode artifacts or
negation pivots; hints `uniform_paragraph_structure`, `repeated_ngrams`.

Cut: Dave "Tiger" Williams's career PIM record (the NHL API gives 3,971; the commonly cited figure is 3,966, so neither went in).

The current hover short agrees with the page; no change proposed.
