# Claims register: individual-shot-attempts.json

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | iCF counts every shot attempt a player takes, on goal, missed or blocked | Natural Stat Trick glossary ("iCF - Any shot attempt (goals, shots on net, misses and blocks) by the player, outside of the shootout"); NHL glossary iSAT/60 | SUPPORTED |
| 2 | It's the shooter's own slice of Corsi (on-ice attempts by his team) | NHL glossary SAT ("also known as Corsi"); NST glossary | SUPPORTED |
| 3 | A forward's 5v5 attempt rate carries over about twice as well as his goal rate (0.85 vs 0.42) | W&W calc, MoneyPuck 2024-25 and 2025-26, 324 forwards with 500+ 5v5 min in both | SUPPORTED (computed) |
| 4 | Corsi naming: Vic Ferrari (Tim Barnes) heard Sabres GM Darcy Regier talk about shot attempts on the radio, picked goalie coach Jim Corsi's name off the Sabres website, partly for the moustache; Ferrari's site 2006-2008 birthplace of Corsi, Fenwick and PDO | Bob McKenzie, TSN, Oct 6, 2014 (Wayback copy) | SUPPORTED |
| 5 | NHL tracks skater shots on goal since 1959-60, missed shots since 1997-98, blocked shots since 2002-03 | NHL stats glossary (S, MsS, BkS entries) | SUPPORTED |
| 6 | NHL.com calls Corsi SAT and a player's own attempts iSAT; quote of the iSAT/60 definition | NHL stats glossary | SUPPORTED |
| 7 | NST uses iCF and iFF (unblocked) | NST glossary | SUPPORTED |
| 8 | MoneyPuck's column is I_F_shotAttempts (shots on goal, missed, blocked attempts); the site reads it | MoneyPuck data dictionary; MoneyPuck skater file | SUPPORTED |
| 9 | NST's definition excludes the shootout | NST glossary ("outside of the shootout") | SUPPORTED |
| 10 | Worked example (6 attempts, iFF 5, SOG 3; 24 per 60 over 15 minutes ≈ double the 5v5 median) | Invented numbers; median 11.86 (row 15) | SUPPORTED (illustrative) |
| 11 | MoneyPuck's shot-attempt column equals SOG + misses + blocked for all 940 skaters; 152,884 attempts; 40,841 blocked (26.7%, a little more than a quarter) | W&W calc, MoneyPuck 2025-26 skater file | SUPPORTED (computed) |
| 12 | Forwards with 60+ GP (327): median 248 attempts, top 10% ≥ 421 | Same | SUPPORTED (computed) |
| 13 | MacKinnon led with 600; Werenski second (590), the only defenseman in the top eight | Same | SUPPORTED (computed) |
| 14 | DeBrincat third at 579, more than twice the median forward; Larkin next in Detroit at 452 | Same | SUPPORTED (computed) |
| 15 | 5v5 median forward (385, 500+ min) 11.86 attempts per 60; DeBrincat 20.09, 6th; defensemen median 9.27 (213) | Same, 5on5 | SUPPORTED (computed) |
| 16 | Year-to-year: iCF/60 0.85, G/60 0.42, shooting % 0.25 (324 forwards) | W&W calc, MoneyPuck 2024-25 and 2025-26 | SUPPORTED (computed) |
| 17 | Copp 5v5 attempt rate 9.67, 304th of 385; ixG 19.8 above the 17.3 forward median; 0.107 xG per unblocked attempt vs league 0.073 | W&W calc, MoneyPuck 2025-26 (league = 8,213 xG ÷ 112,043 unblocked) | SUPPORTED (computed) |
| 18 | Blocked share: median defenseman 36% (161 with 60+ GP), median forward 22%; Sandin-Pellikka 89 of 211 (42%), 16th-highest; Seider 123 of 409 (30%) | Same | SUPPORTED (computed) |
| 19 | Share of on-ice 5v5 attempts: median forward 21%; DeBrincat 33%, 2nd behind Arvidsson (37%); Copp 17% | Same | SUPPORTED (computed) |
| 20 | The NHL logs a blocked attempt at the spot of the block, so blocks have no shot location and xG models leave them out | NHL.com (Lukan, 2022, "the NHL marks where a shot is blocked not where it was shot from"); Evolving-Hockey glossary | SUPPORTED |
| 21 | Power-play time produces attempts much faster than 5v5 | W&W calc, MoneyPuck 2025-26: forwards pooled, 20.08 attempts per 60 at 5on4 vs 12.22 at 5on5 | SUPPORTED (computed) |

Computed rows: `research/glossary-pseo/raw/mp_skaters_2025.csv` (MoneyPuck 2025-26, downloaded 2026-10-09) and `raw/mp_skaters_2024_repeatability.csv` (MoneyPuck 2024-25, downloaded 2026-10-09).

## Voice metrics (running prose, `--target barnwell_lean`)

1,031 words. Sentence mean 18.4, SD 10.3; short 12%, long 12%; 57 words per paragraph; one-sentence paragraphs 11%; contractions 33.9/1k; I 0.0; you 7.8; questions 1.9; parentheses 5.8; intensifiers 1.0; transition openers 0%; numbers 47.5/1k; hedges 0.0. Every metric in range ("you" sits near the top of its band). ai-content-detection: no contrast frames, colon pivots or unicode artifacts; hints are uniform_paragraph_structure and repeated_ngrams.
