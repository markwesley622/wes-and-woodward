# Claims register: fenwick.json

Reviewed 2026-10-09. Computed rows come from `research/glossary-pseo/raw/mp_teams_2025.csv`, `mp_skaters_2025.csv`
(MoneyPuck season "2025" = 2025-26) and `mp_team_games_5on5_2023-2025_extract.csv`, all downloaded 2026-10-09.
NHL rows come from `nhl_stats_glossary_2026-10-09.json` and `nhl_team_percentages_20252026.json`, same day.

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Fenwick counts unblocked attempts (on goal or missed), for and against | MoneyPuck glossary (Fenwick); NHL glossary USAT; Evolving-Hockey General Terms | SUPPORTED |
| 2 | Corsi with blocked shots taken out | NHL glossary USAT ("SAT, which includes blocked shots"); Evolving-Hockey ("excludes blocked shots") | SUPPORTED |
| 3 | Same set of shots expected goals uses | Evolving-Hockey glossary (xGF from Fenwick shots); MoneyPuck xG on unblocked attempts (see expected-goals register row 18) | SUPPORTED |
| 4 | FF% is the share; NHL calls it USAT / USAT% | NHL glossary USAT% ("also known as Fenwick for percentage, or FF%") | SUPPORTED |
| 5 | Matt Fenwick, a Flames blogger at Battle of Alberta, proposed dropping blocked shots in November 2007; the version took his name | Battle of Alberta, "Flames thru 20", posted by Matt, Nov 2007 (archive date header Nov 19; Wikipedia and PPP say Nov 22, so the page says "November 2007"); raw `battleofalberta_2007-11_archive_fetched_2026-10-09.html`; Pension Plan Puppets 2012-07-25; Wikipedia Fenwick (statistic) | SUPPORTED |
| 6 | Post covered Calgary's first 20 games and showed two versions of the Corsi plus-minus at the bottom, with and without blocks | Same post ("Cumulative (Games 1 thru 20)"; "the two versions of the Corsi +/- at the end"; shots directed at net with and without blocked shots) | SUPPORTED |
| 7 | Quote: "As a proxy for scoring chances for & against, I think it works best if blocked shots are excluded" | Same post, verbatim | SUPPORTED |
| 8 | Iginla post vs. Willie Mitchell deflection example; counting both the same fails to credit the defense | Same post (paraphrase of the Iginla/Mitchell paragraph, "failing to credit the defensive team") | SUPPORTED |
| 9 | Version with blocks a proxy for zone time, "Where The Puck Is" | Same post, verbatim | SUPPORTED |
| 10 | Detroit blocked the most 5v5 attempts in 2025-26, tied with Seattle at 1,179; about 108 more than the median team (1,071.5); 1,029 of Detroit's own attempts blocked, median 1,031.5 | W&W calc, MoneyPuck teams file 5on5 (blockedShotAttemptsAgainst / For) | SUPPORTED (computed) |
| 11 | Detroit FF% ran nearly a point above CF% (49.7 vs 48.8, gap 0.88), second-largest gap behind Philadelphia (0.92) | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |
| 12 | NHL adopted it as USAT in February 2015 | SI (Allan Muir) 2015-02-20 | SUPPORTED |
| 13 | NHL glossary: USAT takes shot-blocking performance into account, SAT doesn't; available since 2009-10 | NHL glossary USAT entry | SUPPORTED |
| 14 | NST, MoneyPuck, Evolving-Hockey, Hockey-Reference publish Fenwick | NST glossary (Wayback capture); MoneyPuck glossary; Evolving-Hockey General Terms; Hockey-Reference analytics ("Fenwick (EV)") | SUPPORTED |
| 15 | 31 of 32 teams had FF% within a point of CF% in 2025-26 (Nashville 1.7 the exception) | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |
| 16 | Worked example (invented): CF 45, FF 30, CA 40, FA 30; Corsi 45-40, Fenwick even | arithmetic | SUPPORTED |
| 17 | FF% and CF% correlated 0.98 across 32 teams; 72% of 5v5 attempts unblocked (87,486 of 121,106) | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |
| 18 | 2025-26 5v5 FF%: Carolina 58.9 (1st), Colorado 55.9 (2nd), Toronto 45.1 (last), Detroit 49.7 (16th, CF% rank 21st) | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |
| 19 | 598 skaters 500+ 5v5 min: median on-ice FF% 49.6, top tenth ≥ 55.0; player FF% vs CF% r = 0.97 | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 20 | Split test (96 team-seasons, last three seasons): first-half FF% to second-half GF% 0.44, CF% 0.42; repeat CF% 0.81, FF% 0.77 | W&W calc, game-by-game extract, first 41 vs last 41 | SUPPORTED (computed) |
| 21 | Rink effects 2007-08 through 2012-13: Corsi events 12 rinks, Fenwick 5, blocks 15, misses 9; blocks the least consistently recorded shot event (shots on goal 2) | Schuckers and Macdonald, arXiv 1412.1035, Table 19 | SUPPORTED |
| 22 | Detroit's opponents out-attempted the Wings mostly with blocked shots | CA − CF = 184; FA − FF = 34, MoneyPuck teams file | SUPPORTED (computed) |
| 23 | MoneyPuck and Evolving-Hockey xG models price only unblocked attempts; NHL logs blocked shots at the spot of the block | Evolving-Hockey model write-up and glossary; MoneyPuck about (see expected-goals register rows 17-18) | SUPPORTED |
| 24 | NHL close-game definition; close-game filtering removes score-effect skew at a modest cost in sample | NHL glossary "Close or close game" | SUPPORTED |
| 25 | NHL calls USAT% close (Fenwick close) a strong indicator of possession and good predictor of future success | NHL glossary USAT% Close | SUPPORTED |
| 26 | Detroit 2025-26 USAT% 49.7 overall, 49.9 in close games | NHL team percentages report (usatPct, usatPctClose) | SUPPORTED |
| 27 | USAT% Relative = player's USAT% minus team's with him off the ice | NHL glossary USAT% Relative | SUPPORTED |
| 28 | Fenwick conceded blocks indicate zone time; Corsi repeated a little better half to half | Battle of Alberta post; row 20 | SUPPORTED |
| 29 | On-ice FF% correlated 0.73 with team FF% (598 skaters) | W&W calc, MoneyPuck skaters + teams files | SUPPORTED (computed) |

Live slot: omitted. The pipeline carries no Fenwick field. Wanted: `team.situations.5on5.fenwickPct` with
`leagueRanks.fenwickPct_5on5`, and `skaters.fiveOnFive.onIceFenwickPct` (both are already in MoneyPuck's files as
`fenwickPercentage` and `onIce_fenwickPercentage`).

## Voice metrics (running prose, `--target barnwell_lean`)

Running prose, 1,150 words.

| Metric | Page | Target |
|---|---|---|
| Sentence mean / SD | 18.9 / 11.2 | 17-21 / ≥ 10 |
| Short / long sentences | 13% / 16% | 6-15% / ≤ 20% |
| Words per paragraph | 64 | 55-85 |
| One-sentence paragraphs | 6% | 5-12% |
| Contractions per 1k | 30.4 | ≥ 28 |
| I / you per 1k | 0.9 / 3.5 | ≤ 6 / 3-8 |
| Questions / parentheses per 1k | 2.6 / 5.2 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0.0 / 0.0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 42.6 | 30-55 |
