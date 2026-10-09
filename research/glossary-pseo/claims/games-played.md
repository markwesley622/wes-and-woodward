# Claims register: games-played.json

Raw files (all downloaded 2026-10-09, in `research/glossary-pseo/raw/`): `nhl_skater_summary_20252026_sogfamily.json`,
`nhl_goalie_summary_20252026_sogfamily.json`, `nhl_skater_summary_20252026_DETonly_sogfamily.json`,
`nhl_goalie_summary_20252026_DETonly_sogfamily.json` (teamId 17 splits), `nhl_stats_glossary_api_20261009.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | GP = games with at least one shift on the ice (or a shootout appearance); healthy scratches and dressed backups who never play don't get one; rare skater case too | NHL stats glossary GP | SUPPORTED |
| 2 | Per-game stats divide by GP | NHL glossary P/GP, G/GP, A/GP definitions | SUPPORTED |
| 3 | Tracked since 1917-18, the NHL's first season | NHL glossary GP (`firstSeasonForStat` 19171918) | SUPPORTED |
| 4 | Rule 33 (2025-26): In-Arena Scorer lists eligible players and starting lineup on the Official Report of Match and indicates which took part in the game | NHL Official Rules 2025-26, Rule 33.1 | SUPPORTED |
| 5 | Shootout stats start in 2005-06; shootout-only appearance earns a GP at zero minutes | NHL glossary SO stats (`firstSeasonForStat` 20052006) and GP definition | SUPPORTED |
| 6 | GS = games started; GR = GP − GS; pulled-and-returned goalie gets one start and zero relief | NHL glossary GS and GR | SUPPORTED |
| 7 | Worked example: 22 scratches, 60 GP, 15 points = 0.25/game, 20-point pace over 82; injured-on-first-shift game counts | Arithmetic + GP definition; labelled invented | SUPPORTED (invented, labelled) |
| 8 | NHL glossary: dividing by GP "does not account for varying time on ice and varying special teams time" | NHL glossary P/GP (same wording in G/GP, A/GP) | SUPPORTED |
| 9 | 2025-26: 940 skaters played; median 61 GP; 488 with 60+; 99 played exactly 82; Brett Kulak (EDM, PIT, COL) 83; 31 played one game | W&W calc, NHL skater summary 2025-26 | SUPPORTED (computed) |
| 10 | Detroit used 29 skaters; Seider, DeBrincat, Chiarot, Compher, Finnie, Albert Johansson played 82; Kasper 81, Raymond 80, Larkin 74 | NHL skater summary 2025-26, Detroit-only split (teamId 17) | SUPPORTED |
| 11 | 98 goalies, 2,768 GP, 2,624 starts (32 × 82), 144 relief appearances; Vejmelka 64 GP, 63 GS led; four goalies 1 GP, 0 GS (Shepard, Buteyets, DiPietro, Hogberg) | W&W calc, NHL goalie summary 2025-26 | SUPPORTED (computed) |
| 12 | MacKinnon 0.66 G/GP best among 60+ GP; four one-game skaters scored (Rooney, Bonk, Luneau, Booth) for 1.00; Bonk 2 points in 1 game tops Kucherov's 1.71 P/GP (130 in 76), best among 60+ GP | W&W calc, NHL skater summary 2025-26 | SUPPORTED (computed) |
| 13 | Larkin 34 goals in 74 GP = 0.46/game, 37.7 → 38-goal pace over 82; DeBrincat 41 in 82 = 0.50 | W&W calc, NHL skater summary | SUPPORTED (computed) |
| 14 | Gibson 57 GP, 57 GS for Detroit; Talbot 34 GP, 25 GS (9 relief); the two combined for 91 GP in 82 games | NHL goalie summary, Detroit-only split | SUPPORTED |
| 14b | Larkin's eight missed games worth about four goals at 0.46/game, more than half the seven-goal gap to DeBrincat (41 − 34) | 8 × 0.459 = 3.7; 3.7 / 7 = 53% | SUPPORTED (computed) |
| 15 | Hockey-Reference goalie SV%/GAA minimum 0.3125 GP per scheduled game (25.6 → 26 in 82 games); 55 goalies had 26+ GP | Hockey-Reference NHL Leaderboard Stat Requirements; W&W count from NHL goalie summary | SUPPORTED |
| 16 | Jennings Trophy: minimum 25 games | Hockey Hall of Fame, William M. Jennings Trophy page | SUPPORTED |
| 17 | This site requires 300 five-on-five minutes for skater percentiles and 600 minutes for goalies | `pipeline/build_site_data.py` (MIN_SKATER_5V5_SECONDS = 300 × 60; MIN_GOALIE_SECONDS = 600 × 60, all-situations goalie ice time) | SUPPORTED |
| 18 | GP records only games on the ice, so scratches, injuries, suspensions and minors stints look the same | GP definition (no reason field) | SUPPORTED |
| 19 | A traded player can exceed the team schedule (Kulak 83) | NHL skater summary 2025-26 | SUPPORTED |
| 20 | FAQ: Calder eligibility, no more than 25 games in any single preceding season nor six or more in each of any two preceding seasons in any major pro league; no older than 26 by Sept. 15 of rookie season | NHL.com "NHL Calder Memorial Trophy winners complete list," May 13, 2026 | SUPPORTED |
| 21 | FAQ: Marleau 1,779 regular-season games (career 1997-98 to 2020-21), Howe 1,767, Messier 1,756 | Hockey-Reference career games-played leaders | SUPPORTED |

## Voice metrics (extract_prose.py → style_metrics.py --target barnwell_lean)

1,242 words. Sentence mean 17.7 / SD 10.1; short 11%; long 16%; words per paragraph 59; one-sentence paragraphs 10%;
contractions 30.6/1k; I 0; you 4.0/1k; questions 1.6/1k; parentheses 4.0/1k; intensifiers 0; transition openers 0%;
numbers 51.5/1k; hedges 0. All in range. Hardest: sentence SD (kept landing at 9.6-9.9) and numbers per 1k (first
draft 61); the rule's own wording "actually took part" tripped the intensifier count and was paraphrased.

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, balanced negation, false ranges or unicode
artifacts. Hints `uniform_paragraph_structure` and `repeated_ngrams` only.

Cut for lack of verification: Larkin's captaincy, Lidström's career-with-Detroit aside, and any claim about why Talbot's
relief appearances happened.

No hover-short change proposed; the current `short` agrees with the page.
