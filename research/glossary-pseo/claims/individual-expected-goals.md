# Claims register: individual-expected-goals.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/mp_skaters_2025.csv` (MoneyPuck season
"2025" = 2025-26) and `mp_skaters_2024-25_ixg_gax_yoy_dl2026-10-09.csv` (2024-25; byte-identical to
`mp_skaters_2024.csv`), both downloaded 2026-10-09, all situations unless marked 5on5. Figures shared with the xG
page (McDavid 43.6, median forward 17.3, top 10% 29.7, DeBrincat 36.9 fifth, Larkin 18th, Copp 9 on 19.8) were
recomputed from the same file and match.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | ixG = sum of expected goals on every unblocked shot a player takes himself | Evolving-Hockey Standard Skater Tables ("Total individual expected goals (total xG of all iFF shots)"); MoneyPuck glossary (xG on unblocked attempts) | SUPPORTED |
| 2 | ixG is the half of scoring that holds up best year to year (r 0.77 vs goals 0.73, GAx 0.38) | W&W calc, 260 forwards with 60+ GP in both seasons | SUPPORTED (computed) |
| 3 | McDavid 43.6 led; ≈ 2.5× the median forward (17.3); MacKinnon (40.6) and Kaprizov (38.4) next; DeBrincat fifth (36.9) | W&W calc, 327 forwards 60+ GP | SUPPORTED (computed) |
| 4 | Copp 19.8 ixG, 9 goals, fifth-largest shortfall among 940 skaters | W&W calc (rank 936 of 940 on goals − ixG) | SUPPORTED (computed) |
| 5 | Sprigings and Toumi, Hockey-Graphs, October 2015, tested individual players: ixG/60 outperformed iCF and Sh% at estimating future individual scoring | Hockey-Graphs 2015-10-01 ("individual xG per 60 minutes (ixG/60) outperforms iCF% and Sh% across the board"); HockeyStats Medium names the authors | SUPPORTED |
| 6 | Evolving-Hockey lists iCF, iFF, iSF and defines ixG as total xG of iFF shots | Evolving-Hockey Standard Skater Tables | SUPPORTED |
| 7 | MoneyPuck's data files carry it as I_F_xGoals | Header of MoneyPuck skaters file | SUPPORTED |
| 8 | EH trains its own model, so totals differ by site | Evolving-Hockey xG model write-up; xG page register row 29 | SUPPORTED |
| 9 | MoneyPuck inputs: distance and angle, shot type, last event (what/where/seconds), skaters per side and empty net, off wing | MoneyPuck about page; xG page register row 15 | SUPPORTED |
| 10 | Worked example (invented): 200 × 0.09 = 18.0; 22 goals = +4, 14 = −4 | arithmetic | SUPPORTED |
| 11 | Blocked attempts excluded because the NHL logs a block where it happened | Evolving-Hockey write-up + glossary; xG page register row 17 | SUPPORTED |
| 12 | Site totals are all situations unless a column says otherwise; power-play time pads them | `src/data/glossary-terms.json` all-situations short; MoneyPuck teams file (5v4 xGF/60 7.37 vs 5v5 2.47 league) | SUPPORTED (computed) |
| 13 | Top 10% of 327 forwards ≥ 29.7 | W&W calc | SUPPORTED (computed) |
| 14 | Defensemen: median xG per unblocked attempt 0.039 vs forwards 0.087 (150+ attempts); median D with 60 GP 5.1 ixG; Chychrun led D at 18.8 | W&W calc (78 D and 238 F with 150+ attempts; 161 D with 60+ GP) | SUPPORTED (computed) |
| 15 | DeBrincat only Red Wing in the top 15; Larkin 18th; Copp 19.8, Raymond 19.5, van Riemsdyk 19.2, Finnie 19.2 | W&W calc | SUPPORTED (computed) |
| 16 | Every other Red Wing at or below the forward median (Kane 16.5, Kasper 15.4, Compher 12.1, defensemen lower) | W&W calc | SUPPORTED (computed) |
| 17 | Per 60 (all situations): ixG r 0.76 vs goals 0.62 | W&W calc, same 260 forwards | SUPPORTED (computed) |
| 18 | Copp's ixG went up: 12.3 in 2024-25 (56 GP) to 19.8 | Both skater files | SUPPORTED (computed) |
| 19 | DeBrincat 443 unblocked attempts at 0.083 each, below the 0.087 median (238 forwards, 150+ attempts); Hyman 35.2 ixG on 245 at 0.144, highest among them | W&W calc | SUPPORTED (computed) |
| 20 | Hyman 31 goals, DeBrincat 41 | Skaters file I_F_goals | SUPPORTED |
| 21 | 5v5 ixG/60: median 0.70 (385 forwards, 500+ min); DeBrincat 0.88, 53rd; Kasper 0.81 above Larkin 0.66 | W&W calc, 5on5 rows | SUPPORTED (computed) |
| 22 | Kasper's goals fell from 19 (2024-25) to 9 | Both skater files | SUPPORTED |
| 23 | MoneyPuck's base model doesn't factor in shooting skill | MoneyPuck glossary ("A player's shooting talent is not factored into this metric") | SUPPORTED |
| 24 | Play-by-play doesn't record passes; cross-crease feed priced like any shot from that spot; passer gets no ixG | Evolving-Hockey write-up; xG page register row 25; definition (row 1) | SUPPORTED |
| 25 | MoneyPuck flurry adjustment gives less credit for rebound chances than first shots | MoneyPuck glossary (Flurry Adjusted) | SUPPORTED |

Live slot: team `situations.all.xGoalsFor`, `situations.5on5.xGoalsFor`, dashboard tile `finishing`; leaderboard on
`ixG` with GP, goals, shots (NHL API) and ixG, 5v5 ixG/60, goals − ixG (MoneyPuck); `live.credit` = "NHL API and
MoneyPuck". Wanted: skater `iFF` (unblocked attempts) so the table can show xG per attempt, and
`fiveOnFive.ixG` totals.

## Voice metrics (running prose, `--target barnwell_lean`, 1,083 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.3 / 10.2 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 16% | 6-15% / ≤ 20% |
| Words per paragraph | 57 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 32.3 | ≥ 28 |
| I / you per 1k | 0.0 / 6.5 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 4.6 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 53.6 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts, question fragments, sentence-negation
pivots or false ranges. Remaining hints (`uniform_paragraph_structure`, `repeated_ngrams`) come from the fixed
template and metric names. `gate_glossary.py individual-expected-goals`: PASS. JSON parses.
Hardest metric: numbers per 1k (first draft 65.6) together with words per paragraph and one-sentence paragraphs (first draft 21%, from one-sentence limits); limits went to two sentences and benchmarks moved into words.

Hover short: the current `short` agrees with the page. No change proposed.
