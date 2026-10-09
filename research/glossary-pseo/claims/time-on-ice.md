# Claims register: time-on-ice.json

Raw files (all downloaded 2026-10-09, in `research/glossary-pseo/raw/`): `nhl_skater_timeonice_20252026_sogfamily.json`,
`nhl_skater_timeonice_20252026_DETonly_sogfamily.json` (teamId 17), `nhl_skater_summary_20252026_sogfamily.json`,
`nhl_skater_summary_20252026_DETonly_sogfamily.json`, `nhl_skater_summary_20242025_sogfamily.json`,
`nhl_goalie_summary_20252026_sogfamily.json`, `mp_teams_2025.csv`, `nhl_stats_glossary_api_20261009.json`,
`nhl_boxscore_2025020001_sogfamily.json`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | TOI = minutes on the ice, total or per game; per-game version is ATOI; NHL splits into EV, PP, SH | NHL glossary TOI ("TOI = EV TOI + PP TOI + SH TOI"), TOI/GP; Hockey-Reference glossary ATOI | SUPPORTED |
| 2 | The NHL game sheet carries ice time for every player | NHL gamecenter boxscore feed, per-player `toi` field | SUPPORTED |
| 3 | Official since 1997-98, splits too | NHL glossary TOI, PP TOI, SH TOI, EV TOI/GP ("available since 1997-98") | SUPPORTED |
| 4 | Skater shots counted for nearly four decades before (1959-60 to 1997-98) | NHL glossary S | SUPPORTED |
| 5 | Rule 36 (2025-26): time-on-ice scorer among the Real Time Scorers at every game, with three stats-entry scorers and an event analyst; reports during the 1st and 2nd intermissions and post-game; scoring system manager oversees the data | NHL Official Rules 2025-26, Rule 36.1-36.3 | SUPPORTED |
| 6 | Box-score minutes come from that log | Rule 36.1 (Real Time Scorers electronically record all official statistics) | SUPPORTED (inference from the rule) |
| 7 | NHL writes TOI and TOI/GP; Hockey-Reference writes ATOI in minutes and seconds per game | NHL glossary; Hockey-Reference glossary ("ATOI: Average time on ice (in minutes:seconds per game)") | SUPPORTED |
| 8 | TOI is playing time in all situations, so overtime counts; OT TOI is its own column | NHL glossary TOI ("playing time in all situations") and OT TOI | SUPPORTED |
| 9 | Ice time is game-clock time summed over shifts; stoppages add nothing; penalty-box time isn't ice time | Definition (TOI = playing time; shifts and TOI/shift columns in the NHL time-on-ice report) | SUPPORTED |
| 10 | Worked example: 24 shifts × 50 s = 20:00; minus 3 PP and 2 SH = 15 EV; × 80 games = 1,600 minutes | Arithmetic, labelled invented | SUPPORTED (invented, labelled) |
| 11 | EV TOI is the glossary's way to compare usage "in normal situations"; PP TOI% and SH TOI% are a player's share of team special-teams time | NHL glossary EV TOI, PP TOI%, SH TOI% | SUPPORTED |
| 12 | 327 forwards with 60+ GP: median TOI/GP 15:56 ("just under 16"); 161 defensemen: 20:21 ("a bit over 20"); defensemen median 24.2 shifts/game to forwards' 20.1, shift length 49.2 s vs 47.5 s | W&W calc, NHL time-on-ice report 2025-26 | SUPPORTED (computed) |
| 13 | Quinn Hughes 27:44 led; Werenski 26:37 second; Seider 25:40 third, all 82 GP; Seider led NHL in total minutes, 2,104.7, about 52 more than Hughes (2,052.6) | W&W calc, NHL time-on-ice report (league and Detroit-only) | SUPPORTED (computed) |
| 14 | McDavid led forwards at 22:59 ("just under 23"); Larkin 20:11 ranked 29th of 327 | W&W calc | SUPPORTED (computed) |
| 15 | Median forward splits: EV 13:26, PP 1:40, SH 0:40 (each median taken separately) | W&W calc | SUPPORTED (computed) |
| 16 | DeBrincat PP 3:20, SH 0:02; Larkin PP 3:16, SH 1:31; Compher SH 1:32, PP 0:40 | NHL time-on-ice report, Detroit-only split | SUPPORTED |
| 17 | 379 skaters with 60+ GP in both 2024-25 and 2025-26; TOI/GP correlation 0.90 (forwards 0.88, defensemen 0.76) | W&W calc, NHL skater summaries, Pearson r | SUPPORTED (computed) |
| 18 | Detroit: Seider 25:40 and Edvinsson 22:21 heaviest-used defensemen, Chiarot next at 20:50 (Faulk's Detroit-only 20:15 below him); Larkin 20:11, Raymond 18:48, DeBrincat 18:30 top forwards; Sandin-Pellikka 16:13 ranked 149th of 161 regular defensemen | NHL time-on-ice report, Detroit-only split; ranks from the league file | SUPPORTED (computed) |
| 19 | van Riemsdyk 31 points in 72 GP (0.43/game), 2.20 P/60 at 11:45; Copp 43 in 79 (0.54/game), 1.97 P/60 at 16:34; van Riemsdyk PP 1:51 per game | W&W calc: points ÷ (TOI/GP × GP) × 60, NHL summary + time-on-ice reports (Detroit-only) | SUPPORTED (computed) |
| 20 | Seider 28.6 shifts per game, 82 games, most minutes in the league | NHL time-on-ice report | SUPPORTED |
| 21 | 5-on-4 scoring 7.32 goals per 60 vs 2.48 at 5-on-5 in 2025-26 (almost three times) | W&W calc, MoneyPuck teams file: 1,446 goals / 197.4 h; 5,367 / 2,165.9 h | SUPPORTED (computed) |
| 22 | A one-shift game counts as a game played, so it stays in the TOI/GP denominator | NHL glossary GP | SUPPORTED |
| 23 | Zone starts and quality of competition exist as separate stats | `src/data/glossary-terms.json` (zone-starts, quality-of-competition-and-teammates) | SUPPORTED |
| 24 | FAQ: GAA = GA × 60 ÷ TOI; Vejmelka led goalies with 3,692.75 minutes ("almost 3,700"); Gibson 3,181 minutes, 144 GA, 2.72 GAA | NHL glossary GAA; NHL goalie summary 2025-26; Hockey-Reference leaders page (Vejmelka 3,693 minutes) | SUPPORTED |

## Voice metrics (extract_prose.py → style_metrics.py --target barnwell_lean)

1,198 words. Sentence mean 18.7 / SD 10.6; short 11%; long 16%; words per paragraph 60; one-sentence paragraphs 5%;
contractions 36.7/1k; I 0; you 4.2/1k; questions 1.7/1k; parentheses 5.0/1k; intensifiers 0; transition openers 0%;
numbers 51.8/1k; hedges 0. All in range. Hardest by far: numbers per 1k (first draft 95.7), because the metric
counts every mm:ss time as two numbers; most times are now written as rounded minutes ("just under 16 minutes")
with exact values kept in the quick-facts tiles. Sentence SD sat at 9.9-10.0 until a limit sentence was lengthened.

ai-content-detection `analyze_text.py`: no contrast frames, payoff colons, false ranges or unicode artifacts. Hints
`uniform_paragraph_structure` and `repeated_ngrams` only.

Cut for lack of verification: any claim that official TOI now comes from player tracking, and any accuracy figure for
the human shift log (none published that I could find).

No hover-short change proposed; the current `short` agrees with the page.
