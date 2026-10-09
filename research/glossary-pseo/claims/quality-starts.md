# Claims register: quality-starts.json

Reviewed 2026-10-09. All NHL API files downloaded 2026-10-09 to `research/glossary-pseo/raw/`. "W&W calc" = computed by the writer from the named file.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | QS: start SV% beats season league SV%, or ≥ .885 on ≤ 20 shots; RBS < .850 | raw/hr_goalies_2025-26_downloaded_2026-10-09.html QS and RBS column tips ('Developed by Rob Vollman in the Hockey Abstract') | SUPPORTED |
| 2 | Vollman built it at Hockey Prospectus around 2009, rule laid out in his Hockey Abstract books | The Leafs Nation 2016-10-27 ('created back in 2009 at the Hockey Prospectus web site'); DobberHockey 2014-12-13 ('around since 2009'); Hockey-Reference credit | SUPPORTED |
| 3 | Idea: credit only when he played well enough for an average team to win | DobberHockey 2014-12-13 ('only be earned when he plays well enough for an average team to win') | SUPPORTED |
| 4 | 2013 Hockey Abstract: league-average share (about 91.7% then; 91.3% before 2009-10) or replacement level 88.5% with ≤ 2 GA | Vollman quoted in The Leafs Nation 2016-10-27 | SUPPORTED |
| 5 | DobberHockey 2014: from year-end annuals like Hockey Prospectus to live on Hockey-Reference | DobberHockey 2014-12-13 | SUPPORTED |
| 6 | NHL keeps its own QS column: 1,286 in 2025-26 vs 1,421 under Vollman's rule; NHL glossary has no QS entry | raw/nhl_goalie_advanced_20252026.json qualityStart; NHL stats glossary (api.nhle.com/stats/rest/en/glossary, saved raw/nhl_stats_glossary_2026-10-09.json) (no QS entry) | SUPPORTED (computed) |
| 7 | NHL count matches, for all 98 goalies, a flat bar better than .900 with no small-shot clause | W&W calc, raw/nhl_goalie_games_20252026.json vs raw/nhl_goalie_advanced_20252026.json: cutoffs .880-.934 tested, 98/98 match for any cutoff in (.900, .902] | SUPPORTED (computed) |
| 8 | Bar = full-season league SV% (.896 in 2025-26) | W&W calc, raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 9 | Worked example (invented, .900 average): 28/30 QS, 25/28 not, 2 GA on 18 (.889: under .900, over .885, so QS via the small-shot rule), 5 GA on 27 (.815) RBS | Arithmetic | SUPPORTED (computed) |
| 10 | 424 starts on ≤ 20 shots; 38 QS via the .885 clause only | W&W calc, raw/nhl_goalie_games_20252026.json | SUPPORTED (computed) |
| 11 | Rule on NHL game logs reproduces Hockey-Reference's 2025-26 totals (1,421 QS, 594 RBS over 2,624 starts) and per-goalie counts | W&W calc, raw/nhl_goalie_games_20252026.json vs raw/hr_goalies_2025-26_downloaded_2026-10-09.html (all 98 goalies match after name normalization) | SUPPORTED (computed) |
| 12 | 54.2% of starts qualified; Hockey-Reference: > 60% good, < 50% bad, ~53% league average | W&W calc; raw/hr_goalies_2025-26_downloaded_2026-10-09.html QS% tooltip | SUPPORTED |
| 13 | League SV% lowest in decades (since 1993-94) | W&W calc, raw/nhl_league_goalie_totals_by_season_1983-2026.json | SUPPORTED (computed) |
| 14 | 41 goalies with 30+ starts: median 57.1%; Wedgewood 74.4% best; Wallstedt, Vladar, Vasilevskiy > 72%; Andersen 31.4% worst; Markstrom and Lankinen next | W&W calc, raw/nhl_goalie_games_20252026.json | SUPPORTED (computed) |
| 15 | Gibson 29 QS in 57, bottom quarter (32nd of 41), 10 RBS; Talbot 48.0%, 8 of 25 starts under .850 | W&W calc, raw/nhl_goalie_games_20252026.json | SUPPORTED (computed) |
| 16 | QS% vs SV% correlation 0.89, 53 goalies with 25+ starts | W&W calc, raw/nhl_goalie_games_20252026.json | SUPPORTED (computed) |
| 17 | Vladar and Sorokin a hair over .905 in starts; Vladar 37 QS in 51, Sorokin 28 in 54; Sorokin led with 7 shutouts | W&W calc, raw/nhl_goalie_games_20252026.json; raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 18 | Binnington 18 RBS in 39 starts; league RBS 22.6% (between a fifth and a quarter) | W&W calc, raw/nhl_goalie_games_20252026.json (matches raw/hr_goalies_2025-26_downloaded_2026-10-09.html) | SUPPORTED (computed) |
| 19 | Bussi 56.4% and Hellebuyck 56.1% QS; 31 vs 23 wins | W&W calc, raw/nhl_goalie_games_20252026.json; raw/nhl_goalie_summary_20252026.json | SUPPORTED (computed) |
| 20 | YoY QS% correlation 0.05, SV% 0.07 (same starts), 39 goalies with 25+ starts both seasons; Leafs Nation 2016: QS not a repeatable skill | W&W calc, raw/nhl_goalie_games_20242025.json + raw/nhl_goalie_games_20252026.json; The Leafs Nation 2016-10-27 | SUPPORTED (computed) |
| 21 | HR and NHL QS disagree for most goalies; gap can run several starts (Vasilevskiy 42 vs 35) | W&W calc, raw/hr_goalies_2025-26_downloaded_2026-10-09.html vs raw/nhl_goalie_advanced_20252026.json | SUPPORTED (computed) |

## Voice metrics (`extract_prose.py quality-starts` + `style_metrics.py --target barnwell_lean`)

| Metric | Page | Target |
|---|---|---|
| Words (running prose) | 1186 | |
| sent_mean | 18.8 | 17-21 |
| sent_sd | 10.1 | >=10 |
| pct_short_le6 | 11 | 6-15 |
| pct_long_ge30 | 14 | <=20 |
| para_words | 62 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 34.6 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 5.9 | 3-8 |
| q_per_k | 1.7 | 1-5 |
| paren_per_k | 5.1 | 3-8 |
| intens_per_k | 0.8 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 54.8 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

Every metric is inside the target. ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, negation pivots or unicode artifacts; remaining hints are `uniform_paragraph_structure` and `repeated_ngrams` (fixed template + metric names).

Live slot omitted: the pipeline doesn't carry per-game goalie logs, quality starts or RBS yet. 
Proposed hover short: none (the current `short` in glossary-terms.json agrees with the page).
