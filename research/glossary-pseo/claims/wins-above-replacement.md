# Claims register: wins-above-replacement.json

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | WAR is one number for total value over a replacement-level player; EH publishes it in goals (GAR), wins (WAR) and an expected-goals form (xGAR); covers even strength, special teams and penalties | EH GAR glossary (components EVO, EVD, PPO, SHD, Take, Draw; "GAR, WAR, and SPAR"); EH overview (xGAR) | SUPPORTED |
| 2 | Replacement level = outside a team's top 13 F / top 7 D by TOI at even strength; special teams use top 11 skaters | EH GAR glossary (current: EVO/EVD top 13 F or 7 D; PPO/SHD top 11 skaters); Hockey-Graphs WAR Part 3 (2019) | SUPPORTED |
| 3 | EH took the TOI cutoff because there aren't enough league-minimum players ("poor man's replacement") | Hockey-Graphs WAR Part 3, Jan 18, 2019 | SUPPORTED |
| 4 | EH's model is the main public version and the foundation of the site's W-Value | Writer brief (EH models are the main public source); pipeline/build_player.py (W-Value built on EH xGAR/GAR components) | SUPPORTED (editorial + code) |
| 5 | FanGraphs: WAR sums a player's total contribution in one statistic against a freely available minor leaguer who'd replace him if hurt | FanGraphs library, WAR | SUPPORTED |
| 6 | Alan Ryder's Player Contribution, 2003 | Hockey-Graphs WAR Part 1 ("Player Contribution method from August, 2003") | SUPPORTED |
| 7 | Tom Awad's GVT at Hockey Prospectus, explained in 2009 as hockey's VORP, value in goals above a replacement | "Understanding GVT, Part 1", Hockey Prospectus, July 30, 2009 | SUPPORTED |
| 8 | Andrew (C.) Thomas, Sam Ventura and Alexandra Mandrycky built a WAR model for WAR On Ice in fall 2014 | Hockey-Graphs WAR Part 1; CMU news, Nov 2014 (Thomas and Ventura built WAR-On-Ice.com) | SUPPORTED |
| 9 | Dawson Sprigings released a WAR model in summer 2016 | Hockey-Graphs WAR Part 1; Perry 2017 ("Dawson Sprigings' version from 2016") | SUPPORTED |
| 10 | Emmanuel Perry published a WAR on Corsica, May 2017 | "The Art of WAR", corsica.hockey, May 20, 2017 | SUPPORTED |
| 11 | Josh and Luke Younggren, three-part Hockey-Graphs series Jan 16-18, 2019, two days after the RAPM write-up (Jan 14) | Hockey-Graphs dates; EH reposts credit Josh and Luke Younggren | SUPPORTED |
| 12 | "we don't care whether it's predictive"; descriptive model | Hockey-Graphs WAR Part 1 | SUPPORTED |
| 13 | xGAR followed in October 2019; EH calls it the "deserved" or "expected" model | EH About (xGAR 1.0, 2019-10-02); EH overview | SUPPORTED |
| 14 | Patrick Bacon's model at HockeyStats has a separate shooting component | hockeystats.com/methodology/war (byline Patrick Bacon; six components incl. Shooting) | SUPPORTED |
| 15 | Luszczyszyn's Game Score Value Added does a similar job at The Athletic | The Athletic (search snippet "Game Score Value Added, or GSVA"); All About The Jersey primer (translated into wins) | SUPPORTED (paywalled original, secondary confirms) |
| 16 | Public models run three steps: goals above average, replacement baseline, goals to wins | Hockey-Graphs WAR Part 3 (EH steps); HockeyStats methodology (replacement level, Pythagorean goals per win) | SUPPORTED |
| 17 | EH runs long-term RAPM per component, trains SPM on play-by-play/box-score metrics to predict it, uses SPM output per season | Hockey-Graphs WAR Parts 2 and 3 | SUPPORTED |
| 18 | In the 2019 write-up offense was built on goals for, defense on expected goals against | Hockey-Graphs WAR Parts 2 and 3 | SUPPORTED |
| 19 | Goals to wins through a rolling season-by-season conversion | EH GAR glossary (Laidig method, rolling weighted average) | SUPPORTED |
| 20 | About six (6.2) goals per win in the 2025-26 export | W&W calc: median GAR ÷ WAR = 6.16 among skaters with abs(WAR) ≥ 1, EH 2025-26 export | SUPPORTED (computed) |
| 21 | Worked example: 10 GAR ≈ 1.7 WAR, a little over three standings points | Arithmetic; median SPAR ÷ WAR = 1.91 in the 2025-26 export, so 1.67 × 1.91 = 3.2 | SUPPORTED (computed, invented inputs labelled) |
| 22 | Median forward (327 with 60+ GP) 0.9 WAR; top 10% ≥ 2.4; defensemen median 0.7 (161) | W&W calc, EH 2025-26 GAR export, team rows summed per player | SUPPORTED (computed) |
| 23 | Hutson and Hughes tied for the lead among 940 skaters at 4.9 WAR; Hutson ahead on GAR 30.2 to 29.9 | W&W calc, same file | SUPPORTED (computed) |
| 24 | Seider tied for 4th at 4.3 (with Kucherov), 0.8 clear of any other Red Wing; DeBrincat tied for 10th at 3.5; Raymond 2.7 | W&W calc, same file (tie-aware ranks) | SUPPORTED (computed) |
| 25 | 23% of skaters with 60+ GP below replacement; Chiarot −1.2 WAR, 925th of 940 | W&W calc, same file | SUPPORTED (computed) |
| 26 | xGAR year-to-year r = 0.50, GAR 0.44 (consecutive seasons since 2007-08, 800+ min both) | W&W calc, EH xGAR/GAR exports, 5,919 pairs (same method as build_player.reliability_constants) | SUPPORTED (computed) |
| 27 | EH suggests a ±0.5-win error range on a season | Hockey-Graphs WAR Part 3 | SUPPORTED |
| 28 | W-Value: 0-100, blends xGAR and GAR 60/40 per component, leans to chances because they repeat better, 50 = average skater with 20+ GP, ~23 points per SD | pipeline/build_player.py (BLEND 0.60/0.40, method string); src/pages/players/[slug].astro "Where the W-Value comes from" | SUPPORTED |
| 29 | EH awards average xGAR and GAR; EH says GAR isn't its preferred model for defensemen because it uses on-ice shooting % | EH "NHL Awards 24-25" blog | SUPPORTED |
| 30 | Seider 26.3 GAR: EVO 10.9, EVD 10.4, PPO 4.4; DeBrincat 21.4 GAR with EVO 14.1 | W&W calc, EH 2025-26 GAR export | SUPPORTED (computed) |
| 31 | Sandin-Pellikka rookie season −1.9 GAR, +3.3 xGAR, below the median defenseman's 4.3 GAR | W&W calc, EH 2025-26 exports | SUPPORTED (computed) |
| 32 | Bacon's model uses a similar replacement cut (below 13th F / 7th D in TOI%) | HockeyStats WAR methodology | SUPPORTED |
| 33 | EH, HockeyStats and The Athletic build their own components and conversions | EH glossary; HockeyStats methodology (Pythagorean exponent 2.022, own components); GSVA secondary | SUPPORTED |
| 34 | FAQ: EH rates goalies separately on unblocked shots against (GAA/GAR from EV and SH Fenwick against) | EH GAR glossary, goalie section | SUPPORTED |
| 35 | FAQ: site's goalie rating = MoneyPuck GSAx scaled 0-100 among goalies with 600+ minutes | pipeline/build_player.py goalie method string | SUPPORTED |

Computed rows use Evolving-Hockey's GAR, xGAR and WAR exports in `research/rasmussen/raw/eh/` (all seasons through 2025-26, downloaded 2026-09-08), traded players' team rows summed.

## Voice metrics (running prose, `--target barnwell_lean`)

1,233 words. Sentence mean 18.7, SD 10.0; short 15%, long 20%; 59 words per paragraph; one-sentence paragraphs 10%; contractions 44.5/1k; I 0.0; you 5.7; questions 1.6; parentheses 5.7; intensifiers 0.0; transition openers 0%; numbers 51.0/1k; hedges 0.8/1k (the "May" in "May 2017"). Every metric in range; SD, short and long sentences sit on the edges of their ranges. ai-content-detection: no contrast frames, colon pivots or unicode artifacts; hints are uniform_paragraph_structure and repeated_ngrams (template and metric names).
