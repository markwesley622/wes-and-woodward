# Claims register: high-danger-chances.json

Reviewed 2026-10-09. Computed rows use `research/glossary-pseo/raw/mp_teams_2025.csv` and `mp_skaters_2025.csv`
(MoneyPuck season "2025" = 2025-26, downloaded 2026-10-09). NST definitions were read from Internet Archive
snapshots saved in `raw/` (`nst_glossary_teams_wayback_20250105.html`, `nst_glossary_players_wayback_20250109.html`,
`nst_danger_zones_wayback_20240416.png`), because NST blocks automated fetches. War-on-Ice pages saved as
`raw/waronice_annotated_glossary_2015_dl20261009.html` and `raw/waronice_defining_scoring_chances_2014_dl20261009.html`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | HDCF = attempts NST rates most dangerous (danger score 3+), mostly from a box right in front of the net, +1 for rebounds and rush shots | NST team glossary (archived 2025-01-05): "High Danger Scoring Chances - A scoring chance with a score of 3 or higher"; area values 1/2/3; +1 rebound or rush. NST danger-zone map (archived 2024-04-16): the 3 area is the box directly in front of the net | SUPPORTED |
| 2 | NST's count goes back to 2007-08; covers every team and skater | NST glossary: "Choose your starting season ... going back to 2007-08"; team and player on-ice tables carry HDCF/HDCA | SUPPORTED |
| 3 | HDCF% is a team's share, HDCF ÷ (HDCF + HDCA) | NST glossary formula HDCF*100/(HDCF+HDCA) | SUPPORTED |
| 4 | Dek: at 5v5 in 2025-26 MoneyPuck high-danger shots went in 15.6%, low-danger 3.8% | W&W calc: 799/5,133 and 2,507/66,529 (goals ÷ shots by danger tier, 5on5), MoneyPuck teams file | SUPPORTED (computed) |
| 5 | War-on-Ice started in 2014 by Andrew C. Thomas, Sam Ventura and Alexandra Mandrycky | Detroit Free Press 2024-05-23 ("created ... war-on-ice in 2014 alongside Sam Ventura ... and Alexandra Mandrycky"); CBS Minnesota/AP 2016-01-26 (Thomas, Mandrycky co-founders); NHL.com 2017-06-16 (Ventura co-founded) | SUPPORTED |
| 6 | Published its scoring-chance definition December 31, 2014 | War-on-Ice blog, "NEW: Defining Scoring Chances", posted December 31, 2014 | SUPPORTED |
| 7 | Annotated glossary lists high-danger scoring chances (danger 3+) as a WOI original; credits Vollman's "home plate" and David Johnson's rush-shot work | War-on-Ice Annotated Glossary (posted 2015-11-26): HSC = "All shot attempts that have danger 3 or greater", footnote "WOI Original."; "The 'Home Plate' demarcation from Rob Vollman"; rush shots "a definition derived from David Johnson's work" | SUPPORTED |
| 8 | War-on-Ice shut down after about two years once NHL teams hired its founders | Detroit Free Press 2024-05-23: "shut down after two years once the founders started getting hired by NHL teams" | SUPPORTED |
| 9 | Thomas and Mandrycky joined the Wild's front office in January 2016 | CBS Minnesota (AP), 2016-01-26 | SUPPORTED |
| 10 | Ventura went to the Penguins | NHL.com 2017-06-16: co-founded war-on-ice.com "before joining the Penguins in a part-time role" | SUPPORTED |
| 11 | In 2024 the Tigers hired Thomas as a VP to run their baseball analytics department | Detroit Free Press 2024-05-23 (VP of baseball analytics; "leads the analytics department") | SUPPORTED |
| 12 | NST describes scoring chances "as originally defined by War-on-Ice" | NST team glossary, verbatim | SUPPORTED |
| 13 | The Kraken's analytics column on NHL.com used NST's model in a 2022 scoring-chance piece | NHL.com (Kraken), Alison Lukan, "De-Bunking the Stat: What Makes a Scoring Chance?", 2022-05-01: "the model employed by NaturalStatTrick.com and developed by War-On-Ice.com" | SUPPORTED |
| 14 | MoneyPuck publishes its own version built on expected goals; the two counts run on different scales | MoneyPuck glossary (danger tiers by goal probability); row 28 (385 vs 71 for Larkin) | SUPPORTED |
| 15 | Only offensive-zone attempts scored; location 1 / 2 (high slot and the two wedges) / 3 (net-front box); rebound = within 3 s of a blocked, missed or saved attempt, no stoppage; rush = within 4 s of any NZ/DZ event, no stoppage; blocked −1 | NST glossary (verbatim rules); NST danger-zone map for the area shapes | SUPPORTED |
| 16 | Blocked shots lose a point because the league logs a block where it was blocked | War-on-Ice glossary: blocked shots are "recorded at the point at which they've been blocked" | SUPPORTED |
| 17 | Worked example (invented plays): point shot 1; high slot 2; high slot within 2 s of a neutral-zone takeaway = rush, 3; net-front rebound 4, counts as one HD chance | Labelled invented; applies rule rows 1, 15; NST HDCF is a count of attempts scoring 3+ | SUPPORTED |
| 18 | MoneyPuck: high-danger = unblocked attempt with ≥20% goal probability, medium 8-20%, low <8%; blocked shots excluded | MoneyPuck glossary, verbatim cutoffs ("Unblocked Shot attempts ...") | SUPPORTED |
| 19 | MoneyPuck's cut folds in shot type and the previous event | MoneyPuck about (xG model inputs; xG page claims row 15) | SUPPORTED |
| 20 | 5v5 2025-26: 5.9% of unblocked attempts high-danger, 14.9% of goals; all situations nearly three goals in ten (28.9%), closer to MoneyPuck glossary's "~33% of goals" | W&W calc: 5,133/87,486 attempts, 799/5,367 goals (5on5); 2,338/8,086 goals (all); MoneyPuck glossary "~5% of shots and ~33% of goals" | SUPPORTED (computed) |
| 21 | Team 5v5 HD share: Colorado 59.0% (1st), Chicago 42.4% (last), Detroit 48.6% (18th), median 48.9% | W&W calc highDangerShotsFor ÷ (for + against), 5on5 | SUPPORTED (computed) |
| 22 | Detroit generated 2.11 HD shots per 60 (29th; median 2.31) and allowed 2.23 (12th) | W&W calc per 60 of 5on5 iceTime | SUPPORTED (computed) |
| 23 | 327 forwards with 60+ GP: median 20 HD shots, top 10% ≥36 (all situations); Wyatt Johnston led with 51; Larkin tied for 15th with 40; DeBrincat tied for 28th with 37 | W&W calc I_F_highDangerShots, all situations, ties checked (6 skaters at 40, 5 at 37) | SUPPORTED (computed) |
| 24 | HD shot ≈ 4x the scoring odds of a low-danger shot (15.6 vs 3.8); medium-danger 13.0% | W&W calc, row 4; 2,061/15,824 | SUPPORTED (computed) |
| 25 | Detroit 5v5: scored on 17 of 143 HD shots (11.9%), allowed 30 on 151 (19.9%), league 15.6%; at league rate ~22 for and ~24 against; net ~12 goals; shooters (−5.3) and goalies (−6.4) split it almost evenly | W&W calc, DET 5on5 row: highDangerGoalsFor/ShotsFor and Against; 143 × 0.156 = 22.3, 151 × 0.156 = 23.6 | SUPPORTED (computed) |
| 26 | Seider 1,612 5v5 min, on ice for 66 HD for / 56 against (54.1%); Faulk 1,395 min, 41 / 61 (40.2%), 20 more allowed than created | W&W calc OnIce_F/A_highDangerShots, 5on5, skaters file | SUPPORTED (computed) |
| 27 | Copp 29 HD shots all situations, tied for 62nd (7 at 29), nine above the median forward (20), scored on 5, 9 goals | W&W calc I_F_highDangerShots, I_F_highDangerGoals, I_F_goals | SUPPORTED (computed) |
| 28 | NST counted 385 HD chances (170 for, 215 against) with Larkin on at 5v5; MoneyPuck 71 (30, 41); shares 44.2% and 42.3% | NST 2025-26 5v5 DET on-ice table pulled 2026-09-02 (`research/wings-type/raw/nst_5v5_2025.json`, HDCF 170 / HDCA 215 / HDCF% 44.16); W&W calc MoneyPuck | SUPPORTED |
| 29 | Hohl's case against binning (cliff at the line, all attempts inside equal); expected goals prices each attempt | Hockey-Graphs, Garret Hohl, 2017-02-06 | SUPPORTED |
| 30 | Rebound and rush flags come from timestamps (3 s, 4 s); feed doesn't log passes | NST glossary (timing); Evolving-Hockey xG write-up (no pass data; xG page row 25) | SUPPORTED |
| 31 | MoneyPuck's explainer flags a slap shot recorded closer to the net than taken | MoneyPuck about, flurry/demo section (xG page row 27) | SUPPORTED |
| 32 | The count is shooter-blind | Definition (rows 1, 15) has no shooter input | SUPPORTED |
| 33 | FAQ: NST tables filter by game state (all, 5v5, PP, PK); MoneyPuck splits by situation | NST glossary "Game State" filters; MoneyPuck files' `situation` column (all/5on5/5on4/4on5/other) | SUPPORTED |
| 34 | Variant HDSV%: save percentage on HD shots on goal | NST glossary: HDSV% = 100 − (HDGA*100/HDSA) | SUPPORTED |
| 35 | Tile: "This site uses MoneyPuck, its cut is an xG of 0.20 or more" | MoneyPuck glossary; pipeline uses MoneyPuck | SUPPORTED |

Cut for lack of a verifiable source: that HDCF is "the standard" public count; that broadcasts and team sites usually quote NST's
number; War-on-Ice's "Better Than Corsi" post on scoring chances predicting goals (the page is gone from the blog mirror).

## Voice metrics

Running prose: 1315 words (extract_prose.py → style_metrics.py --target barnwell_lean).

| Metric | Page | Target |
|---|---|---|
| sent_mean | 18.8 | 17-21 |
| sent_sd | 10.8 | >=10 |
| pct_short_le6 | 14 | 6-15 |
| pct_long_ge30 | 19 | <=20 |
| para_words | 60 | 55-85 |
| one_sent_paras | 9 | 5-12 |
| contractions_per_k | 32.7 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 6.8 | 3-8 |
| q_per_k | 1.5 | 1-5 |
| paren_per_k | 6.1 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 54.8 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

ai-content-detection analyze_text.py: unicode artifacts 0, em dashes 0, contrast frames 0, payoff colons 0, question fragments 0, sentence-negation flags 0. Remaining n-gram hints are metric names ("five on five", "on the ice").

Hover short: the current `short` in glossary-terms.json agrees with the page (NST rating, net-front box, +1 for rebounds and rush shots confirmed against the archived NST glossary). No change proposed.
