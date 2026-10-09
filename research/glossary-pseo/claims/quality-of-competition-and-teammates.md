# Claims register: quality-of-competition-and-teammates.json

Reviewed 2026-10-09. QoC/QoT figures use Evolving-Hockey's 2025-26 even-strength QoC and QoT exports
(`research/wings-type/raw/eh/qoc_ev_rates_2025.csv`, `qot_ev_rates_2025.csv`, subscriber data downloaded 2026-09-02;
cited, not republished), skaters with ≥500 EV minutes (372 forwards, 214 defensemen). xG shares are MoneyPuck 5v5 from
`research/glossary-pseo/raw/mp_skaters_2025.csv` (downloaded 2026-10-09). Sandin-Pellikka's per-game QoC is
`research/sandin-pellikka/raw/asp_qoc_by_game.json` (built by `build_qoc_by_date.py` from NHL shift charts, September 2026).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | QoC/QoT measure opponents' and linemates' strength, usually averaged and weighted by shared ice time | Evolving-Hockey QoT/QoC page: "a weighted average of a player's teammates' or opponents' metric, where the weights are the percentage of time ..." | SUPPORTED |
| 2 | "He plays tough minutes" is a common defense of a bad shot share | Hockey-Graphs, garik16, 2014-01-01 ("Sure he has a bad corsi, but he gets tough minutes!") | SUPPORTED |
| 3 | The gap in teammates is more than twice as wide as in competition | W&W calc: SD of TOI% QoT 1.204 vs QoC 0.559 (2.2x), forwards | SUPPORTED (computed) |
| 4 | By 2014 Behind the Net carried three measures of competition and three of teammates, by one Hockey-Graphs writer's count | garik16, 2014-01-01, verbatim | SUPPORTED |
| 5 | Vollman's usage charts put QoC on one axis and zone starts on the other | War-on-Ice Annotated Glossary (x-axis zone starts, y-axis quality of competition) | SUPPORTED |
| 6 | Tulsky's August 2012 NHL Numbers post measured competition by ice time, the earliest War-on-Ice could find | War-on-Ice glossary: "Time on ice as a measure: Eric Tulsky has the first reference we can find" → nhlnumbers.com/2012/8/16/a-competition-metric-based-on-ice-time | SUPPORTED |
| 7 | A month later his histograms showed how narrow the competition spread was | Hockey-Graphs, Garret Hohl, 2015-10-08 (image credit "Competition Histograms by Eric Tulsky from NHL Numbers, Sep 23, 2012"; "distribution ... for competition tended to be a lot smaller than many realized") | SUPPORTED |
| 8 | Hohl's summary: ice time became the preferred measure; line matching went from important to overrated to "inconsequential" | Hohl 2015-10-08, verbatim | SUPPORTED |
| 9 | 2014 Hockey-Graphs piece: nearly every player's average opponent within ±1 Corsi/60 of average, extremes ~2 | garik16 2014-01-01, verbatim | SUPPORTED |
| 10 | Hohl 2015: teammate quality ~5x the variance of competition; a one-point change in either moves own shot share ~1.5 points (up for teammates, down for opponents) | Hohl 2015-10-08 ("about 5 times the deviation and variance"; "+1.5 ... -1.5") | SUPPORTED |
| 11 | Stimson and DTMAboutHeart 2016 split by position; for a forward's shot generation, defensemen faced and forwards played with carried the weight | Hockey-Graphs 2016-10-10, verbatim finding | SUPPORTED |
| 12 | EH publishes QoC and QoT built on ice time, RAPM, GAR and xGAR, weighted by shared minutes | Evolving-Hockey QoT/QoC page; export columns TOI%, TOI/GP, RAPM_C±/60, RAPM_xG±/60, GAR±/60, xGAR±/60 | SUPPORTED |
| 13 | Inputs: opponents/teammates, shared seconds from NHL shift charts, a rating, game state | EH page; shift-chart reconstruction in `build_qoc_by_date.py` | SUPPORTED |
| 14 | TOI% = a player's ice time ÷ minutes available | EH: "percentage of available minutes a player played" | SUPPORTED |
| 15 | Worked example (invented): 600 min vs 30% opponents, 400 vs 27% → 28.8%, about what the average forward faces (mean 28.72%) | Labelled invented; arithmetic; W&W calc forward mean | SUPPORTED |
| 16 | Hohl: a 13-minute forward on a contender isn't the same talent as one on a lottery team | Hohl 2015-10-08, paraphrased | SUPPORTED |
| 17 | 372 forwards: QoC TOI% 27.23% to 29.86%, SD 0.56; opponents' TOI/GP 13.65 to 14.99 | W&W calc EH QoC export | SUPPORTED (computed) |
| 18 | QoT TOI% 26.21% to 33.19%, SD 1.20, 2.2x QoC's SD, 4.6x variance; xGAR/60 rating SD ratio 5.6 | W&W calc EH QoC/QoT exports | SUPPORTED (computed) |
| 19 | Larkin toughest Wings QoC 29.71%, 6th of 372; van Riemsdyk softest 27.85%, 346th; opponents' TOI/GP 14.9 vs 13.95; whole Detroit range < 1 minute | W&W calc | SUPPORTED (computed) |
| 20 | Larkin xGF% 47.2% at 5v5; QoT ranked 41st of 372 | MoneyPuck calc; EH QoT export | SUPPORTED (computed) |
| 21 | Seider QoC 29.12%, Chiarot 28.87%; QoT ranks 15th and 168th of 214 D (153 places); xGF% 55.3% and 45.2% | EH exports; MoneyPuck calc | SUPPORTED (computed) |
| 22 | EH's QoT/QoC table is season-only; W&W rebuilt ASP's QoC per game from NHL shift charts, matching EH's 5v5 TOI to the hundredth (13.66) | `research/sandin-pellikka/BRIEF.md` §5 and §12 (Filter Type offers only "Seasons"; validation 13.66 vs 13.66) | SUPPORTED |
| 23 | ASP opponents' xGAR/60: +0.156 first 34 games, +0.253 last 34 (TOI-weighted); ice time fell (15.2 → 12.1 per game); r(TOI, QoC) = −0.21 | W&W recalculation from `asp_qoc_by_game.json` on 2026-10-09 | SUPPORTED (computed) |
| 24 | Hohl 2017 conceded the mean-only problem and argued that binning opponents into tiers is arbitrary; regression models superior | Hockey-Graphs 2017-02-06, verbatim ideas | SUPPORTED |
| 25 | Ice-time QoC rewards facing high-minute players; RAPM/GAR versions rate on results | EH column definitions; Hohl 2015 (row 16) | SUPPORTED |
| 26 | RAPM controls for teammates, opponents, zone starts and score at once | Evolving-Hockey RAPM glossary | SUPPORTED |
| 27 | Hohl: teammate effect isn't the same for every player, unlike competition | Hohl 2015-10-08 ("unlike with competition Corsi%, teammate Corsi% impact is not the same for all players") | SUPPORTED |

Cut: a projected "point or two of shot share" cost of the hardest assignment (would need competition rated in shot
share, which this pass didn't pull); "most complete public tables" for Evolving-Hockey (unverifiable superlative).

## Voice metrics

Running prose: 1144 words (extract_prose.py → style_metrics.py --target barnwell_lean).

| Metric | Page | Target |
|---|---|---|
| sent_mean | 18.5 | 17-21 |
| sent_sd | 10.1 | >=10 |
| pct_short_le6 | 15 | 6-15 |
| pct_long_ge30 | 15 | <=20 |
| para_words | 57 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 36.7 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 5.2 | 3-8 |
| q_per_k | 2.6 | 1-5 |
| paren_per_k | 6.1 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 2 | <=5 |
| nums_per_k | 54.2 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

ai-content-detection analyze_text.py: unicode artifacts 0, em dashes 0, contrast frames 0, payoff colons 0, question fragments 0, sentence-negation flags 0. Remaining n-gram hints are metric names ("five on five", "on the ice").

Hover short: the current `short` agrees with the page. No change proposed.
