# Claims register: goals-above-expected.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/mp_skaters_2025.csv`, `mp_teams_2025.csv`
(MoneyPuck season "2025" = 2025-26) and `mp_skaters_2024-25_ixg_gax_yoy_dl2026-10-09.csv` (2024-25), all downloaded
2026-10-09. GAx = I_F_goals − I_F_xGoals, all situations. Caufield, Copp, DeBrincat and Detroit's team five-on-five
figures match the xG page's register (rows 20-21, 34).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | GAx = goals minus expected goals; positive = finishing beat an average shooter on the same chances; one season carries a lot of luck | MoneyPuck about (xG excludes shooting skill; "a lot of luck involved in whether a shot goes in"); definition | SUPPORTED |
| 2 | Caufield led at +17.3 (51 on 33.7); Copp −10.8 fifth-worst of 940 | W&W calc | SUPPORTED (computed) |
| 3 | Repeats weakly: r 0.38 year to year vs ixG 0.77 (260 forwards, 60+ GP both seasons) | W&W calc | SUPPORTED (computed) |
| 4 | Ryder's 2004 shot-quality paper set out to separate shot quality allowed from goaltending | Ryder, Shot Quality (2004), introduction | SUPPORTED |
| 5 | MoneyPuck and this site grade goalies with GSAx (expected goals faced minus goals allowed) | MoneyPuck glossary (Goals Saved Above Expected); `data/site/dashboard.json` gsax tile; xG page register row 24 | SUPPORTED |
| 6 | Sprigings and Toumi (Hockey-Graphs, 2015) folded shooter talent in with regressed shooting percentage, adding 375 shots for forwards and 275 for defensemen | Hockey-Graphs 2015-10-01 (Shot Multiplier steps) | SUPPORTED |
| 7 | MoneyPuck's base model is talent-free; it publishes shooting talent above average ("ability to score more goals than an average player given the same scoring opportunities") | MoneyPuck about + glossary | SUPPORTED |
| 8 | Evolving-Hockey: FSh% = G ÷ iFF, xFSh% = ixG ÷ iFF | Evolving-Hockey Standard Skater Tables | SUPPORTED |
| 9 | Team page calls the team version finishing and rebuilds it nightly | `data/site/dashboard.json` tile `finishing` ("Finishing, goals above expected"); nightly refresh per TEMPLATE.md | SUPPORTED |
| 10 | Worked example (invented): 20 on 15.0 = +5.0; 20/150 = 13.3% vs 15/150 = 10.0% | arithmetic | SUPPORTED |
| 11 | League skaters: 8,084 goals on 8,213 ixG, 129 under (≈ 1.6%) | W&W calc, sum over 940 skaters | SUPPORTED (computed) |
| 12 | 327 forwards 60+ GP: median −0.8, SD 4.9, three in four within ±5 (74.6%) | W&W calc | SUPPORTED (computed) |
| 13 | Geekie +16.5, Mantha +14.7; Lee last at −13.6 (19 on 32.6) behind DeBrusk (−11.9) and Hertl (−11.6); each 32+ xG and 24 or fewer goals | W&W calc | SUPPORTED (computed) |
| 14 | Faulk +8.2 (16 on 7.8), 23rd of 940; Raymond +5.5; DeBrincat +4.1; Kasper −6.4, Finnie −6.2, Copp all in the 30 worst | W&W calc (ranks 5, 25, 30 from the bottom) | SUPPORTED (computed) |
| 15 | Faulk's shots priced at 0.038 xG each; in 2024-25 (St. Louis) 4 goals on 6.0 xG | W&W calc, both skater files | SUPPORTED (computed) |
| 16 | MoneyPuck: a player's goals over a season can run above or below his true shooting talent | MoneyPuck about, shooting talent section | SUPPORTED |
| 17 | Caufield +7.8 in 2024-25 (37 on 29.2); Copp −2.3 (10 on 12.3) | 2024-25 skater file | SUPPORTED (computed) |
| 18 | Detroit 5v5 2025-26: 142 goals on 161.1 xG, 19.1 short; only NJD, NYI, VAN worse | W&W calc, MoneyPuck teams file 5on5 | SUPPORTED (computed) |
| 19 | Pre-shot passes and screens aren't in the public feature lists, so the goals that follow look like finishing | xG page register rows 25, 28 (EH write-up, MoneyPuck about, HockeyStats) | SUPPORTED |
| 20 | Models disagree by site | Each site's methodology page; xG page register row 29 | SUPPORTED |

Live slot: dashboard tile `finishing`, team `situations.all.goalsFor` and `situations.all.xGoalsFor`; leaderboard on
`goalsAboveExpected` with GP, goals, shots, Sh% (NHL API) and ixG, GAx (MoneyPuck); `live.credit` = "NHL API and
MoneyPuck". The pipeline's `goalsAboveExpected` is NHL goals minus MoneyPuck ixG (`pipeline/build_site_data.py`).
Wanted: skater `iFF` for a per-shot column, and a
five-on-five GAx.

## Voice metrics (running prose, `--target barnwell_lean`, 1,106 words)

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 19.8 / 10.7 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 16% | 6-15% / ≤ 20% |
| Words per paragraph | 55 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 39.8 | ≥ 28 |
| I / you per 1k | 0.0 / 6.3 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 5.4 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 54.2 | 30-55 |

ai-content-detection: no contrast frames, payoff colons, unicode artifacts, question fragments, sentence-negation
pivots or false ranges. Remaining hints (`uniform_paragraph_structure`, `repeated_ngrams`) come from the fixed
template and metric names. `gate_glossary.py goals-above-expected`: PASS. JSON parses.
Hardest metric: words per paragraph and one-sentence paragraphs pulled against numbers per 1k (first draft 61.6); fixed by removing repeated player figures (Caufield and Copp appeared three times) and expanding the extremes paragraph in words.

Hover short: the current `short` agrees with the page. No change proposed.
