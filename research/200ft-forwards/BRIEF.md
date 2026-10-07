# What does a team of 200-ft forwards get you? Research brief

Working package for the Wes & Woodward column. Pulled 2026-10-03. Regular seasons only.
"Last three years" = 2023-24, 2024-25, 2025-26. Charts are inline-ready SVGs in `charts/`
(760px, site tokens, `charts/make_charts.py` regenerates all seven, `charts/contact-sheet.png`
shows them together). Raw pulls and analysis JSONs are in `raw/`.

Your three questions, in order: (1) how hard is it for Detroit to score at 5v5, (2) has this
forward archetype ever worked and did those teams have stars, (3) is under-finishing systemic,
and is the defense and goaltending good enough to carry it.

---

## 1. The verdict on the hypothesis

| Claim | Verdict | The number |
|---|---|---|
| Detroit struggles to generate 5v5 goals | True for two of the three years | 29th and 30th in 5v5 goals per 60 the last two seasons. 6th in 2023-24. |
| Scoring below expected is systemic | Half true. Two years, not three, and the roster only explains part of it | +33 (1st) in 2023-24, then -21 (26th) and -19 (29th). Three-year net is -7, 15th. |
| This archetype needs top-of-league defense and goaltending | True, and it is the strongest finding | Low-scoring teams with top-third defense and top-third goaltending made the playoffs 11 of 13 times. Middle and middle: 5 of 22. |
| Detroit has gotten average at best from both | True | Chances allowed: 20th, 22nd, 15th. 5v5 goaltending: 29th, 9th, 18th. One top-ten finish in six tries. |
| (Yours to decide) Did the teams it worked for have stars? | Not scoring stars | 2 of the 18 that won a round had a top-ten scoring forward. 12 of 18 had a top-ten defensive forward group. |

**Framing decided 10/3 (Mark):** keep the three-year window and treat 2023-24 as the outlier
that explains the next two years. Sprong and Fabbri gave that team a scoring boost without
defending, they left, and Detroit leaned further into defensively responsible forwards.
Section 2b has the numbers for that.

Two things the data adds that the hypothesis didn't have:

1. **The 2023-24 team is the outlier, and it sets up the piece.** That roster
   (Kane, DeBrincat, Perron, Sprong, Fabbri) created less than any Detroit team in the window
   (30th in xG for per 60) and outscored its chances by 33 goals, best in the NHL. It still
   missed, because the defense was 20th and the goaltending 29th. So Detroit has now tried
   both versions: the shooter roster with no defense, and the 200-ft roster with no shooters.
2. **Detroit's "200-ft forwards" have not been good defensively.** Evolving Hockey's
   even-strength defense for the forward group ranks 25th, 21st, 14th. The teams that won
   with this model had forwards who ranked in the top ten. The label is ahead of the results.

---

## 2. Detroit at 5v5, three seasons

Charts: `c1-goals-vs-expected.svg`, `c2-rank-card.svg`.

| | 2023-24 | 2024-25 | 2025-26 |
|---|---|---|---|
| 5v5 goals (rank) | 179 (8th) | 143 (28th) | 142 (30th) |
| 5v5 goals per 60 | 2.68 (6th) | 2.06 (29th) | 2.10 (30th) |
| xG for per 60 | 2.19 (30th) | 2.36 (24th) | 2.38 (21st) |
| Goals minus xG | +33.0 (1st) | -20.9 (26th) | -19.1 (29th) |
| 5v5 shooting % | 10.16 (2nd) | 8.19 (26th) | 8.06 (30th) |
| xG against per 60 | 2.58 (20th) | 2.58 (22nd) | 2.50 (15th) |
| Forwards' EV defense, EH (rank) | -6.0 (25th) | -3.6 (21st) | +3.8 (14th) |
| Defensemen's EV defense, EH (rank) | +3.6 (23rd) | +5.5 (22nd) | +4.2 (21st) |
| 5v5 goals saved above expected | -18.1 (29th) | +17.0 (9th) | -0.8 (18th) |
| All-situations GSAx | -0.4 (18th) | +8.2 (15th) | -1.6 (21st) |
| Points (rank) | 91 (18th) | 86 (21st) | 92 (16th) |

Three seasons pooled, rank of 32: 464 5v5 goals (26th), xG for per 60 2.31 (27th), finishing
-7 (15th), xG against per 60 2.55 (22nd), 5v5 GSAx -2 (21st), 5v5 goal differential -58 (27th).

Already in the Kreider brief (NHL.com): from Jan 24, 2026 on, Detroit scored 41 5v5 goals,
last in the league.

Read: the chance creation actually improved every year (30th, 24th, 21st) while the goals
collapsed. The 2025-26 team created more than the 2023-24 team and scored 37 fewer.

---

## 2b. 2023-24 as the outlier: Sprong, Fabbri, and what replaced them

Chart: `c7-2023-24-outlier.svg`. Data: `raw/outlier.json` (`raw/outlier.py`).

**How big an outlier.** +33 at 5v5 is the 12th-best finishing season of 554 since 2008-09,
about two standard deviations above average. Teams at +25 or better average +11.5 the
following year. Detroit went to -21.

**Sprong and Fabbri.**

| 2023-24 | 5v5 goals | 5v5 xG | Gap | Career goals per xG (entering) | EH even-strength defense | On-ice 5v5 goals against per 60 |
|---|---|---|---|---|---|---|
| Daniel Sprong | 15 | 9.3 | +5.7 | 1.44 | -4.3, 6th percentile | 3.21 |
| Robby Fabbri | 13 | 10.8 | +2.2 | 1.14 | -5.2, 3rd percentile | 3.25 |

- Together: 28 5v5 goals on 20.1 xG, 16% of the team's 179, from two wingers who played
  about 11 minutes a night (912 and 875 total minutes).
- They were the two worst defensive forwards on the roster by a wide margin, and bottom 6%
  of the 412 NHL forwards with 400+ minutes. Next worst Red Wing was DeBrincat at the 35th
  percentile.
- Both were gone before 2024-25.

**What replaced them.** Forwards with 300+ minutes at or above the 60th percentile
defensively: 3 of 12 in 2023-24, 8 of 14 in 2024-25, 6 of 13 in 2025-26. The forward
group's defensive rank went 25th, 21st, 14th. The additions and promotions were Kasper
(71st percentile defense in 2024-25), Motte (69th), then Finnie (52nd) and Appleton, with
Copp (81st in 2025-26) and Rasmussen (63rd to 72nd) taking larger roles.
The offense of that same group: Motte 13th percentile, Compher 19th, Veleno 6th in 2024-25;
Kasper 14th, Rasmussen 10th, Appleton 19th in 2025-26.

**Keep the claim sized correctly.** Sprong and Fabbri account for +7.9 of the +33. The rest
of the 2023-24 overshoot was spread around: Kane +6.6, Raymond +5.5, Larkin +2.9, and the
defensemen +13.5 as a group. So "they provided a big share of the scoring and none of the
defense" is supported; "they were the outlier" by themselves is not. Also, Kane was the
worst defensive forward on the 2024-25 team (4th percentile), so the lean toward
responsible forwards was at the bottom of the lineup, not across it.

**The trade Detroit made, in one line.** Forward defense improved 11 spots in two years
(25th to 14th). 5v5 scoring fell 24 spots (6th to 30th).

---

## 3. Is the under-finishing systemic?

Charts: `c5-forward-finishing.svg`, `c6-finishing-by-danger.svg`.

**What supports "systemic":**

- The misses sit with the checking-center group, and those players have always finished
  below their chances. Career 5v5 goals per xG entering the season: Rasmussen 0.78, Copp 0.92,
  Kasper 0.91, Appleton 0.91, Motte 0.76.
  - 2025-26: Copp 4 goals on 12.6 xG (-8.6), Finnie 8 on 14.3 (-6.3), Kasper 7 on 13.1 (-6.1),
    Rasmussen 3 on 7.4 (-4.4). Those four are -25.4 of the forwards' -22.
  - 2024-25: Rasmussen -4.6, Compher -4.5, Motte -3.0.
- The scorers held up: DeBrincat +5.8 then -0.2, Raymond +1.2 then +4.6, Kane -1.4 then +1.3.
- The long-range scoring left with the shooters. Detroit's finishing on low-danger shots
  ranked 1st in 2023-24 (+31), then 31st and 26th. Sprong (career 1.44), Fabbri (1.14) and
  Perron (1.25) all left after 2023-24.
- Two straight years this bad is uncommon: 32 of 520 back-to-back team pairs since 2008-09
  (6%) total -40 or worse per 82. Detroit is one.

**What cuts against it:**

- It is two years, not three. The window opens with the best finishing season in the league.
- Team finishing only partly repeats. Year-to-year correlation is 0.30 (chance creation is
  0.64). Teams at -15 or worse average -7 the next year. A fair forecast for 2026-27 is
  somewhere around -5 to -10, not another -20.
- The roster's shooting history did not predict this. Weighting each forward's xG by his
  career finishing rate (shrunk toward average), the 2024-25 forwards should have scored
  about 147 on 137 xG and scored 122. In 2025-26: about 141 on 133, scored 112. So roughly
  10 goals a year of the gap is personnel you could see coming, and 20 to 25 is either bad
  luck or something the shot model can't see (pre-shot movement, screens, rush vs. cycle).
- Under-finishing is survivable when you create a lot. Carolina has posted -15 or worse in
  eight different back-to-back pairs and keeps winning, because it is top five in chances.
  Detroit is 21st to 24th.

Suggested framing: the under-finishing is real and tied to who takes the shots, but the
bigger structural problem is that this group has to be efficient because it does not create
enough to be wasteful.

---

## 4. Has the archetype ever worked?

Charts: `c3-defense-goalie-grid.svg`, `c4-teams-it-worked-for.svg`.

**Definition.** A team in the bottom third of the league in 5v5 goals per 60. That is the
outcome a forward group without scoring produces, and it keeps one xG model (MoneyPuck)
on both sides of the comparison. 554 team seasons, 2008-09 to 2025-26. 189 qualify.
Detroit qualifies in 2024-25 and 2025-26.

**Base rates.**

- 44 of 189 made the playoffs (23%). Everyone else: 67%.
- 18 won a round. 10 won two. 6 reached the Final. 3 won the Cup (2011-12 Kings, 2013-14
  Kings, 2023-24 Panthers).
- Cup winners by 5v5 scoring tier since 2008-09: top third 12, middle 3, bottom 3.

**What separates the ones that made it** (playoff teams of total, low-scoring teams only):

| 5v5 defense (xGA/60) | Goalie top third | Goalie middle | Goalie bottom |
|---|---|---|---|
| Top third | 11 of 13 (85%) | 11 of 21 (52%) | 4 of 19 (21%) |
| Middle third | 9 of 14 (64%) | 5 of 22 (23%) | 0 of 24 |
| Bottom third | 3 of 19 (16%) | 1 of 24 (4%) | 0 of 33 |

Detroit 2025-26 sits in the middle cell (15th defense, 18th goaltending): 5 of 22, one round
won. Detroit 2024-25 sits bottom-left (22nd defense, 9th goaltending): 3 of 19.
By actual 5v5 goals against: no low-scoring team in the bottom third made the playoffs (0 of 79).

**The 18 that won a round** (rank in xGA/60, 5v5 GSAx, forwards' EH defense; top scorer and
his rank among NHL forwards in points):

| Team | Result | xGA/60 | GSAx | F defense | Top-scoring forward |
|---|---|---|---|---|---|
| 2011-12 LAK | Cup | 8 | 3 | 5 | Kopitar, 16th |
| 2013-14 LAK | Cup | 7 | 1 | 4 | Kopitar, 16th |
| 2023-24 FLA | Cup | 5 | 3 | 7 | Reinhart, 13th |
| 2011-12 NJD | Final | 1 | 27 | 1 | Kovalchuk, 5th |
| 2019-20 DAL | Final | 2 | 7 | 5 | Seguin, 64th |
| 2020-21 MTL | Final | 9 | 11 | 6 | Toffoli, 47th |
| 2009-10 MTL | 2 rounds | 19 | 5 | 14 | Plekanec, 28th |
| 2013-14 MTL | 2 rounds | 22 | 7 | 23 | Vanek, 24th |
| 2016-17 OTT | 2 rounds | 10 | 13 | 10 | Hoffman, 39th |
| 2019-20 NYI | 2 rounds | 10 | 15 | 15 | Barzal, 29th |
| 2009-10 BOS | 1 round | 2 | 22 | 2 | Krejci, 82nd |
| 2009-10 DET | 1 round | 12 | 18 | 13 | Datsyuk, 24th |
| 2011-12 STL | 1 round | 2 | 1 | 2 | Oshie, 72nd |
| 2012-13 SJS | 1 round | 9 | 13 | 12 | Thornton, 32nd |
| 2012-13 OTT | 1 round | 13 | 10 | 10 | Turris, 86th |
| 2012-13 DET | 1 round | 8 | 5 | 11 | Datsyuk, 10th |
| 2013-14 MIN | 1 round | 2 | 12 | 2 | Pominville, 46th |
| 2018-19 DAL | 1 round | 4 | 3 | 6 | Seguin, 27th |
| **2024-25 DET** | missed | 22 | 9 | 21 | Raymond, 26th |
| **2025-26 DET** | missed | 15 | 18 | 14 | DeBrincat, 19th |

- 17 of 18 were top ten in chances allowed or in goaltending. 7 were top ten in both.
  The one exception is the 2009-10 Red Wings (Datsyuk, Zetterberg, Lidstrom).
- Of the 145 low-scoring teams that missed, 2 were top ten in both.
- 12 of 18 had a top-ten defensive forward group. Median rank 6.5. Detroit: 21st and 14th.
- Medians for the 18: xGA/60 8th, GSAx 8.5, forwards' defense 6.5.

**Stars.** Not the scoring kind. 2 of 18 had a top-ten scoring forward (Kovalchuk, Datsyuk).
5 of 18 had a top-twenty one. Median rank of the leading scorer: 28.5. What they had instead
was a Selke-grade center or a goalie having a top-ten year: Kopitar, Barkov, Bergeron,
Datsyuk, Backes up front; Quick (2nd in GSAx), Price (3rd), Bishop (2nd), Anderson (3rd),
Halak, Rask, Bobrovsky in net. 6 of 18 had a top-ten forward by Evolving Hockey GAR.

Detroit has comparable individual talent on paper: Seider ranked 2nd among defensemen in EH
GAR in 2025-26 (10th in 2024-25), DeBrincat 8th among forwards, Gibson 12th of 61 goalies
(+11.7 all situations). The team totals still come out 15th and 18th, so the shortfall is
depth behind them (Gibson's own number is positive while the team's 5v5 figure is -1).

**Two sub-types worth separating.** 7 of the 18 winners were top ten in chance creation and
simply did not finish (2013-14 Kings were 2nd in xG for and -29 in finishing). They controlled
play. Teams that were bottom third in both goals and chances, which is Detroit's 2024-25
profile: 113 team seasons, 17 playoff teams (15%), 6 round winners (2009-10 BOS, 2009-10 MTL,
2013-14 MIN, 2016-17 OTT, 2018-19 DAL, 2019-20 NYI).

---

## 5. Suggested outline

1. The title question, answered with one number: two straight years in the bottom four of
   5v5 scoring. (c1)
2. 2023-24 as the outlier: Sprong and Fabbri scored and didn't defend, the team missed
   anyway, and the front office went further toward responsible forwards. (c7, c2)
3. Where the goals went: the checking centers, and the vanished long-range scoring. (c5, c6)
4. Has it ever worked? 189 teams, 3 Cups, and the grid. (c3)
5. What the 18 had: elite defensive forwards, a top-ten goalie, almost never a top-ten
   scorer. Detroit's rows underneath. (c4)
6. What it would take: either a top-ten defense and goalie (Detroit's best finish in either
   is 9th, once), or a forward group that creates like Carolina so the misses don't matter.

---

## 6. Method and caveats

- **Sources.** MoneyPuck team, skater and goalie season summaries 2008-2025 (`raw/mp/`); NHL
  stats API team summary for points and playoff brackets for rounds won (`raw/nhl/`);
  Evolving Hockey GAR and xGAR all seasons (`research/rasmussen/raw/eh/`).
- **Scripts**, run in this order: `raw/fetch.py`, `team_table.py`, `fgroup.py`, `master.py`,
  `history.py`, `detroit.py`. Outputs: `team_seasons.json`, `fgroup.json`, `master.json`,
  `history.json`, `detroit_detail.json`.
- **Ranks are within season.** Thirds are by rank divided by league size (30, 31 or 32 teams).
  Per-82 scaling for 2012-13, 2019-20 and 2020-21.
- **2019-20 rounds** exclude the qualifying round.
- **Two xG models disagree on Detroit's offense.** Evolving Hockey's forward offense had
  Detroit 10th in 2023-24 where MoneyPuck's team xG had it 30th. EH's offensive numbers
  track MoneyPuck's finishing (r = 0.66), so I used MoneyPuck for everything on offense and
  EH only to split defense between forwards and defensemen, where the two models agree
  (r = 0.95 to 0.98 with MoneyPuck's xG against).
- **MoneyPuck's high-danger band** runs under expected for every team. Use the ranks in c6,
  not the raw high-danger gaps.
- **Traded players** carry their whole season in MoneyPuck's skater file. Perron's 2025-26
  row is 49 games with Ottawa plus 16 with Detroit. Team totals are unaffected; the
  forward-by-forward chart is approximate for him.
- **Prior finishing talent** = career 5v5 goals and xG before that season, shrunk with 30 xG
  of league-average shooting. Rookies count as average.
- **Not done:** no shot-level work (rush vs. cycle, pre-shot passes) to explain the 20 to 25
  goals a year the roster's history doesn't. That would need the MoneyPuck shot files and is
  the natural follow-up if you want to push the "systemic" argument harder.
