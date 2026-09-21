# Chris Kreider and the Red Wings — research brief

Working package for the Wes & Woodward column. Everything below was pulled on 2026-09-09,
the day Anaheim put Kreider on waivers. Regular season 2025-26 unless stated. Charts are
inline-ready SVGs in `charts/` (760px, site tokens, same kit as the Copp/Finnie/Kasper piece);
raw pulls and analysis JSONs are in `raw/`; `charts/make_charts.py` regenerates every chart.
Contact sheet: `charts/contact-sheet.png`.

The three questions you asked, in order: (1) is he the Copp/Compher/Arvidsson archetype or a
new dimension, (2) claim him at $6.5M or wait for him to clear, (3) does he fit.

---

## 0. The situation, as of today

| | |
|---|---|
| Reported | Sept 9, 2026, Elliotte Friedman (Sportsnet). Ducks place Kreider on waivers "for the purposes of contract termination," mutually agreed. Kreider approved it. |
| Contract | Final year of the 7-yr / $45.5M deal signed with NYR in Feb 2020. $6.5M cap hit. Signing bonus was paid July 1; $4M salary remains, and he forfeits it on termination. UFA July 1, 2027 either way. |
| If claimed | Claiming team inherits the $6.5M hit ($4M cash). Friedman: he "will not report if claimed somewhere he prefers not to play." A claimed player who refuses can be suspended without pay (Nabokov/Islanders 2011 is the precedent, and it was Detroit he refused to leave). |
| If he clears | Contract terminated, he is a free agent. PHR's read: he can sign for the same $4M cash at a $4M hit, saving a team $2.5M vs the claim. |
| Why Anaheim | Carlsson's $18M x 5 (matched Flyers offer sheet, July 1) plus Gauthier (41 goals, RFA, asking near $15M) with only ~$9.1M of room. Verbeek didn't like the sweeteners trade partners wanted. Termination frees $6.5M. |
| What he wants | East, near family. Boxford, Mass. native; 13 years in New York. Named suitors: BOS, BUF, TBL, CAR (THN); NJD; NYR reunion floated but they lack cap space. |
| Age | 35 (born Apr 30, 1991). Turns 36 in April. 6'3", 232. Left shot, LW. |
| Waiver order | Before Nov 1, claims go in reverse order of last season's standings. Detroit finished 16th of 32 (92 pts, tied with UTA, CBJ and ANA). Eastern teams that pick ahead of Detroit: NYR, TOR, FLA, NJD, NYI and (tie) CBJ. |

Detroit's side of the ledger:

- 41-31-10, 92 points, led the Atlantic on Jan 25, missed by 8. Tenth straight miss. From Jan 24 on: 2.59 goals/game (30th) and 41 5v5 goals (last in the league). Source: NHL.com.
- Larkin asked for a trade June 4 (list: MIN, FLA, VGK, later DAL). Yzerman: "I cannot make any guarantees." Still on the roster as of this week.
- Yzerman moved to senior advisor July 16. No GM yet. Horcoff is running day-to-day and reportedly won't get the job; Lidstrom and Draper are internal names; Peterson (FLA), Kealty (SJS), Yorke and Dellow (CAR) have interviewed. The Labor Day target passed.
- Kane signed in Chicago (2 x $8M, July 23). van Riemsdyk and Perron gone. Arvidsson in (2 x $5M, July 1), Kolesar in.
- Cap: $104M ceiling, $84.46M committed, $19.54M space, no dead money (PHR, Aug). Edvinsson is an unsigned RFA and talks are frozen until a GM is hired; PHR puts his ceiling near Seider's $8.55M.
- Projected lines (THN, Sept 8): Finnie-Larkin-Raymond / DeBrincat-Copp-Arvidsson / Kasper-Compher-Appleton / Mazur-Rasmussen-Kolesar.

---

## 1. The headline

**He is not the Copp/Compher/Arvidsson archetype. He is a different problem: a top-six
power-play specialist whose 5v5 game has already aged out, and whose one elite remaining skill
is the exact one Detroit is about to lose.**

Three findings carry that:

1. **By style he is a top-six winger.** On the 17-dim style model his nearest comps are Bratt,
   Buchnevich, Kane, Verhaeghe, Stamkos, Nugent-Hopkins. His distance to Copp is 1.13 (only the
   26th percentile of all forward pairs, i.e. not especially alike), to Compher 1.33 (dead
   median), to Arvidsson 1.48 (66th, dissimilar). Chart `c5`.
2. **By value he is now exactly their tier.** Evolving Hockey GAR 3.7 (43rd percentile among
   forwards), xGAR 2.1 (40th). Two seasons ago he was 83rd/90th. The whole drop is 5v5 scoring:
   5v5 goals/60 went from the 89th percentile (2021-22) to the 27th (2025-26). Charts `c1`, `c2`.
3. **The net-front power-play skill is still real.** 8 tip/deflection goals, 6th in the NHL
   (he led the league in 2021-22 and 2023-24). PP individual xG/60 2.06, 73rd percentile; EH
   xPPO GAR 3.5, 87th. Detroit's whole net-front presence on the PP last year was Larkin
   (97th percentile) and van Riemsdyk (99th). One is gone and the other asked out. Charts `c3`, `c4`.

4. **The legs explain the split.** NHL Edge: top speed still 82nd percentile, but bursts over
   20 mph per game fell from 3.51 (99th) to 1.25 (68th) in four seasons. He can still get to
   the net; he no longer beats anyone there. Chart `c8`.

The "dimension" answer is therefore yes, but narrow: he brings something the roster does not
have (a 6'3" body that scores on tips from the crease on PP1), and nothing else that the
roster does not already have in Copp-tier quantity.

---

## 2. Is he the archetype? (style vs value)

### Style, 2025-26 (384 forwards, 41+ GP, 500+ 5v5 min)

| Kreider, 5v5 unless noted | Value | Percentile |
|---|---|---|
| O-zone start share | 66% | 86th |
| On-ice xGF/60 | 3.01 | 92nd |
| On-ice CF% | 56% | 90th |
| On-ice xGF% | 54% | 76th |
| Individual xG/60 | 0.76 | 64th |
| Primary assists/60 | 0.63 | 66th |
| Goals/60 | 0.51 | 27th |
| Points/60 | 1.52 | 43rd |
| Shots/60 | 5.50 | 39th |
| Hits/60 | 3.24 | 46th |
| Blocks/60 | 0.94 | 5th |
| Penalties drawn/60 | 0.19 (4 all season) | 0th |
| TOI/game (all) | 17:03 | 67th |
| Game score/game | 0.74 | 74th |

Anaheim used him as a pure offensive-zone top-six winger: 391 minutes with Carlsson and Terry
(58% xGF, 21-18 in goals), another 96 with Gauthier-Carlsson (59%). The line drove play. He
did not block shots, did not draw penalties, did not kill penalties (Quenneville never used him
there; 41 short-handed minutes all year, none of his 13 career SHG).

Style distance from Kreider (lower = more alike; league median pair 1.33):

| Player | Distance | Read |
|---|---|---|
| Jesper Bratt | 0.59 | nearest in the league |
| Pavel Buchnevich | 0.65 | |
| Patrick Kane | 0.68 | 1st percentile of pairs; same usage Detroit just lost |
| Raymond, van Riemsdyk | 0.97 | |
| Kasper, Finnie | 1.03, 1.04 | |
| **Copp** | **1.13** | 26th percentile |
| Larkin | 1.29 | |
| **Compher** | **1.33** | 50th |
| DeBrincat | 1.36 | |
| **Arvidsson** | **1.48** | 66th, i.e. unlike |

Distance to the Copp/Finnie/Kasper centroid from the last piece: 0.95, league median 1.01. He
does not belong to that type.

### Value, Evolving Hockey (percentile among forwards with 41+ GP)

| Season | GAR | xGAR | EVO | PPO | xPPO |
|---|---|---|---|---|---|
| 2018-19 | 15.8 (92nd) | 13.2 (87th) | 95th | 82nd | 79th |
| 2021-22 | 8.3 (73rd) | 25.8 (98th) | 57th | 97th | 15.3 (100th) |
| 2022-23 | 12.1 (86th) | 17.8 (91st) | 70th | 90th | 65th |
| 2023-24 | 12.0 (83rd) | 15.4 (90th) | 83rd | 96th | 8.1 (98th) |
| 2024-25 | 1.3 (28th) | -2.8 (10th) | 44th | 59th | 64th |
| 2025-26 | 3.7 (43rd) | 2.1 (40th) | 70th | 75th | 3.5 (87th) |

The comps, same season:

| 2025-26 | GAR | xGAR | EVO | PPO / xPPO |
|---|---|---|---|---|
| Kreider | 3.7 (43rd) | 2.1 (40th) | 6.2 (70th) | 1.9 / 3.5 (75th / 87th) |
| Copp | 8.1 (69th) | -3.7 (8th) | 5.2 (61st) | 2.2 / -0.9 |
| Compher | 1.7 (32nd) | -0.1 (24th) | 5.5 (64th) | -1.6 / -0.9 |
| Arvidsson (BOS) | 12.9 (88th) | 8.9 (73rd) | 11.7 (93rd) | 1.7 / 1.7 |
| Larkin | 7.0 (63rd) | 7.3 (66th) | 4.5 (57th) | 4.1 / 6.1 (93rd / 95th) |
| Finnie | 6.8 (62nd) | 6.4 (61st) | | |
| Kane | 8.6 (71st) | 5.3 (55th) | 6.7 (73rd) | 1.8 / 0.3 |

Worth saying in the piece: the premise lumps Arvidsson in with Copp and Compher, and last
year's numbers don't support that. Arvidsson's 12.9 GAR in Boston was 88th percentile, on
1.30 5v5 goals/60 and 3.03 points/60. He was a legitimate top-six producer at 33; whether that
survives the move is a different column. Copp's 8.1 GAR sits on a -3.7 xGAR, the same
finishing-luck gap (in the other direction) the last piece found. Compher is what the premise
says. Kreider's 2025-26 value lands between Compher and Copp.

RAPM (EH, EV): Kreider xG±/60 +0.059, Corsi± +3.37 per 60. Copp +0.056 / +1.18. Compher
-0.121 / -3.91. Arvidsson +0.046 / +2.73. His teammates were the best of the four (QoT xG
+0.051), so the on-ice numbers are partly Carlsson.

Evolving Hockey Teammate Tool, 5v5 score-and-venue adjusted (`raw/eh/tmt_kreider_5v5_2025.csv`,
derived splits in `raw/wowy_kreider_2025.json`):

| Teammate | Min together | xGF% together | Kreider without | Teammate without Kreider |
|---|---|---|---|---|
| Carlsson | 574 | 55.0 | 49.2 | 50.2 |
| Terry | 506 | 55.0 | 50.3 | 50.6 |
| McTavish | 146 | 49.6 | 53.5 | 49.6 |
| Gauthier | 133 | 52.8 | 52.9 | 50.5 |

Away from Carlsson, Kreider was a 49% xGF player in 359 minutes. Carlsson away from Kreider
was 50%. Together 55%. That is the Anaheim usage in one row: he made a good line better and
did not carry one on his own. EH relative-to-teammate xG±/60: +0.21 (Copp +0.14, Arvidsson
+0.10, Compher -0.24). EH 5v5 on-ice: 53.5 xGF%, 48-47 in goals, on-ice sh% 9.8 and sv% .885,
so the actual goal share (50.5%) ran below the chance share all year.

---

## 3. What is gone, in rank, goals and odds

House rule: size a rate change three ways (rank, goal-equivalent at his minutes, chance it is noise).

### 5v5 (MoneyPuck, forwards 41+ GP and 500+ 5v5 min)

| Season | G/60 (pct) | ixG/60 (pct) | 5v5 G on xG |
|---|---|---|---|
| 2021-22 | 1.10 (89th) | 0.95 (87th) | 20 on 17.2 |
| 2022-23 | 1.12 (87th) | 0.92 (83rd) | 19 on 15.6 |
| 2023-24 | 0.86 (74th) | 0.94 (90th) | 15 on 16.5 |
| 2024-25 | 0.54 (33rd) | 0.69 (44th) | 7 on 8.8 |
| 2025-26 | 0.51 (27th) | 0.76 (64th) | 8 on 12.1 |

- Chance creation, 2023-24 to 2025-26: 90th to 64th percentile. At his 950 5v5 minutes that is
  2.9 expected goals a season.
- Finishing, same window: 74th to 27th. At 950 minutes, 5.5 goals a season.
- Odds the 2025-26 under-finish is noise: P(8 or fewer on 12.1 xG) = 0.15. One-in-seven. The
  2024-25 gap (7 on 8.8) was P = 0.34. Two straight years below the chances is starting to
  look like a shooter who has lost his release, not a cold streak, but neither year alone
  clears the bar.

### All situations

| Season | SOG/60 | ixG/60 | Goals | xG | G - xG |
|---|---|---|---|---|---|
| 2021-22 | 10.20 | 1.54 | 52 | 38.9 | +13.1 |
| 2022-23 | 9.45 | 1.52 | 36 | 36.8 | -0.8 |
| 2023-24 | 9.58 | 1.51 | 39 | 38.8 | +0.2 |
| 2024-25 | 8.01 | 1.29 | 22 | 24.5 | -2.5 |
| 2025-26 | 6.52 | 1.18 | 22 | 25.1 | -3.1 |

Shot volume is down a third in two years: 65 fewer shots on goal per 1,279 minutes. ixG/60
1.51 to 1.18 is 7.0 expected goals a season at his minutes. The 2021-22 season was +13 goals
over expected (P = 0.98); nothing since has been.

### Power play

| Season | PP min | ixG/60 | G on xG | G/60 |
|---|---|---|---|---|
| 2021-22 | 233 | 4.20 | 24 on 16.3 | 6.17 |
| 2022-23 | 259 | 3.02 | 7 on 13.0 | 1.62 |
| 2023-24 | 271 | 3.06 | 16 on 13.8 | 3.55 |
| 2024-25 | 179 | 3.17 | 6 on 9.5 | 2.01 |
| 2025-26 | 233 | 2.06 | 8 on 8.0 | 2.06 |

PP chance rate fell 3.06 to 2.06 per 60, 3.9 expected goals at 233 minutes, and he finished
exactly to it. Still 73rd percentile among 275 forwards with 50+ PP minutes; league median
PP G/60 among regulars is about 1.5.

### The legs (NHL Edge, pulled through your Personal Chrome; chart `c8`)

| Season | GP | Bursts over 20 mph | Per game | Max speed (pct) | Miles/game (pct) | HD shots on goal (pct) |
|---|---|---|---|---|---|---|
| 2021-22 | 81 | 284 (99th) | 3.51 | 23.19 (93rd) | 3.67 (84th) | 133 (99th) |
| 2022-23 | 79 | 249 (98th) | 3.15 | 23.21 (93rd) | 3.30 (68th) | 125 (99th) |
| 2023-24 | 82 | 185 (93rd) | 2.26 | 23.02 (89th) | 3.61 (81st) | 136 (99th) |
| 2024-25 | 68 | 139 (83rd) | 2.04 | 22.70 (71st) | 3.41 (73rd) | 70 (93rd) |
| 2025-26 | 75 | 94 (68th) | 1.25 | 22.89 (82nd) | 3.13 (60th) | 73 (93rd) |

This is the cleanest number in the package. His top speed is intact: 22.9 mph is still the
82nd percentile of forwards, three tenths off his 2021-22 peak. What is gone is how often he
gets there. Bursts over 20 mph per game fell from 3.51 to 1.25, a 64% drop, from the 99th
percentile to the 68th. The average forward has about 0.92 a game, so he still bursts more
than most; he used to burst four times as much as most. High-danger shots on goal went from
133 to 73 in the same window while the percentile only slid from 99th to 93rd, which tells you
how skewed that stat is, not that the volume held.

Read with the boxcar proxies:

| Season | Hits/60 | Pen drawn/60 (pct) | Giveaways/60 |
|---|---|---|---|
| 2021-22 | 5.58 | 0.28 (4th) | 1.78 |
| 2022-23 | 5.28 | 0.45 (16th) | 1.61 |
| 2023-24 | 3.86 | 0.43 (13th) | 1.13 |
| 2024-25 | 4.16 | 0.16 (1st) | 2.05 |
| 2025-26 | 3.24 | 0.19 (1st) | 3.19 |

He drew 4 penalties all season, hits are down 40%, giveaways nearly doubled. Same story from
three directions: the player who used to beat defenders to the net at speed now gets to the
net by being 6'3" and standing there. That is why the tips survived and the 5v5 goals did not.

### The 2025-26 shape (chart `c6`)

| Stretch | GP | Attempts/gm | xG | Goals | Poisson P |
|---|---|---|---|---|---|
| Games 1-9 (Oct 9 - Nov 6) | 9 | 4.2 | 5.3 | 9 | 0.04 (over) |
| Games 10-56 (Nov 8 - Mar 6) | 47 | 2.8 | 14.1 | 12 | 0.35 |
| Games 57-75 (Mar 8 - Apr 16) | 19 | 3.1 | 5.9 | 1 | 0.02 (under) |

Nine goals in nine games was a 1-in-25 heater on 5.3 xG. The last nineteen were 0 for 3.1 xG
at 5v5 and 1 for 2.8 xG on the PP, a 1-in-50 cold streak on the same chance volume as the
middle of the season. The season number (22) is the two tails cancelling. The honest per-game
chance rate was about 0.30 xG for 66 games, which is a 25-goal pace over 82. Playoffs: 12 GP,
2-5-7, 13 shots, 10:49 to 19:46 a night.

Missed 7 games: hand-foot-and-mouth disease (4) and an upper-body injury aggravated in
Buffalo. The 2024-25 season in New York had the vertigo and back problems.

---

## 4. The dimension: tips, and who Detroit has at the net

Goals on tips and deflections (NHL API shot-type split), with league rank:

| Season | Tip/defl G | Rank | League leader | Share of his goals |
|---|---|---|---|---|
| 2021-22 | 18 | 1st | Kreider | 35% |
| 2022-23 | 12 | 5th | Kuzmenko, Pavelski 15 | 33% |
| 2023-24 | 16 | 1st | Kreider | 41% |
| 2024-25 | 6 | 27th | Tuch 12 | 27% |
| 2025-26 | 8 | 6th | Voronkov 12 | 36% |

43 of his 139 shots on goal (31%) were tips. The two seasons he led the league he was also a
39- and 52-goal scorer, so the tips were on top of a real shot. Now they are the shot: 5 wrist
goals, 6 snap, 1 slap, 2 backhand, 8 tips.

Detroit's entire tip output last season: Raymond 2, nobody else more than 0 among forwards.

Detroit's net-front options on the power play, 5v4, 50+ PP minutes (275 forwards):

| | PP min | ixG/60 (pct) | HD shots/60 (pct) | PP goals |
|---|---|---|---|---|
| **Larkin** | 232 | 3.09 (97th) | 4.91 (96th) | 13 |
| van Riemsdyk (gone) | 127 | 3.72 (99th) | 6.15 (97th) | 7 |
| DeBrincat | 264 | 2.76 (93rd) | 2.73 (70th) | 14 |
| **Kreider** | 233 | 2.06 (73rd) | 2.32 (60th) | 8 |
| Finnie | 109 | 2.06 (73rd) | 3.31 (81st) | 4 |
| Copp | 103 | 1.53 (46th) | 2.92 (75th) | 1 |
| Raymond | 251 | 1.37 (35th) | 1.67 (38th) | 7 |
| Kasper | 61 | 1.16 (25th) | 0.99 (16th) | 1 |
| Compher | 54 | 1.05 (19th) | 0.00 (0th) | 0 |
| Kane (gone) | 204 | 0.95 (14th) | 0.29 (5th) | 0 |
| Arvidsson (BOS) | 131 | 2.27 (81st) | 2.75 (71st) | 4 |

Two things for the piece. Kane played 204 PP minutes on PP1 and scored zero power-play goals
on 3.2 xG, and Octopus Thrower was writing "take Kane off the power play" in-season; that PP1
flank is open. And Larkin was Detroit's net-front: 97th percentile chance rate from the slot,
13 PP goals. The unit was 12th in the league (22.6%) with him there. If the Larkin trade
happens, the only forward left who generated PP1-grade chances from the net is Finnie in 109
minutes.

That is the case for Kreider in one line: he is a 73rd-percentile PP net-front producer on a
team that is one trade away from having none, and it is the one skill on his card that did
not decline to the middle-six band.

The case against, same line: 73rd is not 97th. He would not replace Larkin's PP production; he
would replace the absence of it.

---

## 5. What players like this did at 35 (chart `c7`)

Production comps (MoneyPuck, forwards 2010-2024, nearest 30 at age 33-35 on 5v5 P/60, G/60,
ixG/60, on-ice xGF%, TOI/GP, game score/GP). His inputs: 1.52 / 0.51 / 0.76 / .54 / 17.0 / 0.74.

Nearest: Eberle 2023, Briere 2011, Radulov 2019, Smyth 2010, Justin Williams 2017, Parise
2019, Stastny 2019, Joel Ward 2015, Sharp 2015, Hecht 2010, O'Reilly 2024, Backes 2017,
Reilly Smith 2024, Eric Staal 2018, van Riemsdyk 2022, Hossa 2014, Backlund 2023/24, Kunitz
2014/15, Oshie 2020, Ryder 2013, Steen 2017/18, Franzen 2013, Pavelski 2017, Langkow 2011,
Arnott 2010.

Next season:
- 28 of 30 played again; Radulov and Langkow did not.
- Median 12 goals in a median 70 games. Median change in 5v5 G/60: +0.02 (no change; they
  were already at the floor).
- 5 of 28 reached 20 again (Williams 23, O'Reilly 25, Stastny 21, Pavelski 38, Ward 21).
  12 reached 15. 11 scored under 10.

Base rate, every age-34 forward season since 2010 with 17-27 goals (n = 26): 1 did not play,
median 16 goals the next year, 6 of 25 reached 20, 14 reached 15.

Value comps (EH, age-34 forwards with 50+ GP, 2007-2024, n = 111; his GAR/82 is 4.0):
- Every age 34 to 35 pair: median GAR/82 change -2.8; 31 of 80 did not get a 20-game season
  the next year.
- Same band as him (GAR/82 between 0 and 8, n = 58): 12 of 58 gone, median next-year GAR/82
  0.5, median change -3.8, 30% improved.

So the central projection is a 12-16 goal winger worth about replacement level at 5v5, with
a one-in-five shot at another 20 and a one-in-five shot at falling out of a lineup.

---

## 6. Fit on the 2026-27 roster

**Left wing is the crowded side.** Finnie (1LW), DeBrincat (2LW), Kasper and Mazur are the
projected left wings. Kreider does not displace Finnie or DeBrincat; he displaces Mazur or
pushes Kasper to center, which is where the last piece argued he belongs anyway. Practical
slot: 3LW at even strength, PP1 net front.

**He doesn't fix the 5v5 collapse.** Detroit was last in the league in 5v5 goals from Jan 24
on. Kreider scored 8 5v5 goals in 75 games. That is Compher's number (Compher: 0.63/60). This
is the strongest argument that he is "more of the same" for the part of the season that
actually sank them.

**He does fix the specific hole Kane and van Riemsdyk left, and hedges the Larkin one.** PP1
last year: Larkin (net), Kane and DeBrincat (flanks), Raymond, Seider. Kane's 204 minutes
produced 0 goals; van Riemsdyk's 127 on PP2 produced 7. Kreider on PP1 in Kane's minutes at
his 2025-26 rate is 7 PP goals; at his 2023-24 rate, 12. If Larkin goes, Kreider is the only
body on the roster who has ever done the net-front job at PP1 level.

**Special teams only, or he's a 4th-liner.** He doesn't kill penalties, block shots, or take
draws. If McLellan wants a 3LW who plays 200 feet, that is Mazur or Kolesar, not Kreider. His
value is 3 minutes of PP a night plus 12 O-zone minutes with skilled linemates. In Anaheim that
was Carlsson. In Detroit it would be Copp and Arvidsson, or Kasper and Compher.

**Physical profile is not the type.** 6'3" 232 vs the 6'1" 200 type. Not a center, not a
skater by volume anymore (see §3). He would be the biggest forward on the roster.

---

## 7. Claim, sign, or pass

### The ledger

| | Claim (Sept 10) | Sign after he clears | Pass |
|---|---|---|---|
| Cap hit 2026-27 | $6.5M | Market. PHR frames $4M; the bidding is BOS/TBL/CAR/BUF/NJD, none flush. $2.5M-$4M x 1 is the realistic band | 0 |
| Cash | $4M | Whatever he signs for | 0 |
| Term | 1 yr, UFA July 2027 | 1 yr (he is 35; nobody offers 2) | |
| Cap left after Edvinsson (~$8.5M ceiling) | ~$4.5M | ~$7M-$8.5M | ~$11M |
| Priority | 16 teams ahead, six in the East (NYR, TOR, FLA, NJD, NYI, CBJ) | Open market; DET has the most cap space in the NHL | |
| His consent | Not required, but he said he won't report where he doesn't want to be. Detroit is East but not "near family"; he'd need to want it | Required, and he picks | |
| Who makes the call | Nobody. There is no GM. Horcoff is caretaker and reportedly not the hire | New GM, if hired in time; otherwise Horcoff | |
| Value | 4-GAR player at $6.5M is a ~$1.5M/GAR price; Copp is $5.6M for 8 | 4 GAR at $3M is fair for a PP specialist | |

### The read

- **Claiming is a bad trade with yourself.** You pay $2.5M-$4M of cap and give up the
  right to negotiate to skip a line you are 17th in, for a player who has said he might not
  show, in a week your franchise has no GM to sign the form. A team in Detroit's position
  claims a player when the alternative is losing him to a rival at the same price. The
  alternative here is getting him cheaper, or letting Boston have a 12-goal winger.
- **Signing him after he clears is a Copp-type move at a non-Copp price.** One year, under
  $4M, PP1 net front, 3LW. It is exactly the kind of "fine in the middle six" signing the
  premise complains about, except that the premise is about $5.6M and $5.1M multi-year deals.
  At $3M x 1 the downside is a healthy scratch in March. The upside is 25 goals if the PP
  clicks (his 66-game chance rate last year was a 25-goal pace).
- **It is not a ceiling move, and the numbers say nobody should pretend it is.** Ceiling for
  this roster is Raymond (93rd pct GAR), DeBrincat, and whatever Larkin turns into. A 43rd
  percentile forward at 35 with a 20% chance of another 20-goal year does not change the
  team's top end. It changes one slot on one special-teams unit.
- **The real question in the column is Larkin.** If he stays, Kreider is a luxury: PP2 net
  front, third-line O-zone minutes, $3M. If he goes, Kreider is the only PP1 net-front option
  on the roster, and the same $3M buys the one thing the trade return probably won't.

---

## 8. Suggested structure

1. Cold open on the Nabokov precedent: the last time a veteran refused a waiver claim, he
   refused to leave Detroit. Now Detroit is deciding whether to be the team that claims.
2. The premise: Copp, Compher, Arvidsson, and the "fine" trap. State it, then test it.
3. Style says no (chart `c5`): his comps are Bratt and Kane, not Copp. What Anaheim used him for.
4. Value says yes (chart `c1`): GAR 92nd to 43rd, and where it went (chart `c2`; the 5v5
   ranks with the goal equivalents and the 1-in-7 odds). Then the why (chart `c8`): same top
   speed, a third of the bursts.
5. The one thing left (chart `c3`, `c4`): tips, and Detroit's net-front chart with Larkin at
   the top and Kane at zero.
6. What 35 looks like (chart `c7`): median 12-16, one in five hits 20, one in five is gone.
7. The season in three pieces (chart `c6`): the heater and the freeze, and the honest 25-goal
   pace in between.
8. Claim vs sign vs pass: the ledger, the priority list, the GM vacancy.
9. Land on Larkin: the signing is a hedge on the trade, not a bet on the player.

---

## 9. Method notes and what is missing

- **Style vector** (17 dims) and pool (384 forwards) are identical to the wings-type piece;
  results-based stats excluded. Distances are RMS of z-score differences.
- **Percentiles**: EH ranks among forwards with 41+ GP per season (n 299-395). MoneyPuck 5v5
  ranks among forwards with 41+ GP and 500+ 5v5 minutes. PP ranks among forwards with 50+ PP
  minutes (n = 275); the 100+ minute pool is only 18 players, so I used 50+.
- **Luck tests** are Poisson on the season xG (the shots-three bootstrap from the last piece
  would give the same answer to two decimals at these counts).
- **Segments** join the MoneyPuck shot file to the NHL game log on game_id; all situations
  including empty-net attempts (he had none that scored).
- **Age comps** reuse the rasmussen `fw_seasons_2010_2025.json` (MoneyPuck forward seasons)
  and the EH all-seasons GAR file; EH ages come from joining on name, so a handful of
  duplicate-name players are dropped.
- **Waiver order** assumes the standard pre-Nov 1 rule (reverse of last season's standings).
  Detroit tied UTA, CBJ and ANA at 92; I have not checked the tiebreak, so "16 ahead" could
  be 15-18.
- **Pulled through the Personal Chrome profile (second pass):** NHL Edge for all five tracked
  seasons (`raw/edge_kreider.json`; the page takes the season in the URL as
  `/skaters/chris-kreider-8475184/20222023/2`, no dropdown needed) and the Evolving Hockey
  Teammate Tool (`raw/eh/tmt_kreider_5v5_2025.csv`). Evolving Hockey GAR, xGAR, RAPM, QoT/QoC
  and the standard on-ice / relative / zones / box tables for 2025-26 were already on disk
  from the Rasmussen, Söderblom and wings-type packages and are the subscriber source for §2.
- **Not in this package:** the Natural Stat Trick player page. It sat behind a Cloudflare
  "verify you are human" checkbox in the Personal profile and that is yours to click, not
  mine. Everything NST would add (5v5 on-ice, relative, zone starts, individual HD chances)
  is covered by the EH tables above; the only NST-specific number missing is his rush-attempt
  count, which was single digits for the Copp trio and would be worth one line here.
- **Not verified:** whether Detroit's 2025-26 PP1 used Larkin or Raymond at the net for the
  full season (the MoneyPuck chance profile says Larkin; beat coverage names Larkin on PP1 and
  Rasmussen on PP2's net front).

## 10. Files

```
charts/c1-value-arc.svg          EH GAR / xGAR percentile 2018-19 to 2025-26
charts/c2-5v5-arc.svg            5v5 G/60 and ixG/60 percentiles 2021-22 to 2025-26
charts/c3-tip-goals.svg          tip/deflection goals by season with league rank and leader
charts/c4-pp-netfront.svg        5v4 ixG/60 vs HD shots/60, 275 forwards, DET + comps labelled
charts/c5-style-distance.svg     style distance from Kreider, DET forwards + the three comps
charts/c6-season-segments.svg    2025-26 in three stretches, goals vs xG per game
charts/c7-age-comps.svg          next-season goals for the 30 nearest age-33-35 comps
charts/c8-edge-bursts.svg        NHL Edge bursts per game + max speed percentile, five seasons
charts/contact-sheet.png         all eight rendered
raw/edge_kreider.json            NHL Edge tracking, 2021-22 through 2025-26
raw/eh/tmt_kreider_5v5_2025.csv  EH Teammate Tool, 5v5 adjusted rates (subscriber data)
raw/wowy_kreider_2025.json       with / without splits derived from the teammate table
charts/make_charts.py            regenerates everything from raw/
raw/kreider_landing.json         NHL bio + every season line
raw/kreider_gamelog_2025*.json   2025-26 regular season and playoff game logs (2024-25 too)
raw/kreider_shottype*.json       shot-type splits by season; tip_ranks.json = league ranks
raw/league_shottype_20252026.json  all skaters' shot-type splits, 2025-26
raw/league_pp_2025.json          NHL PP report, all skaters
raw/kreider_mp_arc.json          MoneyPuck all/5v5/5v4 rates 2021-2025 with Poisson P
raw/kreider_5v5_pcts.json        the 5v5 percentiles table
raw/kreider_segments_2025.json   the three-stretch split
raw/kreider_trend.json           hits, penalties drawn, giveaways 2021-2025
raw/kreider_lines_2025.json      MoneyPuck 5v5 line results
raw/kreider_style.json           nearest comps, z-vector, feature percentiles
raw/eh_ranks.json                EH GAR/xGAR/EVO/PPO percentiles by season, 11 players
raw/age_comps.json               production comps + base rate
raw/gar_age34.json               every age-34 forward season with next-year GAR/82
raw/eh/*_selected.csv            EH GAR/xGAR/RAPM rows for the 12 players, all seasons (subscriber data)
raw/eh/*_2025.csv                EH RAPM / QoT / QoC 2025-26, all forwards (from wings-type)
raw/forward_features_2025.json   384-forward feature table (from wings-type)
raw/mp_skaters_2025.csv          MoneyPuck 2025-26 skaters (from wings-type)
raw/standings.json               final 2025-26 standings (waiver order)
raw/web/sources.md               every article used, with the fact each one carries
```
