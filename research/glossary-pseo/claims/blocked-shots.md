# Claims register: blocked-shots.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`mp_skaters_2025.csv` and `mp_teams_2025.csv` (MoneyPuck season "2025" = 2025-26),
`nhl_team_realtime_20252026_realtimefamily_dl2026-10-09.json`,
`nhl_team_realtime_bygame_20252026_realtimefamily_dl2026-10-09.json`,
`nhl_team_realtime_byseason_2005-2026_realtimefamily_dl2026-10-09.json`,
`nhl_skater_realtime_top_blockedShots_2005-2026_realtimefamily_dl2026-10-09.json` and
`nhl_pbp_20252026_pergame_summary_realtimefamily_dl2026-10-09.csv` (W&W summary of all 1,312 games' play-by-play).
Sources: `schuckers_macdonald_rink_effects_arxiv1412.1035_dl2026-10-09.pdf`,
`espn_frei_rtss_dropped_2002-09-24_dl2026-10-09.html`, `nhl_rulebook_2025-26_downloaded_20261009.pdf`,
`nhl_stats_glossary_20261009.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | A blocked shot is an opponent's attempt a skater stops with his body or stick, credited to the blocker | NHL glossary BkS ("blocked by a skater, with his stick or body"); play-by-play blockingPlayerId | SUPPORTED |
| 2 | Logged by each game's real-time scorers | Rule 36, 2025-26 rulebook | SUPPORTED |
| 3 | A team that blocks a lot is usually defending a lot | W&W calc: team blocks vs five-on-five attempts against per 60, r = 0.59; vs five-on-five CF%, r = −0.56 (32 teams) | SUPPORTED (computed) |
| 4 | Detroit blocked the third-most shots in 2025-26 (1,304) | NHL team realtime report (MTL 1,331, WSH 1,307, DET 1,304) | SUPPORTED |
| 5 | Every blocked shot is an opponent's attempt, so the other team controlled the puck long enough to shoot | Row 1 | SUPPORTED |
| 6 | Shooter's blocked attempt counts toward SAT (Corsi), not USAT (Fenwick) | NHL glossary BkS, SAT, USAT | SUPPORTED |
| 7 | Frei, September 2002: blocks distributed for two seasons, dropped from player summaries with hits, giveaways, takeaways; quote "far less justifiable than the other deletions" | Frei, ESPN.com, September 24, 2002 | SUPPORTED |
| 8 | NHL glossary says blocks recorded since 2002-03; public report has them for every team from 2005-06 | NHL glossary BkS; team realtime report (blocks = 0 for all teams before 2005-06) | SUPPORTED |
| 9 | Schuckers and Macdonald, six seasons ending 2012-13: many rinks with persistent block effects; New Jersey about 54%; Montreal and Toronto more than 24% above; Detroit 0.88 | arXiv 1412.1035 section 4.1, Table 2 (15 rinks; N.J 0.541, MTL 1.271, TOR 1.245, DET 0.879) | SUPPORTED |
| 10 | Home teams got about 5% more blocks; no rink favored its own team | arXiv 1412.1035 Table 1 (home ice 1.037-1.070), "no persistent 'homer' effects for BLOCKs" | SUPPORTED |
| 11 | Play-by-play logs shooter, blocker, block location | Play-by-play blocked-shot fields (shootingPlayerId, blockingPlayerId, x/y, zone, reason) | SUPPORTED |
| 12 | 40,853 blocked attempts; defenders credited with 37,236; 3,617 tagged "teammate-blocked" | NHL team realtime (shotAttemptsBlocked 40,853, blockedShots 37,236); play-by-play reason counts (blocked 37,236, teammate-blocked 3,617, other-block 13) | SUPPORTED (computed) |
| 13 | Worked example (600/60, 400/60) | Invented round numbers, labelled | SUPPORTED (illustrative) |
| 14 | Blocks logged where the block happened; expected-goals models leave them out | Evolving-Hockey glossary and xG write-up (same as expected-goals register row 17) | SUPPORTED |
| 15 | Detroit faced 58.4 five-on-five attempts per 60, eighth-most; median team 56.4 | W&W calc, MoneyPuck teams file, 5on5 shotAttemptsAgainst ÷ (iceTime/3600) | SUPPORTED (computed) |
| 16 | Defenders blocked 24.3% of 152,961 attempts | W&W calc, 37,236 ÷ MoneyPuck teams sum of shotAttemptsFor (all situations) | SUPPORTED (computed) |
| 17 | Block share: Chicago 20.9% (lowest), Montreal 27.1% (highest), Detroit 26.2%, fifth | W&W calc, NHL team blocks ÷ MoneyPuck shotAttemptsAgainst | SUPPORTED (computed) |
| 18 | Regular defensemen median 99 blocks, regular forwards 36 (60+ GP) | W&W calc, MoneyPuck skaters file shotsBlockedByPlayer | SUPPORTED (computed) |
| 19 | McCabe led with 190; Seider fourth with 180; Chiarot 160; Edvinsson 148; three Wings in the top 25 | MoneyPuck skaters file (ranks 4, 11, tied 21 of 940); NHL skater realtime matches | SUPPORTED (computed) |
| 20 | Team with more blocks won 59.1% of games not tied on blocks | W&W calc, 737 of 1,248, NHL team realtime game by game + play-by-play final scores | SUPPORTED (computed) |
| 21 | Teams with a lead take fewer shots and get fewer of them blocked | arXiv 1412.1035 section 4.1 ("teams who are leading a game generally take fewer shots and, consequently, have fewer shots that are blocked") | SUPPORTED |
| 22 | Game-level correlation of block differential with shot-attempt differential −0.72 | W&W calc, Pearson r, 1,312 games, NHL team realtime game by game | SUPPORTED (computed) |
| 23 | Chiarot 5.6 blocks per 60, Seider 5.1 while playing the heaviest minutes on the team (25.7 a game); regular-defenseman median 4.1 | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 24 | Blocked attempts are the gap between Corsi and Fenwick; a defender blocked about one attempt in four | NHL glossary SAT/USAT; row 16 | SUPPORTED |
| 25 | 2025-26 arena blocks (both teams): Los Angeles 31.8 a game, 37% more than Chicago's 23.2 | W&W calc, NHL team realtime game by game, grouped by home team | SUPPORTED (computed) |
| 26 | Teammate-blocked attempt counts against the shooter, no block credited | Row 12 (attempts blocked include teammate blocks; credited blocks don't) | SUPPORTED |
| 27 | Play-by-play has no field for what happens after a block | Row 11 | SUPPORTED |
| 28 | FAQ: Kris Russell 283 for Calgary in 2014-15 is the high in the public data (from 2005-06) | NHL skater realtime, all seasons sorted by blockedShots | SUPPORTED |
| 29 | FAQ: blocks per game peaked two seasons ago (2023-24, 31.5 both teams; 2025-26 28.4) | W&W calc, NHL team realtime by season | SUPPORTED (computed) |
| 30 | FAQ: shots on goal exclude blocked attempts and missed shots | NHL glossary S ("Attempts blocked and missed shots are not included") | SUPPORTED |
| 31 | Facts: 14.2 blocks per team per game (37,236 ÷ 2,624); Carolina fewest 928; McCabe 190 Toronto | NHL team realtime; MoneyPuck skaters | SUPPORTED (computed) |

Cut for lack of verification: when the NHL feed began tagging teammate blocks; any cause for the rink differences;
Frei's guess that general managers disliked blocks for arbitration reasons (opinion, left out).

## Voice metrics (running prose, `--target barnwell_lean`, 1,197 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 18.1 / 10.2 | 17-21 / ≥ 10 |
| Short / long sentences | 8% / 14% | 6-15% / ≤ 20% |
| Words per paragraph | 57 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 35.9 | ≥ 28 |
| I / you per 1k | 0 / 4.2 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.7 / 5.8 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 47.6 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts or trailing participles. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and metric names.

Proposed hover short: Opponents' shot attempts a skater stops with his body or stick before they reach the net. A team that blocks a lot is usually defending a lot.

(The current short says "with his body" only; the NHL glossary and the page say "stick or body".)
