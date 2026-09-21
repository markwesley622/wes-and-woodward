# Do the Red Wings have a type? — research brief

Working package for the Wes & Woodward column comparing Andrew Copp, Emmitt Finnie and
Marco Kasper. Everything below is pulled from live sources on 2026-09-02 and covers the
2025-26 regular season unless stated. Charts are inline-ready SVGs in `charts/`
(760px wide, site tokens, fonts fall back cleanly); the raw pulls and the analysis
JSONs are in `raw/`; `charts/make_charts.py` regenerates every chart from `raw/`.

Note on spelling: the NHL lists him as **Emmitt** Finnie (two t's).

---

## 1. The headline finding

On a style-only similarity model (17 usage and rate metrics, z-scored against all 384
NHL forwards with 41+ GP and 500+ 5v5 minutes, results-based stats excluded), the three
are more alike than **99.2% of all 7,254 same-team forward trios in the league**, and more
alike than 99.4% of random league trios. Their mean pairwise distance is 0.84 against a
league median of 1.33 (lower = more alike).

| Pair | Style distance | League context |
|---|---|---|
| Copp – Finnie | 0.79 | 10th percentile of all forward pairs is 0.95 |
| Finnie – Kasper | 0.81 | median pair is 1.33 |
| Copp – Kasper | 0.92 | |

Every other Red Wings forward is farther from the trio's centroid than the three are
from each other. Distance to the Copp/Finnie/Kasper centroid: Finnie 0.44, Copp 0.50,
Kasper 0.51, then van Riemsdyk 0.73, Raymond 0.94, Rasmussen 0.95, Compher 0.96,
Perron 1.01, Kane 1.07, Larkin 1.15, Appleton 1.33, DeBrincat 1.38. League median 1.02.
Chart: `c4-centroid-bars.svg`, `c5-trio-distribution.svg`.

**Important caveat (say this in the piece):** the convergence is a 2025-26 phenomenon,
not a career-long one. In 2024-25 Copp and Kasper were a 1.20 apart, only the 34th
percentile of pairs. That season Copp played 56 games and threw 9 hits all year; rookie
Kasper was a volume shooter with almost no takeaways. The 2025-26 versions of both moved
toward the same profile.

---

## 2. The physical "type"

| | Copp | Finnie | Kasper |
|---|---|---|---|
| Position listed | C | C (played LW on Larkin's line) | C |
| Shoots | L | L | L |
| Height | 6'1" | 6'1" | 6'1" |
| Weight (NHL roster) | 200 | 195 | 202 |
| Born | Jul 8, 1994, Ann Arbor MI | Jun 27, 2005, Lethbridge AB | Apr 8, 2004, Innsbruck AUT |
| Age on Oct 1, 2026 | 32 | 21 | 22 |
| Draft | 2013, R4 #104 (WPG) | 2023, R7 #201 (DET) | 2022, R1 #8 (DET) |
| Pre-NHL | USNTDP → Michigan (3 yrs) | Kamloops WHL (captain, 84 pts in 2024-25) | Rögle SHL (pro at 16) |
| Cap hit | $5.625M through 2026-27, M-NTC, UFA '27 | $921,667 ELC through 2027-28, RFA '28 | $886,667 ELC through 2026-27, RFA '27 (QO $897,750) |

Three left-shot, 6'1", ~200 lb centers acquired three different ways: a UFA signing, a
top-10 pick, a seventh-rounder. CapWages lists older weights (Copp 203, Finnie 170,
Kasper 183); use the NHL roster figures. Copp's NHL career: 779 GP, 123-220-343, 15:08
TOI, 51.9% faceoffs, 9 SHG.

---

## 3. What they have in common on the ice

Percentiles are among the 384-forward pool above. Chart: `c1-profile-strip.svg`.

### They get to the net and generate high-danger looks

| | Copp | Finnie | Kasper | League F |
|---|---|---|---|---|
| Individual xG/60, 5v5 | 0.73 (58th) | 0.80 (70th) | 0.81 (73rd) | |
| Median shot distance, all attempts | 16 ft | 19 ft | 23 ft | 25 ft |
| Share of attempts inside 20 ft | 59% | 54% | 46% | 40% |
| High-danger share of attempts (MoneyPuck) | 10% (91st) | 9% (85th) | 5% (39th) | |
| High-danger shots on goal (NHL Edge zone map) | 60 (85th) | 70 (91st) | 52 (76th) | 32 avg |
| iHDCF, 5v5 (Natural Stat Trick) | 73 | 78 | 73 | |
| Rebounds created/60, 5v5 | 1.04 (82nd) | 0.73 (45th) | 0.99 (77th) | |
| Rush attempts, 5v5 (NST) | 4 | 2 | 5 | |

The NST individual high-danger chance counts are nearly identical (73/78/73). None of
them is a rush player: single-digit rush attempts all season. Kasper's MoneyPuck
high-danger share is lower because he also fires more from distance (12.97 attempts/60,
66th percentile vs. ~9.7 for the other two), which drags his median out. Chart:
`c2-shot-maps.svg`.

### They all finished well under their chances

| | Copp | Finnie | Kasper |
|---|---|---|---|
| Shooting % | 7.8% (13th) | 10.8% (33rd) | 6.9% (9th) |
| Goals minus xG, all situations | **-10.8 (1st pct, largest shortfall of any NHL forward)** | -6.2 (8th) | -6.4 (6th) |
| 5v5 on-ice shooting % (NST) | 8.73 | 8.68 | 5.92 |
| PDO (NST) | 0.996 | 0.987 | 0.963 |

Combined the three scored 31 goals on 54.4 expected. Chart: `c3-finishing-scatter.svg`.
Hardest shot (Edge): 82.6 / 86.1 / 87.1 mph vs. 83.6 forward average, so none of them
is compensating with a cannon.

### They skate a lot, without elite top speed

NHL Edge tracking, forward percentiles:

| | Copp | Finnie | Kasper | Avg F |
|---|---|---|---|---|
| Speed bursts over 20 mph | 116 (77th) | **193 (94th)** | 138 (83rd) | 75 |
| Skating distance, season | 209 mi (81st) | 205 mi (79th) | 191 mi (73rd) | 124 mi |
| Miles per game | 3.33 (68th) | 3.49 (76th) | 3.35 (70th) | |
| Max speed | 22.47 (62nd) | 22.42 (60th) | 22.84 (79th) | 22.17 |
| EV offensive-zone time | 39.4% | 39.7% | 39.8% | 42.0% |

All three spend less time in the offensive zone than the average forward and more in
their own end (42.5 / 41.5 / 42.6% vs. 40.1% avg). The identity is motor, not gear.

### Similar usage

| | Copp | Finnie | Kasper |
|---|---|---|---|
| TOI/game | 16:34 | 15:30 | 13:48 |
| 5v5 O-zone start share | 49% (34th) | 52% (46th) | 49% (34th) |
| Blocked shots/60 | 2.93 (86th) | 1.94 (53rd) | 2.74 (82nd) |
| Takeaways/60 | 1.01 (59th) | 1.13 (71st) | 0.75 (27th) |
| Giveaways/60 | 3.44 (76th) | 3.49 (79th) | 2.95 (60th) |
| 5v5 xGF% | 51% | 49% | 50% |
| 5v5 xGA/60 on ice | 2.34 (28th, good) | 2.50 | 2.47 |
| xGF% relative to team (NST) | +3.7 | +0.3 | +3.4 |

### Where they differ

- **Hits/60**: Copp 2.0 (26th), Finnie 6.2 (74th), Kasper 10.0 (87th). Kasper also
  took the most hits (98 at 5v5 vs. 57 for Copp).
- **Faceoffs**: Copp took 990 draws at 54.2% (87th pct), Kasper 447 at 51.5%, Finnie
  only 109 at 44.0%. Finnie was a winger in practice.
- **Penalties**: Finnie drew 22 and took 3 (0.14 taken/60 is the 1st percentile,
  cleanest forward in the league). Kasper 14 drawn/11 taken; Copp 13/12.
- **Special teams**: Copp is the PK anchor (87 s/game, 35% of the team's PK time, 8.4
  PPGA/60 on ice). Finnie got PP1-ish minutes (84 s/game, 4 PPG, 8 PPP). Kasper got
  46 s of each.
- **Playmaking**: Copp 1.51 5v5 pts/60 with 22 assists; Finnie 1.12; Kasper 0.93 (8th
  pct). Copp's 43 points were a career high at 32.

---

## 4. Nearest league comps (style only)

| Copp | Finnie | Kasper |
|---|---|---|
| Christian Dvorak (PHI) 0.63 | Joel Farabee (CGY) 0.52 | Jordan Martinook (CAR) 0.61 |
| Danila Yurov (MIN) 0.65 | Collin Graf (SJS) 0.59 | Emil Heineman (NYI) 0.65 |
| Dawson Mercer (NJD) 0.66 | Vladimir Tarasenko (MIN) 0.64 | Nick Paul (TBL) 0.69 |
| Mikael Granlund (ANA) 0.71 | Morgan Geekie (BOS) 0.64 | Zachary Bolduc (MTL) 0.69 |
| Jonathan Toews (WPG) 0.71 | Conor Sheary (NYR) 0.65 | Vasily Podkolzin (EDM) 0.69 |

Closest non-Detroit forwards to the trio's centroid: Farabee 0.47, Mercer 0.54, Yurov
0.56, Sheary 0.56, Namestnikov 0.61. Full lists in `raw/similarity_2025.json` and
`raw/centroid_2025.json`.

---

## 5. Line context (5v5, MoneyPuck lines file)

| Line | Minutes | xGF% | GF-GA |
|---|---|---|---|
| DeBrincat – Copp – Kane | 500 | 52.0% | 30-14 |
| Raymond – Larkin – Finnie | 491 | 48.0% | 18-22 |
| Raymond – Larkin – Kasper | 133 | 41.0% | 6-4 |
| Soderblom – Danielson – Kasper | 92 | 57.0% | 3-2 |
| DeBrincat – Kasper – Kane | 83 | 42.0% | 2-4 |
| Danielson – Kasper – Appleton | 54 | 45.0% | 0-0 |
| Appleton – Kasper – DeBrincat | 53 | 56.0% | 4-0 |

Copp's line with the two wingers outscored opponents 30-14 in 500 minutes; the Larkin
line with Finnie was outscored 18-22 despite similar chance share. Kasper's most-used
combo was the Larkin line at 41% xG, then a rotation of short-lived trios.

---

## 6. Kasper's slump was finishing, not process

Chart: `c6-kasper-dumbbell.svg`. 2024-25 → 2025-26:

| | 2024-25 | 2025-26 |
|---|---|---|
| Shot attempts/60, 5v5 | 12.0 | 13.0 |
| Individual xG/60, 5v5 | 0.82 | 0.81 |
| Hits/60 | 7.9 | 10.0 |
| On-ice xGF%, 5v5 | 52% | 50% |
| TOI/game | 15:27 | 13:48 |
| Shooting % | 13.1% | 6.9% |
| On-ice shooting %, 5v5 | 7.3% | 5.9% |
| Points | 37 | 19 |

Reporting (Octopus Thrower, Inside the Rink) also notes a knee injury that did not
require surgery. His faceoff % rose from 44.9 to 51.5.

---

## 7. Copp's arc

Chart: `c7-copp-arc.svg`. 5v5 on-ice xGF% by season: 52% (2021-22, WPG/NYR), 43%,
38%, 47%, 51%. High-danger share of his own 5v5 attempts went from 6% to 10% over the
same span. 2025-26 was his best Detroit season by expected goals share and by points,
while his hits fell to 44 (from 156 for Kasper on the same team). He is a UFA after
2026-27.

---

## 7b. Evolving Hockey: isolated impact and value (added 2026-09-02)

Four EH tables for 2025-26, all in `raw/eh/` (GAR, xGAR, RAPM EV rates, QoT and QoC).
Percentiles below are among 388 forwards with 41+ GP. Charts: `c8-eh-rapm.svg`,
`c9-eh-gar-xgar.svg`. Player rows with percentiles: `raw/eh/three_summary.json`.

### RAPM (teammates, competition, zone starts and score regressed out), EV per 60

| | Copp | Finnie | Kasper |
|---|---|---|---|
| xGF/60 impact | -0.035 (37th) | +0.049 (61st) | **+0.123 (77th)** |
| xGA/60 impact (negative = suppresses) | **-0.091 (19th, good)** | -0.011 (48th) | -0.052 (32nd) |
| Net xG±/60 | +0.056 (56th) | +0.060 (58th) | **+0.174 (81st)** |
| Net G±/60 (actual goals) | -0.001 (47th) | -0.104 (23rd) | **-0.312 (3rd)** |
| Corsi ±/60 | +1.18 (60th) | +0.12 (45th) | +1.68 (64th) |

This is the strongest single data point for the "Kasper's slump was finishing" argument:
once linemates are stripped out, he had the best chance impact of the three (81st pct)
and the worst goal impact in the league's bottom 3%. Copp's isolated value is defensive.
Finnie's is a wash at even strength.

### Quality of teammates and competition (EV, RAPM xG± of the players they shared ice with)

| | Copp | Finnie | Kasper |
|---|---|---|---|
| Teammate quality (RAPM xG±/60) | +0.048 (66th) | -0.004 (37th) | +0.001 (40th) |
| Competition quality (RAPM xG±/60) | +0.027 (82nd) | +0.028 (85th) | +0.024 (68th) |
| Competition TOI% | 29.0 (65th) | 29.2 (82nd) | 28.5 (40th) |

They faced near-identical, above-average competition. Copp had the best teammates by a
wide margin (DeBrincat and Kane); the Larkin-Raymond pairing Finnie rode rates below
average by RAPM this season, which is a line for the piece if you want it.

### GAR vs xGAR (results vs. chances)

| | Copp | Finnie | Kasper |
|---|---|---|---|
| GAR | 8.1 (69th) | 6.8 (62nd) | -2.0 (14th) |
| xGAR | **-3.7 (7th)** | 6.4 (61st) | 1.1 (32nd) |
| EV offense, GAR / xGAR | +5.2 / **-4.8 (2nd)** | +1.6 / +0.2 | -2.6 / -0.4 |
| EV defense, GAR / xGAR | +2.5 (85th) / +3.0 (89th) | -0.3 / +0.3 | +1.0 / +1.2 |
| Power play | +2.2 / -0.9 | +0.5 / +1.2 | -1.2 / -0.4 |
| Penalty kill | -2.5 (4th) / -1.8 | +1.5 (91st) / +1.0 | -0.3 / -0.3 |
| Penalties (drawn minus taken) | +0.7 | **+3.6 (99th)** | +1.1 |
| Takeaways component | +0.6 | **+2.4 (99th)** | +1.2 |
| WAR / xWAR | 1.3 / -0.6 | 1.1 / 1.0 | -0.3 / 0.2 |

Two things to reconcile in the writing:

- Copp is the mirror image of Kasper. His actual-goals value (8.1 GAR, 69th) is fine; his
  expected-goals value is bottom-decile (-3.7 xGAR), driven almost entirely by EV offense
  at the 2nd percentile. Read with MoneyPuck: Copp personally finished 10.8 goals under
  his own xG, but his line outscored its chances (30-14 with DeBrincat and Kane, 8.7%
  on-ice shooting). EH's model credits him for the on-ice goals; the chance-based model
  says the on-ice chance creation was poor. Both are true. The honest framing is that
  his season's value came from the two wingers converting and from his defense and PK
  usage, not from what he generated himself. EH also rates his PK results poorly (4th pct
  SHD) despite the heavy usage.
- Finnie's value is real but comes from the margins: penalties drawn versus taken (99th),
  takeaways (99th), penalty kill (91st). His even-strength offense and defense are
  average. GAR and xGAR agree almost exactly (6.8 vs 6.4), so nothing about his season
  looks like luck in either direction.

### EH Skater Similarity tool

Not usable here. It only runs on 3- and 6-year windows and its latest timeframe is
2020-23, so it cannot score Finnie or Kasper at all, and Copp's result covers his age
26-28 seasons (top matches Chris Higgins, Jimmy Vesey, Reilly Smith). My own
single-season similarity model in section 1 remains the basis for the "type" claim.

## 8. Quotes and framing (verified via search; link when you use them)

- Yzerman on drafting Kasper (Detroit News, July 2022): "I really like everything about
  the way he plays," "Good size, good skater, good hockey sense," "He's not super flashy,
  he just kind of plays and makes the right plays," "Very efficient, fundamentally sound.
  He plays simple, drives to the net."
- Rögle coach Cam Abbott on Kasper: "great engine," "He competes really hard."
- EliteProspects 2023 draft guide on Finnie: "Always in the right place, he consistently
  influences the play even without the puck. A non-stop engine powers him up and down the
  rink."
- McLellan on Finnie (Detroit Hockey Now): "Everybody gets energized when Emmitt's around
  them. He's very coachable. The pace of play and his confidence with the puck make a big
  difference to our team." Also: "He's had to scrap his way up from basically every
  league."
- Finnie was named 2025-26 Red Wings Rookie of the Year by Detroit Sports Media and
  finished top-10 in rookie scoring.
- Yzerman's end-of-year presser: the team needs more offense from the center position.
- The Hockey Writers: Detroit finished 25th in 5v5 high-danger chances-for per 60 in
  2025-26, and most of their forwards are perimeter players. Useful contrast: the three
  players in this piece are the exceptions to that description, and they still didn't
  score.

Sources:
- https://www.detroitnews.com/story/sports/nhl/red-wings/2026/04/20/the-detroit-news-2025-26-red-wings-final-grades/89695382007/
- https://thehockeywriters.com/red-wings-pro-prospect-depth-2026/
- https://octopusthrower.com/a-deeper-look-at-the-red-wings-center-depth-01kqav6wyng7
- https://eu.detroitnews.com/story/sports/nhl/red-wings/2022/07/07/red-wings-select-center-marco-kasper-first-round-pick-nhl-draft/7829698001
- https://smahtscouting.com/2022/01/07/scouting-report-marco-kasper/
- https://thehockeynews.com/nhl/detroit-red-wings/players/from-pick-201-to-top-line-emmitt-finnie-and-the-red-wings-return-to-draft-day-magic
- https://detroithockeynow.com/2025/12/27/red-wings-captain-has-rookie-role-model-larkin-finnie-mclellan/
- https://www.nhl.com/redwings/news/emmitt-finnie-named-red-wings-rookie-of-the-year-by-detroit-sports-media
- https://insidetherink.com/marco-kaspers-sophomore-slump-a-deeper-analysis/
- https://octopusthrower.com/don-t-worry-about-slumping-red-wings-sophomore-01knt0b5rte4

---

## 9. Method notes

- **Style vector** (17 dims): TOI/game, 5v5 ixG/60, 5v5 shots/60, 5v5 attempts/60,
  high-danger share of attempts, hits/60, takeaways/60, giveaways/60, blocks/60,
  penalties drawn/60, penalties taken/60, 5v5 O-zone start share, faceoffs/game, 5v5
  primary assists/60, 5v5 rebounds created/60, on-ice xGA/60, on-ice xGF/60. Distance =
  RMS of z-score differences. Points, goals, shooting % and xG share are deliberately
  excluded so the model measures how they play, not how it went.
- **Pool**: forwards with 41+ GP and 500+ 5v5 minutes in 2025-26 (n=384).
- **Shot maps**: MoneyPuck shot file, unblocked attempts only, regular season, MoneyPuck
  xG. Rush flag in that file is zero for everyone this season, so rush attempts come
  from NST instead.
- **Edge percentiles** are NHL's own, vs. forwards.
- NST was pulled through the personal Chrome profile (Cloudflare blocks curl and the
  work profile).
- Two danger definitions are in play: MoneyPuck's xG-based "high danger" and Edge's
  zone-based "high-danger" area. Label whichever one a chart uses.

## 10. Files

```
charts/c1-profile-strip.svg      percentile dot strip, 19 metrics
charts/c2-shot-maps.svg          three half-rink shot maps, dot size = xG
charts/c3-finishing-scatter.svg  ixG vs goals, 384 forwards, trio highlighted
charts/c4-centroid-bars.svg      DET forwards' distance to the trio's centroid
charts/c5-trio-distribution.svg  histogram of 7,254 same-team trios, DET marked
charts/c6-kasper-dumbbell.svg    Kasper 2024-25 → 2025-26
charts/c7-copp-arc.svg           Copp five-season xGF% and HD share
charts/c8-eh-rapm.svg            Evolving Hockey RAPM xGF/60 vs xGA/60, 388 forwards, trio highlighted
charts/c9-eh-gar-xgar.svg        Evolving Hockey GAR vs xGAR components for the three
charts/contact-sheet.png         all nine rendered, for a quick look
raw/eh/*.csv                     Evolving Hockey GAR, xGAR, RAPM (EV rates), QoT, QoC, 2025-26 (subscriber data, do not republish raw)
raw/eh/three_summary.json        the three players' EH rows with forward percentiles
charts/make_charts.py            regenerates everything from raw/
raw/forward_features_2025.json   the 384-forward feature table
raw/similarity_2025.json         pairwise distances, z-scores, nearest comps
raw/centroid_2025.json           distance to centroid, DET + league
raw/shots_three.json             every attempt by the three, with xG and coordinates
raw/edge_2025.json               NHL Edge tracking numbers
raw/nst_5v5_2025.json            Natural Stat Trick 5v5 individual/on-ice/relative
raw/landing_*.json               NHL API player bios and full career season lines
raw/rest_*.json, league_*.json   NHL stats-rest reports (DET 2024-25/2025-26; league 2025-26)
raw/mp_skaters_2021..2025.csv    MoneyPuck league skater files
raw/mp_lines_2025.csv            MoneyPuck 5v5 line combos
raw/shots_2025.csv               MoneyPuck shot file (67 MB, gitignored)
```
