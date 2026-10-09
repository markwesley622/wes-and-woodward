# Claims register: goals-saved-above-average.json

Reviewed 2026-10-09. Raw files in `research/glossary-pseo/raw/`, all downloaded 2026-10-09.

Formula check (brief asked to verify it): GSAA = saves − shots against × league SV%, equivalently (SV% − league SV%) × SA, equivalently SA × (1 − league SV%) − GA when GA = SA − saves. Vollman on NHL.com (2017) gives the saves form; Natural Stat Trick's glossary prose gives the goals form ("the difference between the goalie's Goals Against and a Goals Against with the same Shots Against and the average SV%"). NST's and Evolving-Hockey's one-line shorthand ("Average SV% * Shots Against − Goals Against", "(League Sv% * SA) − GA") doesn't compute as written if read literally (it's missing the "1 −"), so the page uses the prose definitions, not the shorthand.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | GSAA = goals saved vs a league-average goalie facing the same number of shots on goal; saves minus SA × league SV%; treats every shot as equally dangerous | Rob Vollman, NHL.com, Aug 7, 2017 ("multiplying a goalie's shots faced by the League-average save percentage" and "subtracting that from a goalie's actual number of saves"); NST glossary prose (Internet Archive copy, Jan 9, 2025) | SUPPORTED |
| 2 | Gibson +8.2, Talbot −10.0 in 2025-26 | W&W calc, NHL stats API goalie summary (`nhl_goalie_summary_20252026_gsaa_xsv.json`): 1,317 − 1,461 × .89585; 704 − 797 × .89585. Matches save-percentage page | SUPPORTED (computed) |
| 3 | Vollman wrote the recipe for NHL.com in 2017 | NHL.com "Chicago Blackhawks key statistics," Rob Vollman, Aug 7, 2017 | SUPPORTED |
| 4 | Needs only shots and saves, so it reaches back decades further than location-based stats | Hockey-Reference GSAA tables begin 1955-56; location-based shot quality starts with Ryder's 2002-03 data (xG page row 7) | SUPPORTED |
| 5 | Hockey-Reference computes it back to 1955-56, first season in its GSAA tables | Hockey-Reference progressive leaders page (table begins 1955-56) | SUPPORTED |
| 6 | Single-season record Parent +73 in 1973-74; Esposito +65 same season second | Hockey-Reference single-season GSAA leaders (1. Parent 73, 1973-74; 2. Esposito 65, 1973-74) | SUPPORTED |
| 7 | GSAA rewards stopping more than the league and facing a lot of shots | Formula (rate gap × shots) | SUPPORTED |
| 8 | NST and EH publish GSAA; EH shows it beside GSAx in the same goalie table | NST goalie glossary; Evolving-Hockey Standard Goalie Tables (lists GSAA and GSAx) | SUPPORTED |
| 9 | NST takes the average within selected filters (e.g. five-on-five, a team's games) and runs it inside each danger band (HD, MD, LD GSAA) | NST goalie glossary ("average SV% (within the selected filters)"; HDGSAA, MDGSAA, LDGSAA); NST filter glossary (game state, team) | SUPPORTED |
| 10 | NHL goalies stopped 64,976 of 72,530 shots in 2025-26, .8958 | NHL stats API goalie summary, summed | SUPPORTED (computed) |
| 11 | League GSAA sums to zero | W&W calc (Σ saves − .89585 × Σ SA = 0.000) | SUPPORTED (computed) |
| 12 | Worked example (1,500 shots at .900 → 150 expected; 135 = +15; 165 = −15; a point of SV% = 1.5 goals) | Arithmetic, labelled invented | SUPPORTED |
| 13 | Wedgewood stopped .921 of 1,093 shots, +27.8 | NHL API (1,007/1,093 = .9213; 1,007 − 1,093 × .89585 = 27.8) | SUPPORTED (computed) |
| 14 | Team GSAA: Detroit's pair −1.8 | 8.18 − 9.98 | SUPPORTED (computed) |
| 15 | Median among 51 goalies with 30+ GP +2.5 | W&W calc (2.47) | SUPPORTED (computed) |
| 16 | Wedgewood led (+27.8), Thompson and Vasilevskiy next, Lankinen last (−26.2, VAN); Gibson 19th of 51, Talbot 40th | W&W calc, 30+ GP pool (Thompson +25.3, Vasilevskiy +24.5) | SUPPORTED (computed) |
| 17 | GSAA and GSAx correlated at 0.88 among the 51 regulars | W&W calc, Pearson, NHL API GSAA vs MoneyPuck GSAx (`mp_goalies_2025.csv`) | SUPPORTED (computed) |
| 18 | Average Talbot = 10 fewer goals = about three points at 3.3 goals per point; 92 → about 95; still four short of Ottawa's 99 for the East's last wild card | OLS points on goal differential, 32 teams, `nhl_standings_2026-04-17_final_20252026_ptspct_rw.json` (slope 0.305 points per goal = 3.28 goals per point; matches goal-differential page); OTT 99 = East WC2 (`nhl_playoff_bracket_2026_rw.json`) | SUPPORTED (computed) |
| 19 | 35 goalies with 30+ GP in both seasons; GSAA year-to-year r 0.25, about save percentage's (0.28) | W&W calc, Pearson, NHL API 2025-26 + `nhl_goalie_summary_20242025_gsaa_repeatability.json`; save-percentage page also reports 0.28 for 35 goalies | SUPPORTED (computed) |
| 20 | A starter faces something like 1,500 shots | NHL API (Gibson 1,461; Thompson 1,587) | SUPPORTED |
| 21 | League stopped .900 in 2024-25 and .896 in 2025-26 | NHL API goalie summaries (.9001, .8958) | SUPPORTED (computed) |
| 22 | GSAA re-centers each year, which is how Hockey-Reference ranks Parent's season next to modern ones | Hockey-Reference single-season leaders list spans eras | SUPPORTED |
| 23 | Trent Miner .933 for Colorado, 104 shots in four games, +3.8; Wedgewood's more than seven times that | NHL API (97/104 = .9327, GP 4, COL; 97 − 104 × .89585 = 3.8; 27.8/3.8 = 7.3) | SUPPORTED (computed) |
| 24 | Talbot stopped 157 of 211 high-danger shots, about 14 fewer than average; about two goals better than average on everything else, each zone against its own league rate | NHL EDGE goalie detail (`nhl_edge_goalie_detail_all98_20252026_hdsv.json`): league HD .8110, non-HD .9296; 157 − 211 × .8110 = −14.1; 547 − 586 × .9296 = +2.2 | SUPPORTED (computed) |
| 25 | NST publishes HDGSAA with medium- and low-danger versions | NST goalie glossary | SUPPORTED |
| 26 | Minnesota's goalies had the two gentlest shot mixes among 51 regulars; GSAA credits Wallstedt and Gustavsson 24 more goals than GSAx | MoneyPuck xFSv% ranks 1-2; GSAA 20.2 and 11.4 vs GSAx 6.2 and 1.4 (14.0 + 10.0) | SUPPORTED (computed) |
| 27 | Andersen (CAR) had the hardest mix; −18.6 GSAA vs −3.3 GSAx | MoneyPuck xFSv% rank 51 of 51; NHL API GSAA; MoneyPuck GSAx | SUPPORTED (computed) |
| 28 | League save percentage changes from season to season | Row 21 | SUPPORTED |
| 29 | Hockey-Reference lists Gibson +8.6, Talbot −9.7; its numbers match a league baseline of .8955 (GA ÷ SA) vs NHL saves ÷ SA .8958 | `hr_goalies_2025-26_downloaded_2026-10-09.html` (Gibson 8.6, Talbot −9.7, Thompson 25.8, Wedgewood 28.2, Lankinen −25.7); W&W reproduction with 1 − 7,578/72,530 = .89552 matches all five to the decimal | SUPPORTED (computed) |
| 30 | NST's average moves with filters | NST glossary | SUPPORTED |
| 31 | GSAA is a counting stat; dividing by shots returns SV% minus league rate | Algebra | SUPPORTED |

## Voice metrics (`style_metrics.py --target barnwell_lean`, running prose, 1,106 words)

| Metric | Value | Target |
|---|---|---|
| Sentence mean / SD | 19.4 / 10.4 | 17-21 / ≥ 10 |
| Short / long sentences | 12% / 19% | 6-15% / ≤ 20% |
| Words per paragraph | 58 | 55-85 |
| One-sentence paragraphs | 5% | 5-12% |
| Contractions per 1k | 39.8 | ≥ 28 |
| I / you per 1k | 0.0 / 5.4 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 1.8 / 4.5 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 53.3 | 30-55 |

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, unicode artifacts, question fragments or false ranges. Remaining hint `repeated_ngrams` (metric names).

Hover short in `glossary-terms.json` agrees with the page; no change proposed.
