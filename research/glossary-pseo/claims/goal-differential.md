# Claims register: goal-differential.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/nhl_standings_2026-04-16_final_20252026.json`
(NHL standings API, final day of the 2025-26 regular season), `nhl_standings_2024-04-18_final_20232024.json`,
`nhl_team_summary_20252026_pp_pk_gd.json`, `nhl_team_summary_allseasons_to_20252026.json` (NHL stats API team summary,
every regular season) and `mp_teams_2025.csv` (MoneyPuck season "2025" = 2025-26), all downloaded 2026-10-09.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Goal differential = goals for minus goals against; shown as DIFF in the NHL standings | NHL.com hockey glossary (DIFF column, tiebreaker wording); NHL standings API field goalDifferential = goalFor − goalAgainst | SUPPORTED |
| 2 | The standings version counts a shootout win as one goal for (and a shootout loss as one against) | NHL.com tie-breaking procedure ("goals ... awarded for prevailing in Shootouts"); NHL.com glossary ("a victory in a shootout counts as one goal for, while a shootout loss counts as one goal against") | SUPPORTED |
| 3 | 2025-26: R² 0.91 between standings DIFF and points across 32 teams; one point ≈ 3.3 goals; ≈ 6.5 goals per win | W&W calc, OLS points on DIFF (slope 0.305, r 0.954); wins on DIFF slope 0.153 | SUPPORTED (computed) |
| 4 | Detroit minus-17 (20th) with 92 points; line predicts ~87; beat it by ~5, third-largest overshoot behind San Jose (+6.3) and Montreal (+5.6) | W&W calc, standings file (92.19 + 0.305 × −17 = 87.0; residual +5.0) | SUPPORTED (computed) |
| 5 | Detroit 10th in the East, level on points with Columbus (92), missed the playoffs | Standings file (conferenceSequence 10, clinchIndicator e; CBJ 92) | SUPPORTED |
| 6 | Bill James built the Pythagorean won-loss formula in the early 1980s from runs scored and allowed | Dayaratna & Miller, arXiv 1208.1725, introduction | SUPPORTED |
| 7 | Alan Ryder (HockeyAnalytics.com) one of the few to justify the hockey version from first principles before Dayaratna and Miller | arXiv 1208.1725 ("Few outside of Alan Ryder (hockeyanalytics.com) ... have provided a theoretical verification from first principles") | SUPPORTED |
| 8 | Dayaratna and Miller, 2012, three seasons (2008-09 to 2010-11), formula as applicable to hockey as baseball, exponent slightly above two | arXiv 1208.1725 (v1 Aug 8, 2012; Data and Results; Conclusions) | SUPPORTED |
| 9 | DIFF is the sixth tiebreaker, after games played, regulation wins, regulation + overtime wins, total wins, head-to-head points; overtime goals count | NHL.com tie-breaking procedure, steps 1-6 | SUPPORTED |
| 10 | Hockey-Reference's SRS adjusts average goal differential for strength of schedule; reads in goals above/below average, zero = average | Hockey-Reference glossary (SRS) | SUPPORTED |
| 11 | This site's expected standings run James's (Pythagorean) formula on expected goals | `pipeline/build_site_data.py` deserved method ("xG-Pythagorean (exponent 2)"); `src/pages/team.astro` lede | SUPPORTED |
| 12 | Worked example (invented): 250-230 = +20; with 6 SO wins and 4 SO losses, 256-234 = +22 | arithmetic | SUPPORTED |
| 13 | Detroit 2025-26 minus-15 in stats tables (239-254), minus-17 in standings (241-258); 2 SO wins, 4 SO losses | NHL team summary vs standings file | SUPPORTED (computed) |
| 14 | Colorado's 302 standings goals = 298 scored + 4 shootout wins | Same two files | SUPPORTED (computed) |
| 15 | League average DIFF is zero by construction | Standings file (sum of goalDifferential = 0); arithmetic | SUPPORTED |
| 16 | 326 games went to OT/SO in 2025-26; average club 92.2 points, ten more than an even split (82 of 164) | Standings file (sum otLosses 326; 2,950 points / 32) | SUPPORTED (computed) |
| 17 | Colorado +99 (best), Vancouver −100 (last), median team −4 | Standings file | SUPPORTED (computed) |
| 18 | 608 back-to-back season pairs since 2005-06: DIFF per game → next season's points % r = 0.54; points % → next points % r = 0.52 | W&W calc, NHL team summary all seasons (same franchise ID) | SUPPORTED (computed) |
| 19 | Rangers −12 with 77 points, ~11 below the line, largest shortfall | W&W calc, standings file (residual −11.5) | SUPPORTED (computed) |
| 20 | 2023-24: Detroit +4, Washington −37, both 91 points; Capitals took the East's last spot on regulation wins, 32 to 27; 41-goal edge never came into play | Standings file 2024-04-18 (WSH x, 8th; DET 9th; equal GP so step 2 decides) + tiebreak procedure | SUPPORTED |
| 21 | Colorado +99 = 1.21 goals a game; Tampa Bay second at +59 | Standings file (99/82) | SUPPORTED (computed) |
| 22 | Detroit 2025-26 5v5: minus-28 on goals (142-170), minus-8.1 on xG (161.1-169.2); nearly all of the gap was finishing; allowed almost exactly what the model expected | W&W calc, MoneyPuck teams file 5on5 (GF − xGF −19.1 of a 19.9 gap; GA 170 vs xGA 169.2) | SUPPORTED (computed) |
| 23 | Philadelphia 10 shootout wins, 4 losses; +1 in stats tables (240-239) became +7 in standings (250-243) | Standings file + NHL team summary | SUPPORTED (computed) |
| 24 | 19.1-goal finishing shortfall ≈ six standings points at the league's rate | 19.1 ÷ 3.28 = 5.8 (rows 3, 22) | SUPPORTED (computed) |
| 25 | Empty-net goals, blowouts and shootout goals all count in the differential; schedule strength isn't adjusted | Definition (rows 1-2); Hockey-Reference SRS exists to adjust schedule | SUPPORTED |
| 26 | FAQ: Montreal 1976-77 +216 (387-171) best ever; 1974-75 Capitals −265 worst; Detroit's best +144 in 1995-96, 62 wins | NHL team summary all seasons | SUPPORTED (computed) |
| 27 | FAQ: plus-minus counts even-strength and shorthanded goals while on ice and skips power-play goals at both ends | Hockey-Reference glossary (plus/minus definition) | SUPPORTED |

Live slot: `record.goalFor`, `record.goalAgainst` (NHL standings, shootout goals included) and
`situations.5on5.goalsFor/goalsAgainst` (MoneyPuck); `live.credit` = "NHL API and MoneyPuck". No leaderboard (skaters
carry no plus-minus or on-ice goals). Wanted: `record.goalDifferential` in team.json with a league rank
(`dashboard.standings.goalDifferential` already exists, so `{ source: "dashboard", path: "standings.goalDifferential" }`
would work today if Mark is happy to read outside the listed fields), plus `leagueRanks.goalDifferential` and a
skater `fiveOnFive.onIceGoalsFor/Against`.

## Voice metrics (running prose, `--target barnwell_lean`, 1,285 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 17.8 / 10.1 | 17-21 / ≥ 10 |
| Short / long sentences | 11% / 15% | 6-15% / ≤ 20% |
| Words per paragraph | 56 | 55-85 |
| One-sentence paragraphs | 9% | 5-12% |
| Contractions per 1k | 35.8 | ≥ 28 |
| I / you per 1k | 0.0 / 3.1 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.6 / 4.7 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 52.9 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts, question fragments, sentence-negation
pivots or false ranges. Remaining hints (`uniform_paragraph_structure`, `repeated_ngrams`) come from the fixed
template and metric names. `gate_glossary.py goal-differential`: PASS. JSON parses.
Hardest metric: numbers per 1k (first draft 86.5; season ranges count twice, so most "2025-26" became "last season"), then words per paragraph and "you" per 1k.

Hover short: the current `short` agrees with the page. No change proposed.
