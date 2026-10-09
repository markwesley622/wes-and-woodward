# Claims register: zone-entries-and-exits.json

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Entries and exits track how a team gets the puck into the offensive zone (with control or by dumping) and out of its own end | Sloan 2013 paper (carry, dump, misc entries); All Three Zones FAQ (exit types) | SUPPORTED |
| 2 | Counted by hand; the NHL's play-by-play doesn't log them | Sloan 2013 ("data that is not tracked by the NHL"); All Three Zones about ("tracking data that the NHL doesn't provide"); JFresh (manual tracking) | SUPPORTED |
| 3 | Carrying beat dumping in every data set the original researchers collected | Sloan 2013 ("every data set collected showed entries with possession being more than twice as effective as dump-ins at 5-on-5") | SUPPORTED |
| 4 | A carry-in produces about twice the shots of a dump-in | Sloan 2013 | SUPPORTED |
| 5 | Started on a fan blog in 2011; its author became an NHL GM | Broad Street Hockey zone-entry archive (tracking began in the 2011 playoffs); NHL.com, Jun 18, 2024 (Tulsky named Hurricanes GM) | SUPPORTED |
| 6 | Tulsky logged who crossed and whether he carried, passed or dumped; by Oct 2011, 0.51 shot attempts per controlled entry vs 0.20 per uncontrolled | Broad Street Hockey, Oct 25, 2011 | SUPPORTED |
| 7 | Sloan 2013: Tulsky, Detweiler, Spencer, Sznajder; 330 games from 2011-12; full season for Flyers and Wild, a handful (7-10) for most teams; quote "generates more than twice as many shots, scoring chances, and goals as dumping the puck in" | Sloan 2013 PDF (Wayback copy) | SUPPORTED |
| 8 | Tulsky joined Carolina as a consultant in 2014, named GM June 2024 | NHL.com (Hurricanes), May and June 2024 | SUPPORTED |
| 9 | Sznajder tracked every 2013-14 regular-season game, has tracked publicly since 2016-17 (30-50 games per team), shares data via the All Three Zones Patreon | Sznajder Patreon about page; The Hockey News, Sep 29, 2015 | SUPPORTED |
| 10 | CJ Turtoro's Tableau dashboards visualize the data | JFresh, Oct 1, 2020 (A3Z Dashboard on Tableau); github cjtdevil/a3z-prep | SUPPORTED |
| 11 | Costella's 2015 Nashville-Chicago series study; a 2019 Hockey-Graphs analysis of Sznajder's exit data | jenlc13.wordpress.com, May 19, 2015 (author Jennifer Lute Costella); Hockey-Graphs, Jul 30, 2019 | SUPPORTED |
| 12 | NHL EDGE reports puck zone time without entries; zone starts added later | NHL.com, Oct 23, 2023 (EDGE launch list incl. Puck Zone Time); NHL.com Oct 2025 redesign (Zone Starts Percentage); no entry metric listed | SUPPORTED (EDGE stat lists) |
| 13 | Sportlogiq lists controlled entries among its metrics; used by 97% of NHL teams | Sportlogiq, Aug 19, 2020; BetaKit, Jan 21, 2026 | SUPPORTED |
| 14 | Inputs and the entry types (carry, pass at the line, dump, misc such as a shot on goal from the neutral zone) | Sloan 2013; All Three Zones FAQ | SUPPORTED |
| 15 | Worked example (60 entries, 0.6 vs 0.3 attempts, five dumps turned into carries = 1.5 attempts) | Invented round numbers, labelled, near the Sloan rates | SUPPORTED (illustrative) |
| 16 | A3Z definitions: controlled entry "skating over the line or passing to a teammate at the blue line"; denial = failed entry for the attacker; exits with possession, without, failed | All Three Zones player-card FAQ | SUPPORTED |
| 17 | Observers agreed on entries more than 85% of the time, so disagreement up to about one in seven | Sloan 2013 | SUPPORTED |
| 18 | Rest of league 0.62 shot attempts per carry-in vs 0.28 per dump-in; goals at more than twice the rate (0.035 vs 0.015) | Sloan 2013 Table 1 (shots include misses) | SUPPORTED |
| 19 | 14% of carry-in attempts in the Capitals games ended in a turnover; 34% confidence break-even | Sloan 2013 | SUPPORTED |
| 20 | High-end forwards carry in on 70%+ of entries, grinders as low as 30% | Tulsky, SB Nation, Apr 9, 2014 | SUPPORTED |
| 21 | Coburn 62.8% carry-against, 11.7% break-up; MacDonald 78.1% and 4.7% (Flyers games tracked for the piece) | Tulsky, SB Nation, Apr 9, 2014 | SUPPORTED |
| 22 | Costella: controlled exits led to an entry attempt 88% of the time, dump-outs 29%; six games at even strength | Costella, May 19, 2015 (88.27%, 28.73%) | SUPPORTED |
| 23 | Hockey-Graphs 2019: carries and passes out work almost nine in ten, dump-outs one in five; almost four times as likely | Hockey-Graphs, Jul 30, 2019 | SUPPORTED |
| 24 | Net value per entry: carry attempt 0.42 shots, dump-and-chase 0.12, dump-and-change −0.10 | Sloan 2013 Table 3 | SUPPORTED |
| 25 | The 2013 paper's title separates offensive, neutral and defensive zone performance | Sloan 2013 | SUPPORTED |
| 26 | Exit studies tie controlled exits to the next entry | Costella 2015; Hockey-Graphs 2019 (recovered dump-out → 89% chance of next entry) | SUPPORTED |
| 27 | Neither entries nor exits appear in the NHL's own numbers | Rows 2 and 12 | SUPPORTED |

No Wes & Woodward calculations on this page apart from the labelled worked example; no 2025-26 league or Red Wings benchmarks exist publicly (All Three Zones data sits behind its Patreon).

## Voice metrics (running prose, `--target barnwell_lean`)

1,184 words. Sentence mean 17.7, SD 10.0; short 12%, long 15%; 59 words per paragraph; one-sentence paragraphs 10%; contractions 32.1/1k; I 0.0; you 4.2; questions 1.7; parentheses 4.2; intensifiers 0.0; transition openers 3%; numbers 43.1/1k; hedges 0.8 (the hit is "likely" inside Hockey-Graphs' "almost four times as likely to work"). Every metric in range. Hardest: long sentences (the first draft ran 31%, research citations run long) and contractions. ai-content-detection: no contrast frames, colon pivots or unicode artifacts; hints are uniform_paragraph_structure and repeated_ngrams.

## Proposed hover short

How a team gets the puck into the offensive zone, carrying it or dumping it in, and how it gets out of its own end. The NHL doesn't log either.

(The current short says a team "carries the puck into the offensive zone ... by dumping it in", which contradicts itself.)
