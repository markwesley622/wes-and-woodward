# Claims register: points.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`nhl_skater_summary_20252026_scoringbasics.json`, `nhl_skater_summary_20242025_scoringbasics.json`,
`nhl_standings_20260417_final_scoringbasics.json`, `nhl_skater_season_top_points_thru20252026_scoringbasics.json`,
`nhl_skater_career_points_thru20252026_scoringbasics.json`, `nhl_det_franchise_career_points_thru20252026_scoringbasics.json`,
`nhl_det_franchise_season_points_thru20252026_scoringbasics.json`, `nhl_howe_points_titles_check_scoringbasics.txt`,
`mp_skaters_2025.csv` (MoneyPuck season "2025" = 2025-26). Rule text: `nhl_rulebook_2025-26_excerpts_rules6_33_78_84_scoringbasics.txt`.
Glossary text: `nhl_stats_glossary_api_20261009_scoringbasics.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Points are goals plus assists, each worth one point | Rules 78.2, 78.3; NHL glossary P | SUPPORTED |
| 2 | Standard way to rank skaters; counts a secondary assist the same as a goal | Rule 78.3 (each assist one point); Art Ross is decided on points (row 6) | SUPPORTED |
| 3 | Art Ross Trophy goes to the regular season's points leader | NHL.com (Condor, Jan. 16, 2020) | SUPPORTED |
| 4 | PTS and P both used; standings points are another stat | NHL glossary P and P (Standings) | SUPPORTED |
| 5 | Rule 78.2 quote "shall count one point in the player's record"; 78.3 same for assists; one point per player per goal; scorer never gets an assist on his own goal | Rules 78.2, 78.3; NHL glossary P | SUPPORTED |
| 6 | Art Ross, former Bruins coach and GM, presented it in 1947; Elmer Lach won the first; no vote; tiebreakers more goals, then fewer games | NHL.com (Condor) | SUPPORTED |
| 7 | Gretzky won it a record 10 times; Howe six, all as a Red Wing | NHL.com (Condor) for counts; NHL stats API season-by-season check (Howe led in 1950-51, 51-52, 52-53, 53-54, 56-57, 62-63, all DET) | SUPPORTED |
| 8 | Howe's 1,809 points are the franchise career high; Yzerman second; Yzerman's 155-point season is the franchise best | NHL stats API franchise aggregates (Howe 1,809, Yzerman 1,755; Yzerman 155 in 1988-89) | SUPPORTED |
| 9 | NHL.com, Hockey-Reference, MoneyPuck publish points from official scoring; MoneyPuck's 2025-26 file six short | W&W calc: MoneyPuck I_F_points 21,735 vs NHL 21,741; Hockey-Reference data credits | SUPPORTED (computed) |
| 10 | PTS = EVP + PPP + SHP | NHL skater summary: 16,697 + 4,640 + 404 = 21,741 | SUPPORTED (computed) |
| 11 | Worked example (25 G, 20 A1, 15 A2, 60 points) | Invented round numbers, labelled | SUPPORTED (illustrative) |
| 12 | Two standings points for any win, one for a loss after regulation; Rule 84.1 awards the point when regulation ends tied | Rules 78.1, 84.1 | SUPPORTED |
| 13 | Detroit finished 2025-26 with 92 standings points, 16th | NHL final standings (points 92, leagueSequence 16) | SUPPORTED |
| 14 | PPP were 21% of all skater points in 2025-26 | W&W calc: 4,640 ÷ 21,741 | SUPPORTED (computed) |
| 15 | YoY (260 forwards): P/GP r = 0.88, G/GP 0.74 | W&W calc, NHL skater summaries 2024-25 and 2025-26 | SUPPORTED (computed) |
| 16 | Total holds up better than either half | Row 15 plus assists rows (A1/GP 0.80, A2/GP 0.73) | SUPPORTED (computed) |
| 17 | Skaters turned goals into 2.69 points apiece | W&W calc: 21,741 ÷ 8,086 | SUPPORTED (computed) |
| 18 | Regulars: median forward 37, top tenth 74+, median defenseman 25 | W&W calc, NHL skater summary, 60+ GP (33rd-highest F = 74) | SUPPORTED (computed) |
| 19 | McDavid led with 138 | NHL skater summary 2025-26 | SUPPORTED |
| 20 | DeBrincat 85, tied for 19th; Raymond 76; Larkin 67; Seider 60, tied for 11th among defensemen | NHL skater summary (18 players above 85; 10 defensemen above 60) | SUPPORTED |
| 21 | Only 20 of 161 regular defensemen reached 50; a third of regular forwards did | W&W calc (20/161; 109/327) | SUPPORTED (computed) |
| 22 | Points decide the Art Ross without a vote | Row 6 | SUPPORTED |
| 23 | About one point in five came on the power play; DeBrincat 62 of 85 at even strength; Raymond and Larkin about a third on the PP; Seider 28 of 60 | NHL skater summary (PPP 27/76, 24/67) | SUPPORTED (computed) |
| 24 | At even strength DeBrincat's lead grows from 9 to 13; Seider falls behind Kane | NHL skater summary EVP (DeBrincat 62, Raymond 49; Kane 38, Seider 32) | SUPPORTED (computed) |
| 25 | Seider 25.7 minutes a night, DeBrincat 18.5; 1.71 vs 3.36 points per hour of ice time; nearly twice | W&W calc: points ÷ (GP × timeOnIcePerGame ÷ 3600) | SUPPORTED (computed) |
| 26 | Median regular forward 1.96 points per hour, defenseman 0.99 | W&W calc, same method, 60+ GP | SUPPORTED (computed) |
| 27 | Game Score values a goal at 0.75 and a secondary assist at 0.55; built by Dom Luszczyszyn at Hockey-Graphs | Hockey-Graphs 2016 and 2018 (assists register row 12) | SUPPORTED |
| 28 | NHL.com's glossary says dividing points by games doesn't account for ice time or special-teams time | NHL glossary P/GP | SUPPORTED |
| 29 | FAQ: Gretzky 2,857, single-season record 215 (1985-86); Jagr second with 1,921 | NHL stats API career and season aggregates | SUPPORTED |
| 30 | Facts: 2.69 per goal; median forward 37; McDavid 138; DeBrincat 85 tied 19th; Gretzky 215 | Rows 17-20, 29 | SUPPORTED |

Cut for lack of verification: "the oldest way to rank skaters" (current hover short); the Art Ross's third
tiebreaker (NHL.com's wording is garbled); any claim about "the point" as a position name.

## Voice metrics (running prose, `--target barnwell_lean`, 1,110 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 18.2 / 10.5 | 17-21 / ≥ 10 |
| Short / long sentences | 7% / 13% | 6-15% / ≤ 20% |
| Words per paragraph | 56 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 31.5 | ≥ 28 |
| I / you per 1k | 0 / 3.6 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 3.6 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 2% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 49.5 | 30-55 |

ai-content-detection: no contrast frames, payoff colons or unicode artifacts. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and stat names ("the power play").

Proposed hover short: Goals plus assists, each worth one point. It's the standard way to rank skaters, and it counts a secondary assist the same as a goal.

(The current short calls points "the oldest way to rank skaters," which no source here supports; goals have the
older record.)
