# Claims register: zone-starts.json

Reviewed 2026-10-09. Computed rows use `research/glossary-pseo/raw/mp_skaters_2025.csv` (MoneyPuck 2025-26,
downloaded 2026-10-09; shift-start columns I_F_oZoneShiftStarts / dZone / neutralZone / flyShiftStarts, situation
5on5, skaters with ≥500 five-on-five minutes). NHL OZ Ratio from `raw/nhl_skater_puckPossessions_20252026_zonestarts.json`
(NHL stats API, downloaded 2026-10-09). Source pages saved in `raw/` (HockeyViz, Hockey-Graphs, War-on-Ice, NST snapshots).

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | OZS% = share of offensive- plus defensive-zone faceoff starts that came in the offensive zone; DZS% the own-end share | NST player glossary: "Off. Zone Start % ... excluding Neutral Zone and On The Fly Starts", OZS*100/(OZS+DZS); Hockey-Reference oZS%/dZS% tips | SUPPORTED |
| 2 | Coaches use them to shelter or bury players; starts tilt results | NHL glossary: players "deployed offensively ... should expect a slight increase in stats like SAT% and points"; HockeyViz 2015 (start location is the coach's decision) | SUPPORTED |
| 3 | Six in ten 5v5 shifts began on the fly in 2025-26 (61.2%); about one in five (21.6%) began with an end-zone faceoff | W&W calc: 501,945 fly / 819,613 shift starts; (89,875 + 87,220) / 819,613 | SUPPORTED (computed) |
| 4 | War-on-Ice's glossary: "probably Gabe and Vic", "found at behindthenet.ca for the longest time" | War-on-Ice Annotated Glossary (2015-11-26), footnote on zone starts, verbatim | SUPPORTED |
| 5 | Vollman's player usage charts: zone starts on one axis, quality of competition on the other, bubbles colored by relative Corsi; War-on-Ice credited them | War-on-Ice Annotated Glossary, "Bubble charts" entry | SUPPORTED |
| 6 | Tulsky (named Hurricanes GM in 2024) estimated an OZ start worth ~0.31 unblocked attempts (~0.4 Corsi), about half of earlier estimates, per a 2014 Hockey-Graphs summary | Hockey-Graphs, garik16, 2014-01-01 ("around .31 Fenwick per o zone start (roughly .4 Corsi) as seen in this Eric T study, which is about half of what was previously believed"); NHL.com 2024-06-18 (Tulsky named GM) | SUPPORTED |
| 7 | Cane 2015: after an OZ faceoff win and 45 seconds of play, the net effect is under 0.02 goals | Hockey-Graphs, Matt Cane, 2015-10-19, verbatim | SUPPORTED |
| 8 | McCurdy 2015: around half of shifts start on the fly; after reweighting shots by shift-start location, only 5% of players with 100 5v5 min in 2014-15 moved more than one point of shot share; two moved more than two | HockeyViz, "Shift Starts and Ends, Part 2", 2015-09-03, verbatim | SUPPORTED |
| 9 | NHL publishes OZ Start% and OZ Ratio, 5-on-5, available since 2009-10; H-R has oZS%/dZS%; NST and MoneyPuck count shift starts | NHL stats glossary (`raw/nhl_stats_glossary_api_20261009.json`, firstSeasonForStat 20092010); H-R table; NST glossary; MoneyPuck columns | SUPPORTED |
| 10 | NST and MoneyPuck count shift starts; NHL and H-R count every OZ/DZ faceoff the player was on the ice for | NST "Number of shifts for the player that started with an offensive zone faceoff"; MoneyPuck shift-start columns; NHL "face-offs ... while the player is on the ice"; H-R "Faceoffs ... that took place while on the ice" | SUPPORTED |
| 11 | NHL OZ Start% = OZ ÷ (OZ + NZ + DZ) on-ice faceoffs; OZ Ratio excludes NZ | NHL stats glossary, verbatim | SUPPORTED |
| 12 | Worked example (invented): 1,000 shifts, 600 fly, 160 NZ, 140 OZ, 100 DZ → 58.3%; 24% of shifts were end-zone starts | Labelled invented; arithmetic | SUPPORTED |
| 13 | Seider 34.5% by MoneyPuck shift starts, 42.8% by NHL OZ Ratio | W&W calc 130/(130+247); NHL puckPossessions offensiveZoneStartRatio 0.42842 | SUPPORTED (computed) |
| 14 | Median forward 53.1%, median defenseman 46.3% (5v5, 500+ min) | W&W calc | SUPPORTED (computed) |
| 15 | More than half of 385 forwards between 40% and 60% (57%); 10th and 90th percentiles 36.1% and 67.6% | W&W calc | SUPPORTED (computed) |
| 16 | Ovechkin 305 OZ starts, 6 DZ (98.1%); Lizotte, Acciari, Dewar (all PIT) the three most buried forwards, Lizotte 6.6% | W&W calc (Lizotte 14/199, Acciari 11.3%, Dewar 12.0%) | SUPPORTED (computed) |
| 17 | Detroit's eight forwards with 900 5v5 min all between 46.1% (Compher) and 56.2% (Kane) | W&W calc | SUPPORTED (computed) |
| 18 | Seider 34.5% and Edvinsson 34.8% were 16th- and 17th-lowest of 213 defensemen with 500 min; Sandin-Pellikka most sheltered Wings D at 50.8%; only fifteen regular defensemen had a lower share than Seider | W&W calc (rank from bottom 16 and 17) | SUPPORTED (computed) |
| 19 | Tulsky's rate on Seider's 117-start gap (247 − 130) ≈ 36 unblocked attempts of differential; Fenwick share 55.3% → ~56.2% | W&W calc 0.31 × 117 = 36.3, split evenly for/against on 1,173 FF / 947 FA | SUPPORTED (computed, labelled as an application of Tulsky's rate) |
| 20 | Seider began 247 shifts in his own end, 130 in the offensive zone; DET had 55.3% of xG and 54.1% of HD shots with him on at 5v5 | W&W calc | SUPPORTED (computed) |
| 21 | Washington had 49.6% of unblocked attempts with Ovechkin on at 5v5; Lizotte's on-ice share 52.5% | W&W calc FF% | SUPPORTED (computed) |
| 22 | McCurdy's weights: after OZ starts shots for 0.80, against 1.23; after DZ starts 1.33 for, 0.78 against | HockeyViz 2015-09-03 table | SUPPORTED |
| 23 | EH's RAPM regresses out zone starts with teammates, competition and score state | Evolving-Hockey RAPM glossary ("control for all teammates, opponents, score state, zone starts") | SUPPORTED |
| 24 | Cane: DZ win effect stabilizes in ~8 s, NZ ~14 s, OZ win takes nearly 60 s; leaving 15 s after an OZ win gets ~75% of a full 45-second shift's benefit | Hockey-Graphs 2015-10-19, verbatim | SUPPORTED |
| 25 | OZS% ignores the faceoff result; Cane's xFOGD accounts for result and shift length | Hockey-Graphs 2015-10-19 | SUPPORTED |
| 26 | McCurdy: where and how a shift starts is the coach's decision; what happens next (faceoffs, breakouts) is the player's | HockeyViz 2015-09-03, verbatim idea | SUPPORTED |
| 27 | FAQ: NHL versions at 5-on-5; H-R labels zone starts EV; MoneyPuck and NST filter by situation | NHL glossary; H-R header "Zone Starts (EV)"; MoneyPuck situation column; NST game-state filter | SUPPORTED |
| 28 | Tile: "oZS% at Hockey-Reference, OZ Ratio at NHL.com" | Rows 9, 11 | SUPPORTED |

Cut: Todd McLellan as the coach making the defensive assignments (not verified for 2025-26); Matt Cane's "true zone
starts" causation argument (only a secondary summary was found); the NHL icing no-change rule as a source of DZ starts
(not sourced in this pass).

## Voice metrics

Running prose: 1256 words (extract_prose.py → style_metrics.py --target barnwell_lean).

| Metric | Page | Target |
|---|---|---|
| sent_mean | 19.0 | 17-21 |
| sent_sd | 10.9 | >=10 |
| pct_short_le6 | 14 | 6-15 |
| pct_long_ge30 | 18 | <=20 |
| para_words | 57 | 55-85 |
| one_sent_paras | 5 | 5-12 |
| contractions_per_k | 30.3 | >=28 |
| I_per_k | 0.0 | <=6 |
| you_per_k | 5.6 | 3-8 |
| q_per_k | 1.6 | 1-5 |
| paren_per_k | 4.8 | 3-8 |
| intens_per_k | 0.0 | <=3 |
| trans_open_pct | 0 | <=5 |
| nums_per_k | 54.9 | 30-55 |
| hedge_narrow_per_k | 0.8 | <=3 |

ai-content-detection analyze_text.py: unicode artifacts 0, em dashes 0, contrast frames 0, payoff colons 0, question fragments 0, sentence-negation flags 0. Remaining n-gram hints are metric names ("five on five", "on the ice").

Proposed hover short: The share of a player's end-zone faceoff starts that came in the offensive zone (OZS%) or his own end (DZS%). Coaches use them to shelter or bury players.

(Why: the current short says "the share of a player's shifts that begin with an offensive-zone ... faceoff", which reads as
OZ starts ÷ all shifts, about 11% for a typical player. Every site's OZS% divides by offensive- plus defensive-zone starts only,
as the page defines it. 28 words, no colon.)
