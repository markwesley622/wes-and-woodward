# Claims register: hits.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`mp_skaters_2025.csv` (MoneyPuck season "2025" = 2025-26),
`nhl_team_realtime_20252026_realtimefamily_dl2026-10-09.json`,
`nhl_team_realtime_bygame_{20232024,20242025,20252026}_realtimefamily_dl2026-10-09.json`,
`nhl_team_realtime_byseason_2005-2026_realtimefamily_dl2026-10-09.json`,
`nhl_skater_realtime_top_hits_2005-2026_realtimefamily_dl2026-10-09.json` and
`nhl_pbp_20252026_pergame_summary_realtimefamily_dl2026-10-09.csv` (W&W summary of all 1,312 games' play-by-play,
for final scores). Sources: `schuckers_macdonald_rink_effects_arxiv1412.1035_dl2026-10-09.pdf`,
`espn_frei_rtss_dropped_2002-09-24_dl2026-10-09.html`, `hockeygraphs_hohl_hit_totals_2015_dl20261009.html`,
`nhl_rulebook_2025-26_downloaded_20261009.pdf`, `nhl_stats_glossary_20261009.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | A hit is a body check delivered on the opposing puck carrier, credited to the hitter | NHL glossary Hits ("body checks delivered by a player on the opposing team's puck carrier"); play-by-play hit events carry hittingPlayerId | SUPPORTED |
| 2 | Logged by the real-time scorers at each game | Rule 36 (Real Time Scorers), 2025-26 rulebook | SUPPORTED |
| 3 | Scorers in different arenas don't count them the same way | Schuckers and Macdonald 2014, Table 6 (12 rinks with persistent hit effects) | SUPPORTED |
| 4 | The team that out-hits its opponent loses more often than it wins | W&W calc, 2025-26: out-hitting team won 549 of 1,254 games not tied on hits (43.8%); Hohl 2015 ("out-scoring team tends to be out-hit") | SUPPORTED (computed) |
| 5 | Every hit is thrown by the team that doesn't have the puck | Row 1 (hit lands on the opposing puck carrier) | SUPPORTED |
| 6 | Rule 36 crew makeup and "electronically record all official statistics" | Rule 36.1-36.2 | SUPPORTED |
| 7 | Frei, ESPN, September 2002: NHL had distributed hits, giveaways, takeaways and blocks for two seasons and was scrubbing them from player summaries; quote "involved subjective judgments that could vary from building to building" as Frei's summary of the league's explanation | Frei, "NHL taking the crunch out of numbers," ESPN.com, Tuesday September 24 (2002; the column lists 2001-02 leaders as "last season") | SUPPORTED |
| 8 | Robert Svehla led with 386 hits the season before (2001-02) | Frei column, 2001-02 leaders box | SUPPORTED |
| 9 | Public realtime report carries hits for every team from 2005-06 on | NHL team realtime report: hits = 0 for every team 1997-98 through 2003-04, populated from 2005-06 | SUPPORTED |
| 10 | Facts tile: the glossary says 1997-98 | NHL glossary Hits ("available since 1997-98") | SUPPORTED |
| 11 | Schuckers and Macdonald, twelve years after Frei (2014), five-on-five, six seasons ending 2012-13, rink effect per rink, home teams credited about 11% more hits after team and score effects | arXiv 1412.1035 sections 2-4.3, Table 5 (home ice 1.098-1.144) | SUPPORTED |
| 12 | LA 1.30, Rangers' rink 1.27, New Jersey 0.59 | arXiv 1412.1035 Table 6 (1.298, 1.274, 0.592) | SUPPORTED |
| 13 | Play-by-play logs hitter, player hit and location; 53,658 hits in 2025-26 | Play-by-play hit event fields (hittingPlayerId, hitteePlayerId, x/y, zone); NHL team realtime total 53,658 (MoneyPuck 53,657) | SUPPORTED |
| 14 | Worked example (90 home, 60 road) | Invented round numbers, labelled | SUPPORTED (illustrative) |
| 15 | A legal hit lands on the player with the puck or who's just lost it; Rule 56 calls a check on anyone else interference | Rule 56.1 (possession definition; check "rendered immediately following his loss of possession"; contact with the non-puck carrier penalized as interference) | SUPPORTED |
| 16 | Hohl, Hockey-Graphs, data from October 2007 ("seven-plus seasons", to January 2015), game level; quote "out-scoring team tends to be out-hit" | Hohl, Feb 9 2015 (War-On-Ice data Oct 2007 to Jan 2015) | SUPPORTED |
| 17 | Within a game, hit differential tracked goal differential about as strongly as shot differential, in the opposite direction | Hohl ("hit differentials almost have an equal and opposite relationship with goal differentials as shot differentials have with goals") | SUPPORTED |
| 18 | Hohl cites the saying "you cannot hit when you have the puck" | Hohl, closing thoughts | SUPPORTED |
| 19 | 2025-26 team range Chicago 1,346 to Rangers 2,112; Detroit 1,480, fourth-fewest (29th of 32) | NHL team realtime report | SUPPORTED |
| 20 | Hits per game (both teams) peaked at 50.0 in 2014-15, 40.9 in 2025-26 | W&W calc, NHL team realtime by season, 2005-06 to 2025-26 | SUPPORTED (computed) |
| 21 | 327 forwards with 60+ GP: median 66 hits; Trenin 413 led, more than six times the median | W&W calc, MoneyPuck skaters file (413 ÷ 66 = 6.3) | SUPPORTED (computed) |
| 22 | Defensemen threw about as many per player (median 65) and fewer per minute (2.4 vs 3.6 per 60) | W&W calc, MoneyPuck skaters file, 161 defensemen with 60+ GP | SUPPORTED (computed) |
| 23 | Kasper led Detroit with 186, Chiarot 170 | MoneyPuck skaters file; NHL skater realtime (same) | SUPPORTED |
| 24 | Hits and points correlated at −0.25 across 488 regulars | W&W calc, Pearson r, MoneyPuck skaters file | SUPPORTED (computed) |
| 25 | Teams with a lead have fewer hits recorded, about 3% fewer per goal of average lead | arXiv 1412.1035 section 4.3, Table 5 (ASD exp(β) 0.965-0.979) | SUPPORTED |
| 26 | Chicago skaters 18.0 hits a game at home, 14.8 on the road, biggest home bump; Detroit 18.4 and 17.7 | W&W calc, NHL team realtime game by game, 2025-26 (CHI ratio 1.22, 1st) | SUPPORTED (computed) |
| 27 | Kasper 10.0 hits per 60, almost three times the median regular forward's 3.6, highest of any Wing with 20+ GP | W&W calc, MoneyPuck skaters file (9.99; next Finnie 6.18) | SUPPORTED (computed) |
| 28 | 2025-26 arena totals (both teams): Ottawa 46.1 a game, Seattle 36.8; 2023-24 Toronto 69.6, Columbus 30.6 | W&W calc, NHL team realtime game by game, grouped by home team | SUPPORTED (computed) |
| 29 | Home teams credited 4.4% more hits in 2025-26 | W&W calc, 27,402 home vs 26,256 road | SUPPORTED (computed) |
| 30 | Three rinks (New Jersey, Dallas, Toronto) recorded home and visiting hits differently | arXiv 1412.1035 Table 6 (N.J, DAL, TOR home interactions) | SUPPORTED |
| 31 | Play-by-play has no field for what happened after a hit | Play-by-play hit event detail fields (row 13) | SUPPORTED |
| 32 | FAQ: Sherwood 462 for Vancouver in 2024-25 is the high in the public data (from 2005-06); Trenin's 413 second | NHL skater realtime, all seasons 2005-06 to 2025-26 sorted by hits | SUPPORTED |
| 33 | Facts: 20.4 hits per team per game (53,658 ÷ 2,624); Trenin 413 Minnesota | NHL team realtime; MoneyPuck skaters | SUPPORTED (computed) |

Cut for lack of verification: Hohl's −0.02 was Corsi differential vs goal differential, not hits vs Corsi, so it's
out; no cause is given for the decline in hits per game; the 2025-26 team-season correlation of hits with five-on-five
CF% (−0.11) was too weak to support a "teams that hit don't have the puck" line at the season level, so the page
leans on the definition, Hohl and the 43.8% game result instead.

## Voice metrics (running prose, `--target barnwell_lean`, 1,108 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 17.9 / 10.3 | 17-21 / ≥ 10 |
| Short / long sentences | 11% / 11% | 6-15% / ≤ 20% |
| Words per paragraph | 58 | 55-85 |
| One-sentence paragraphs | 11% | 5-12% |
| Contractions per 1k | 35.2 | ≥ 28 |
| I / you per 1k | 0 / 3.6 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 3.6 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 53.2 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts or trailing participles. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and metric names.

Hover short: the current `short` in glossary-terms.json agrees with the page. No change proposed.
