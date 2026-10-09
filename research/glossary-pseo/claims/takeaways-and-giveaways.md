# Claims register: takeaways-and-giveaways.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`mp_skaters_2025.csv` and `mp_teams_2025.csv` (MoneyPuck season "2025" = 2025-26),
`nhl_team_realtime_20252026_realtimefamily_dl2026-10-09.json`,
`nhl_team_realtime_bygame_{20232024,20242025,20252026}_realtimefamily_dl2026-10-09.json`,
`nhl_team_realtime_byseason_2005-2026_realtimefamily_dl2026-10-09.json`,
`nhl_skater_realtime_top_{giveaways,takeaways}_2005-2026_realtimefamily_dl2026-10-09.json` and
`nhl_pbp_20252026_pergame_summary_realtimefamily_dl2026-10-09.csv` (W&W summary of all 1,312 games' play-by-play).
Sources: `schuckers_macdonald_rink_effects_arxiv1412.1035_dl2026-10-09.pdf`,
`espn_frei_rtss_dropped_2002-09-24_dl2026-10-09.html`, `nhl_rulebook_2025-26_downloaded_20261009.pdf`,
`nhl_stats_glossary_20261009.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Takeaway = player takes the puck from an opponent; giveaway = player gives it up on an unforced error (glossary quotes) | NHL glossary TkA, GvA | SUPPORTED |
| 2 | Arena scorers log both by judgment; counts vary by rink and by season | Rule 36; Schuckers and Macdonald Tables 4 and 12; rows 9-12 below | SUPPORTED |
| 3 | Players with the most giveaways are usually the ones who have the puck most | W&W calc: forwards with 60+ GP, giveaways vs points r = 0.80; all 488 regulars giveaways vs ice time r = 0.79 | SUPPORTED (computed) |
| 4 | MacKinnon led with 165 giveaways while scoring 127 points | MoneyPuck skaters file; NHL skater realtime (165) | SUPPORTED |
| 5 | Forced vs unforced is a real-time scorer's call | Rule 36 (scorers record all official statistics); glossary definitions hinge on forced vs unforced | SUPPORTED |
| 6 | Frei, September 2002: league dropping takeaways, giveaways, hits and blocks from player summaries; quote as Frei's summary of the league's reasoning | Frei, ESPN.com, September 24, 2002 | SUPPORTED |
| 7 | Public realtime report carries both for every team from 2005-06 on | NHL team realtime report (zeros for every team before 2005-06) | SUPPORTED |
| 8 | Schuckers and Macdonald (2014, twelve years after Frei), six seasons ending 2012-13: home teams credited about 68% more giveaways and about 50% more takeaways, the biggest home effects of any event studied | arXiv 1412.1035 Tables 3 and 11 (home ice GIVE 1.67-1.69, TAKE 1.43-1.63; HIT ~1.1, BLOCK ~1.05, SHOT ~1.06, MISS ≤1.13) | SUPPORTED |
| 9 | Columbus recorded giveaways at about 14% of the league rate, Edmonton more than twice it | arXiv 1412.1035 Table 4 (CBJ 0.144, EDM 2.167) | SUPPORTED |
| 10 | Islanders' rink logged takeaways at about twice the rate, Pittsburgh's about a fifth | arXiv 1412.1035 Table 12 and text (NYI 1.943, PIT 0.214) | SUPPORTED |
| 11 | For most of the public era the league logged a few more giveaways than takeaways | W&W calc, NHL team realtime by season: GV/TK ratio 1.03 to 1.36, 2005-06 through 2023-24 | SUPPORTED (computed) |
| 12 | In 2024-25 giveaways doubled and takeaways fell by about a third; 2025-26 29.9 giveaways and 9.2 takeaways a game | W&W calc, by season: GV 14.6 → 29.4 → 29.9, TK 13.9 → 9.6 → 9.2 per game, both teams | SUPPORTED (computed) |
| 13 | Home teams credited 44% more giveaways than visitors in 2023-24, slightly fewer in 2025-26 | W&W calc, NHL team realtime game by game (home/road 1.441; 0.996) | SUPPORTED (computed) |
| 14 | 2025-26 play-by-play: 40,366 giveaways (1,186 charged to goalies) and 12,099 takeaways | W&W play-by-play pull; goalie IDs from MoneyPuck goalies file; NHL skater-credited total 39,180 = 40,366 − 1,186 | SUPPORTED (computed) |
| 15 | Worked example (90 GV, 30 TK, −60) | Invented round numbers, labelled | SUPPORTED (illustrative) |
| 16 | MoneyPuck splits out defensive-zone giveaways; 46% of all giveaways in 2025-26 | MoneyPuck teams file dZoneGiveawaysFor 18,647 ÷ giveawaysFor 40,366 | SUPPORTED (computed) |
| 17 | Combined turnover count: a team's takeaways plus its opponent's giveaways, built to deal with rink effects | arXiv 1412.1035 section 4 ("TURNs events are TAKEs by a 'for team' and GIVEs by the 'against team'"; "created to deal with the issue of REs") | SUPPORTED |
| 18 | Top four in giveaways: MacKinnon 165, Celebrini 150, McDavid 134, Pastrnak 134; all scored 100+ points (127, 115, 138, 100) | MoneyPuck skaters file | SUPPORTED |
| 19 | Team giveaways vs five-on-five CF% r = 0.13; takeaways r = 0.28 | W&W calc, Pearson r, 32 teams, NHL team realtime + MoneyPuck teams 5on5 | SUPPORTED (computed) |
| 20 | Team giveaways ranged Montreal 1,094 to Utah 1,313 | NHL team realtime report (skater-credited) | SUPPORTED |
| 21 | Detroit bottom third in both (1,189 GV, 23rd most; 364 TK, 22nd most) | NHL team realtime report | SUPPORTED |
| 22 | Regular forwards median 55 GV and 19 TK; regular defensemen 80 and 21 | W&W calc, MoneyPuck skaters file, 60+ GP | SUPPORTED (computed) |
| 23 | Seider charged with Detroit's most giveaways (99); DeBrincat led Detroit with 43 takeaways, tied for ninth in the league, and had 87 giveaways | MoneyPuck skaters file; NHL skater realtime matches | SUPPORTED |
| 24 | Datsyuk's 144 takeaways for Detroit in 2007-08 is the single-season high in the public data; he holds second too (132, 2009-10) | NHL skater realtime, all seasons 2005-06 to 2025-26 sorted by takeaways | SUPPORTED |
| 25 | LaCombe led 2025-26 with 52 | MoneyPuck skaters file; NHL skater realtime | SUPPORTED |
| 26 | Takeaways per game down about a third from 2007-08 (13.6 to 9.2) | W&W calc, NHL team realtime by season | SUPPORTED (computed) |
| 27 | DeBrincat 43, Raymond 31, Larkin 18 takeaways, same home scorers | MoneyPuck skaters file | SUPPORTED |
| 28 | Little Caesars Arena credited visitors with 13.5 giveaways a game, fewest; median building 14.8; 8.5 takeaways a game (both teams) ranked 31st | W&W calc, NHL team realtime game by game, 2025-26, grouped by home team | SUPPORTED (computed) |
| 29 | Schuckers and Macdonald required five of six seasons in the same direction | arXiv 1412.1035 section 3, persistence conditions | SUPPORTED |
| 30 | In 2024-25 Detroit's building sat near the middle (13th in giveaways, 20th in takeaways) | W&W calc, NHL team realtime game by game, 2024-25 | SUPPORTED (computed) |
| 31 | Werenski 125, Weegar 124, Bouchard 123 were the three defensemen in the top 11; all played 22+ minutes (26.6, 22.5, 24.7) vs regular-D median 20.4; Bouchard and Werenski were the top two scoring defensemen (95, 81) | MoneyPuck skaters file | SUPPORTED (computed) |
| 32 | 2023-24 arena giveaways (both teams): Montreal 24.1 a game, Columbus 6.2 | W&W calc, NHL team realtime game by game, 2023-24 | SUPPORTED (computed) |
| 33 | Calls made by a different crew in every building | Frei (stats "could vary from building to building, from NHL-paid stats crew to stats crew"); Rule 36 | SUPPORTED |
| 34 | Career or multi-season totals straddling 2024-25 mix eras whose league averages differ by a factor of two | Row 12 (14.6 vs 29.4 giveaways a game) | SUPPORTED (computed) |
| 35 | Play-by-play doesn't record puck touches | Play-by-play event types (no possession or touch event) | SUPPORTED |
| 36 | Facts: per-game figures, MacKinnon 165/127, LaCombe 52, DET 1,189 GV (10th-fewest) and 364 TK (11th-fewest), Datsyuk 144 | Rows 4, 12, 21, 24, 25 | SUPPORTED |

Cut for lack of verification: any cause for the 2024-25 jump in giveaways and drop in takeaways (searched; no
league statement or reporting found, so the page reports the numbers and says nothing about why); claims that most
turnovers go unlogged; the "press box" location of the scorers.

## Voice metrics (running prose, `--target barnwell_lean`, 1,122 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.7 / 10.7 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 19% | 6-15% / ≤ 20% |
| Words per paragraph | 56 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 31.2 | ≥ 28 |
| I / you per 1k | 0 / 5.3 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 5.3 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 51.7 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts or trailing participles. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and metric names.

Hover short: the current `short` in glossary-terms.json agrees with the page. No change proposed.
