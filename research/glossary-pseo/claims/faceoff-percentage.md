# Claims register: faceoff-percentage.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`mp_skaters_2025.csv` and `mp_teams_2025.csv` (MoneyPuck season "2025" = 2025-26),
`nhl_team_faceoffpct_20252026_realtimefamily_dl2026-10-09.json`,
`nhl_skater_faceoffwins_20252026_realtimefamily_dl2026-10-09.json`, and
`nhl_pbp_20252026_pergame_summary_realtimefamily_dl2026-10-09.csv` (W&W summary of all 1,312 games' NHL
play-by-play). Sources: `schuckers_pasquali_curro_faceoff_analysis_2012_wayback_dl2026-10-09.pdf`,
`czuzoj-shulman_sportlogiq_faceoffs_arxiv1902.02397_dl2026-10-09.pdf`, `nhl_rulebook_2025-26_downloaded_20261009.pdf`,
`nhl_stats_glossary_20261009.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | FO% = faceoffs won ÷ faceoffs taken; FOW counts wins, FOL losses | NHL glossary FOW% ("FOW/FO or FOW/(FOW+FOL)"), FOW, FOL | SUPPORTED |
| 2 | Every draw has one winner, so the league sits at 50% | Definition; 2025-26 even-strength league FO% 49.9995% (NHL team report, 120,400 EV draws) | SUPPORTED |
| 3 | Best regular centers win around 60%; only five of 120 skaters with 500+ draws reached 60%, Giroux led at 63.1% on 799 | W&W calc, MoneyPuck skaters file, faceoffsWon ÷ (faceoffsWon + faceoffsLost), all situations | SUPPORTED (computed) |
| 4 | NHL has published FOW for every player since 1997-98 ("nearly three decades" = 29 seasons) | NHL glossary FOW, FOL, FOW% firstSeasonForStat 19971998; API returns 1997-98 team faceoff data | SUPPORTED |
| 5 | A single win is worth about one seventy-sixth of a goal | Schuckers, Pasquali, Curro 2012: 76.5 wins per goal of differential | SUPPORTED |
| 6 | EV/PP/SH splits from 1997-98; zone splits from 2009-10 ("a dozen seasons later") | NHL glossary EV/PP/SH FOW% (1997-98), OZ/DZ/NZ FOW% (2009-10) | SUPPORTED |
| 7 | Rule 36: three stats-entry scorers, a time-on-ice scorer, an event analyst, overseen by a scoring system manager, to "electronically record all official statistics" | NHL Official Rules 2025-26, Rule 36.1-36.2 | SUPPORTED |
| 8 | Rule 76: linesperson drops the puck; defending player places stick first at the eight non-center spots, visitor first at center | Rule 76.4, 2025-26 rulebook | SUPPORTED |
| 9 | The rule doesn't say who wins the draw | Searched Rule 76 text (2025-26) for win/won/possession: "win" appears only in "gain an advantage to win the face-off" | SUPPORTED |
| 10 | Working standard: team that gets the puck first after the drop wins; the two players who took the draw get the win and loss | Czuzoj-Shulman et al. 2019 ("considered to be won or lost based on which team earns possession first after puck drop"); NHL play-by-play faceoff events carry winningPlayerId/losingPlayerId | SUPPORTED |
| 11 | Sportlogiq paper was a Sloan paper | arXiv 1902.02397 listing: accepted to the 2019 MIT Sloan Sports Analytics Conference | SUPPORTED |
| 12 | Wingers take draws, including when an official removes a center for a violation; a team's second violation on the same draw is a bench minor | Rule 76.4 (replacement "by any teammate then on the ice"), 76.7 (two violations, bench minor) | SUPPORTED |
| 13 | Players listed as centers took 86% of 2025-26 draws | W&W calc, MoneyPuck skaters file by position (C 127,001 of 146,934) | SUPPORTED (computed) |
| 14 | Schuckers, Pasquali, Curro (St. Lawrence) ran 211,372 faceoffs from 2008-09 through 2010-11; 76.5 wins per goal | Schuckers et al. 2012 summary and Table 1 | SUPPORTED |
| 15 | Czuzoj-Shulman and four co-authors cited the same figure in 2019 ("seven years later"), used computer-vision tracking data, argued win type matters | arXiv 1902.02397 (five authors; "~75 face-off wins to achieve a +1 goal differential", ref 3 = Schuckers et al.; "proprietary SPORTLOGiQ set created via advanced computer vision techniques") | SUPPORTED |
| 16 | 73,496 faceoffs in 2025-26, a little over 56 a game | NHL team faceoff report (146,992 team draws ÷ 2) and play-by-play count; 73,496 ÷ 1,312 = 56.0 | SUPPORTED (computed) |
| 17 | Worked example (1,000 draws, 550 wins, +100, ≈1.3 goals) | Invented round numbers, labelled; 100 ÷ 76.5 = 1.31 | SUPPORTED (illustrative) |
| 18 | NHL spells it face-off win percentage; labels it FOW% | NHL glossary FOW% "Face-off win percentage" | SUPPORTED |
| 19 | End-zone wins worth far more than neutral; special-teams wins worth more than even strength | Schuckers et al. Table 1: Off/Def 60.1 vs Neutral 163.8; PP/SH 40.9 vs EV 101.6 | SUPPORTED |
| 20 | Adjusted model (zone, strength, home) correlated with raw FO% at better than 0.95; conclusion: raw FO% needs no adjusting | Schuckers et al. ("r>0.95"; "adjusting for these other factors is unnecessary") | SUPPORTED |
| 21 | More than you can say for the hits and giveaways the same scorers log | Schuckers and Macdonald 2014 rink effects for HITs and GIVEs (see hits / takeaways registers) | SUPPORTED |
| 22 | 2025-26 team FO%: Buffalo 45.9% (last), Rangers 54.5% (1st), Ottawa a hair behind (54.511% vs 54.515%) on more draws (4,610 vs 4,496) | NHL team faceoff report | SUPPORTED |
| 23 | Detroit 51.0%, 10th, 93 more wins than losses | NHL team report (0.51003 on 4,635; MTL 0.50978, VGK 0.50954); MoneyPuck teams 2,364 won, 2,271 lost | SUPPORTED (computed) |
| 24 | Teams on the power play won 54.4% of power-play draws | W&W calc, draw-weighted ppFaceoffPct across 32 teams (13,296 PP draws) | SUPPORTED (computed) |
| 25 | A team's number blends several centers | Detroit had five players with 286+ draws (MoneyPuck skaters) | SUPPORTED |
| 26 | 120 skaters with 500+ draws, median 51.1% | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 27 | Larkin took the third-most draws (1,492, behind Hischier 1,808 and Staal 1,512), won 52.9%, a little above the median | MoneyPuck skaters file (43rd of 120) | SUPPORTED (computed) |
| 28 | Copp was Detroit's best regular (500+ draws) at 54.2% | MoneyPuck skaters file (Copp 54.2% on 990; Larkin 52.9%; Compher 50.9%) | SUPPORTED (computed) |
| 29 | At 76.5: Ottawa's league-best +416 ≈ 5.4 goals; Buffalo −384 ≈ 5.0; Detroit +93 ≈ 1.2 | MoneyPuck teams faceOffsWonFor/Against (OTT 2,513-2,097; BUF 2,149-2,533; NYR +406); ÷ 76.5 | SUPPORTED (computed) |
| 30 | Team FO% and goal differential correlated at 0.10 across the league | W&W calc, Pearson r, 32 teams, MoneyPuck teams file (r = 0.0998) | SUPPORTED (computed) |
| 31 | Larkin 50.3% in the defensive zone, 54.5% in the offensive zone | NHL skater faceoff report (278/553, 297/545) | SUPPORTED (computed) |
| 32 | Compher took 448 defensive-zone draws, far more than offensive (268), won 47.3% | NHL skater faceoff report (212/448) | SUPPORTED (computed) |
| 33 | Copp won 53.4% of his defensive-zone draws, best of the three | NHL skater faceoff report (173/324) | SUPPORTED (computed) |
| 34 | About 60 end-zone wins and about 164 neutral-zone wins per goal | Schuckers et al. Table 1 (60.1, 163.8) | SUPPORTED |
| 35 | Special-teams draws worth about 2.5 times even-strength (40.9 vs 101.6) | Schuckers et al. Table 1; 101.6 ÷ 40.9 = 2.48 | SUPPORTED |
| 36 | Schuckers' group: best faceoff men should take more draws outside the neutral zone and on special teams | Schuckers et al. conclusion | SUPPORTED |
| 37 | Larkin 264 power-play draws, 59.5%, more than six points above his overall 52.9% | NHL skater faceoff report (157/264) | SUPPORTED (computed) |
| 38 | 1,200 draws at 60% ≈ 3.1 goals a season, about one standings point | Schuckers et al. ("1200 faceoffs ... 60% ... 3.13 ... one point per season") | SUPPORTED |
| 39 | Only 23 skaters took 1,200+ draws in 2025-26; only five won 60% of 500+ | MoneyPuck skaters file | SUPPORTED (computed) |
| 40 | 44.5% of wins clean; clean offensive-zone wins led to a shot event 38.6% vs 30.3% | Czuzoj-Shulman et al. 2019 (2017-18 sample) | SUPPORTED |
| 41 | A teammate recovering a loose puck earns the center the win | Possession-first definition (row 10); paper's non-clean win definition ("a player must skate ... to recover the loose puck") | SUPPORTED |
| 42 | Team analyst: about 5% of faceoffs recorded wrong; Nassau Coliseum singled out | Schuckers et al. 2012 ("approximately 5% ... Nassau Coliseum is especially egregious") | SUPPORTED |
| 43 | FO%'s correlation with goals −1.8% and with wins 0.03% | Czuzoj-Shulman et al. 2019 (2017-18) | SUPPORTED |
| 44 | FAQ: home ice raised win chance by 1.5% (Schuckers); home teams won 50.4% of 2025-26 draws | Schuckers et al. ("being at home increase the win percentage by 1.5%"); W&W play-by-play tally 37,070 of 73,496 | SUPPORTED (computed) |
| 45 | Facts: NYR 54.5%, BUF 45.9%, Giroux 63.1% on 799, DET 51.0% 10th, NHL since 1997-98, zone splits since 2009-10 | Rows 3, 6, 22, 23 | SUPPORTED |
| 46 | Variant: OZ/DZ/NZ FO% published since 2009-10 | NHL glossary | SUPPORTED |

Cut for lack of verification: any claim that the NHL rulebook or stats glossary defines who wins a draw (it doesn't);
a Sportlogiq-original "75 wins per goal" (the paper cites Schuckers for it); claims about why teams keep specialists
on the ice for power-play draws.

## Voice metrics (running prose, `--target barnwell_lean`, 1,241 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 18.5 / 10.1 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 15% | 6-15% / ≤ 20% |
| Words per paragraph | 62 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 29.0 | ≥ 28 |
| I / you per 1k | 0 / 3.2 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.6 / 4.8 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 54.0 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts or trailing participles. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and metric names.

Hover short: the current `short` in glossary-terms.json agrees with the page. No change proposed.
