# Is Michael Rasmussen really as bad as Red Wings fans think he is? — research brief

Working package for the Wes & Woodward column. All numbers pulled 2026-09-08 and cover
regular seasons only (he has never played an NHL playoff game). Charts are inline-ready
SVGs in `charts/` (760px, site tokens); raw pulls and analysis JSONs are in `raw/`;
`charts/make_charts.py` regenerates every chart from `raw/`. Sources: NHL API, NHL Edge,
MoneyPuck (season files, line files, and the shot-by-shot files 2018-2025), Evolving
Hockey (subscriber: GAR, xGAR, RAPM, QoT/QoC, 2007-2025), CapWages, and a web sweep of
beat coverage and fan forums. Natural Stat Trick could not be pulled (see §12).

Bio: born Apr 17, 1999, Surrey BC. 6'6", 222 lb, left shot, listed C. Drafted 2017 R1 #9
(DET). 454 GP, 66-88-154, 13:56 TOI/GP, 48.1% faceoffs. Age 27 for 2026-27.

---

## 1. The verdict in one paragraph

Fans are right about the thing they complain about most and wrong about the conclusion.
The finishing problem is real and it is not luck: 66 goals on 91.3 expected across seven
seasons, and on his exact career shot mix the chance of scoring that few by variance alone
is about 1 in 2,000. He is one of the worst finishers in the league relative to his chances,
and the worst in his draft class. But "bad" implies below replacement, and he is not that:
Evolving Hockey has him at +13.2 GAR over his career (about +1.9 per season), his defense
and penalty-kill components grade well in most seasons, and in 2025-26 specifically his PK
was elite (94th and 98th percentile on chances against and for) while his even-strength
offense collapsed (5th percentile). He is a replacement-level-plus fourth-line forward with
one genuine specialty, paid $3.2M for two more seasons. The deployment story cuts both
ways: he has had bottom-quartile linemates in every one of his seven seasons and has never
been sheltered into offense, but the numbers also say he produces more on the wing than at
center, and Detroit keeps moving him back to center.

Ceiling: what he was in 2022-23 (GAR 9.3, 82nd percentile; 29 points in 56 games; on-ice
xGF% 58th percentile). That season was cut off by a kneecap injury and was propped up by
on-ice goals (xGAR only 3.7, 56th percentile). Floor: what he was in 2025-26 (GAR -0.7,
22nd percentile; 14 points; 6th-percentile 5v5 points/60). Base case for 27-28 from his
comps: a small bounce toward +0.5 to +2 GAR per 82, a 1-in-4 shot at a real jump, a 1-in-7
chance he is out of a regular NHL role.

---

## 2. What fans think (`raw/web/fan_sentiment.md`)

Caveat for the piece: Reddit blocked every fetch, so the r/DetroitRedWings quotes are verbatim
search-index snippets with approximate dates; the sample skews to high-engagement extremes.
Treat it as a map of the arguments, not a poll. Recurring critiques, most common first:

1. "6'6 and plays small" / soft / doesn't use his size. The single most common complaint
   across every season. "A soft giant that refuses to use his size, doesn't win faceoffs,
   and can't hang onto pucks" (Jan 2025).
2. No hands / can't produce / "empty-net merchant". Thread title, Jan 2026: "Noted sniper
   Rasmussen scores the Wings first SHG in 78 games."
3. Bust / didn't justify #9. "Doesn't have the offensive skillset to ever justify his draft
   position" (~Jul 2026).
4. "Just a jersey" / detriment (2025-26 nadir). "27 has looked absolutely useless the past
   few games. Worse than just a jersey, feels like he's a detriment" (Mar 2026, 80 votes).
5. Overpaid at $3.2M / trade him / buy him out / send him to Grand Rapids.
6. "Always hurt in March" (factually: late-season injuries in 2019, 2023, 2024, 2026).

Recurring defenses: hard minutes, PK and forecheck ("a really good defender who gets asked
to handle some REALLY hard minutes", Jan 2025); "used as a defensive forward with one of
the highest defensive zone starts on the team" (Mar 2026); "a really good grinder, that's
not the same as checking/hitting" (Apr 2026). Sentiment arc: peak 2022-24 ("most
underrated", "Four more years of THE MOOSE" at the Feb 2024 extension), turned in 2024-25,
bottomed in 2025-26.

Media grades: The Hockey Writers D+ (2024-25) and D (2025-26: "29th-worst Offensive Rating
among NHL forwards", "awful zone exit numbers", led DET forwards in blocks). Detroit Hockey
Now D (2025-26), "experiment has run its course" (Oct 2025). At signing, ClutchPoints
graded the contract B and THW called it "tremendous value". No Athletic/Luszczyszyn card,
JFresh card or HockeyViz card was findable.

---

## 3. Career arc (`raw/mp_rasmussen_arc.json`, `raw/eh_rasmussen.json`, `raw/nhl/rasmussen_career_table.json`)

Percentiles are among NHL forwards: MoneyPuck 5v5 rates among forwards with 300+ 5v5
minutes; Evolving Hockey among forwards with 20+ GP. Chart: `c1-career-arc.svg`,
`c12-gar-xgar.svg`, `c7-rolling.svg`.

| Season | GP | TOI/GP (PP / SH) | G-A-P | 5v5 P/60 (pct) | 5v5 ixG/60 (pct) | GAx all-sit | 5v5 xGF% (pct) | GAR (pct) | xGAR (pct) |
|---|---|---|---|---|---|---|---|---|---|
| 2018-19 | 62 | 12:05 (1:48 / 0:00) | 8-10-18 | 1.06 (18) | 0.53 (17) | -1.7 | .453 (16) | -0.2 (25) | -1.2 (17) |
| 2019-20 | 0 | AHL Grand Rapids, 35 GP 7-15-22; back injury Nov-Jan | | | | | | | |
| 2020-21 | 40 | 14:48 (2:16 / 0:35) | 3-9-12 | 1.03 (15) | 0.57 (34) | -4.5 | .414 (3) | 0.9 (38) | -5.5 (1) |
| 2021-22 | 80 | 14:31 (0:53 / 1:14) | 15-12-27 | 1.31 (30) | 0.73 (59) | -1.6 | .435 (10) | 0.7 (34) | 0.5 (35) |
| 2022-23 | 56 | 15:06 (0:31 / 1:41) | 10-19-29 | 1.83 (64) | 0.79 (62) | -4.9 | .508 (58) | 9.3 (82) | 3.7 (56) |
| 2023-24 | 75 | 15:11 (0:09 / 1:47) | 13-20-33 | 1.61 (52) | 0.72 (53) | -2.7 | .458 (26) | 2.0 (44) | 1.7 (40) |
| 2024-25 | 77 | 13:25 (1:04 / 0:49) | 11-10-21 | 0.90 (9) | 0.80 (72) | -6.0 | .487 (40) | 1.2 (33) | -1.2 (19) |
| 2025-26 | 64 | 12:39 (0:14 / 1:22) | 6-8-14 | 0.88 (9) | 0.65 (40) | -3.9 | .476 (33) | -0.7 (22) | 0.1 (30) |

Career: GAR +13.2, xGAR -1.9. Reading: a slow climb from a 19-year-old who should not have
been in the NHL (2018-19) to a legitimate middle-six season at 23 (2022-23), a decent
follow-up at 24, then two seasons of decline in which the chance generation held up
(ixG/60 72nd percentile in 2024-25!) but nothing went in, and then in 2025-26 the chance
generation slid too. Note the 2022-23 peak was the one season where on-ice shooting broke
his way: GAR 82nd percentile but xGAR only 56th.

Rolling 20-game view (`raw/rolling20.json`): his production peaked in the Nov 2022-Feb 2023
stretch, held through 2023-24, and then the slide is continuous from Oct 2024. There is no
single cliff.

Same season, production by calendar (`raw/per_game.json`):

| Window | GP | TOI/GP | G | P | P/60 | ixG/60 |
|---|---|---|---|---|---|---|
| 2022-23 through the Feb 25 kneecap injury | 56 | 15.1 | 10 | 29 | 2.06 | 1.06 |
| 2023-24 Oct-Dec | 37 | 15.4 | 7 | 15 | 1.58 | 0.88 |
| 2023-24 Jan-Apr | 38 | 15.0 | 6 | 18 | 1.89 | 0.77 |
| 2024-25 before the Feb 23 Zegras hit | 56 | 13.3 | 9 | 16 | 1.29 | 0.95 |
| 2024-25 after return | 21 | 13.7 | 2 | 5 | 1.04 | 1.00 |
| 2025-26 Oct-Nov 19 (pre-IR) | 18 | 11.6 | 2 | 5 | 1.44 | 0.92 |
| 2025-26 Dec 3-Mar 11 | 39 | 13.3 | 2 | 6 | 0.69 | 0.56 |
| 2025-26 Mar 12-Apr (leg) | 4 | 10.6 | 0 | 0 | 0.00 | 0.22 |

---

## 4. External factors (`raw/web/injuries_and_transactions.md`, `raw/det_team_context.json`)

### Injuries
No surgery since the 2017 broken wrist (WHL, draft year). Everything since has been
soft-tissue, impact or shot-block injuries, none of them the kind that changes a player:

| Date | Injury | Missed |
|---|---|---|
| Jan-Feb 2019 | hamstring (IR, GR conditioning stint) | 10 |
| Mar 2019 | upper body | last 8 |
| Nov 2019-Jan 2020 | back, while in Grand Rapids | 23 AHL games; 0 NHL GP that season |
| Feb 25, 2023 | kneecap, blocked shot | last 24 of his best season |
| Apr 1, 2024 | upper body | last 7 |
| Feb 23, 2025 | head/upper body (Zegras hit, 3-game suspension to Zegras) | 4 |
| Nov 20-Dec 3, 2025 | undisclosed (IR) | 3 |
| Mar 12-Apr 4, 2026 | leg, shot block | 9 |
| Apr 7, 2026 | same leg, Werenski shot | last 4 |

What the data says about them: the kneecap did not derail him (his 2023-24 was nearly as
good per 60 as the season it interrupted); the Zegras hit did not cause the 2024-25
decline (he was already at 1.29 P/60 before it, versus 1.83 the prior year); and the 2025-26
collapse happened in the healthy Dec-Mar stretch, when he was playing more (13.3 min), not
less. The honest read is that injuries cost him games and a couple of strong finishes to
seasons, but they do not explain the trend. The fans' "always hurt in March" line is true
as a pattern (four late-season injuries) and irrelevant to the quality question.

### Team context
Detroit was a bottom-third 5v5 xG team in all seven of his seasons and never better than
21st (2025-26). Team 5v5 save percentage ranked 26th-28th in 2021-22 through 2023-24, his
prime. That environment depresses on-ice goal share and plus-minus (career -50) more than
it depresses his own finishing, which is measured shot by shot.

| Season | DET 5v5 xGF% (rank) | 5v5 sv% (rank) | PDO |
|---|---|---|---|
| 2018-19 | .449 (31/31) | .918 (16) | .997 |
| 2020-21 | .453 (28/31) | .921 (9) | .993 |
| 2021-22 | .462 (28/32) | .908 (28) | .992 |
| 2022-23 | .467 (25/32) | .904 (27) | .989 |
| 2023-24 | .459 (28/32) | .907 (26) | 1.009 |
| 2024-25 | .478 (26/32) | .914 (11) | .996 |
| 2025-26 | .488 (21/32) | .905 (17) | .985 |

### Coaching and role churn (`raw/web/coach_and_media_usage.md`)
Three head coaches (Blashill through 2021-22, Lalonde to Dec 26 2024, McLellan since) and
at least six distinct roles: PP net-front rookie (2018-19), 2C/3C (2020-22), checking
center late in games under Lalonde (2022-23), checking wing on the Copp-Fischer "identity
line" plus stints on Larkin's line (2023-24), 4th line/wing with occasional PP (2024-25),
then a 2025-26 season with two healthy scratches (Oct 25-26) and a partial move back to
center (31 games with 5+ faceoffs). McLellan, verbatim: "A little bit of a utility guy...
the real positive is his contribution on the penalty kill" and "He's probably never going
to score 40, but he's going to get you 10 or 12 consistently." Lalonde at extension time
(Feb 22, 2024): "Last month alone, he centered a quality fourth line, he's been on a
checking line, we put him on our top line to give us a spark."

Front-office context for the piece: Yzerman stepped down to senior advisor July 15, 2026;
the GM search was still open on Sept 8 (Horcoff interim). Bultman named Rasmussen a trade
candidate on Apr 27; no move has been made. Larkin has also requested a trade.

---

## 5. Finishing: the real problem (`raw/mp_shots_rasmussen.json`, `raw/luck_test.json`, `raw/empty_net_goals.json`)

Charts: `c2-goals-vs-xg.svg`, `c3-danger-conversion.svg`, `c4-luck-test.svg`.

All situations, MoneyPuck season files: 66 goals on 91.3 xG, -25.3 over seven seasons.
Every season is negative: -1.7, -4.5, -1.6, -4.9, -2.7, -6.0, -3.9. Among the 30 skaters
taken in the 2017 first round this is the worst GAx by a wide margin (next worst Hischier
-14.8 on four times the volume; Makar +39.4, Pettersson +45.0).

**Luck test.** Shot-by-shot, non-empty-net, unblocked attempts 2018-2025: 859 attempts,
79.8 xG, 53 goals. Simulating his exact shot mix 20,000 times, he scored 53 or fewer in 1 run
in 20,000; the normal approximation (z = -3.27, one-tailed) gives about 1 in 2,000. Say
"about 1 in 2,000" in the piece (the conservative figure; the chart uses it too). Either
way this is a skill deficit, not variance. It is the single most important number in
the package: the fans' "no hands" is quantitatively correct.

**Where it goes wrong.** Conversion per unblocked attempt by MoneyPuck danger bucket
(career, him vs league forwards):

| Bucket | Attempts | Goals | His conversion | League forwards |
|---|---|---|---|---|
| Low danger (xG < .08) | 496 | 19 | 3.8% | 3.8% |
| Medium (.08-.20) | 268 | 19 | 7.1% | 12.7% |
| High (≥ .20) | 95 | 15 | 15.8% | 26.3% |

He is a league-average shooter from distance and roughly half the league rate from the
slot and the crease, which is exactly where a 6'6" net-front player is supposed to make his
living. Shot mix is fine: median shot distance 16-21 feet (league ~25), xG per attempt
above league in every season (0.093 vs 0.082 in 2025-26). Shot types: wrist shots and tips
dominate; 2025-26 wrist shots went 1 for 45 (4.7 xG). The chances arrive; the puck does not
go in.

**Empty-netters.** 11 of his 66 career goals came into an empty net (5 of his last 28 over
2023-26). Detroit Hockey Now's "10 of his last 37" is the same point stated more
aggressively; use our count.

---

## 6. Deployment: is he being used properly? (`raw/eh_rasmussen.json`, `raw/per_game.json`, `raw/mp_lines_rasmussen.json`, `raw/pk_rasmussen.json`)

Charts: `c5-role-splits.svg`, `c6-lines-with-without.svg`, `c10-pk.svg`, `c13-rapm-off-def.svg`, `c14-qot-qoc.svg`.

### Teammates and competition (Evolving Hockey QoT/QoC, EV)
Quality of teammates has been bottom-quartile in all seven seasons (percentile of the RAPM
xG impact of the skaters he shared ice with: 0, 15, 20, 25, 15, 18, 18). Quality of
competition was middling to hard in his prime (66th-80th percentile in 2021-23) and soft in
2025-26 (20th). His TOI share (~28% of the team's EV minutes) marks him as a 3rd/4th liner
every year. Translation: he has never once been given good linemates, and the year he was
worst he was also facing the easiest competition of his career. Deployment does not
explain 2025-26.

### Center vs wing
Games with 5+ faceoffs taken (a center proxy) vs fewer (`raw/per_game.json`, all
situations, career): center 195 games, 1.36 P/60, 0.95 ixG/60; wing 259 games, 1.53 P/60,
0.78 ixG/60. He generates more of his own chances at center and produces more points on
the wing. His two best seasons were mostly wing seasons (2022-23 was 36 C / 20 W games;
2023-24 was 7 C / 68 W). In 2025-26 he was moved back toward center (31 C games) and those
games were his worst: 0.64 P/60 vs 1.39 on the wing. Faceoffs: 48.1% career, 46.2% in
2025-26. There is a reasonable article argument that the "utility" usage (bouncing to center
whenever a body is needed) has cost him a stable wing role where his production was
tolerable.

### Ice time tiers
Career P/60 by TOI tier: <12 min 1.10; 12-15 min 1.55; 15+ min 1.51. More ice time did
not make him worse; it also did not make him better. In 2025-26 he got 15+ minutes in
only 7 games.

### Zone starts
5v5 offensive-zone start share (MoneyPuck): .49, .54, .40, .55, .41, .49, .50. The heavy
defensive deployment was 2021-22 and 2023-24 (14th percentile both years). 2025-26 was
neutral, so "he's buried in the D zone" was true two years ago and not last season.

### Line-level with/without (MoneyPuck 5v5 line file, DET forward lines)

| Season | DET lines with Rasmussen: min, xGF% | DET lines without him: min, xGF% |
|---|---|---|
| 2022-23 | 508, .536 | 2,509, .458 |
| 2023-24 | 799, .444 | 2,436, .459 |
| 2024-25 | 702, .498 | 2,671, .479 |
| 2025-26 | 537, .523 | 2,645, .496 |

In three of four seasons the team's line-level xG share was better with him on the line
than without, including 2025-26, where the Soderblom-Rasmussen-Appleton line ran a .604 xGF%
over 115 minutes and was outscored 0-4. The Van Riemsdyk-Rasmussen-Soderblom line was .646
over 91 minutes. Those are the two most-used 2025-26 combos and they are good process
lines with terrible results. This is the strongest pro-Rasmussen data point in the package
and the piece should be honest that line xGF% is a shared credit.

### Isolated impact (Evolving Hockey RAPM, EV per 60)
xGF/60 impact by season: -.11, -.08, -.16, +.14, -.03, -.03, -.05 (percentiles 14, 25, 7,
81, 43, 39, 34). xGA/60 impact (negative is good): -.09, +.04, +.04, -.10, .00, -.08, -.02
(percentiles 74, 32, 30, 75, 46, 76, 55). He suppresses chances about as well as an
average-to-good forward and drags chance creation in every season but one. The defensive
side is real; it is just not worth much on its own.

### Penalty kill
MoneyPuck 4v5 on-ice xGA/60 percentile among forwards with 60+ PK minutes: 71 (2021-22),
14, 45, 7 (2024-25, only 63 PK minutes), 70 (2025-26). Evolving Hockey PK RAPM 2025-26:
xGA/60 impact 94th percentile, xGF/60 impact 98th, and 1 of his 6 goals plus 1 SHP came
shorthanded. GAR's shorthanded-defense component: +1.8, 95th percentile. It is a genuinely
strong PK season and the one thing his coach cites; the two previous PK seasons were poor
(2024-25 was 1st-percentile bad on a small sample), so "elite penalty killer" is one
season, not a body of work.

---

## 7. What he does well

- Blocks: 4.7 per 60 at 5v5 in 2025-26, 99th percentile among forwards; led DET forwards.
- Discipline: 0.30 penalties taken per 60 (10th percentile, i.e. very few), 0.44 drawn.
  Positive penalty differential every season since 2021-22 (GAR Pens component +0.5 to +1.2).
- Defense: EH defensive GAR 79th percentile in 2025-26, 77th in 2022-23; EV xGA impact
  better than median in four of seven seasons.
- Hits: 4.7 per 60 (63rd) in 2025-26, down from 9.7 (80th) the year before and 10.3 (85th)
  in 2022-23. The "plays small" complaint has data behind it for 2025-26 specifically: his
  hit rate roughly halved.
- Skating (NHL Edge, `raw/edge/edge_rasmussen.json`): 20+ mph bursts 68th-79th percentile
  every season since 2021-22; top speed 94th percentile in 2024-25 (23.3 mph), 51st in
  2025-26. Not a plodder. Distance per game fell to below-median in 2025-26 (125 miles over
  64 games), which tracks with the reduced minutes rather than effort.
- High-danger shots on goal (Edge): 67 (87th) in 2021-22, 54 (75th), 46 (69th), 51 (79th),
  30 (52nd) in 2025-26. He gets to the net; see §5 for what happens next.

---

## 8. Comparables (`raw/style_comps_2025.json`, `raw/age_curve_comps.json`, `raw/age_curve_comps_gar.json`)

Charts: `c8-age-comps.svg`.

### Who he looks like right now (style only, 2025-26, 17 usage/rate dims, 384 forwards)
Nearest: Ondrej Palat (0.53), Adam Henrique (0.72), Alexey Toropchenko (0.75), Luke
Glendening (0.76), Eeli Tolvanen (0.76), Taylor Raddysh, Noah Laba, Alex Iafallo, Lars
Eller, Luke Kunin, Barclay Goodrow, Adam Lowry. League median pair distance is 1.33. That
is a list of 30-something checking veterans on their last contracts, plus Tolvanen, who was
taken 21 picks after him. His 2025-26 percentile profile among forwards: TOI/GP 18th, 5v5
P/60 6th, G/60 5th, ixG/60 38th, CF% 8th, xGF% 29th, blocks 99th, hits 63rd, giveaways
11th (few), penalties taken 10th (few), game score per game 6th.

### What players like him did next (age curve)
Method: forwards 2010-2022 whose age 24-26 three-season window matched his (5v5 P/60 1.13,
G/60 0.48, ixG/60 0.72, xGF% .47, TOI/GP 13.8, game score/GP 0.23), then their age 27-28
seasons. Two comp sets, one on production (MoneyPuck) and one on value (Evolving Hockey
GAR/82, xGAR/82, off/def split, TOI/GP; his window: GAR/82 +0.9, xGAR/82 +0.2).

Production comps (30 nearest): Bouma, Santorelli, Kassian, Smith-Pelly, Paquette, Watson,
Calvert, Sheahan, Tanev, Jimmy Hayes, Rieder, Dorsett, Jooris, Matt Martin, Faksa, Gerbe,
Lindblom, Nick Paul, Namestnikov, Martinook, Clutterbuck, Lazar, Fast, Cizikas, Zack Smith,
Eakin, Trevor Lewis, Kampf, Rodrigues, Nieto. Outcomes at 27-28: 2 of 30 out of the league,
median 5v5 P/60 change +0.10 to +0.12 depending on GP-weighting (chart c8 uses the weighted
version: 16 of 28 plottable comps improved), 8 of 30 had at least one season +0.5 P/60
better. Same-bin base rate (39 forwards within ±0.2 P/60 and ±2 min): 8% gone, median
+0.11, 58% improved, 8% gained ≥0.5.

Value comps (30 nearest by GAR profile): Bernier, Trevor Moore, Clarkson, Powe, Lindblom,
Sheahan, Talbot, Tanev, Dickinson, Chiasson, Larsson, Nordstrom, Glendening, Abdelkader,
Spaling, Vatrano, Khaira, Boyd Gordon, Kiviranta, Kampf, Janmark, Kuraly, Calvert...
Outcomes: 6 of 30 out of a regular role by 27-28; median GAR/82 change +1.8; 62% improved;
42% gained ≥3 GAR/82. Same-bin base rate (29 forwards within ±1.5 GAR/82): 14% gone, median
+0.5, 60% improved, 32% gained ≥3, 24% gained ≥5. For context the league-wide paired
median for forwards from age 26 to 27 is -0.6 GAR/82; players at his level bounce because
they have nowhere to fall but out.

The break-out names (Moore, Dickinson, Abdelkader, Clarkson, Kassian, Nick Paul) share a
trait he does not have: either real finishing (Moore, Clarkson) or a coach who handed them
a fixed, larger role (Dickinson in Vancouver, Paul in Tampa). Sheahan, Glendening, Faksa,
Kampf and Kuraly are the modal outcome: a decade of 12-14 minute fourth-line hockey at
roughly replacement level.

### The draft class (`raw/draft_2017_r1.json`, chart `c9-draft-class.svg`)
Among the 30 first-round skaters, he is 9th in games played, 16th in total points and 19th in points per game (0.34), ahead of all but two defensemen. Picks
10-13 were Tippett, Vilardi, Necas, Suzuki. The Hockey News' Aug 2026 re-draft gives
Detroit Tippett at 9 and does not place him in the top 10. Draft-day framing: "prototype
power forward", Corey Perry comparable, "unquestioned finishing touch" (50 goals in 114 WHL
games). The scouting miss was specifically the hands, which is the one thing that did not
translate.

---

## 9. Contract and value (`raw/web/capwages_rasmussen.html`, `raw/cap/`)

Feb 20, 2024 extension: 4 years, $12.8M, $3.2M cap hit, no trade protection, two years
left (2026-27, 2027-28), UFA July 2028, requires waivers. Prior deals: ELC Aug 2017
($894K, slid a year), bridge Jul 2021 3 x $1.46M. The 2025-26 cap was $95.5M, so he is
3.4% of it.

**Value at the price (`raw/cap_value.json`, `raw/cap/forwards_2025_26.csv`; Spotrac 2025-26
cap hits joined to Evolving Hockey GAR).** Among the 72 forwards with 2025-26 cap hits
between $2.5M and $4.0M who played 20+ games:

| Measure | Rasmussen | Rank in band (of 72) | Band median |
|---|---|---|---|
| 2025-26 GAR | -0.7 | 51st | +3.1 |
| 2025-26 xGAR | +0.1 | 49th | +1.3 |
| 2024-26 GAR per 82 | +0.3 | 56th | +4.3 |
| 2024-26 xGAR per 82 | -0.6 | 57th | +3.7 |

The neighbors on that list are the right frame for the piece: Jake Evans ($2.85M), Andrew
Mangiapane ($3.6M), Colton Sissons ($2.86M) just above him; Nic Dowd ($3.0M), Adam Henrique
($3.0M), Anthony Beauvillier ($2.75M) just below; Trent Frederic ($3.85M), Max Domi ($3.75M),
Brandon Tanev ($2.5M) and Barclay Goodrow ($3.64M) at the bottom. Top of the band: Protas,
Evangelista, Foegele, Cody Glass (the #6 pick in his draft, $2.5M, +12 GAR/82), Marchenko.

Two framing numbers: forwards priced $2.9M-$3.5M returned a median +3.4 GAR/82 over
2024-26, so $3.2M buys roughly a 3-goal-a-year forward and Detroit is getting about zero.
And forwards who produced what he produced (2-year GAR/82 between -1 and +2, n=68) carry a
median cap hit of $2.42M, with a third of them under $1.5M. The contract is an overpay of
roughly $1M-$2M a year for two more years, not an albatross; league-wide he ranks 249th of
302 forwards at $1M+ in GAR per cap dollar. The February 2024 extension was priced off the
2022-24 version of him (GAR 9.3 then 2.0), which is the version that has not shown up since.

---

## 10. Ceiling, floor, and whether it's fair to expect better

- **Floor (already observed):** 2025-26. 64 GP, 14 points, 12:39, GAR -0.7, 5v5 P/60 at
  the 6th percentile. If 2026-27 looks like this he is a waiver candidate, and 2 of the 30
  production comps and 6 of the 30 value comps were out of a regular NHL role at 27-28.
- **Ceiling (already observed):** 2022-23. A 56-game, 29-point, 82nd-percentile GAR season
  that projected to roughly 40 points over 82, and that even then carried a finishing
  deficit (-4.9 GAx) and a chance-based value that was merely average (xGAR 56th
  percentile). His ceiling is "good third-line checking forward who gets 30-35 points";
  nothing in seven seasons suggests a 20-goal season exists.
- **Base case at 27-28:** modest regression up from a bad year. Same-bin median +0.5 GAR/82
  and +0.1 P/60; about 60% of comparable forwards improved at least a little. A real jump
  (≥5 GAR/82, the difference between a replacement forward and a solid third-liner)
  happened for about one in four; those who did it either had finishing he has not shown
  or were handed a stable role.
- **Is it fair to expect better?** Modestly, yes: 2025-26 has the marks of a trough (career-
  low PDO context, healthy scratches, position churn, soft competition, good line process
  with 0-for-115-minute results). It is not fair to expect the finishing to change; seven
  seasons and 859 shots say it is who he is. The realistic upside is 2023-24 again (33
  points, GAR +2.0), not 2022-23.
- **Is he bad?** Not by the replacement standard: career +13.2 GAR, positive defensive and
  PK value, disciplined, blocks shots, skates fine. He is bad at exactly one thing, and it
  is the thing a 6'6" ninth-overall power forward was drafted to do. Whether $3.2M for a
  replacement-plus fourth liner with a PK specialty is "bad" is a cap question, not a
  player question; see §9.

---

## 11. Suggested structure for the column

1. Open with the fan consensus, verbatim, and the McLellan "utility guy" quote.
2. The luck test as the reveal: it isn't bad luck, it's him. Chart c4, then c3.
3. The arc and the injuries: a 2022-24 peak nobody remembers, a slide that isn't injury-
   driven. Charts c1/c7 with the injury markers, c2.
4. Deployment: never given linemates (c14), better on the wing than at center (c5), lines
   were fine (c6), PK is real this year (c10, c13).
5. Comps and the class (c8, c9): what "a Rasmussen" becomes at 27-29.
6. Verdict: floor, ceiling, base case, and the cap framing (c12 for the GAR/xGAR split).

Register notes for the piece: never call the finishing "unlucky"; the piece's credibility
rests on saying the opposite. Use "replacement level" precisely (GAR 0 = a freely available
AHL call-up). Don't call the PK "elite" without "in 2025-26".

---

## 12. Method notes and gotchas

- **Percentiles**: MoneyPuck rates among forwards with 300+ 5v5 minutes (or 60+ PK
  minutes, 500+ all-situation minutes); Evolving Hockey among forwards with 20+ GP; NHL
  Edge percentiles are the NHL's own vs forwards, and Edge reports sub-median values only as
  "<50th", stored here as 50.
- **Luck test**: MoneyPuck shot files, regular season, unblocked attempts, empty-net shots
  excluded; Poisson-binomial by simulation on the per-shot xG values. The shot files carry
  only the shooter, not on-ice players, so with/without work uses the MoneyPuck line file.
- **Center proxy**: games with 5+ faceoffs taken (NHL REST per-game rows; the api-web
  game log has no faceoff, PP/SH TOI, hit or block fields). NHL lists him as C in every
  season regardless.
- **Age**: age at Sept 15 of the season start. Comp windows require all three base seasons
  with 300+ 5v5 minutes and are limited to windows whose age 27-28 seasons are observable
  (base windows ending by 2022-23).
- **Goal totals**: MoneyPuck season files match the NHL API exactly (66 G); the shot files
  sum to 53 non-empty-net goals with a few rows missing in 2024 (9 vs 11 incl. EN), so use
  the season files for totals and the shot files only for the bucket/luck work.
- **Natural Stat Trick**: NOT pulled. Both Chrome profiles hit a Cloudflare "verify you are
  human" checkbox (not the auto-passing challenge). If Mark clicks it once in Personal
  Chrome the cookie should carry and the NST list (WOWY, zone starts, DET line combos,
  league tables) can be run as a follow-up. Nothing in §1-10 depends on it; WOWY would
  sharpen §6.
- **Reddit** blocked all fetch routes; quotes are index snippets. X was not searchable.
- **Cap tables**: CapWages/PuckPedia/Spotrac are JS-rendered; curl gets a shell. Pulled via
  Personal Chrome.
- **nhl.com CSP** blocks fetch to 127.0.0.1, so the local-receiver POST trick fails on Edge
  pages; use short JS returns there. Evolving Hockey season selectors are multi-select, so
  one download covers all seasons (2007-08 onward). Min TOI filter accepts 0.
- Evolving Hockey data is subscriber data: cite, chart, do not republish the raw CSVs.

## 13. Files

```
BRIEF.md                              this document
charts/make_charts.py                 regenerates every SVG from raw/
charts/c1-career-arc.svg              5v5 P/60 and ixG/60 by season with percentiles, injury markers
charts/c2-goals-vs-xg.svg             goals vs expected by season, 66 on 91.3
charts/c3-danger-conversion.svg       conversion by danger bucket vs league forwards
charts/c4-luck-test.svg               distribution of goals from his shot mix; observed 53
charts/c5-role-splits.svg             per-60 rates at center vs wing and by TOI tier
charts/c6-lines-with-without.svg      DET line xGF% with vs without him
charts/c7-rolling.svg                 rolling 20-game production across the career
charts/c8-age-comps.svg               what his comps did at 27-28
charts/c9-draft-class.svg             2017 first round, points per game and GAx
charts/c10-pk.svg                     PK xGA/60 percentile by season
charts/c11-team-context.svg           DET xGF% rank and sv% by season
charts/c12-gar-xgar.svg               Evolving Hockey GAR vs xGAR by season
charts/c13-rapm-off-def.svg           RAPM offense vs defense impact by season
charts/c14-qot-qoc.svg                teammate and competition quality percentiles
charts/contact-sheet.png              all charts rendered for QA
raw/nhl/                              NHL API landing, game logs, per-game REST rows, league REST tables 2018-2026, bios 2010-2026
raw/mp/                               MoneyPuck skaters 2010-2025, lines 2022-2025, teams 2018-2025, shots 2018-2025 (large)
raw/eh/                               Evolving Hockey GAR/xGAR/RAPM 2007-2025, PK RAPM 2023-25, QoT/QoC 2018-25 (subscriber data)
raw/edge/edge_rasmussen.json          NHL Edge 2021-22 to 2025-26
raw/web/                              injuries_and_transactions.md, fan_sentiment.md, coach_and_media_usage.md, draft_and_development.md, CapWages HTML
raw/cap/                              league forward cap table (see §9)
raw/*.json                            analysis outputs: mp_rasmussen_arc, mp_shots_rasmussen, luck_test, per_game, rolling20,
                                      mp_lines_rasmussen, pk_rasmussen, det_team_context, style_comps_2025, age_curve_comps,
                                      age_curve_comps_gar, draft_2017_r1, eh_rasmussen, empty_net_goals
```
