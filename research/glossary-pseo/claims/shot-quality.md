# Claims register: shot-quality.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/mp_teams_2025.csv`, `mp_skaters_2025.csv`
(MoneyPuck season "2025" = 2025-26) and `mp_teams_2024-25_shotquality_yoy_dl2026-10-09.csv` (2024-25;
byte-identical to `mp_teams_2024.csv`), all downloaded 2026-10-09. Shot quality = xG ÷ unblocked attempts. The
league average (0.073, 112,096 attempts) matches the xG page's register rows 3 and 32.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Shot quality = average danger of a team's or player's shots, usually xG per unblocked attempt | Evolving-Hockey Standard Skater Tables (xFSh% = ixG ÷ iFF); Ryder 2004 (quality = probability of a goal) | SUPPORTED |
| 2 | Distance to the net is the biggest single factor | Evolving-Hockey xG write-up ("shot distance is the most 'important' variable in the model, regardless of strength state") | SUPPORTED |
| 3 | Shot type and what happened just before the shot also matter | MoneyPuck about (shot type, last event inputs); Ryder 2004 (shot type, rebounds) | SUPPORTED |
| 4 | League average 0.073 xG per unblocked attempt (all situations), 0.061 at 5v5, 2025-26 | W&W calc, teams file | SUPPORTED (computed) |
| 5 | Across 32 teams quality barely tracked volume (5v5 attempt rate vs xG per attempt r = −0.10) | W&W calc | SUPPORTED (computed) |
| 6 | Detroit 5v5: 40.5 unblocked attempts per 60 (median 40.7, 17th); 0.059 xG per attempt, 28th; 0.061 against, 15th | W&W calc | SUPPORTED (computed) |
| 7 | Ryder, Shot Quality, January 2004, HockeyAnalytics.com; first line "Not all shots on goal are created equal"; quality = chance of becoming a goal | Ryder PDF, title page and introduction | SUPPORTED |
| 8 | 2002-03 data, 62,351 shots including 5,810 goals; priced by distance, type and rebound; team measure "shot quality against" | Ryder PDF (The Data; Analysis; Measuring the Aggregate Quality) | SUPPORTED |
| 9 | Purpose was splitting defense from goaltending | Ryder PDF ("To measure defense, it is necessary to measure shot quality. To measure goaltending, it is necessary to neutralize shot quality") | SUPPORTED |
| 10 | New Jersey allowed the least dangerous shots; spread worth roughly ±19 goals for an average team | Ryder PDF (NJ led SQA; "+/- 8.5% goals means +/- 19 goals for an average team") | SUPPORTED |
| 11 | Sprigings and Toumi (2015) called shot quality the subject of spirited debate | Hockey-Graphs 2015-10-01 ("Shot quality has been the subject of spirited debate despite evidence...") | SUPPORTED |
| 12 | Earliest xG models were often described as shot-quality models | Evolving-Hockey xG write-up | SUPPORTED |
| 13 | EH publishes xFSh% = ixG ÷ iFF | Evolving-Hockey Standard Skater Tables | SUPPORTED |
| 14 | MoneyPuck inputs (distance/angle, type, last event and seconds, skaters, empty net, off wing) | MoneyPuck about; xG page register row 15 | SUPPORTED |
| 15 | Worked example (invented): 50 × 0.06 = 3.0; 30 × 0.10 = 3.0 | arithmetic | SUPPORTED |
| 16 | MoneyPuck danger tiers: low < 8%, medium 8-20%, high ≥ 20% | MoneyPuck glossary | SUPPORTED |
| 17 | 2025-26: 73% of unblocked attempts low danger, 7.9% high danger (all situations) | W&W calc, teams file danger counts | SUPPORTED (computed) |
| 18 | 5v5 best Dallas 0.068; Seattle and Los Angeles last at 0.058; band about 0.01 wide | W&W calc | SUPPORTED (computed) |
| 19 | 5v5: attempt rate vs xGF/60 r 0.90; quality vs xGF/60 r 0.33 | W&W calc | SUPPORTED (computed) |
| 20 | Colorado led 5v5 xGF/60 (3.03) on the most attempts (49.0 per 60) at league-average quality (0.0619 vs median 0.0617); Dallas best quality, fewest attempts (34.7), 22nd in xGF/60 | W&W calc | SUPPORTED (computed) |
| 21 | Minnesota allowed least dangerous attempts at 5v5 (0.056), Carolina most (0.068); Carolina second in 5v5 xGF% | W&W calc; xG page register row 4 | SUPPORTED (computed) |
| 22 | Copp 0.107 xG per attempt, 31st of 238 forwards with 150+ unblocked attempts; 9 goals | W&W calc, skaters file | SUPPORTED (computed) |
| 23 | Hyman 0.144 highest among those forwards; median 0.087; DeBrincat 0.083 on 443 attempts | W&W calc | SUPPORTED (computed) |
| 24 | Detroit's highest-quality shooters van Riemsdyk (0.117, 7th), Finnie (0.108), Copp (0.107), none over 185 attempts; DeBrincat (0.083), Raymond (0.072), Kane (0.067) below the median | W&W calc | SUPPORTED (computed) |
| 25 | Model blind spots: passes not recorded, scorer location errors; Ryder's data had wrap shots from 60 feet | xG page register rows 25, 27; Ryder PDF (Data Quality) | SUPPORTED |
| 26 | Team shot quality year to year (2024-25 → 2025-26, 5v5): 0.48 for, 0.54 against vs 0.62 for attempt rate | W&W calc, 32 teams | SUPPORTED (computed) |
| 27 | MoneyPuck's base model doesn't factor in shooting skill; finishing measured separately as goals above expected | MoneyPuck glossary + about | SUPPORTED |

Live slot: omitted. The pipeline carries team xGF/xGA but no attempt counts. Wanted: team
`situations.{5on5,all}.unblockedShotAttemptsFor/Against` (or computed `xgPerAttemptFor/Against`) with league ranks,
and skater `iFF` (I_F_unblockedShotAttempts) so a leaderboard can sort on xG per attempt.

Abbreviation: `stat.abbr` is set to "xFSh%" (Evolving-Hockey's published name for ixG ÷ iFF) because
glossary-terms.json lists no abbreviation and the hub row and related cards show one. Swap it out if Mark prefers a
blank.

## Voice metrics (running prose, `--target barnwell_lean`, 1,095 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.6 / 10.0 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 18% | 6-15% / ≤ 20% |
| Words per paragraph | 58 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 31.1 | ≥ 28 |
| I / you per 1k | 0.0 / 4.6 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 4.6 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 50.2 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts, question fragments, sentence-negation
pivots or false ranges. Remaining hints (`uniform_paragraph_structure`, `repeated_ngrams`) come from the fixed
template and metric names. `gate_glossary.py shot-quality`: PASS. JSON parses.
Hardest metric: sentence-length SD (first draft 9.4) and one-sentence paragraphs (first draft 21%, every limit was one sentence); fixed by giving limits a second sentence and adding a short beat after a long sentence. Numbers per 1k started at 61 and fell once season ranges became "last season".

Proposed hover short: "How dangerous a team's or player's shots are on average, usually expected goals per unblocked
attempt. Distance to the net is the biggest single factor." (24 words.) Reason: the current short ranks the factors
("Location matters most, then shot type and what happened just before"); the sources confirm distance is first but
don't rank the rest, and the page doesn't either.
