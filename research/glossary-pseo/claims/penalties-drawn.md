# Claims register: penalties-drawn.json

Raw files (downloaded 2026-10-09, `research/glossary-pseo/raw/`): `nhl_skater_penalties_20252026.json`,
`nhl_skater_penalties_20242025.json`, `nhl_skater_summary_20252026.json`, `nhl_team_penalties_20252026.json`,
`nhl_team_powerplay_20252026.json`, `nhl_team_penaltykill_20252026.json`, `nhl_skater_penalties_20082009_drawn_check.json`,
`nhl_skater_penalties_20092010_drawn_check.json`, `nhl_pbp_2025020001_penalty_fields_check.json`,
`nhl_stats_glossary_20261009.json`, `nhl_rulebook_2025-26_downloaded_20261009.pdf`, `mp_skaters_2025.csv`.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Penalties drawn = penalties called on opponents because of a player; net = drawn minus taken | NHL glossary Pen Drawn, Net Pen | SUPPORTED |
| 2 | Most drawn penalties hand his team a power play | 7,555 PP opportunities vs 9,692 penalties drawn by teams in 2025-26 (NHL team reports) | SUPPORTED (computed) |
| 3 | McDavid drew 56 in 2025-26 | NHL skater penalties report | SUPPORTED (computed) |
| 4 | Detroit second in penalty differential (+44), one behind Minnesota (+45) | NHL team penalties report (netPenalties) | SUPPORTED (computed) |
| 5 | Tracked since 2009-10 | NHL glossary firstSeasonForStat 20092010; API 2008-09 penaltiesDrawn null | SUPPORTED |
| 6 | 0.17 net goals per penalty, WAR-On-Ice's average (A.C. Thomas et al.) | Evolving-Hockey, Penalty Goals: "first shown in the penalty component of the WAR model from WAR-On-Ice"; Thomas's "average figure of 0.17 net goals per penalty taken or drawn" | SUPPORTED |
| 7 | 9,692 penalties drawn by the 32 teams in 2025-26 | NHL team penalties report (totalPenaltiesDrawn sum) | SUPPORTED (computed) |
| 8 | Median forward drew 15 (327, 60+ GP) | W&W calc, NHL skater penalties | SUPPORTED (computed) |
| 9 | Drawn per 60 correlated 0.73 year to year (379 skaters); taken per 60 0.79; plus-minus 0.35 | W&W calc (Pearson), NHL skater penalties and summaries 2024-25 and 2025-26 | SUPPORTED (computed) |
| 10 | NHL started publishing drawn alongside taken and net in 2009-10; Dustin Brown (LAK) led with 75 | NHL glossary (all three 20092010); API 2009-10 penalties report | SUPPORTED |
| 11 | Play-by-play tags each penalty with the player who committed it and the player who drew it | NHL play-by-play (game 2025020001) penalty details committedByPlayerId, drawnByPlayerId | SUPPORTED |
| 12 | Penalty value based on how much more often teams score with the extra man | Evolving-Hockey Penalty Goals (5v5 → 5v4 GF60/GA60 change, after Thomas et al.) | SUPPORTED |
| 13 | Quote: "taking penalties is a bad thing and drawing penalties is a good thing"; first published at Hockey-Graphs in January 2019 | Evolving-Hockey Penalty Goals (verbatim; originally Hockey-Graphs 2019-01-15) | SUPPORTED |
| 14 | EH prices each penalty by the strength state it creates; 5v5 minor 0.182; one that turns 5v4 into 5v3 is worth more (0.419) | Evolving-Hockey Penalty Goals | SUPPORTED |
| 15 | Drawn and taken are separate EH WAR components; MoneyPuck skater files carry the drawn count | EH GAR glossary (Take, Draw); MoneyPuck skaters file column penaltiesDrawn | SUPPORTED |
| 16 | The count includes all penalty types, all situations | NHL glossary Pen Drawn | SUPPORTED |
| 17 | Skaters credited with 8,673 of 9,692 drawn; 1,019 not on a skater's line | W&W calc: skater penaltiesDrawn sum vs team totalPenaltiesDrawn sum | SUPPORTED (computed) |
| 18 | NHL glossary: forwards tend to post better net numbers than defensemen | NHL glossary Net Pen | SUPPORTED |
| 19 | D median drew 10 (161 regulars); median D 0.39 drawn and 0.63 taken per 60 | W&W calc, NHL skater penalties | SUPPORTED (computed) |
| 20 | McDavid 18 more than Schaefer (38); net +34, 14 better than anyone (Vilardi +20) | NHL skater penalties | SUPPORTED (computed) |
| 21 | Hathaway (PHI) led regulars per 60 at more than two (2.10), about 10 minutes a night | NHL skater penalties (60+ GP; 10.4 min TOI/GP) | SUPPORTED (computed) |
| 22 | Detroit drew 312 (10th), took 268 | NHL team penalties report | SUPPORTED (computed) |
| 23 | Raymond 26 led Detroit, Larkin (24) and Compher (23) close behind | NHL skater penalties | SUPPORTED (computed) |
| 24 | Detroit's +44 ≈ 7.5 goals at 0.17 | 44 × 0.17 = 7.48 | SUPPORTED (computed) |
| 25 | Finnie drew 22, took 3, net +19 tied third behind McDavid and Vilardi; about three goals; 30 points; 6 PIM; only McDavid and Vilardi higher among forwards (Schaefer, tied at +19, is a defenseman) | NHL skater penalties + summary; 19 × 0.17 = 3.2 | SUPPORTED (computed) |
| 26 | Detroit 248 PP opportunities, shorthanded 210, gap 38; 56 PPG; Minnesota scored 65 PPG | NHL team power-play and penalty-kill reports | SUPPORTED (computed) |
| 27 | Defensemen tend to sit on the wrong side | NHL glossary Net Pen; D60 median net −6 vs F60 +2 | SUPPORTED |
| 28 | Chiarot took 31, drew 10, −21 fifth-worst, about 3.5 goals; Zadorov −25 worst | NHL skater penalties; 21 × 0.17 = 3.57 | SUPPORTED (computed) |
| 29 | Seider averaged the most ice time on Detroit (25.7 min) and finished at −6, the median for a regular D | NHL skater summary + penalties | SUPPORTED (computed) |
| 30 | A delayed minor washed out by a goal is never imposed | Rule 15.2 | SUPPORTED |
| 31 | EH notes the NHL doesn't record those delayed-penalty situations | Evolving-Hockey Penalty Goals ("Delayed penalty goals are not recorded by the NHL") | SUPPORTED |
| 32 | A drawn misconduct puts nobody's team a man down | Rule 22.3 | SUPPORTED |
| 33 | Median forward net +2; spread Finnie +19 to Chiarot −21 ≈ seven goals at 0.17 | W&W calc; 40 × 0.17 = 6.8 | SUPPORTED (computed) |
| 34 | FAQ: not a point; not on the main skater summary; kept in a separate penalties report with taken and net | NHL stats API: skater summary fields have no penalties drawn; skater penalties report carries penaltiesDrawn, penalties, netPenalties | SUPPORTED |

Keywords: stat_themes.json lists penalties-drawn as `no_volume` (0 candidates), so the primary is the natural phrase
"penalties drawn in hockey" with no supporting keywords; `keywords.source` says so.

Worked example uses invented round numbers and says so.

## Voice metrics (running prose, `--target barnwell_lean`)

1,147 words. Sentence mean 18.5 / SD 10.5; short 11% / long 8%; 57 words per paragraph; one-sentence paragraphs 5%;
contractions 36.6/1k; I 0.0; you 3.5; questions 1.7; parentheses 3.5; intensifiers 0.0; transition openers 0%;
numbers 54.1/1k; hedges 0.0. All in range. ai-content-detection: no contrast frames, payoff colons, unicode artifacts or
negation pivots; hints `uniform_paragraph_structure`, `repeated_ngrams`.

Cut: claims that penalty drawing is a proven repeatable skill from secondary sources (TSN, Leafs Nation citing Gabe
Desjardins); the page uses its own season-to-season correlation instead.

Proposed hover short: Penalties a player draws from opponents, most of them power plays for his team. Drawn minus taken is penalty differential, a small but real piece of a player's value.

(Reason: the NHL count includes every penalty type, so drawn misconducts and coincidental majors don't create power plays; "each one a power play" overstates it.)
