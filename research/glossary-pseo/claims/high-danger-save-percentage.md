# Claims register: high-danger-save-percentage.json

Reviewed 2026-10-09. Raw files in `research/glossary-pseo/raw/`, all downloaded 2026-10-09. Natural Stat Trick blocks automated fetches (403), so its definitions come from the Internet Archive copies of its own glossary pages (`raw/nst_glossary_teams_archived_2025-01-05_via_wayback_dl2026-10-09.html`, `raw/nst_glossary_players_archived_2025-01-09_via_wayback_dl2026-10-09.html`), confirmed in part by NHL.com (Lukan 2022) and the high-danger-chances page.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | HDSV% is save percentage on shots from the most dangerous ice; NHL version = shots on goal from a zone within 29 feet of the goal (between lines from the faceoff dots to two feet outside the posts) | NHL EDGE glossary ("High-Danger Save Percentage (saves divided by shots on goal faced) is calculated on shots from the area within 29 feet of the center of the goal and bound on both sides by an imaginary line drawn from the face-off dot to 2 feet outside the goal post") | SUPPORTED |
| 2 | Last season goalies faced 28% of their shots and allowed 52% of their goals from that zone (28.5% and 51.7% in meaning) | W&W calc, NHL EDGE goalie detail for 97 goalies (`nhl_edge_goalie_detail_all98_20252026_hdsv.json`): 20,653 of 72,528 shots; 3,904 of 7,554 goals | SUPPORTED (computed) |
| 3 | Three versions (NHL, NST, MoneyPuck) draw the zone differently | NHL EDGE glossary; NST glossary; MoneyPuck glossary | SUPPORTED |
| 4 | Talbot's .744 was the lowest among regulars (30+ GP) | EDGE detail, 157/211; rank 51 of 51 | SUPPORTED (computed) |
| 5 | High danger began as a grade of scoring chance; War-on-Ice built the scale NST uses; NST quote "as originally defined by War-on-Ice" | NST team glossary (archived); Lukan, NHL.com, May 1, 2022 ("the model employed by NaturalStatTrick.com and developed by War-On-Ice.com") | SUPPORTED |
| 6 | Each offensive-zone attempt gets 1-3 by location, +1 for rebound or rush, −1 if blocked; 3 or more = high danger | NST team glossary (archived) | SUPPORTED |
| 7 | Rebound = attempt within three seconds of another blocked, missed or saved attempt with no stoppage; rush = within four seconds of an event in the neutral or defensive zone; first defined by David Johnson at Hockey Analysis, set to four seconds by War-on-Ice | NST team glossary (archived): "originally defined by David Johnson on the now-offline Hockey Analysis, and modified to 4 seconds by War-on-Ice" | SUPPORTED |
| 8 | NST's HDSV% = share of high-danger shots on goal stopped | NST goalie glossary (archived): HD Shots Against = shots on goal that are HD chances; HDSV% = HD Saves / HD Shots Against | SUPPORTED |
| 9 | NHL publishes EDGE stats back to 2021-22 | NHL EDGE API `seasonsWithEdgeStats` begins 20212022 (`nhl_edge_goalie_landing_20252026_hdsv.json`) | SUPPORTED |
| 10 | NHL zone is pure geometry with no rebound or rush bonus | NHL EDGE glossary (location-only definition) | SUPPORTED |
| 11 | MoneyPuck calls an unblocked attempt high danger at a 20% or better chance | MoneyPuck glossary ("Unblocked Shot attempts with >= 20% probability of being a goal") | SUPPORTED |
| 12 | NHL numbers are shots on goal, so the result is a box-score save percentage | NHL EDGE glossary | SUPPORTED |
| 13 | Worked example (246/300 = .820; 240 = .800; 252 = .840; one goal ≈ .003 on 300 shots vs < .001 on 1,500) | Arithmetic, labelled invented | SUPPORTED |
| 14 | Regulars spanned 120 points of HDSV% and about 50 of overall SV% | EDGE: .8642 − .7441 = .120; overall .9213 − .8696 = .052 | SUPPORTED (computed) |
| 15 | League stopped .811 of high-danger shots and .930 of everything else; HD shots went in nearly three times as often (18.9% vs 7.0%) | EDGE: 16,749/20,653 = .8110; (64,974 − 16,749)/(72,528 − 20,653) = .9296 | SUPPORTED (computed) |
| 16 | Median among 51 regulars .814; Sorokin led at .864 and his 452 HD saves led the league | EDGE detail (median .8142); EDGE goalie landing leaders (highDangerSavePctg Sorokin .864245, highDangerSaves Sorokin 452) | SUPPORTED |
| 17 | Bottom four: Saros, Binnington, Bobrovsky, Talbot; only Talbot below .750; Gibson exactly the median | EDGE detail, 30+ GP (.775, .765, .758, .744; Gibson .8142 = 26th of 51) | SUPPORTED (computed) |
| 18 | Detroit's goalies faced 26.7% of shots from the zone vs league 28.5%; both in the lighter half of the league in HD share (39th and 42nd of 51) | EDGE detail (604/2,258; Gibson 26.9%, Talbot 26.5%; median 28.5%) | SUPPORTED (computed) |
| 19 | Talbot stopped a smaller share than anyone else with 30 games | Row 4 | SUPPORTED (computed) |
| 20 | 47 goalies with 150+ HD shots in both seasons; year-to-year r 0.17, a little better than overall SV% for the same group (0.12) | W&W calc, Pearson, EDGE detail 2025-26 + `nhl_edge_goalie_detail_20242025_for_2025-26_25gp_goalies_hdsv.json` | SUPPORTED (computed) |
| 21 | Talbot was .788 the season before | EDGE detail 2024-25 (260/330) | SUPPORTED (computed) |
| 22 | Talbot's overall SV% .883; 54 goals on 211 HD shots, about 14 more than average; about two goals better than average on the other 586 | NHL API (.8833); EDGE: 211 × .189 = 39.9 expected vs 54; 547 − 586 × .9296 = +2.2 | SUPPORTED (computed) |
| 23 | Sorokin's 34.2% HD share was the second-heaviest among regulars, behind Andersen | EDGE detail (Andersen 34.7%, Sorokin 34.2%) | SUPPORTED (computed) |
| 24 | A regular faces about 300 HD shots (median 316); a league-average goalie lands between .767 and .855 in 19 seasons of 20; that band holds 47 of 51 regulars | Binomial 95% interval around .811 on 300 shots (SD .0226); EDGE detail | SUPPORTED (computed) |
| 25 | Talbot .633 on MoneyPuck's cut, 79 qualifying attempts | `mp_goalies_2025.csv` (highDangerShots 79, highDangerGoals 29) | SUPPORTED (computed) |
| 26 | NST's scale adds rebounds and rush shots the NHL's map ignores | Rows 6, 10 | SUPPORTED |
| 27 | Neither the NHL zone nor NST's scale knows whether the goalie was screened | Both definitions list no screen input | SUPPORTED (by omission) |
| 28 | Every version but MoneyPuck's counts only shots on goal | NHL EDGE glossary; NST goalie glossary; MoneyPuck glossary (unblocked attempts) | SUPPORTED |

## Voice metrics (`style_metrics.py --target barnwell_lean`, running prose, 1,058 words)

| Metric | Value | Target |
|---|---|---|
| Sentence mean / SD | 19.6 / 11.9 | 17-21 / ≥ 10 |
| Short / long sentences | 7% / 20% | 6-15% / ≤ 20% |
| Words per paragraph | 59 | 55-85 |
| One-sentence paragraphs | 6% | 5-12% |
| Contractions per 1k | 38.8 | ≥ 28 |
| I / you per 1k | 0.0 / 3.8 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.9 / 4.7 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 49.1 | 30-55 |

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, unicode artifacts, question fragments or false ranges. Remaining hints `uniform_paragraph_structure` and `repeated_ngrams` come from the template and metric names.

Proposed hover short: Save percentage on high-danger shots only, the shots on goal from right in front of the net. It isolates the saves that swing games, though the samples get small fast.

(Current short says "the attempts from right in front of the net"; the NHL and NST versions count shots on goal only, so "attempts" misdescribes them.)
