# Claims register: scoring-chances.json

Reviewed 2026-10-09. Computed rows use `research/glossary-pseo/raw/mp_teams_2025.csv` and `mp_skaters_2025.csv`
(MoneyPuck 2025-26, downloaded 2026-10-09). MoneyPuck has no scoring-chance stat, so league benchmarks use its
medium- plus high-danger shots (goal probability ≥ 8%) and say so on the page. NST definitions come from Internet
Archive snapshots saved in `raw/` (NST blocks automated fetches); NST numbers for four Red Wings forwards come from
the 2025-26 five-on-five DET tables pulled 2026-09-02 for the wings-type research (`research/wings-type/raw/nst_5v5_2025.json`).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | SCF = attempts NST counts as scoring chances, by location in the offensive zone, with extra credit for rebounds and rush shots; SCF% is the share | NST team glossary (archived 2025-01-05): points system, "Any attempt with a score of 2 or higher is considered a scoring chance"; SCF% = SCF*100/(SCF+SCA) | SUPPORTED |
| 2 | Hohl quote: "If you were to ask 30 coaches the definition of a scoring chance, you will get 20 or more different answers"; bloggers' usual shortcut was the "home plate" area | Hockey-Graphs, Garret Hohl, 2017-02-06, verbatim | SUPPORTED |
| 3 | 2022 Kraken column on NHL.com: teams define chances their own way; walked through broadcaster JT Brown's checklist | NHL.com (Kraken), Alison Lukan, 2022-05-01: chances "can be defined differently (particularly within teams themselves)"; JT Brown's approach | SUPPORTED |
| 4 | War-on-Ice published its definition zone by zone on December 31, 2014, built on its own goal-probability research and David Johnson's rush-shot work | War-on-Ice blog, "NEW: Defining Scoring Chances", 2014-12-31 (empirical testing; "based on David Johnson's definition"); Annotated Glossary (danger zones a WOI original) | SUPPORTED |
| 5 | War-on-Ice's run ended about two years later after NHL teams hired its founders | Detroit Free Press, 2024-05-23 | SUPPORTED |
| 6 | NST describes a scoring chance "as originally defined by War-on-Ice", restates it as points, publishes SCF/SCA/SCF% for every team and skater back to 2007-08 | NST team and player glossaries (archived); season filter back to 2007-08 | SUPPORTED |
| 7 | MoneyPuck's glossary doesn't define a scoring-chance stat; closest equivalent is medium + high danger (≥8%) | MoneyPuck glossary fetched 2026-10-09 (only "scoring chances" mention is in the Deserve-To-Win meter text); danger cutoffs | SUPPORTED |
| 8 | Points system: offensive zone only; 1 outer areas, 2 high slot and wedges, 3 net-front box; +1 rebound (3 s after blocked/missed/saved attempt), +1 rush (4 s after NZ/DZ event), −1 blocked; chance = 2+ | NST glossary verbatim; NST danger-zone map (archived 2024-04-16) for areas | SUPPORTED |
| 9 | SCF/60 = SCF × 60 ÷ TOI | NST glossary SCF*60/TOI | SUPPORTED |
| 10 | Worked example (invented): point shot 1, high slot 2, outer-edge rush 1+1, blocked net-front 3−1 → three of four are chances, none high-danger | Labelled invented; applies rows 8 and NST HD threshold (3+) | SUPPORTED |
| 11 | WoI's zone-by-zone form: low-danger area only unblocked rebounds and rush shots; medium all unblocked; high everything including blocks | War-on-Ice 2014-12-31 post, verbatim conditions | SUPPORTED |
| 12 | Corsi counts every attempt equally; xG prices each attempt | NST glossary (Corsi = any shot attempt); MoneyPuck glossary (xG per attempt) | SUPPORTED |
| 13 | NST 5v5 on-ice SCF% 2025-26: Larkin 47.0%, Finnie 46.3%, Copp 47.4%, Kasper 49.0%; all under 50% | `nst_5v5_2025.json` on_ice (46.97, 46.26, 47.44, 48.98) | SUPPORTED |
| 14 | MoneyPuck medium + high danger at 5v5 2025-26: 24.0% of unblocked attempts, 53.3% of goals | W&W calc (5,133 + 15,824)/87,486; (799 + 2,061)/5,367 | SUPPORTED (computed) |
| 15 | Team share of that cut: Ottawa 56.4% (1st), Vancouver 42.1% (last), Detroit 49.2% (21st), median 49.9%; Detroit 9.40 per 60 (21st), allowed 9.71 (= median) | W&W calc, 5on5 teams file | SUPPORTED (computed) |
| 16 | A MoneyPuck "chance" went in 13.6% at 5v5, everything else 3.8% | W&W calc 2,860/20,957 and 2,507/66,529 | SUPPORTED (computed) |
| 17 | Hohl: home-plate shots scored about 14% of the time, 78% of goals on 46% of attempts | Hockey-Graphs 2017-02-06 (Super Shot Search figures) | SUPPORTED |
| 18 | NST 5v5 xGF%: Copp 51.9%, Kasper 52.0%; SCF% 47.4%, 49.0% | `nst_5v5_2025.json` (51.85, 52.03; 47.44, 48.98) | SUPPORTED |
| 19 | SCF% counts a two and a four the same; xG values each attempt | Definitions (rows 1, 12) | SUPPORTED |
| 20 | NST 5v5 iSCF: Kasper 129 in 963 min (8.0/60), Copp 111 in 1,022:30 (6.5), Finnie 119 in 1,062:16 (6.7); Kasper scored 9 goals | `nst_5v5_2025.json` individual; W&W per-60 calc; MoneyPuck I_F_goals (all situations) = 9 | SUPPORTED (computed) |
| 21 | McDavid led with 168 medium/high-danger shots (all situations), ~2.5x the median forward (68, 60+ GP); DeBrincat 9th with 138; Larkin tied for 21st with 121 (5 at 121) | W&W calc MoneyPuck skaters file | SUPPORTED (computed) |
| 22 | Detroit's two best chance creators were its two leading goal scorers, 41 and 34 | MoneyPuck skaters file: DeBrincat 41, Larkin 34 lead DET | SUPPORTED |
| 23 | NST's formula is reproducible from the play-by-play; team internal counts can differ | Rows 3, 8 | SUPPORTED |
| 24 | Larkin NST SCF% 47.0 vs MoneyPuck medium+high 46.6; Copp 47.4 vs 52.3 | NST file; W&W calc OnIce medium+high for/against 5on5 (157/337; 173/331) | SUPPORTED (computed) |
| 25 | Formula uses only location and timing; feed doesn't log screens or passes | NST rules (row 8); Evolving-Hockey xG write-up (no pass data); MoneyPuck/EH feature lists omit screens (xG page row 28) | SUPPORTED |
| 26 | FAQ: goals are shot attempts in NST's count, so a point-shot goal isn't a chance; NST tracks SCGF and a shooting percentage on SC shots | NST glossary: Corsi includes goals; SCGF, SCSH% definitions | SUPPORTED |

Cut for lack of a verifiable source: that bloggers hand-tracked chances before War-on-Ice (true in the record but no
reputable source retrieved); the content of War-on-Ice's "Better Than Corsi" follow-up post (offline).

## Voice metrics

Running prose: 1174 words (extract_prose.py → style_metrics.py --target barnwell_lean).

| Metric | Page | Target |
|---|---|---|
| sent_mean | 18.3 | 17-21 |
| sent_sd | 10.4 | >=10 |
| pct_short_le6 | 11 | 6-15 |
| pct_long_ge30 | 16 | <=20 |
| para_words | 56 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 29.8 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 5.1 | 3-8 |
| q_per_k | 1.7 | 1-5 |
| paren_per_k | 7.7 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 2 | <=5 |
| nums_per_k | 48.6 | 30-55 |
| hedge_narrow_per_k | 0.0 | <=3 |

ai-content-detection analyze_text.py: unicode artifacts 0, em dashes 0, contrast frames 0, payoff colons 0, question fragments 0, sentence-negation flags 0. Remaining n-gram hints are metric names ("five on five", "on the ice").

Hover short: the current `short` agrees with the page. No change proposed.
