# Claims register: regulation-wins.json

Reviewed 2026-10-09. Raw files in `research/glossary-pseo/raw/`, all downloaded 2026-10-09.

Tiebreak order (brief asked to verify), NHL.com Tie-Breaking Procedure: 1 fewer games played (superior points percentage), 2 regulation wins (RW column), 3 regulation plus overtime wins (ROW column), 4 total wins, 5 points in games among tied clubs (odd game excluded), 6 goal differential, 7 goals scored; a shootout win counts as one goal for and a shootout loss as one goal against. RW became the first wins tiebreaker in 2019-20: the NHL's standings season settings flag `regulationWinsInUse` true from 20192020 (false for 20182019), and Oilers Nation (Sept 12, 2019) reported it as "a new rule tweak for the 2019-20 season." I found no NHL.com announcement page for the change; the NHL's own season-settings feed is the primary source.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | RW = games won within 60 minutes, before OT or shootout; ROW adds OT wins and leaves out only shootout wins | NHL.com tie-breaking procedure ("excluding games won in Overtime or by Shootout (i.e., 'Regulation Wins')"; "excluding games won by Shootout"); NST glossary (ROW) | SUPPORTED |
| 2 | When teams finish level on points, RW is the first tiebreaker | NHL.com procedure (RW follows games played, which are equal at season's end) | SUPPORTED |
| 3 | 2023-24: Washington and Detroit both 91 points; Capitals' 32 RW beat Wings' 27 for the East's last playoff spot | NHL standings for April 18, 2024 (`nhl_standings_season_ends_2015-16_to_2025-26_det_ptspct.json`): WSH 91, RW 32, wildcard 2, clinched; DET 91, RW 27, wildcard 3 | SUPPORTED |
| 4 | OT losses started paying a point in 1999-2000 | NHL standings season settings (`pointForOTlossInUse` from 19992000) | SUPPORTED |
| 5 | NHL standings show ties giving way to the shootout in 2005-06 | Standings for April 4, 2004 (340 team ties, 0 shootout wins) and April 18, 2006 (0 ties, 145 shootout wins); season settings (`tiesInUse` false from 20052006) | SUPPORTED |
| 6 | Before 2010-11 the first tiebreaker "had been total wins of any kind"; Columbus GM Scott Howson proposed counting regulation and OT wins; league's reason "to give more weight to victories gained in some form of team play"; ESPN reported it that August | ESPN, "Source: NHL to change tiebreaker," Aug 22, 2010 (quotes verbatim) | SUPPORTED |
| 7 | The change took effect in 2010-11 and the count became ROW with its own standings column | NHL season settings (`rowInUse` from 20102011); NHL.com procedure ("reflected in the ROW column") | SUPPORTED |
| 8 | Nine seasons later, for 2019-20, RW moved ahead of ROW as the first tiebreaker after games played, with an RW column; order still stands | Season settings (`regulationWinsInUse` from 20192020); Oilers Nation, Sept 12, 2019; NHL.com procedure ("reflected in the RW column") | SUPPORTED |
| 9 | A 60-minute win is the most useful kind for tiebreaks even though it pays the same two points | Row 1 + points = 2 × W + OTL for all 32 teams in 2025-26 | SUPPORTED |
| 10 | Full procedure as listed, shootout win = one goal for | NHL.com tie-breaking procedure | SUPPORTED |
| 11 | RW decides ties only once games played are equal, which they are by the final night of a normal season | NHL.com procedure; 2025-26 final standings (all 32 at 82 GP) | SUPPORTED |
| 12 | Formulas RW = W − OTW − SOW; ROW = W − SOW; RW% = RW ÷ GP | Standings API fields (`regulationWins`, `regulationPlusOtWins`, `shootoutWins`, `regulationWinPctg` = RW/GP; W = ROW + SOW for all 32) | SUPPORTED |
| 13 | Worked example (45 W with 6 OT and 5 SO = 34 RW, 40 ROW; rival 44 W with 36 RW wins the tie) | Arithmetic, labelled invented | SUPPORTED |
| 14 | OT and shootout losses enter neither count; they're OTL and pay a point | NHL standings (OTL column; points formula) | SUPPORTED |
| 15 | SOW/SOL are columns in the NHL's standings feed | Standings API fields `shootoutWins`, `shootoutLosses` | SUPPORTED |
| 16 | Detroit RW% .366 last season | Standings API `regulationWinPctg` 0.365854 | SUPPORTED |
| 17 | 986 of 1,312 wins in regulation, about three in four | W&W calc, `nhl_standings_2026-04-17_final_20252026_ptspct_rw.json` (75.2%) | SUPPORTED (computed) |
| 18 | Colorado most RW (48), Vancouver fewest (15); Detroit's 30 the median | Standings API (median of 32 = 30) | SUPPORTED |
| 19 | St. Louis got 89% of its wins in regulation, the highest share; 63% for Philadelphia, which won a league-high 10 shootouts | W&W calc (STL .892; PHI 27/43 = .628; PHI shootoutWins 10 = max) | SUPPORTED (computed) |
| 20 | Detroit's share 73%, a shade below the league's 75%; nine OT wins, two shootout wins | DET 30/41; ROW 39 − RW 30 = 9; W 41 − ROW 39 = 2 | SUPPORTED (computed) |
| 21 | Six sets of teams finished level on points; two set division seeds | Standings API (ties at 106, 98, 95, 92, 86, 77); TBL/MTL and PIT/PHI were 2nd/3rd in their divisions | SUPPORTED (computed) |
| 22 | Tampa Bay beat Montreal for second in the Atlantic on RW; Pittsburgh beat Philadelphia for second in the Metropolitan (34 to 27) although the Flyers had two more wins; under the old total-wins rule Philadelphia would've been second | Standings API (TBL 40 RW vs MTL 34, division sequence 2 vs 3; PIT 34 vs PHI 27, PIT 41 W vs PHI 43, division sequence 2 vs 3); ESPN 2010 (total wins was the old first tiebreaker) | SUPPORTED |
| 23 | Both pairs met in the first round, and the tiebreak losers won both series | `nhl_playoff_bracket_2026_rw.json` (TBL 3, MTL 4; PIT 2, PHI 4) | SUPPORTED |
| 24 | Detroit's 27 RW in 2023-24 cost it a playoff spot; 30 in each season since, missing by five points (2024-25) and seven (2025-26) | Season-end standings (2024-25: DET 86, East WC2 MTL 91; 2025-26: DET 92, OTT 99) | SUPPORTED |
| 25 | Detroit had more total wins than Washington (41 to 40) and more ROW (38 to 36) in 2023-24, so under either previous rule the spot would've been Detroit's; same 91 points, no postseason | Standings for April 18, 2024; ESPN 2010 (total wins rule); NHL season settings (ROW era 2010-11 to 2018-19, where ROW followed games played) | SUPPORTED |
| 26 | Philadelphia's 43 wins tied for 10th; its 27 RW in the bottom third | Standings API (five teams at 43 W tied from 10th; 22 teams had more than 27 RW) | SUPPORTED (computed) |
| 27 | Los Angeles made the playoffs with 22 RW (tied for second-fewest), 13 wins after regulation, 20 OT/SO losses | Standings API (LAK RW 22, W 35, OTL 20; CHI also 22; VAN 15); bracket (LAK West WC2) | SUPPORTED |
| 28 | Tiebreak reordered six groups, set two division seeds, decided no playoff spots; slotted Detroit 10th in the East, a place ahead of Columbus | Standings API + bracket (no tied group straddled a playoff line; DET conferenceSequence 10, CBJ 11, RW 30 vs 28) | SUPPORTED (computed) |
| 29 | A regulation win and a shootout win are both worth two points | Row 9 | SUPPORTED |
| 30 | Goal differential is sixth in the tiebreak order | NHL.com procedure | SUPPORTED |
| 31 | NHL standings feed lists RW for seasons before it was a tiebreaker | Standings for April 10, 2016 carry `regulationWins` (Detroit 30) while `regulationWinsInUse` is false before 2019-20 | SUPPORTED |

## Voice metrics (`style_metrics.py --target barnwell_lean`, running prose, 1,033 words)

| Metric | Value | Target |
|---|---|---|
| Sentence mean / SD | 18.4 / 10.5 | 17-21 / ≥ 10 |
| Short / long sentences | 9% / 16% | 6-15% / ≤ 20% |
| Words per paragraph | 57 | 55-85 |
| One-sentence paragraphs | 6% | 5-12% |
| Contractions per 1k | 31.0 | ≥ 28 |
| I / you per 1k | 0.0 / 3.9 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.9 / 5.8 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 49.4 | 30-55 |

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, unicode artifacts, question fragments or false ranges. Remaining hints `uniform_paragraph_structure` and `repeated_ngrams` come from the template.

Hover short in `glossary-terms.json` agrees with the page; no change proposed.
