# Claims register: shooting-percentage.json

Raw files (all downloaded 2026-10-09, in `research/glossary-pseo/raw/`): `nhl_skater_summary_20252026_sogfamily.json`,
`nhl_skater_summary_20242025_sogfamily.json`, `nhl_skater_summary_career_through20252026_DET2526_sogfamily.json`,
`nhl_team_summary_20052006_to_20252026_sogfamily.json`, `mp_teams_2025.csv` (MoneyPuck 2025-26 teams),
`nhl_stats_glossary_api_20261009.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | SH% = goals ÷ shots on goal; missed and blocked shots not part of it; NHL tables write S% | NHL stats glossary S% ("goals divided by shots ... does not take missed shots or blocked shots into consideration") | SUPPORTED |
| 2 | Swings a lot year to year; a shooter far above his career rate usually drifts back | W&W year-to-year test (row 11-12); SI 2016 mean-reversion column | SUPPORTED |
| 3 | NHL began tracking S% in 1959-60, the same season it began counting skater shots | NHL glossary S% ("1959-60") and S ("for skaters since 1959-60") | SUPPORTED |
| 4 | League shot about 9% for most of the 2010s (8.9% to 9.2%, 2009-10 through 2017-18); rose every season since 2017-18 to 11.1% in 2025-26, highest in team data back to 2005-06 | W&W calc, NHL team summary 2005-06 to 2025-26 (team goals ÷ shots per game × GP): 9.12, 8.99, 8.94, 9.11, 8.89, 8.90, 8.98, 9.02, 9.17, then 9.48, 9.49, 9.67, 9.82, 10.06, 10.17, 10.65, 11.07; 2005-06 was 10.09 | SUPPORTED (computed) |
| 5 | Grantland 2014 put the league average at "right about 9 percent" | Sean McIndoe, "Your Guide to NHL On-Ice Percentages," Grantland, March 20, 2014 | SUPPORTED |
| 6 | Hockey-Reference ranks players on S% once they've taken one shot per scheduled game | Hockey-Reference NHL Leaderboard Stat Requirements | SUPPORTED |
| 7 | Empty-net goals count toward a player's totals | NHL glossary ENG ("Empty net goals are counted towards a player's overall totals") | SUPPORTED |
| 8 | Worked example 20/200 = 10%, 22/200 = 11% | Arithmetic, labelled invented | SUPPORTED (invented, labelled) |
| 9 | Median regular forward took about 130 shots; one point of SH% on 130 shots is 1.3 goals | Median 131 among 327 forwards with 60+ GP, NHL skater summary 2025-26 | SUPPORTED (computed) |
| 10 | 2025-26: skaters 11.1% (8,086 / 73,022); forwards 13.0%, defensemen 6.1% pooled; 234 forwards with 100+ shots, median 13.4%, 90th percentile 18.4%; Robert Thomas led at 24.5% (25/102) | W&W calc, NHL skater summary 2025-26 | SUPPORTED (computed) |
| 11 | Teams: Dallas 13.2% (1st), Calgary 9.0% (32nd), Detroit 10.3% (26th); at league rate Detroit's 2,315 shots → ~256 goals vs 239, ~17 short | W&W calc, MoneyPuck teams file, goals ÷ SOG, all situations | SUPPORTED (computed) |
| 12 | Detroit's expected-goals numbers flag the same shortfall; Detroit near the middle of the league in shot volume | expected-goals.json claim 20 (142 5v5 goals on 161.1 xGF); Detroit 11th in shots per game (NHL team summary) | SUPPORTED |
| 13 | 189 forwards with 100+ shots in both 2024-25 and 2025-26; top tenth (18) 19.9% → 16.4%, 17 of 18 dropped; bottom tenth 8.1% → 11.9%, 15 of 18 rose; group 13.6% → 13.8%; top kept 42%, bottom 35% of their distance from the group (both gave back more than half) | W&W calc, NHL skater summaries, rates pooled | SUPPORTED (computed) |
| 14 | Year-to-year correlation of SH% for those forwards 0.35 | W&W calc, Pearson r | SUPPORTED (computed) |
| 15 | SI 2016 column calls it mean reversion; 10% career shooter scoring 30 goals on 20% shooting shouldn't be expected to repeat | Sports Illustrated, Department of Hockey Analytics, November 2016 | SUPPORTED |
| 16 | MoneyPuck: a lot of luck in whether a shot goes in; some players are better shooters than others | MoneyPuck about page | SUPPORTED |
| 17 | Larkin 34 goals on 229 shots (14.8%); career 11.4% (276/2,415); at career rate ≈ 26 goals; gap ≈ 8 | NHL skater summary 2025-26 + career aggregate; 229 × 0.1143 = 26.2 | SUPPORTED (computed) |
| 18 | DeBrincat 14.3% on 14.2% career; Raymond 14.5% on 14.5% career | NHL skater summary + career aggregate (41/287, 294/2,064; 25/173, 123/846) | SUPPORTED (computed) |
| 19 | Kasper 19 on 145 (13.1%) then 9 on 131 (6.9%); 277 career shots | NHL skater summaries 2024-25, 2025-26, career aggregate | SUPPORTED |
| 20 | This site's finishing numbers use goals above expected | `data/site/dashboard.json` tile "Finishing, goals above expected" | SUPPORTED |
| 21 | Shot-location mixing; goals above expected prices each shot | MoneyPuck about (model inputs incl. location); goals above expected = goals − xG (MoneyPuck glossary) | SUPPORTED |
| 22 | Regular forward ≈ 34 shots in 20 games; one goal ≈ 3 points of SH% | 1.70 shots/GP median forward × 20 = 34; 1/34 = 2.9% | SUPPORTED (computed) |
| 23 | Corsi counts misses and blocks; xG prices the misses | NHL glossary SAT; Evolving-Hockey glossary (xG on unblocked/Fenwick shots), per expected-goals.json claim 18 | SUPPORTED |
| 24 | Team SH%: empty-net goals count, shootout goals don't | NHL glossary GF/GP ("includes empty net goals but not shootout game-deciding goals") | SUPPORTED |
| 25 | FAQ: Rule 84.4, shootout winner not credited with a goal in personal statistics; NHL keeps shootout goals and attempts in separate columns; shootout S% counts every attempt | NHL Official Rules 2025-26, Rule 84.4; NHL glossary SO G, SO S, S/O S% | SUPPORTED |
| 26 | Forward average 13.0% last season as the regression target for a young player | Row 10 (forwards pooled 13.0%); regression concept per rows 13-15 | SUPPORTED |

## Voice metrics (extract_prose.py → style_metrics.py --target barnwell_lean)

1,242 words. Sentence mean 18.8 / SD 10.4; short 8%; long 15%; words per paragraph 62; one-sentence paragraphs 10%;
contractions 33.0/1k; I 0; you 3.2/1k; questions 1.6/1k; parentheses 4.0/1k; intensifiers 0; transition openers 0%;
numbers 48.3/1k; hedges 0. All in range. Hardest: numbers per 1k (first draft 81) and sentence SD / words per
paragraph (first draft 8.6 and 54); fixed by moving counts into denominators-in-words and lengthening the limits.

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, balanced negation or unicode artifacts.
Hints `uniform_paragraph_structure` and `repeated_ngrams` only (template slots, metric names).

No hover-short change proposed; the current `short` agrees with the page.
