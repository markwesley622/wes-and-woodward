# Michael Brandsegg-Nygård: first 10 games, 2025-26 vs 2026-27

Research brief for the Wes & Woodward piece "Michael Brandsegg-Nygard's Top-6 Glowup." Mark writes the prose; this is the evidence. Built 2026-10-23 from NHL play-by-play and shift charts, MoneyPuck shot xG, HockeyStatCards, NHL Edge and the NHL stats API. Two samples: his first 10 NHL games of 2025-26 (nine in October, then the March 8 game in New Jersey after his recall) and the first 10 games of 2026-27 (Oct 2 through Oct 22 in Vancouver).

## Verdict

The box score says 0-1-1 became 2-6-8. The underlying record says three different things happened at once, and only one of them is the player getting better at hockey. First, his shot map moved about seven feet closer to the net: the same number of attempts per minute, but twice the expected goals per attempt, because the shots now come from the low slot instead of the circles. Second, the Red Wings promoted him, from a Compher-Copp third line at 12:29 a night to a Finnie-DeBrincat second line at 15:29, with more third-period and close-game minutes, against slightly harder competition and with no zone-start shelter either year. Third, the puck started going in: his line shot 1.7% at 5v5 last October and shoots 13.2% now, and his goalies stopped 79% behind him then and 98% now. His on-ice expected-goal share was already first on the team last October. It is first on the team again. The difference is that last year's version only looked that good while Detroit was chasing games, and this year's holds up with the score tied.

A good headline framing: last October's box score lied about him. This October's flatters him. The player in between is a real top-six winger, and the proof is the shot map, not the plus-minus.

## The six things the box score cannot see

Mark's title says Top-6. The data gives six improvements that fit that pun if he wants it. Ranked by how much of the production jump they explain.

### 1. Same shot volume, different ice

{{chart:c1_shotmap}}

He attempts the puck at the same rate he did last year. Where he attempts it changed completely.

| Individual shooting (all situations) | 2025-26 first 10 | 2026-27 first 10 |
|---|---|---|
| Shot attempts per 60 | 18.3 | 17.8 |
| Shots on goal per 60 | 7.7 | 9.7 |
| Unblocked attempts (MoneyPuck) | 25 | 40 |
| Expected goals on those attempts | 1.47 | 3.97 |
| Expected goals per attempt | 0.059 | 0.099 |
| Average shot distance | 31.5 ft | 24.5 ft |
| Attempts from inside 25 ft | 40% | 63% |
| Attempts worth 0.10 xG or more | 3 | 16 |
| Tips / backhands | 3 / 1 | 8 / 4 |
| Rebound attempts (share) | 8% | 15% |

NHL Edge agrees from a different data source. Shots on goal from the low slot: 3 last season (17th percentile) against 11 this season (94th). High-danger shots on goal: 3 of 20 last season, 12 of 24 this season. MoneyPuck's league table puts his xG per unblocked attempt at the 3rd percentile among forwards last season (full 14 games) and the 81st percentile this season. His individual xG per 60 at 5v5 went from 0.76 to 1.47 in our sample; MoneyPuck's version of the same number is 0.58 (22nd percentile) to 1.43 (98th).

So-what: he did not become a volume shooter. He stopped shooting from the perimeter. Goals are at 2 on 3.97 expected, so the goal total is not inflated; if anything he is owed one.

### 2. The promotion: minutes, linemates, trust

{{chart:c2_deployment}}

{{chart:c6_linemates}}

| Deployment | 2025-26 first 10 | 2026-27 first 10 |
|---|---|---|
| Time on ice per game | 12:29 | 15:29 |
| 5v5 time per game | 11:02 | 13:43 |
| Shifts per game / average shift | 17.4 / 43 s | 20.8 / 45 s |
| Share of his minutes in the 3rd period | 30.5% | 34.7% |
| Last 5 min of regulation in a one-goal game | 0:22 per game | 0:57 per game |
| Most-used 5v5 linemates | Compher 75 min, Copp 54 | Finnie 90, DeBrincat 82 |
| 5v5 time beside Detroit's three most-used forwards | 24% | 38% |
| 5v5 time against the opponent's three most-used forwards | 30% | 34% |
| Against the opponent's top pair | 35% | 39% |
| Offensive-zone starts, O/(O+D) | 50.6% | 53.1% |
| Share of Detroit's power-play time | 23% | 25% |
| Penalty-kill time | 0:04 per game | 0:04 per game |

The zone-start line matters: he is not being sheltered in either year. His faceoff starts are a near-even three-way split both seasons (39-38-37 O-D-N last year, 43-38-48 this year). The competition got a touch harder, not easier. The power-play role is the same second unit with about a quarter of Detroit's man-advantage time; it is the 5v5 role that changed.

Among the ten 2026-27 games, his two lowest-TOI nights were the opener (9:39) and the Ottawa game (12:37). Everything since Oct 9 is 14:18 or more. Last October he never reached 15 minutes and his last game before the assignment was 6:37 against St. Louis.

### 3. The process was already elite; now it survives a tied game

{{chart:c5_team_strip}}

{{chart:c3_scorestate}}

| 5v5 on-ice | 2025-26 first 10 | 2026-27 first 10 |
|---|---|---|
| Shot-attempt share (CF%) | 59.3% | 60.2% |
| Expected-goal share (xGF%) | 61.0% | 63.2% |
| xGF / xGA per 60 | 2.59 / 1.66 | 3.38 / 1.97 |
| Detroit's xGF% with him on the bench | 46.3% | 47.0% |
| Rank in xGF% among Red Wings skaters, 60+ min | 1st of 18 | 1st of 16 |
| xGF% with the score tied | 52.4% | 64.8% |
| xGF% while leading | 42.7% | 71.1% |
| xGF% while trailing | 85.9% | 60.0% |
| Share of his 5v5 time trailing / tied / leading | 26 / 33 / 41 | 41 / 38 / 21 |

Last October's 61% was built on 2.36 xG for and 0.39 against in trailing minutes, when every team pushes. With the score tied he was a coin flip. This year the tied-score number is 65% and the leading number is 71%, which is the shape of a line that drives play rather than one that rides score effects. Cross-check: HockeyStatCards' independent NST-based log has him at 62.7% xGF for 2026-27 and the same 10 goals for, 1 against; their player card rates him 96th percentile in Game Score, 93rd in both Offense and Defense.

MoneyPuck's full-season league percentiles for on-ice xGF% among forwards: 93rd last season (14 games), 94th this season. Relative to teammates: 98th and 97th. He was a play-driver last year too. Nobody noticed because of item 4.

### 4. The finishing environment flipped

{{chart:c4_goals_vs_xg}}

| 5v5 on-ice results | 2025-26 first 10 | 2026-27 first 10 |
|---|---|---|
| Shots for / against | 59 / 29 | 76 / 45 |
| Goals for / against | 1 / 6 | 10 / 1 |
| Expected goals for / against | 4.8 / 3.1 | 7.7 / 4.5 |
| On-ice shooting % | 1.7% | 13.2% |
| On-ice save % | .793 | .978 |
| PDO | 0.81 | 1.11 |

Luck test, binomial at a league-average 8.2% 5v5 shooting percentage: the odds of one or fewer goals on 59 shots are 4%; the odds of ten or more on 76 shots are 9%. Six or more goals against on 29 shots is a 3% event; one or fewer against on 45 shots is 11%. Both Octobers are tail outcomes, in opposite directions. His plus-minus went from minus-5 to plus-10 (NHL, all situations), and roughly all of that swing is percentages, not play.

The honest split of the 8 points: his two goals came on 3.97 individual xG, so they are earned with room to spare. The six assists sit on top of a line shooting 13%; on a normal shooting percentage the same chances yield about six goals for, not ten, so expect three or four of those assists to have been bounces. He would still be at 5 or 6 points in 10 games, on a second line, which is the real story.

### 5. The puck management got fixed, and the bully stayed

| Puck events (all situations) | 2025-26 first 10 | 2026-27 first 10 |
|---|---|---|
| Hits delivered / per 60 | 32 / 15.4 | 39 / 15.1 |
| Hits absorbed | 19 | 9 |
| Giveaways / per 60 | 10 / 4.8 | 9 / 3.5 |
| Defensive-zone giveaways | 5 | 1 |
| Takeaways | 4 | 4 |
| Blocked shots | 6 | 6 |
| Penalties taken / drawn | 1 / 2 | 1 / 1 |

Hits per 60 are identical; MoneyPuck has him 92nd and 95th percentile among forwards in both seasons. What changed is the cost of the physical game. MoneyPuck's full-season table had his defensive-zone giveaway rate at the 99th percentile last year (worst in the league among forwards with 150 5v5 minutes); this year it is the 23rd. He is also absorbing half as many hits, which usually means the puck is leaving his stick sooner. McLellan's word is "bully" and the numbers support the same bully with cleaner exits.

### 6. All eight points at 5v5

Zero power-play points on about 1:41 of power-play time a night and 2.45 xG for while he was out there on the man advantage. The rookie he is tied with for the points lead, Ivar Stenberg, has 6 of 8 points on the power play. McKenna has 3 of 7 on it. Brandsegg-Nygård is producing in the hardest state to produce in, with 3 primary assists, 3 secondary, 2 goals. That is the part most likely to persist if the percentages normalize.

Rookie leaderboard through Oct 23 (NHL stats API): points 8 (tied 1st, Stenberg in 11 GP), assists 6 (1st), plus-minus +10 (1st, next is +5), hits 39 (1st, next 30), shots 24 (1st per the Athletic). Shooting percentage 8.3%, below the 13.3% rookie-class average, which is more evidence the goals are not a hot streak.

## What did not change

- Skating. NHL Edge top speed 22.1 mph last season, 21.6 this season (44th and 47th percentile). Bursts over 20 mph: 12 in 14 games, 9 in 10 games. Distance per minute of ice is the same; the total distance per game rose only because the minutes did.
- Shot speed. Top shot 87.7 mph last season (67th percentile), 84.3 this season (70th).
- Shot-attempt rate (see item 1).
- Hits rate (see item 5).
- Power-play role (see item 2).

Edge zone time is the one tracking stat that moved: offensive-zone share of his ice 43.0% (64th percentile) to 46.0% (87th), defensive-zone share 40.0% to 36.7% (82nd percentile, where higher percentile means less D-zone time). He did not get faster. He is playing in a better part of the rink.

## Between the samples

Assigned to Grand Rapids Oct 27, 2025 after 9 games (1 assist, 14 shots, 28 hits, 12:27 a night per the team release). AHL: 60 GP, 20-24-44, plus-17; Griffins coach Dan Watson said he was "our best player in the playoffs" (8 GP, 4-4-8). Recalled under emergency conditions in March; 5 more NHL games, no points. Worlds for Norway in May: 5 GP, 3-3-6, scored an OT winner against Denmark. Camp quote (Detroit Hockey Now, Sept 23): "Last year I didn't really expect to make the team for myself. But this year I have a goal to make the team." McLellan at camp: "He's one year stronger, both physically and mentally... I flat-out expect him to play on our team." Two goals in the Sept 22 preseason win in Pittsburgh. Preseason 2025, for contrast, he led the team with 4-3-7 in 7 games and still got sent down after nine regular-season games.

Team context: Detroit started 7-3-0 in his first 10 games last year and 4-3-3 this year. He was on the ice for 1 of Detroit's 19 5v5 goals in the 2025 sample and 10 of 19 in the 2026 sample.

## Suggested shape

1. Cold open on the shot map (chart 1). Two pictures, same player, same number of dots, seven feet apart.
2. The box score (0-1-1 to 2-6-8) and why it undersold him then and oversells him now (chart 4, the luck tests).
3. The promotion, told through the linemates and the late-game minutes (charts 2 and 6). McLellan's "bully" thread runs through here.
4. The process, including the tied-score split that is the real tell (charts 3 and 5).
5. Close on what did not change (speed, shot speed, hits) and the one thing that did (zone time). The player is the same athlete standing in a better place.

## Caveats to carry into the prose

- Ten games each. Everything here is a sample, and the goalie save percentage behind him will regress hardest.
- "First 10 of 2025-26" includes the March 8 game after his recall; the nine-game October version of every number is within rounding of the ten-game version.
- On-ice xG is my own reconstruction from NHL shift charts and play-by-play joined to MoneyPuck shot xG. It matches HockeyStatCards on goals exactly and on xGF% within half a point. The shift charts for Oct 13 and Oct 15 came from the NHL's HTML reports because the API returned nothing for those games.
- Competition and teammate quality are measured within each game: share of his 5v5 seconds spent against (or beside) the three forwards who played the most that night. It is a usage proxy, not Evolving Hockey's model.
- MoneyPuck league percentiles for 2025-26 use his full 14-game season, not the 10-game sample.
- Score-state splits are small (1 to 3.6 xG per cell). Use them as a shape, not a decimal.
- The Athletic piece of Oct 23 (Finnie and Brandsegg-Nygård) was not readable from here; the "leads rookies with 24 shots" line is from its search snippet.

## Sources

NHL API game logs, play-by-play, shift charts and stats REST (rookie and team tables); NHL HTML shift reports TH/TV020090 and 020110; MoneyPuck shots_2025.csv, shots_2026.csv and skaters season tables; HockeyStatCards player 8484794 (2026-27 log and card); NHL Edge skater-detail for 20252026 and 20262027; DetroitRedWings.com assignment release (Oct 27, 2025); Detroit Hockey Now (Sept 23, 2026); The Hockey News (Oct 14, 2026); Heavy (Oct 5, 2026); Detroit Sports Nation (Oct 23, 2026).

## Appendix: game by game

{{table:games}}
