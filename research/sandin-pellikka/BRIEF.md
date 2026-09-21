# Axel Sandin-Pellikka's rookie year: the numbers didn't get worse, the ice time did — research brief

Working package for the Wes & Woodward column. Everything below was pulled on 2026-09-18 and
covers the 2025-26 regular season unless stated. Charts are inline-ready SVGs in `charts/`
(760px, site tokens, same kit as the Kreider and Rasmussen packages); raw pulls and analysis
JSONs are in `raw/`; `charts/make_charts.py` regenerates every chart from `raw/analysis.json`,
which `raw/build_analysis.py` rebuilds from the pulls. Contact sheet: `charts/contact-sheet.png`.

Sources: NHL API (game logs, bios, career totals, **shift charts**), MoneyPuck season summaries
2010-2025 (league files plus the 2025-26 DET line file), **HockeyStatCards** (hockeystatcards.com
— new to the kit this run, see §12), **Evolving Hockey** (subscriber: GAR, xGAR, RAPM, QoT/QoC,
plus per-game zone and on-ice logs), and a web sweep of beat coverage.

Bio: born Mar 11, 2005, Gällivare, Sweden. 6'0", 189 lb, right shot, RHD. Drafted 2023 R1 #17
(DET). Age 21 for 2026-27, on the second year of his entry-level deal.

---

## 1. The verdict in one paragraph

**The premise holds, and the reason it holds is narrower and better than "the analytics liked
him."** Evolving Hockey's two models disagree about him by 5.2 goals. By results he was a
**-1.9 GAR** defenceman, 20th percentile, below replacement. By chances he was **+3.3 xGAR**,
58th percentile — an above-average NHL defenceman. That gap is not a modelling curiosity; it is
the twelve and a half goals of on-ice variance that ran against him in both directions at once,
including the lowest on-ice 5v5 save percentage of any Red Wing with 300+ minutes (.885, against
a .938 at the other end of the same room). The scoreboard said minus-20. The chances said a
useful rookie.

Two things that survive the correction, and the piece needs both. **His even-strength defending
was genuinely poor**: 10th percentile EVD_GAR, 11th percentile expected goals against per 60,
13th in high-danger chances against, and a RAPM that says he suppressed shot *attempts* (66th
percentile) while conceding *quality* (10th). He was not caved in; he was beaten in front. Both
Dan Watson and Sandin-Pellikka himself describe exactly that. And **his even-strength offence
was better than the raw on-ice numbers suggest** — 82nd percentile xEVO_GAR against 44th
percentile EVO_GAR, because the isolated model credits him for chances his teammates did not
finish.

So: why did he stop playing? Not because his play fell off. His ice time fell 24% (18.4 to 14.0
minutes) across the halves of his season while his chance share held at 48.1% then 47.0% — and
his competition got **harder**, not easier, as the minutes came down. December earned a cut. The
rest was roster math: on March 6 Detroit traded a first, a third, Justin Holl and Dmitri
Buchelnikov for a 33-year-old right-shot defenceman, scratched Sandin-Pellikka seven straight
times, and sent him to Grand Rapids on March 23.

---

## 2. What actually happened, in order

| | |
|---|---|
| Oct 9 | NHL debut, 22:34, top-four minutes from game one |
| Oct (12 GP) | 18.7 min a night, 47% chance share, **outscored 3-11** |
| Dec 2 | Ice time starts coming down: 16.0 min for the month, and a genuine underlying trough (43.6%) |
| Jan-Feb 4 | 13.8 min, chance share recovers to 46.8% |
| Feb 6-24 | Olympic break (Milan). No games |
| Feb 26 - Mar 6 | Five games at 12.1 min. **59.3% chance share**, his best stretch |
| **Mar 6** | Deadline. Detroit acquires **Justin Faulk** from St. Louis for Justin Holl, a 2026 1st, a 2026 3rd and Dmitri Buchelnikov. Faulk is 33, right shot, $6.5M through 2026-27 |
| Mar 6 | Last NHL game of his season, 14:56 vs Florida |
| Mar 8-22 | **Seven straight healthy scratches** |
| **Mar 23** | Assigned to Grand Rapids. At the time: 63 GP, 19 points, minus-21, 16:19 |
| Mar-Apr | 6 AHL regular-season games, 2-1-3 |
| Apr 4 | Recalled. Five more NHL games, 14.9 min, 2 points |
| Apr-Jun | Back to Grand Rapids for the Calder Cup run: 8 playoff games, 1-3-4, Central Division Finals |

Final NHL line: **68 GP, 7-14-21, 16:13, minus-20**. Third among rookie defencemen in goals
(behind Matthew Schaefer's 23 and Alexander Nikishin's 11) and tied for fifth in points.

---

## 3. What the advanced numbers actually say (`raw/asp_percentiles_5v5.json`, chart `c3`)

Percentile among the 237 NHL defencemen with 300+ 5v5 minutes. Rates inverted so higher is
always better.

| | ASP | league median | pct |
|---|---|---|---|
| Corsi share (CF%) | 50.0% | 49.0% | 52 |
| Chances created (xGF/60) | 2.42 | 2.45 | 45 |
| Own shot volume (ixG/60) | 0.16 | 0.17 | 47 |
| Chance share (xGF%) | 46.0% | 49.0% | 18 |
| Relative chance share | -4.0 | 0.0 | 21 |
| High-danger chances against/60 | 2.94 | 2.40 | 13 |
| Chances against (xGA/60) | 2.83 | 2.51 | 11 |
| Goals against (GA/60) | 3.07 | 2.46 | 12 |
| On-ice PDO | 96.31 | 100.03 | 7 |

### Evolving Hockey, percentile among 249 defencemen with 20+ GP

| | value | pct | | value | pct |
|---|---|---|---|---|---|
| EVO_GAR (EV offence, results) | +0.3 | 44 | xEVO_GAR (EV offence, chances) | **+5.2** | **82** |
| EVD_GAR (EV defence, results) | -3.2 | **10** | xEVD_GAR (EV defence, chances) | -2.3 | 15 |
| SHD_GAR (penalty kill) | +0.6 | 69 | | | |
| **GAR (total, results)** | **-1.9** | **20** | **xGAR (total, chances)** | **+3.3** | **58** |

RAPM, even strength per 60, same cohort: C± +1.39 (68th), CF/60 +0.86 (67th), CA/60 -0.53
(66th) — he moved shot volume in both directions. But xG± -0.165 (18th) and **xGA/60 +0.133
(10th)**. Volume good, quality bad. G± -0.288 sits at the 4th percentile, which is the luck
again.

Deployment, season-level: **QoT** 11th-22nd percentile across EH's four measures, **QoC** 25th
to 36th. He played with worse players than he played against, and both were below median — the
bottom of a bad team's depth chart. (Note for §5: season-level QoC below median is fully
compatible with the within-season *trend* going the other way, and it did.)

HockeyStatCards (Luszczyszyn model, NST data): **Offence 53rd percentile, Defence 3rd, Net
14th, Game Score -0.01 (15th)**. HSC's defensive rating is harsher than EH's (3rd vs 10th-15th);
quote EH's, and use HSC's only as corroboration of direction. Read the two together and the shape is unambiguous: he moved
the puck like a league-average NHL defenceman and defended like a bottom-decile one, at twenty,
on a team that finished 41-31-10 and scored 41 5v5 goals after January 24 (last in the league).

The top three rows matter for the piece. He was not hemmed in — his Corsi share was above
median. He gave up *better* chances than he took, not more of them. That is a reading problem
and a strength problem, which is exactly what Grand Rapids said out loud (§9).

---

## 4. The luck ledger (`raw/analysis.json` → `asp_season`, chart `c2`)

All situations, with him on the ice:

| | expected | actual | delta |
|---|---|---|---|
| Goals for | 52.9 | 44 | **-8.9** (shooting) |
| Goals against | 52.4 | 56 | **+3.6** (goaltending) |

Twelve and a half goals, against him, in both directions at once. At 5v5 his on-ice save
percentage was **.885**, the lowest of any Red Wing with 300+ minutes; Jacob Bernard-Docker,
on the same team and the same goalies, was at .938, and the league baseline was .905. His
on-ice shooting percentage was 7.8%.

This is the number that explains the October that set the narrative: 47% of the chances,
**outscored 3-11**, in the first twelve games of his NHL career. His chance share in November
was 50.2% and nobody noticed, because by then the plus-minus was already gone.

---

## 5. The core finding: the minutes fell, the play and the competition didn't (charts `c1`, `c8`)

| phase | GP | TOI/GP | 5v5 xGF% | GF% | GF-GA |
|---|---|---|---|---|---|
| Oct 9 - Nov 29 | 26 | 18.9 | 48.6% | 33% | 9-18 |
| December | 15 | 16.0 | 43.6% | 41% | 9-13 |
| Jan 1 - Feb 4 | 17 | 13.8 | 46.8% | 45% | 9-11 |
| Feb 26 - Mar 6 | 5 | 12.1 | **59.3%** | 40% | 2-3 |
| Apr 4 - 15 (recall) | 5 | 14.9 | 49.0% | 57% | 4-3 |

First 34 games: 18.4 minutes, 48.1%. Last 34: 14.0 minutes, 47.0%. On EH's 5v5 log the same
cut is sharper still — his share of Detroit's 5v5 ice went from **31.9% to 25.6%**.

December is the one stretch that justifies a cut: 43.6%, his real trough, and the minutes came
down in response. That is defensible coaching. What happened after is not: the chance share came
back to 46.8%, then 57.6% (EH 5v5) over his last five games, and the ice time kept falling.

### The competition test (`raw/build_qoc_by_date.py`, `raw/asp_qoc_by_game.json`)

The obvious objection is that his numbers held up because he was being sheltered. EH can't
answer it — its QoT/QoC table is season-only. So we rebuilt QoC from primary data: NHL shift
charts reconstructed to the second, filtered to 5v5 (both teams exactly five skaters, goalies
excluded), then every opponent he shared ice with scored by his EH 2025-26 xGAR/60 and averaged
by shared time. That is EH's own QoC construction at game resolution. **Validation: the rebuilt
5v5 ice time comes to 13.66 minutes per game against EH's 13.66.** 93.8% of opponent seconds
carry a score.

| phase | 5v5 TOI/GP | opponent quality (xGAR/60) |
|---|---|---|
| Oct 9 - Nov 29 | 15.2 | +0.17 |
| December | 14.3 | +0.17 |
| Jan 1 - Feb 4 | 11.8 | +0.25 |
| **Feb 26 - Mar 6** | **10.7** | **+0.33** |
| Apr 4 - 15 (recall) | 13.3 | +0.23 |

First 34 games +0.156, last 34 +0.253. Game-level correlation between his ice time that night
and the quality of his opponents: **r = -0.21**. The competition went up as the minutes went
down, and his five games before the demotion were simultaneously his lowest minutes and his
toughest opponents of the season. The sheltering explanation is dead.

**One honest qualifier.** Zone starts did move his way: his offensive share of non-neutral 5v5
starts went from 49.3% in the first half to 52.7% in the second, and 57.1% in that last
five-game stretch. So he was getting slightly friendlier faceoffs against slightly better
players on materially fewer shifts. The zone-start shift is real and should be stated; it is
much smaller than the ice-time cut and points the opposite way to the competition trend.

**The line for the piece:** he lost his minutes in December for playing badly, and lost the rest
of them in March for a reason that had nothing to do with how he was playing.

---

## 6. Who he played with (`raw/analysis.json` → `pairings`, chart `c6`)

| pairing | 5v5 min | xGF% | CF% | GF-GA | xGF-xGA |
|---|---|---|---|---|---|
| Chiarot - Sandin-Pellikka | 573 | 46% | 48% | 24-25 | 23.4-27.1 |
| Edvinsson - Sandin-Pellikka | 139 | 36% | 49% | 3-8 | 4.2-7.5 |
| Johansson - Sandin-Pellikka | 124 | **58%** | 61% | **6-10** | 6.6-4.8 |
| Gustafsson - Sandin-Pellikka | 28 | 27% | 40% | 0-2 | 0.7-1.8 |

Four-fifths of his season was spent next to Ben Chiarot, who was Detroit's worst regular
defenceman by chance share (45%). Set against Chiarot's other partners, Sandin-Pellikka is
near the top of the non-Seider list: Chiarot-Faulk 47% over 249 minutes, Chiarot-Bernard-Docker
40% over 205, Chiarot-Johansson 29% over 129. **The 20-year-old and the $6.5M deadline rental
produced the same result with the same partner**, one point of chance share apart.

Caveat to state in the piece: 249 minutes is a fifth of a season, in a different part of the
schedule, against different opponents. It is a fair rhetorical point, not a controlled test.

And the pairing that worked — Johansson with Sandin-Pellikka, 58% of the chances, 61% of the
shot attempts — was **outscored 6-10**. That is the whole season in 124 minutes.

---

## 7. Age-20 context (`raw/age20_d_cohort_onice.json`, charts `c4`, `c5`)

Every defenceman with 40+ NHL games in his age-20 season (age on Sept 15), 2010-11 through
2025-26: **69 players**.

Offensively he is the median: 25.3 points per 82, 40th of 69, between Aaron Ekblad's age-20
season (25.3) and Vince Dunn's (26.2). Lane Hutson (66.0), Cale Makar (71.9) and Moritz
Seider (50.0) are a different conversation.

On chance share he is bottom third. Relative xGF% -4.0 ranks 57th:

| season | player | GP | xGF% | rel | PDO | P/82 | career GP |
|---|---|---|---|---|---|---|---|
| 2010-11 | John Carlson | 82 | 50% | -3 | 101.2 | 37.0 | 1159 |
| 2020-21 | K'Andre Miller | 53 | 46% | -3 | 102.1 | 18.6 | 440 |
| **2025-26** | **Axel Sandin-Pellikka** | 68 | 46% | **-4** | **96.3** | 25.3 | 68 |
| 2018-19 | Samuel Girard | 82 | 48% | -4 | 101.8 | 27.0 | 608 |
| 2025-26 | Tom Willander | 70 | 40% | -5 | 98.6 | 24.6 | 70 |

And on luck he is last. **PDO 96.31 is the lowest of all 69**, a hair under Mario Ferraro's
96.33, with Rasmus Dahlin (96.5), John Moore (96.8) and Noah Hanifin (96.9) next. Note the
company: two of the four next-unluckiest age-20 seasons belong to a Norris finalist and a
$7.4M top-pair defenceman.

## 8. Does grading out badly at twenty mean anything? (chart `c5`)

Restricting to age-20 seasons from 2010-11 to 2020-21 so careers have had time to happen
(n = 57):

| age-20 relative chance share | n | median career GP | reached 500 |
|---|---|---|---|
| +2 or better | 19 | 829 | 84% |
| between -2 and +2 | 18 | 736 | 78% |
| -2 or worse | 20 | 720 | 70% |

Correlation between age-20 relative chance share and career games: **r = +0.31**. Age-20
points per 82 does no better (+0.27). The worst-grading tier contains Erik Karlsson, John
Carlson, Nick Leddy, Jonas Brodin, Hampus Lindholm, Rasmus Ristolainen and Darnell Nurse.

**Mandatory caveat, and it should be in the piece, not a footnote:** every player in this
sample already played 40 NHL games at twenty, which is itself an enormous filter. This says
"a bad age-20 season doesn't tell you much about players good enough to have one." It does not
say bad rookie seasons are meaningless in general.

---

## 9. What Grand Rapids actually said

Griffins head coach Dan Watson, during the Calder Cup run:

> "When he came here last year, there were some puck management issues but that's natural.
> He's fixed a lot of that. He's a guy who sees the ice and has good vision, so the next step
> for him is going to be his defensive game. **He's going to need to kill plays, stall pucks
> with his feet or his stick.** Once he learns to do that consistently… He's already an NHL
> player, so we're fortunate to have him."

Sandin-Pellikka himself:

> "I want to get better with the puck, move more, **get stronger in the defensive zone and be
> smarter in the defensive zone**. I just want to be better everywhere. I know I'm not the
> biggest guy, so obviously just getting stronger and smarter."

> "My mind has shifted more to American hockey instead of Swedish hockey now."

Both of them describe exactly what the 11th-percentile xGA/60 and 13th-percentile
high-danger-against describe. That agreement is worth making explicit: this is not a case
where the numbers and the eye test disagree. They agree completely about the problem. They
disagree about whether the response — scratch him seven times and send him down — was the one
the problem called for.

---

## 10. The peg, and it's live right now

The Hockey News projects Detroit's 2026-27 pairings as Edvinsson-Seider, **Chiarot-Faulk**,
**Johansson-Sandin-Pellikka**. PuckPedia has Jacob Bernard-Docker in that spot instead. So the
2026-27 question is a straight restatement of the 2025-26 one:

- The third pairing they're projecting for him is the one pairing of his that actually worked
  (58% of the chances in 124 minutes) and was outscored 6-10 doing it. If the goaltending
  behind him is league-average this time, that pairing looks completely different with the
  same play.
- His competition for the spot, Bernard-Docker, posted a 47% chance share and a **.938 on-ice
  save percentage**, the best on the team. Nearly the same chance share as Sandin-Pellikka's
  46%; a 5.3-point gap in on-ice save percentage that belongs to neither of them.
- The reason he ran out of runway in March, Faulk, is 34 and in a contract year at $6.5M.

That is the piece's closing argument: Detroit has now twice made a roster decision between
these players on the basis of a number that was mostly goaltending.

---

## 11. Suggested shape

Headline candidates (no colons, per house style):

1. **"Axel Sandin-Pellikka lost a quarter of his ice time and none of his game"**
2. "The twelve and a half goals that decided Axel Sandin-Pellikka's rookie year"
3. "Detroit benched a defenceman for the save percentage behind him"

Structure that the evidence supports, in order:

1. **Open on March 6.** The deadline, the Faulk price, the seven scratches, the assignment.
   Then the twist: those five games before it were the lowest minutes and the hardest
   competition of his season.
2. **The two models** (§3, chart `c7`). GAR -1.9 and 20th percentile against xGAR +3.3 and 58th.
   State the gap as 5.2 goals and move straight into where it came from.
3. **Concede the real problem** (§3). 10th percentile EV defence, 10th percentile RAPM xGA/60,
   66th percentile at suppressing attempts — beaten in front, not caved in. Watson and the
   player say the same thing. Put this second or third, never last; a piece that saves the
   criticism for the end reads as an apology.
4. **The ledger** (§4, chart `c2`). 12.5 goals. The .885 against the .938. The 3-11 October that
   wrote the story before anyone had a sample.
5. **The core finding** (§5, charts `c1` and `c8`). December earned the first cut. Nothing
   earned the rest — and the competition went *up* as the minutes came down. Include the
   zone-start qualifier in the same breath.
6. **Chiarot** (§6). Same partner, same result as the man they traded a first for.
7. **The cohort** (§7-8, charts `c4`, `c5`). Bottom-third, lowest PDO of 69, and it predicts
   almost nothing — with the survivorship caveat stated plainly.
8. **Close on 2026-27** (§10).

Things to *not* claim, because the data doesn't support them:
- That his underlying play **improved** over the season. It was flat: 48.1% then 47.0%. Only the
  last 10-15 games improved, on five- and ten-game samples.
- That he was good defensively, or that the defensive criticism is a misreading. It isn't.
- That he was never sheltered at all. His zone starts moved 3.4 points his way in the second
  half (§5). The competition finding is the strong one; the zone-start finding is the honest
  counterweight and belongs next to it.
- That the Faulk trade was made to displace him. It displaced him; there's no evidence that was
  the intent.
- Any claim that EH's xGAR "proves" he was good. It says the chances he was on the ice for were
  worth about three and a half goals above replacement. That is a real finding and a modest one.

---

## 12. Data, sources, limitations

**HockeyStatCards (hockeystatcards.com) — new source, added at Mark's suggestion 2026-09-18.**
Note the domain is plural; `hockeystatcard.com` does not resolve. It's a TanStack Start app
that server-renders its tables, so a plain GET returns the data with no browser and no Patreon
login: `/players/<nhlPlayerId>` is the skater card, `/players/<nhlPlayerId>?tab=logs` is the
game-by-game log. `raw/hsc/fetch_hsc.py` wraps both. It rate-limits hard (HTTP 429) — the
fetcher backs off, but space out cohort pulls. Underlying data is Natural Stat Trick, the
ratings are Dom Luszczyszyn's Game Score model. **This is the cheapest route we have to
per-game on-ice xGF/xGA**, which is what made §5 possible at all; MoneyPuck's season files
can't do it and NST needs a browser. Its logs are 5v5 for the goal and xG columns and
all-situations for TOI, which is confirmed: the 68 logged games sum to the card exactly, and
GF 33 / GA 48 match MoneyPuck's 5v5 row exactly.

Other sources: NHL API (`api-web.nhle.com` game logs and landings; `api.nhle.com/stats/rest`
bios, paginated 100 at a time). MoneyPuck season summaries 2010-2025 in `raw/moneypuck/`, plus
the site pipeline's 2025-26 league and DET files. Beat coverage: NHL.com, Yahoo Sports, The
Hockey News, NHL.com transactions.

**Evolving Hockey** (subscriber). The league-wide GAR / xGAR / RAPM / QoT/QoC exports already
in `../rasmussen/raw/eh/` cover 2025-26, so no new export was needed for the season-level work;
`raw/eh/*_d2526.csv` are the defencemen-only slices. Two things were pulled fresh in Mark's
personal Chrome (Browser 1; the other connected Chrome is not signed in): the per-game **zone**
and **on-ice** skater logs, via Game Logs → Table Type. Useful mechanics learned:

- Its player selector is a Shiny `selectInput` whose options load server-side, so **typing into
  the visible box does nothing**. Drive it from the query string instead — every input is
  settable there, e.g. `.../stats/game_logs/?_inputs_&dir_glog="Skater Logs"&sglog_table="Zones"
  &sglog_str="5v5"&sglog_player="Axel Sandin-Pellikka"&sglog_season="20252026"&sglog_span="Regular"`.
  The page applies it on load; then hit the table's Download button.
- **The QoT/QoC table is season-only.** Its "Filter Type" dropdown has exactly one option,
  "Seasons". There is no way to split competition by date on EH. That is why §5 rebuilds it.
- EH data is subscriber data: cite it, chart it, do not republish the raw CSVs.

**Shift-chart QoC** (`raw/build_qoc_by_date.py`). `api.nhle.com/stats/rest/en/shiftcharts?
cayenneExp=gameId=X` returns every shift; `typeCode == 517` are shifts and 505 are events.
Goalies come back in the same feed and are stripped using the goalie `bios` endpoint. Both
endpoints need `urllib.parse.urlencode` — a raw space in `cayenneExp` raises `InvalidURL`.
Reconstructing to the second and keeping only 5v5 reproduces EH's 5v5 TOI to the hundredth of a
minute, which is the check that the engine is right. This is reusable for any player.

Known limitations, all of which should shape how hard the piece pushes:

1. **Zone starts, not competition, are the surviving deployment caveat** (§5). The competition
   objection is answered; the zone-start shift of 3.4 points is real and unaddressed.
2. **MoneyPuck lists traded players once, under their final team.** Justin Faulk's season row
   (78 GP, 45%) is St. Louis and Detroit combined and is not usable as a Detroit-only figure.
   The Detroit-only Faulk numbers in §6 come from the DET line file, which is correctly scoped.
3. Sample sizes in §5 and §6 are small: 5 games in the post-Olympic phase, 124 minutes for the
   Johansson pairing, 249 for Chiarot-Faulk. Quote them with their minutes attached.
4. The age-20 cohort is survivorship-filtered (§8).
5. The QoC build scores opponents on season-long xGAR/60, so a player who was hurt or
   transformed mid-season is scored at his season average. With 93.8% coverage and 68 games the
   noise should wash out, but it is an approximation, not a measurement.
6. No fan-sentiment sweep this run. The Rasmussen package's method (search-index snippets,
   Reddit blocks direct fetches) would apply if the piece wants a "what everyone thinks"
   section.
7. No WOWY. §6 leans on pairing rows; a real with-or-without-you on Chiarot would sharpen it.

## Charts

| file | what it shows |
|---|---|
| `c1-toi-vs-play.svg` | Rolling 10-game ice time vs 5v5 chance share, with the break and deadline marked |
| `c2-luck-ledger.svg` | On-ice goals vs expected, both directions, all situations |
| `c3-percentiles.svg` | Nine rate percentiles among 237 NHL defencemen |
| `c4-age20-scatter.svg` | The 69-player age-20 cohort, relative chance share vs PDO |
| `c5-cohort-outcomes.svg` | Career games by age-20 chance-share tier |
| `c6-chiarot-partners.svg` | Chiarot's pairings, chance share and minutes |
| `c7-gar-vs-xgar.svg` | Evolving Hockey GAR vs xGAR percentiles, offence / defence / total |
| `c8-qoc-vs-icetime.svg` | 5v5 ice time and rebuilt opponent quality, by phase |
