# Claims register: points-percentage.json

Reviewed 2026-10-09. Raw files in `research/glossary-pseo/raw/`, all downloaded 2026-10-09. The 2025-26 regular season ended April 16, 2026 (NHL schedule API: last regular-season games 4/16, playoffs from 4/18); standings for April 17 are final (all 32 teams at 82 GP; identical to the April 16 file another writer saved).

Tiebreak order (brief asked to verify), NHL.com Tie-Breaking Procedure: 1 fewer games played (superior points percentage), 2 regulation wins, 3 regulation plus overtime wins, 4 total wins, 5 points in games among tied clubs (odd game excluded; points percentage when more than two are tied), 6 goal differential, 7 goals scored; a shootout win counts as one goal for. RW became the first wins tiebreaker in 2019-20 (NHL standings season settings `regulationWinsInUse` from 20192020; Oilers Nation, Sept 12, 2019).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | P% = points ÷ (2 × games played); compares teams with different games played | Hockey-Reference glossary ("PTS%: points divided by maximum possible points"); NHL standings API `pointPctg` = points/(2 × GP) for all 32 teams | SUPPORTED |
| 2 | NHL uses it as the first step in breaking ties | NHL.com tie-breaking procedure step 1 ("The fewer number of games played (i.e., superior points percentage)") | SUPPORTED |
| 3 | League average isn't .500; it was .562 last season | W&W calc, 2,950 points / 5,248 available, `nhl_standings_2026-04-17_final_20252026_ptspct_rw.json` | SUPPORTED (computed) |
| 4 | Win in regulation, OT or shootout = 2 points; OT/SO loss = 1; regulation loss = 0 | NHL standings API: points = 2 × wins + otLosses for all 32 teams, 2025-26 | SUPPORTED (computed) |
| 5 | Loser's point dates to 1999-2000; last ties in 2004-05 | NHL standings season settings (`pointForOTlossInUse` from 19992000; `tiesInUse` false from 20052006) (`nhl_standings_season_flags_downloaded_2026-10-09_rw.json`); standings for April 4, 2004 show 340 team ties | SUPPORTED |
| 6 | Hockey-Reference defines PTS% for teams and goalies; NHL labels it P% | Hockey-Reference glossary; NHL return-to-play release table header "Team P% Odds" | SUPPORTED |
| 7 | Tiebreak quote "the fewer number of games played (i.e., superior points percentage)" | NHL.com tie-breaking procedure | SUPPORTED |
| 8 | Once schedules are complete it's just points | All teams at 82 GP in final 2025-26 standings | SUPPORTED |
| 9 | When the 2019-20 season stopped, the NHL declared the regular season over and picked its 24-team field "on the basis of points percentage at the pause" | NHL release, May 26, 2020 (`nhl_return_to_play_release_2020-05-26_ptspct.pdf`): "The 2019-20 regular season is declared concluded through games of March 11"; "24 teams will resume play: the top 12 in each Conference on the basis of points percentage at the pause"; references COVID-19 | SUPPORTED |
| 10 | Detroit's .275 was the worst; best lottery odds, 18.5% | Same release, lottery table ("1. Detroit Red Wings .275 18.5%") | SUPPORTED |
| 11 | Ties counted a point each before 2005-06 (input and formula) | Row 5; standard tie value in the pre-2005 points system (2 × W + T + OTL matches NHL `points` for 2003-04 teams) | SUPPORTED |
| 12 | Worked example (24 points in 20 games = .600; 25 in 22 = .568; two games in hand) | Arithmetic, labelled invented | SUPPORTED |
| 13 | Printed as a three-digit decimal; standings sort on points, percentage only when level | NHL release format (.275); NHL tie-breaking procedure | SUPPORTED |
| 14 | Detroit's win % .500 last season | NHL standings API `winPctg` 0.5 (41/82) | SUPPORTED |
| 15 | ROW% split Buffalo and New Jersey, tied at .493, in the 2020 lottery order | NHL release: "Buffalo Sabres ranked higher than New Jersey Devils on the basis of higher regulation/OT win percentage (Buffalo, .406 ROW%; New Jersey, .348 ROW%)" | SUPPORTED |
| 16 | 326 of 1,312 games went past regulation, three points each | Standings API: 326 overtime losses (one per such game), 1,312 games (32 × 82 / 2); 2,950 = 2 × 1,312 + 326 | SUPPORTED (computed) |
| 17 | Winnipeg exactly .500, 26th | Standings API (82 points, leagueSequence 26) | SUPPORTED |
| 18 | Colorado led at .738, Vancouver last at .354 | Standings API | SUPPORTED |
| 19 | Detroit .561 = league median exactly; one of four teams tied at 92 (Utah, Columbus, Anaheim) | Standings API (median of 32 = .561; UTA/DET/CBJ/ANA 92) | SUPPORTED (computed) |
| 20 | Ottawa took the East's last wild card at .604 (99), seven points clear of Detroit; Los Angeles got in out West at .549 | Standings API; `nhl_playoff_bracket_2026_rw.json` (East WC2 OTT, West WC2 LAK) | SUPPORTED |
| 21 | 2019-20: teams had played different numbers of games (68-71); NHL ranked by P%; Islanders (.588, 80 points in 68) ahead of Toronto and Columbus (.579, 81 in 70) | Standings for March 11, 2020 (`nhl_standings_season_ends_2015-16_to_2025-26_det_ptspct.json`); NHL release | SUPPORTED |
| 22 | Detroit .275 in 2019-20, .429 in the 56-game 2020-21 season, climbed in four of five seasons since (.451, .488, .555, .524), to .561 | Same file (season-end standings 2019-20 to 2025-26) | SUPPORTED (computed) |
| 23 | Los Angeles won 35, a .427 win percentage; 20 OT/SO losses, the league's most; P% .549 | Standings API (wins 35, winPctg .427, otLosses 20 = max) | SUPPORTED |
| 24 | LA's 20 loser points were more than a fifth of its 90 | 20/90 = 22% | SUPPORTED (computed) |
| 25 | A shootout win is worth the same two points as a regulation win; sorted only in tiebreaks through regulation wins | Row 4; NHL tie-breaking procedure | SUPPORTED |
| 26 | Before the loser point an OT loss paid nothing; before ties ended a game could end level | Row 5 | SUPPORTED |
| 27 | Live: rebuilt nightly from the NHL standings | `pipeline/build_site_data.py` team record from NHL standings; `data/site/team.json` record.pointPctg | SUPPORTED |
| 28 | Live small-sample note: a win vs a regulation loss moves P% by .100 at 10 games and .050 at 20 | 2/(2 × 10); 2/(2 × 20) | SUPPORTED |

## Voice metrics (`style_metrics.py --target barnwell_lean`, running prose, 994 words)

| Metric | Value | Target |
|---|---|---|
| Sentence mean / SD | 18.8 / 10.5 | 17-21 / ≥ 10 |
| Short / long sentences | 9% / 17% | 6-15% / ≤ 20% |
| Words per paragraph | 55 | 55-85 |
| One-sentence paragraphs | 6% | 5-12% |
| Contractions per 1k | 31.2 | ≥ 28 |
| I / you per 1k | 0.0 / 7.0 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 2.0 / 6.0 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 46.3 | 30-55 |

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, unicode artifacts, question fragments or false ranges. Remaining hints `uniform_paragraph_structure` and `repeated_ngrams` come from the template.

Hover short in `glossary-terms.json` agrees with the page; no change proposed.
