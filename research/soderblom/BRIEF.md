# Did Pittsburgh unlock Elmer Söderblom, did Detroit waste him, and was a third-round pick fair? — research brief

Working package for the Wes & Woodward column. All numbers pulled 2026-09-08. Charts are
inline-ready SVGs in `charts/` (760px, site tokens; `charts/make_charts.py` regenerates them
from `raw/`). Sources: NHL API (game logs, schedules, boxscores, play-by-play and shift charts
for all 111 of his NHL games), MoneyPuck (shot-by-shot files 2022-2025, season tables, line
tables), Evolving Hockey (subscriber: GAR, xGAR, RAPM, QoT, split by team), NHL Edge, CapWages,
and a web sweep of Detroit and Pittsburgh coverage (`raw/web/coverage_ledger.md`). The on-ice
splits are an own build from the NHL shift charts, verified line by line against Evolving Hockey's
team-split tables pulled through Mark's subscription (`raw/eh/`, see §10): on-ice goals match
exactly, shot attempts within 1%. Natural Stat Trick was still behind its Cloudflare checkbox at
write time; EH covers everything NST would have added.

Bio: born Jul 5, 2001, Gothenburg. 6'8", 252 lb, left shot, LW. Drafted 2019 R6 #159 (DET).
106 NHL GP, 16-16-32, 11:51 TOI/GP. Age 25 for 2026-27. Contract $1.125M through 2026-27,
RFA with arbitration rights next summer, QO $1.15M, needs waivers.

---

## 1. The verdict in one paragraph

Pittsburgh did not unlock a new player; it unlocked a role and a shooting percentage. The
shooter, the hitter and the skater are the same on both sides of March 6: shot attempts per 60,
hits per 60, giveaways per 60 and skating profile are all within noise of each other in Detroit
and Pittsburgh. What changed is that Pittsburgh dressed him every night (20 of 21 games versus
39 of 63 in Detroit), gave him 12 minutes instead of 10.7, put him on a real line with a
defined job, and his shooting percentage went from 4.8% to 18.5%. His individual expected goals
per 60 rose from 0.69 to 0.88, which is a jump from the league median to the 84th percentile
among forwards (58th to 77th on Evolving Hockey's model): fewer attempts, from closer in. That
is the one genuine piece of "unlock" in the data. It is worth about three expected goals over
82 games at his minutes, and a 20-game stretch that good arises from his Detroit shot profile
by chance roughly one time in six, so it is real enough to write about and too short to bank
on. The rest of the five-goals-on-3.3 burst is finishing, and the shot-level luck test says a
burst that size happens about one time in five on those exact shots. Meanwhile the on-ice numbers moved
the other way: in Detroit the Wings had 51.5% of the expected goals with him on the ice (62nd
percentile, +4.7 relative to the team without him, and every forward he played 100+ minutes with
was better with him than without) but scored 6 and allowed 10, a 3.9% on-ice shooting percentage
and a 0.982 PDO; in Pittsburgh the chance share fell to 48% (39th percentile, below the team
without him) in the hardest zone-start deployment in the league (27% offensive-zone faceoffs, 4th
percentile), and the Penguins scored 14 and allowed 11 with him out there on a 14.9% on-ice
shooting percentage and a 1.035 PDO. So the honest reading is that Detroit had a useful, cheap,
physical fourth-liner producing decent on-ice results and horrendous luck, and it couldn't find
him a lineup spot; Pittsburgh took the same player, gave him a job and a lucky month, and now has
him penciled in as its 12th forward. On
the return: a pick in the 65-80 range becomes a 100-game NHLer about 22% of the time and a
400-game NHLer 12.5% of the time; the base rate for a forward with Söderblom's 2025-26 profile
is 55% to play 60+ NHL games the next season and 25% to reach 30 points. Detroit sold a coin
flip on an NHL regular for a one-in-four lottery ticket, then used the ticket as the fourth
piece in the Faulk trade and missed the playoffs anyway. Fair by the market (Bunting also went
for a third at the same deadline), light by the base rates, and the cost of the decision is
small either way because 11-minute wingers don't decide seasons.

---

## 2. The trade and where the pick went (`raw/web/coverage_ledger.md`)

- **Mar 6, 2026**: Söderblom to PIT for San Jose's 2026 third-round pick. He'd been a healthy
  scratch the previous three games (Feb 28, Mar 2, Mar 4) and had gone 16 games without a point
  since a Dec 20 goal at Washington. Line: 2-1-3 in 39 GP, 10:41.
- **Yzerman, same day**: "Elmer has been in and out of our lineup... We felt like I could get a
  third-round pick for Elmer. Part of our trade with St. Louis was a third-round pick. That had
  some influence in making the decision to move (Soderblom). And we feel we have players that
  if it's in that 13th forward role, we can fill that role from within."
- **Mar 8**: the pick went to STL with Justin Holl, Dmitri Buchelnikov and Detroit's 2026 first
  for Justin Faulk (33, $6.5M AAV through 2026-27). Faulk in Detroit: 17 GP, 5-3-8, 20:15, -5.
  Detroit went 9-15-5 over its last 29 and missed the playoffs for the tenth straight year
  (41-31-10, 92 pts, 6th Atlantic). Pittsburgh finished 41-25-16, 98 pts, 2nd Metro, lost in
  six to Philadelphia; Söderblom played five of the six.
- **Jun 26**: STL moved picks 73 and 76 to TOR for Brandon Carlo. Toronto used No. 73 on
  Zach Olsen (C, Saskatoon, 18-16-34 in 57 WHL games). So the Söderblom pick is now a Leafs
  prospect, three transactions removed.
- "Fill from within" in practice (NHL boxscores, 19 post-trade games): Dominik Shine 14 GP at
  6:44, Carter Mazur 8 GP at 10:42, Sheldon Dries 5 GP at 6:58, Brandsegg-Nygård 5 GP; David
  Perron returned for 16.
- Market comps at the same deadline: Michael Bunting (NSH→DAL) for a 2026 third; Conor
  Garland (VAN→CBJ) for a 2026 third plus a 2028 second.
- **Dubas** (via PensBurgh, March): "the things that have stood out [about] him throughout this
  year have been just really the forecheck. Get in on the forecheck, disrupt pucks, win pucks
  back." Also cited size, age and RFA-2027 contract control.

---

## 3. Career arc (`raw/onice_splits.json`, `raw/eh_soderblom.json`, `raw/nhl/landing.json`)

Percentiles vs NHL forwards: on-ice and rate stats among 441 forwards with 300+ 5v5 minutes
in 2025-26 (MoneyPuck table); GAR/60 among forwards with 150+ minutes that season (Evolving
Hockey). Chart: `c6-eh-gar.svg`.

| Stint | GP | TOI/GP | 5v5 TOI/GP | PP share | G-A-P | 5v5 P/60 (pct) | EH ixG/60 (pct) | EH on-ice xGF% (pct) | on-ice GF-GA | PDO | GAR (pct) | xGAR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022-23 DET (age 21) | 21 | 12:04 | 10.8 | 18.6% | 5-3-8 | 2.13 | – | 55.3 (85th) | 12-12 | 1.001 | +4.1 (97th) | +3.9 |
| 2024-25 DET (23) | 26 | 13:22 | 12.0 | 11.6% | 4-7-11 | 1.92 | – | 48.1 (36th) | 15-12 | 1.020 | +1.6 (59th) | +1.0 |
| 2025-26 DET (24) | 39 | 10:41 | 10.4 | 1.4% | 2-1-3 | 0.44 (3rd) | 0.81 (58th) | 51.5 (62nd) | 6-10 | 0.982 (32nd) | -2.0 (11th) | +0.2 (34th) |
| 2025-26 PIT (24) | 20 | 11:57 | 11.1 | 9.9% | 5-5-10 | 2.66 (97th) | 0.92 (77th) | 48.0 (39th) | 14-11 | 1.035 (89th) | +3.2 (94th) | +2.8 (90th) |
| 2026 PO PIT | 5 | 10:45 | 10.6 | 1.5% | 1-0-1 | 1.13 | – | 43.9 | 1-2 | – | – | – |

On-ice percentiles are Evolving Hockey's 5v5 tables (score-and-venue adjusted) among forward-team
rows with 150+ minutes that season; 2025-26 rows are team-split. My own build gives the same shape
(DET 51.7% xGF, PIT 49.2%) with MoneyPuck's xG model.

Between the NHL stints: 2023-24 entirely in Grand Rapids (61 GP, 13-16-29), 2024-25 started
there (38 GP, 5-12-17) before a January recall; all 26 of his 2024-25 NHL games came under
McLellan, who was hired Dec 26, 2024. Detroit Hockey Now's Feb 2025 headline was "Soderblom
coming up big for Red Wings." He then re-signed for two years at $1.125M in July 2025 and told
the team site he was "confident offseason work will pay off."

The 2025-26 Detroit line is the odd one: on-ice chance share above team and above league median,
on-ice goals 6-10 on a 3.9% shooting percentage, individual production a 3rd-percentile 0.44
points per 60. GAR punishes the box score (-3.2 even-strength
offense, 3.6th percentile); xGAR, which uses expected rather than actual goals, has him at +0.2,
roughly replacement. The Pittsburgh line is the mirror: +3.7 EVO GAR (99.6th percentile per 60)
almost entirely on goals that outran chances. Small-sample caveat for the piece: of 71
forward-team rows with 25 or fewer games and 150+ minutes this season, seven hit +3.2 GAR.

---

## 4. Question 1: did Pittsburgh unlock anything? (`raw/onice_splits.json`, `raw/luck_test.json`, `raw/edge_soderblom.json`)

Charts: `c1-season-timeline.svg`, `c4-individual.svg`, `c5-finishing.svg`.

**What did not change.**

| 2025-26 | Detroit | Pittsburgh |
|---|---|---|
| 5v5 shot attempts / 60 | 14.2 (77th pct) | 12.7 (61st) |
| Hits / 60 | 9.2 (75th) | 8.7 (75th) |
| Giveaways / 60 (5v5) | 4.3 (90th, i.e. bad) | 4.5 (94th) |
| Penalties drawn / taken | 8 / 6 | 6 / 4 |
| Hits taken | 34 | 17 |
| QoT (linemate F 5v5 TOI/GP) | 11.1 | 11.3 |

He shot the same amount, hit the same amount, turned the puck over the same amount, and played
with the same calibre of teammate. NHL Edge for the combined season: hardest shot 92.7 mph
(91st percentile among forwards, seven shots over 90 mph, 98th-percentile count), top speed
22.2 mph (below median), 90 bursts over 20 mph (66th), skating distance below median. He is a
heavy, hard-shooting, average-speed winger on both teams.

**What changed.**

1. *He dressed.* Detroit: 39 of 63 games. Of the 24 missed, 8 were the undisclosed injury after the Dec 21
   Washington game and at least 9 were healthy scratches (five in October, Nov 28, three
   straight before the trade); the six-game gap Nov 13-22 is ambiguous because he went on IR
   Nov 23 and came off Nov 26, so the true scratch count is 9 to 15. Chart c1 marks Nov 22-24 as
   IR and the rest of that gap as scratches.
   Pittsburgh: 20 of 21, then 5 of 6 playoff games (scratched Game 3, back for Game 4).
2. *He played more.* 10:41 to 11:57; 14.4 to 15.8 shifts a night; 5v5 minutes 17th percentile
   to 27th. Power-play share 1.4% to 9.9%, penalty-kill share 1.6% to 4.6% (second PK unit).
3. *He had a job.* 63% of his Pittsburgh 5v5 minutes were with Acciari and 53% with Dewar, the
   Penguins' forechecking line, in a defined forecheck role Dubas had named in advance. In
   Detroit his most common partner was Rasmussen (54%), then Appleton (36%) and van Riemsdyk
   (36%), on a fourth line McLellan kept reshuffling.
4. *Individual chance quality rose, and this is the real unlock.* 0.69 to 0.88 ixG/60 at 5v5 on
   MoneyPuck's model, median to 84th percentile among forwards; 0.81 to 0.92 on Evolving
   Hockey's (58th to 77th). The league's interquartile range on this stat is only 0.21, so a
   0.18 shift moves a player a long way up the table. Fewer attempts (14.2 to 12.7 per 60),
   from closer in (median unblocked shot 26 ft to 22 ft), with more tips and deflections per
   attempt. Sizing it honestly: at 11 five-on-five minutes a night it is about 2.7 expected
   goals over 82 games, so a 7-goal shooter becomes a 9-to-10-goal shooter. Sample caveat: a
   20-game window is noisy (90% bootstrap interval on the Pittsburgh rate is 0.56 to 1.25), and
   resampling 20 games from his own Detroit game log clears the Pittsburgh rate about 15% of the
   time. Real, and worth a paragraph; not yet proof of a new shot profile.
5. *He scored, and so did everyone around him.* 2 goals on 4.7 expected in Detroit; 5 on 3.3 in
   Pittsburgh. Shooting percentage 4.8% to 18.5%. On-ice 5v5 shooting percentage 3.9% in
   Detroit (six goals for in 408 minutes) and 14.9% in Pittsburgh; PDO 0.982 to 1.035 (32nd to
   89th percentile). With Acciari specifically the Penguins outscored opponents 11-4 on a 48.8%
   expected-goals share.

**The luck test** (200,000 simulations on his actual shot list, MoneyPuck xG per shot):

| Stint | Unblocked shots | Goals | xG | P(that few / that many) |
|---|---|---|---|---|
| 2022-23 DET | 36 | 5 | 4.1 | 0.40 (at least) |
| 2024-25 DET | 69 | 4 | 6.3 | 0.23 (at most) |
| 2025-26 DET | 66 | 2 | 4.7 | 0.13 (at most) |
| 2025-26 PIT | 38 | 5 | 3.3 | 0.21 (at least) |
| Career RS | 209 | 16 | 18.3 | 0.33 (at most) |

Neither stretch is outside chance. The Detroit drought was a one-in-eight cold streak; the
Pittsburgh burst was a one-in-five hot streak. Over his career he is a slightly below-average
finisher on his chances, which for a 6'8" net-front winger is roughly what you'd expect. The
"he found his scoring touch" story is a shooting-percentage story. Worth adding: his last ten
Detroit games produced zero points and 0.7 expected goals total, at 10:27 a night with a 7:29
finale. He was not generating anything by the end either, which is what a player who is being
scratched, reinserted and scratched again tends to look like.

**His own account** (exit interview, TribLive, May 9): "I feel like my game improved when I got
here. Just a fresh start." "It's a mix of (a defined role and confidence). Getting the
confidence and just playing my game without thinking too much. Just feeling the trust from the
organization." That matches the data better than the "unlock" framing does: role and trust
changed, tools didn't.

---

## 5. Question 2: was he utilized properly in Detroit? (`raw/onice_splits.json`, `raw/per_game.json`, `raw/eh_soderblom.json`)

Charts: `c2-deployment.svg`, `c3-onice.svg`, `c9-linemates.svg`, `c10-wowy.svg`.

**The case that Detroit misused him.**

- On-ice chance share was good and Detroit ignored it. In his 39 games the Wings had 51.7% of
  the 5v5 expected goals with him on the ice and 47.0% with him on the bench (+4.7 relative);
  Evolving Hockey's relative-to-teammate xG is +0.31 per 60, 81st percentile among forwards.
  EH's RAPM (which isolates him from linemates and competition) has him at +0.087 xG per 60 in
  Detroit, a positive impact, versus -0.009 in Pittsburgh.
- Every forward he played 100+ minutes with in Detroit was better with him than without (EH
  Teammate Tool, chart c10): Rasmussen 56.7% xGF together vs 42.8% apart, Appleton 52.0 vs
  41.5, van Riemsdyk 56.7 vs 46.7, Danielson 55.0 vs 48.3, Kasper level (51.8 vs 51.9). With
  the top pair he was dominant (Seider 68.1 together vs 54.6 apart; Edvinsson 71.3 vs 50.4);
  with the third pair he was underwater (Chiarot 41.2, Johansson 43.9, Sandin-Pellikka 39.8).
  In Pittsburgh the sign flips: Acciari 48.8 with him vs 52.4 without, Dewar 50.5 vs 49.8.
- What sank the Detroit box score was on-ice luck, not on-ice play: 6 goals for and 10 against
  on 18.4 and 17.3 expected (EH), a .943 save percentage behind him and a 3.9% shooting
  percentage in front of him. That is a 37.5% goals share (14th percentile) on a 51.5% chance
  share (62nd).
- He drew more penalties than he took (8 to 6) and EH credits +0.6 GAR of penalty-drawing in
  Detroit, useful on a team that badly needed power plays.
- He got no power-play time at all (1.4% share, 0:04 a night) despite a 91st-percentile shot.
  As a rookie in 2022-23 he had an 18.6% share and 1:08 a night; in 2024-25, 11.6%. McLellan
  cut it to nothing.
- His defensive component graded well in Detroit (EVD GAR +1.0, 79th percentile per 60) and
  poorly in Pittsburgh (-0.8, 12th); Detroit was getting the safer version of him and still
  scratched him. EH's zone data agrees: Detroit gave him a normal 50% offensive-zone shift-start
  share (43rd percentile), Pittsburgh 23% (3rd).
- The scratches themselves: 9 to 15 healthy scratches in a 63-game window, including three of the
  first six (McLellan, Oct 22: "roster decision, not a message... we want to see it show up
  game after game") and the three straight before the trade. McLellan's public line in March
  about players who were "just jerseys" was widely read as including him. Then he was replaced
  with Dominik Shine at 6:44 a night.
- After a Nov 29 game in Boston McLellan praised him on a line with Danielson and Kasper
  ("Elmer was a factor in the game"), a combination that lasted 12 games at 5v5 per MoneyPuck's
  line table with a 57% xGF. It was not kept together.

**The case that Detroit used him about right.**

- The box score was empty for a reason he controlled: 0.44 points per 60 at 5v5 is the 1st
  percentile among 441 forwards. Even at 54% on-ice xGF, a winger producing nothing himself is
  hard to keep in a lineup that had Perron returning and Kasper/Finnie/Danielson/Mazur pushing.
- His individual chance generation in Detroit was ordinary (0.69 ixG/60, 49th percentile), and
  it collapsed to nothing over his last ten games. The scratches roughly track the cold
  stretches on the timeline chart.
- His zone starts were normal (50% offensive-zone shift starts, 46% of on-ice faceoffs) and his
  competition was soft (opponent forwards averaging 11.8 minutes of 5v5, i.e. fourth-liners):
  Detroit was sheltering him, not burying him. Pittsburgh's deployment was objectively harder:
  27% offensive-zone faceoffs (4th percentile), against opponents averaging 12.6 minutes.
- Chance share above team is not the same as driving play: 51.5% xGF is the 62nd percentile,
  7th of 16 Detroit forwards with 150+ minutes, and his shot-attempt share was below team
  (48.7%, 42nd percentile). He tilted quality, not volume, and he turned the puck over at a
  90th-percentile rate.
- Fourth-line usage is what a fourth-liner gets: 10.4 5v5 minutes is the 17th percentile, but
  his Pittsburgh 11.1 is only the 27th. The difference is 45 seconds a night.

**The honest synthesis.** Detroit's real failure wasn't minutes or zone starts; it was
consistency of opportunity. He was scratched, reinserted, moved between three fourth-line
combinations and given no special-teams role, and his on-ice results (good) were never allowed
to matter more than his goal total (bad). Pittsburgh's "utilization" was mostly that Muse
dressed him 25 straight times with the same two linemates and a stated job. The chance share in
that role was 17th of 18 Penguins forwards and his linemates were slightly worse with him than
without, so it is not as if Pittsburgh found the deployment that makes him drive play; Lizotte,
Acciari and Dewar have three of the four lowest offensive-zone faceoff rates among NHL forwards
(15.0%, 15.1%, 18.7% per EH), and he inherited that. In the
playoffs Muse flipped it: 81% offensive-zone starts with Kindel and Mantha, 55% Corsi, 42% xGF.

---

## 6. Question 3: was a third-round pick fair value? (`raw/draft/pick_value_summary.json`, `raw/age_comps.json`)

Charts: `c7-age-comps.svg`, `c8-pick-value.svg`.

**What the pick is worth** (draft classes 2008-2017, career NHL games to Sept 2026):

| Slot | n | ever plays | 100+ GP | 200+ GP | 400+ GP |
|---|---|---|---|---|---|
| Round 2 | 306 | 74% | 34% | 26% | 15% |
| Round 3 | 300 | 53% | 21% | 15% | 10% |
| Picks 65-80 (No. 73's neighbourhood) | 160 | 55% | 22.5% | 17% | 12.5% |
| Round 4 | 301 | 47% | 17% | 12% | 7% |
| Round 6 (his own slot) | 301 | 31% | 9% | 7% | 4% |

Only 8% of sixth-round picks reach the 106 games he already has. The hits in the 65-80 window
are real (Reilly Smith, Adam Lowry, Guentzel, Point, Cirelli, Adam Fox, Lindell, Gostisbehere)
but they are one pick in eight; 45% never play a game.

**What he is worth** (base rates from 521 forward seasons 2010-2023 matching his 2025-26
profile: age 23-25, 35+ GP, 9.5-13 5v5 minutes, 0.8-1.9 5v5 P/60, 0.5-1.1 ixG/60):

| Next season | Two seasons later |
|---|---|
| 15% no NHL season | 24% no NHL season |
| 55% play 60+ games | 47% play 60+ games |
| median 67 GP, 11.9 5v5 min, 23 pts | median 66 GP, 12.0 min, 22 pts |
| 25% reach 30 pts; 9.6% reach 2.0 P/60 | 23% reach 30 pts |

The typical outcome is exactly what Pittsburgh is projecting: a 12th/13th forward for two more
years at $1.125M and then a cheap RFA. The bloomers in the comp set (Kempe, Eriksson Ek,
Hartman, Stephenson, Cirelli, McCann) are one in ten, and they were almost all higher-pedigree
players getting a real opportunity, not sixth-rounders.

**So:** a 55% chance of an NHL regular next season plus two years of control, against a 22%
chance the pick ever becomes a 100-game player, with a four-year lag. On base rates Detroit
gave up more expected NHL games than it got back. On the market it got the going rate for a
scratched 24-year-old with three points (Bunting, a proven 20-goal scorer, also fetched a
third). The pick then went into a trade for a 33-year-old rental-plus-one who didn't get the
team into the playoffs, and the pick has since become a Toronto prospect. The fairest framing
for the column: the deal was market-fair and process-poor. Detroit valued him as a 13th forward
because it had used him as a 13th forward, and the price reflected the usage rather than the
player.

Contract note for context: his $1.125M runs through 2026-27 with a $1.15M qualifying offer and
arbitration rights, so Pittsburgh's downside is one cheap year. THN's August projection has him
as the 12th forward/Acciari replacement ("competitive camp, but I think he has what it takes");
PensBurgh's pre-camp roster has him on the fourth line with Dewar and Lizotte, competing with
Brazeau and Lapierre among roughly 20 forwards.

---

## 7. What he does well, what he doesn't

- Physical volume is real and consistent: 9.2 and 8.7 hits per 60 (79th/78th percentile), 15.6
  per 60 in the playoffs, plus 14 hits in five playoff games (Last Word count). Takes far fewer
  hits than he delivers in Pittsburgh (17 taken vs 35 given).
- Shot is a genuine weapon that neither team uses on the power play: 92.7 mph hardest shot,
  91st percentile; seven shots over 90 mph in 59 games.
- Chance quality is net-front: median unblocked shot 22-26 ft, 10 tips/deflections of 66
  attempts in Detroit, 7 of 38 in Pittsburgh. Edge has his high-danger shots on goal (29) just
  under the forward average (32) in two-thirds of the minutes.
- Skating is the ceiling: top speed below median, distance below median, bursts 66th
  percentile. He is fine for a fourth line, not for a top nine that needs pace.
- Giveaways are high on both teams (4.2 per 60) with few takeaways (1.0 in DET, 1.5 in PIT).
- Faceoffs irrelevant (29.6% career on 27 draws).

---

## 8. Ceiling, floor, and what to expect in 2026-27

- **Ceiling:** what he was in 2022-23 and the Pittsburgh stretch combined: a 12-minute
  fourth-line winger with 12-15 goals, positive on-ice numbers, second-unit PK, occasional
  second-unit PP net-front. GAR in the +3 to +5 range. About one comp in ten gets there.
- **Base case:** 60-70 games, 11-12 minutes, 20-25 points, GAR around zero. That is the median
  comp and it is what a healthy 12th forward looks like.
- **Floor:** the Detroit version. Scratched into a 45-game season, 8-10 points, waived by
  February. Roughly one comp in six is out of the NHL a year later.
- Shooting regression is the main thing to write into any projection: 18.5% will not repeat,
  and on his career shot mix 5 goals per 20 games needs about 11% on the same volume. Expect
  the goals to halve per game before anything else changes.

---

## 9. Suggested structure for the column

1. Open on the Apr 4-5 back-to-back against Florida (goal and assist, then a goal), eight
   points in his last ten as a Penguin, versus the last 16 Detroit games without a point. Ask
   whether it was the player or the address.
2. "Same player, better shots" section: identical attempt, hit and giveaway rates and Edge
   profile, but chance quality per shot jumped from median to 84th percentile, worth about three
   goals a season at his minutes and about a one-in-six chance of being noise. Chart c4.
3. The luck test: 2 on 4.7 vs 5 on 3.3, P = 0.13 and 0.21. Chart c5. Neither stretch is a
   signal.
4. What Pittsburgh actually changed: dressed him, defined the job, gave him 75 extra seconds.
   Timeline chart c1; Söderblom's own "defined role and confidence" quote.
5. The uncomfortable part for the "Pittsburgh unlocked him" crowd: chance share went from 62nd
   percentile (above team) to 39th (below team), and the goal share went the other way because
   PDO went from 0.982 to 1.035. Charts c2, c3.
6. Detroit's misuse, argued narrowly: not minutes, but the scratch-reinsert cycle, no PP for a
   92-mph shot, and letting a 6-10 on-ice goal line on a .943 save percentage overrule a chance
   share every linemate benefited from. McLellan's quotes; chart c10.
7. The return: pick 73's neighbourhood hits 22% of the time; his comps play 60+ games 55% of
   the time. Bunting comp. The pick's path to Zach Olsen via Faulk. Chart c8, c7.
8. Close on the cost: small either way. He is a 12th forward, and the Wings' collapse was not
   about 11 minutes of Elmer Söderblom. But the process that valued him as a 13th forward
   because it used him as one is the thing worth flagging.

---

## 10. Method notes and gotchas

- **On-ice splits are an own build, verified against Evolving Hockey.** `raw/build_onice.py`
  reads every play-by-play and shift chart (`raw/nhl/pbp/`, `raw/nhl/shifts/`), reconstructs who
  was on the ice each second, classifies strength from skater counts and goalie presence, and
  counts Corsi/Fenwick/goals/faceoffs/hits/penalties/takeaways from the NHL events. Expected
  goals come from MoneyPuck's shot file joined on (game, elapsed second, team). **Bug caught by
  the EH check:** goals (and most stoppage events) are logged at the second a shift ends, so
  on-ice attribution for events must be start-exclusive/end-inclusive; the first draft used the
  TOI convention (start-inclusive/end-exclusive) and credited him with 28-22 on-ice goals in
  Detroit instead of 6-10. After the fix: DET GF-GA 6-10 (EH 6-10), CF-CA 364-379 (EH 363-383);
  PIT 14-11 (EH 14-11), 189-223 (EH 190-225); hits 64/35 (EH 63/35); giveaways 29/17 (EH 29/17);
  offensive-zone faceoff share 46.9% / 28.5% (EH 46.3% / 26.7%). xGF% differs by the xG model
  only (DET 51.7 vs EH 51.5; PIT 49.2 vs 48.0). Zone for faceoffs is computed from x-coordinate
  and `homeTeamDefendingSide`, not the event's `zoneCode`, which is relative to the winner.
- **Percentiles** in the on-ice, zone, individual-rate and PDO claims are Evolving Hockey's own
  5v5 tables (forward-team rows with 150+ minutes, 2025-26 split by team). Chart c2's minute
  percentiles and the league medians still come from MoneyPuck's full-season forward table.
- **Evolving Hockey pulls** (`raw/eh/`): Skater Tables (On-Ice, Box Score, Zones, Relative to
  Teammate; 5v5; 2025-26 regular + playoffs, 2024-25, 2022-23; grouped Team, Season) and the
  Teammate Tool for Söderblom. Shiny inputs are bookmarkable, so each table is a URL
  (`/stats/skater_standard/?_inputs_&std_sk_table=%22On-Ice%22&std_sk_str=%225v5%22&std_sk_group=%22Team%2C%20Season%22&std_sk_toi=%220%22...`);
  the CSV is fetched from `a.shiny-download-link` and POSTed to a local receiver. Teammate Tool
  `_p`/`_t` columns are season totals, not "without"; `raw/eh_wowy_2025.json` derives without as
  total minus together. GAR/xGAR/RAPM/QoT files are the ones downloaded for the Rasmussen
  package the same day (they already carried the DET/PIT split).
- **QoC/QoT** are TOI-weighted averages of opponents' and linemates' season 5v5 TOI/GP from
  MoneyPuck, forwards only. EH's own QoT table (TOI%-based) has the two stints identical
  (27.7% vs 27.7%) but Pittsburgh's linemates with better RAPM (+0.077 vs -0.023).
- **Evolving Hockey** 2025-26 files already contain separate DET and PIT rows (downloaded for the
  Rasmussen package on 9/8; nothing new was pulled). Percentiles are GAR/60 among forwards with
  150+ minutes to make 20-game rows comparable.
- **Draft value** uses `api-web.nhle.com/v1/draft/picks/{year}/all` (no player IDs) joined to
  `api.nhle.com/stats/rest/en/skater|goalie/bios?cayenneExp=draftYear=` on (year, overall);
  anyone absent from the bios tables has 0 NHL games. Classes 2008-2017 so every player has had
  8+ years.
- **Age comps** reuse `rasmussen/raw/fw_seasons_2010_2025.json` (MoneyPuck forward seasons with
  age). Söderblom's own 2025-26 combined row is inside the window on every criterion.
- **Browser:** the NHL Edge page was first read in the work Chrome by mistake; Mark flagged it.
  Personal Chrome (`switch_browser`) is where the EH subscription lives. NST showed its
  Cloudflare checkbox in Personal Chrome too and was not clicked through during this session;
  EH's team-split tables cover the same ground. Edge reports sub-median
  values as "<50th", recorded as 50.
- **Fetch blocks:** Post-Gazette (paywall shell), Last Word and PensBurgh (403 to WebFetch; plain
  curl with a browser UA works and is what `raw/web/` holds). Reddit blocked everything; no fan
  sentiment section.
- MoneyPuck shot-file `game_id` is the 5-digit suffix (20010 = 2025020010); `shooterPlayerId` is
  an integer string in the 2025 file but a float string (`8481725.0`) in older ones.

---

## 11. Files

```
BRIEF.md                              this file
charts/make_charts.py                 regenerates c1-c9 from raw/
charts/c1-season-timeline.svg         2025-26 TOI per team game + cumulative G vs ixG
charts/c2-deployment.svg              DET vs PIT dumbbells: minutes, PP share, oZS, QoC, QoT, shifts
charts/c3-onice.svg                   5v5 CF% / xGF% / GF% on vs off ice, both teams
charts/c4-individual.svg              P/60, ixG/60, iCF/60, hits/60 with percentiles
charts/c5-finishing.svg               goals vs xG by stint with luck-test P
charts/c6-eh-gar.svg                  EH GAR / xGAR by stint with percentiles
charts/c7-age-comps.svg               next-season outcomes for 521 profile comps
charts/c8-pick-value.svg              draft-slot hit rates, picks 65-80 highlighted
charts/c9-linemates.svg               5v5 TOI share by linemate, both teams
charts/c10-wowy.svg                   linemates' xGF% with vs without him (EH Teammate Tool)
charts/contact-sheet.html/.png        QA render
raw/onice_games.json                  per-game on-ice build (111 games)
raw/onice_splits.json                 stint aggregates + percentiles + league medians
raw/per_game.json                     date-sorted per-game timeline
raw/build_onice.py, summarize_onice.py
raw/luck_test.json                    shot-level finishing simulation
raw/mp_shots_split.json               MoneyPuck shot summary by stint
raw/eh_soderblom.json                 EH GAR/xGAR/RAPM/QoT rows + percentiles
raw/eh_standard_2025.json             EH 5v5 on-ice / zones / box / relTM values + percentiles, both teams
raw/eh_wowy_2025.json                 EH Teammate Tool with/without, derived
raw/eh/*.csv                          EH downloads (on-ice 2022/2024/2025/PO, box, zones, relTM, teammate tool)
raw/edge_soderblom.json               NHL Edge 2025-26
raw/age_comps.json                    comp set and outcome summaries
raw/draft/                            picks 2008-2017 (r2/3/4/6) with career GP; summary
raw/nhl/                              landing, game logs, schedules, Faulk, pbp/ (111), shifts/ (111)
raw/web/coverage_ledger.md            every quote and source, dated
raw/web/*.html, raw/lastword.html, raw/capwages.html   raw fetches
```
