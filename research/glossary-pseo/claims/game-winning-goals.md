# Claims register: game-winning-goals.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/` files downloaded 2026-10-09:
`nhl_skater_summary_20252026_scoringbasics.json`, `nhl_skater_summary_20242025_scoringbasics.json`,
`nhl_team_summary_20252026_scoringbasics.json`, `nhl_standings_20260417_final_scoringbasics.json`,
`nhl_skater_career_gwg_thru20252026_scoringbasics.json`, `nhl_det_franchise_career_gameWinningGoals_thru20252026_scoringbasics.json`.
Rule text: `nhl_rulebook_2025-26_excerpts_rules6_33_78_84_scoringbasics.txt`. Glossary text:
`nhl_stats_glossary_api_20261009_scoringbasics.json`. Hockey-Reference GWG leader pages read 2026-10-09.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | GWG = the goal that put the winner one ahead of the loser's final total; third goal of a 5-2 win; can come in the first period | NHL glossary GWG ("regardless of when it occurs in a game or what the score is at the time") | SUPPORTED |
| 2 | Every regulation or overtime win produces exactly one; 2025-26 GWG matched non-shootout wins one for one | W&W calc: GWG sum 1,193 = 1,312 wins − 119 shootout wins | SUPPORTED (computed) |
| 3 | Clutch reputation doesn't hold up season to season | Row 16 | SUPPORTED (computed) |
| 4 | NHL glossary quote | NHL glossary GWG | SUPPORTED |
| 5 | In a 7-1 win the GWG is the second goal | Definition (row 1) | SUPPORTED |
| 6 | League database carries GWG back to its first season | NHL glossary GWG firstSeasonForStat 19171918 | SUPPORTED |
| 7 | Esposito (twice) and Goulet share the single-season record of 16 | Hockey-Reference single-season GWG leaders (1970-71, 1971-72, 1983-84) | SUPPORTED |
| 8 | Ovechkin 141 through 2025-26 most in a career; Jagr 135; Howe 121, all for Detroit; Yzerman second on franchise list (94) | NHL stats API career aggregate through 2025-26; franchise aggregate (Howe 121 with DET = career 121; Yzerman 94); Hockey-Reference career list (same counts) | SUPPORTED |
| 9 | Rule 84.4: shootout winner gets one extra goal; quote "will not be credited with a goal scored in his personal statistics" | Rule 84.4 | SUPPORTED |
| 10 | 1,312 wins, 119 shootouts, 1,193 game-winners | NHL team summary and standings; skater summary GWG sum | SUPPORTED (computed) |
| 11 | Worked example (empty-netter in a 3-2 win is the GWG) | Invented game, labelled; logic per row 1 | SUPPORTED (illustrative) |
| 12 | Overtime goals are always game-winners; 207 of 1,193 (about 17%) | Rule 84.1 (first goal wins); skater summary OTG sum 207 = OT wins 207 | SUPPORTED (computed) |
| 13 | 14.8% of goals were game-winners | W&W calc: 1,193 ÷ 8,086 | SUPPORTED (computed) |
| 14 | 327 regular forwards: median 2, top tenth 5+, 42 with none | W&W calc, 60+ GP (33rd-highest = 5) | SUPPORTED (computed) |
| 15 | Caufield led with 12, Stamkos 10, Larkin tied for third with nine (Robertson, Nelson, Schmaltz) | NHL skater summary 2025-26 | SUPPORTED |
| 16 | Larkin 9 of 34 (26%); 3 of 30 in 2024-25 (10%); DeBrincat 6 of 41; Kane 4 of 16 | NHL skater summaries | SUPPORTED |
| 17 | GWG share YoY r = −0.02 for 197 regular forwards with 10+ goals both seasons; GWG/GP r = 0.39 | W&W calc, skater summaries 2024-25 and 2025-26 (60+ GP both; GWG/GP on 260 forwards) | SUPPORTED (computed) |
| 18 | Detroit had 39 wins outside the shootout; Larkin, DeBrincat, Raymond combined 20 (just over half); nobody else above Kane's four | NHL standings (regulationPlusOtWins 39); skater summary | SUPPORTED (computed) |
| 19 | Four of Larkin's nine came in overtime; regulation share five of 30 (17%); league regulation share 12.5% | Skater summary (OTG 4); W&W calc (1,193 − 207) ÷ (8,086 − 207) | SUPPORTED (computed) |
| 20 | Caufield scored five of his 12 in overtime | Skater summary (OTG 5) | SUPPORTED |
| 21 | Goalie has to keep the opponent from tying for an earlier goal to stay the GWG | Definition (row 1), logic | SUPPORTED |
| 22 | Detroit won two shootouts in 2025-26 and nobody got a GWG; the shot still earned two points | Standings (shootoutWins 2); Rule 84.4; Rule 78.1 | SUPPORTED |
| 23 | Facts: 1 per win; 14.8%; median forward 2; Caufield 12; Larkin 9 tied third; record 16; −0.02 | Rows 2, 7, 13-15, 17 | SUPPORTED |

Cut for lack of verification: how many 2025-26 game-winners were empty-netters or first-period goals (needs
play-by-play); any claim about when the NHL first began publishing GWG as a column.

## Voice metrics (running prose, `--target barnwell_lean`, 1,080 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.3 / 10.1 | 17-21 / ≥ 10 |
| Short / long sentences | 11% / 16% | 6-15% / ≤ 20% |
| Words per paragraph | 57 | 55-85 |
| One-sentence paragraphs | 11% | 5-12% |
| Contractions per 1k | 52.8 | ≥ 28 |
| I / you per 1k | 0 / 3.7 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.9 / 3.7 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 2% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 45.4 | 30-55 |

ai-content-detection: no contrast frames, payoff colons or unicode artifacts. Remaining hints
(`uniform_paragraph_structure`, `repeated_ngrams`) come from the template and the stat name ("game-winner").
