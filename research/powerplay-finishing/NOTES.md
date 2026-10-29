# Power play finishing anomaly — research notes

Data: MoneyPuck seasonSummary 2026 regular (teams/skaters/goalies.csv), pulled 2026-10-21 AM.
Covers 9 GP through 10/20 at SEA (L 3-4 SO). Official NHL PPG total = 7 (Arvidsson 3, DeBrincat 2, Faulk 1, Raymond 1).
MoneyPuck 5on4 GF = 5; DeBrincat's two PPG came at 5on3/4on3 ("other" bucket). Always say which split is quoted.

## Team, 5on4 (52.5 min, league ranks of 32)
- xGF/60 9.06 — 5th
- GF/60 5.71 — 22nd
- GF minus xGF: 5 on 7.93 = -2.93 — 31st (DAL -3.63 worst)
- Sh% 10.0% on 50 SOG — 26th
- Medium-danger: 34 shots, 4.32 xG, 0 goals

## Team, all situations
- xGF/60 3.15 — 13th; GF/60 2.37 — 28th; GF minus xGF -7.17 — 31st; sh% 8.2% — 30th
- 5on5: sh% 7.1% (28th), sv% .922 (5th), GA/60 1.92 (6th)

## PP individuals (5on4)
- Raymond 37.9 min, 12 SOG, 1.52 ixG, 1 G (first goal of season, 10/20)
- Seider 37.6 min, 10 SOG, 0.78 ixG, 0 G
- DeBrincat 36.0 min, 8 SOG, 1.30 ixG, 0 G at 5on4 (2 PPG at 5on3/4on3)
- Arvidsson 34.4 min, 6 SOG, 1.98 ixG, 3 G
- Larkin 28.9 min, 3 SOG, 0.62 ixG, 0 G

## Secondary angle: PK is a Gibson split
- Gibson 4on5: 27 SA, 8 GA, 4.44 xGA, .704, GSAx -3.56. 5on5: .908, GSAx +0.92
- Tarasov all: .940, GSAx +5.08 (4 GP)
- Team PK xGA/60 8.47 (24th), GA/60 10.88 (24th), sv% .769 (28th)

## To do before drafting
- Persistence test: prior seasons' PP xGF/60 through ~9 GP vs rest-of-season PP GF/60, compared with early PP GF/60. Needs game-level MoneyPuck (games.csv) or shots data.
- Re-pull after 10/22 at VAN.

---
# 2026-10-23 update: claim verification for the "good process, bad finishing" reframe
Data: raw/2026-10-23/ (MoneyPuck 2026 + 2025 + 2024 teams/skaters/goalies, NHL standings 16:50Z). 10 GP, 4-3-3, 11 pts, 20th by points. VAN 5-2 W: 5v5 xGF 2.51 / xGA 1.27, 4 goals on 2.5 xG.
Top-3 by points now CAR/BOS/EDM (dashboard still showed CAR/VGK/NYR). Finishing percentile after VAN: 9.7 (rank 29), was 3.2.

Percentiles (rank-based, DET / top3 avg): finishing 9.7/87.1 | GSAx 64.5/50.5 | 5v5 xGF/60 58.1/63.4 | 5v5 xGA/60 71.0/67.8 | CF% 80.6/53.8 | PP xGF/60 96.8/59.1 (2nd) | PK xGA/60 35.5/50.5 | PK GA-xGA 22.6/34.4
Caveat: score/venue/flurry-adjusted 5v5 xG% = 50.8% (17th, pct 48.4) vs raw 53.0% (11th). 7 of 10 at home. Raw possession is inflated by trailing + home ice.
xG-Pythagorean win% .525 = 13th. Counterfactual GD with league-avg finishing (+5.2) and league-avg PK results (+2.9): about +7 vs actual -1.

Schedule: opp avg pts% .550 (league .554) = NOT soft by record. Opp all-sit xG% .476 (league .499), adj 5v5 .473 (league Q1 .458, median .510) = soft by underlying quality. SEA x2, SJS, VAN, PHI, WPG all sub-.47.

Persistence (team metric, 2024-25 -> 2025-26 full seasons, r): CF% .74, 5v5 xGF/60 .55, PP xGF/60 .47, sh% .37, 5v5 xGA/60 .33, finishing GF-xGF .26, PK xGA/60 .11, GSAx .05, PK GA-xGA -.07.
DET baselines: finishing -22.3 (26th) and -17.4 (24th) last two seasons; current pace -50/82. Roster's prior two seasons combined: 432 G on 450 ixG (-4.1%); this season -18.4%. Chronic under-finishers: Copp -13, Rasmussen -10, Kasper -7, Finnie -6, Compher -6. Over: DeBrincat +11, Raymond +8, Faulk +6.
PP xGF/60 ranked 7th both prior seasons (8.6, 8.2) -> real strength. PK xGA/60 32nd and 28th prior -> chronic; this year 21st is an improvement in process; Gibson .679 on PK (9 GA on 4.77 xGA) is the results gap.
Gibson GSAx +15.3 (24-25), +11.7 (25-26): his 5v5 is real. Tarasov -4.4, -1.8 prior; .940 now = regression candidate.
Projection: MoneyPuck 88.1 pts, 22% playoffs (preseason 88.6 / 25.5%). Season is 84 games; site labels say per 82.

Site change 2026-10-23: paces are per 84 (pipeline/config.json season_games). xgPointsPerSeason now 97.8 at 10 GP (was labelled per 82). Use per-84 in the article for any pace; MoneyPuck's 88.1 projection is already on the 84-game schedule.

---
# 2026-10-23 finishing deep dive (for "Exactly how bad the Red Wings are at finishing")
Data: MoneyPuck teams/skaters summary (raw/2026-10-23) + MoneyPuck shot-level files shots_2021..2026 (scratchpad only, 68MB each; regular season, shootouts excluded). Danger bands = xG <.08 low, .08-.20 medium, >=.20 high. Shot-level totals differ slightly from summary (32.78 vs 33.09 xGF); quote summary for team totals, shot-level for detail.

Intro check: "top-10 offensive team from chance creation" — true for volume (CF/60 7th, SOG/60 8th, MD shots/60 6th), not for xG (xGF/60 12th raw, 13th score/venue adj, 14th flurry adj; 5v5 14th-16th). HD shots/60 27th. Say "top-10 in shot volume, top-half in expected goals, 2nd on the PP."

Team, all situations: 27 GF on 33.09 xGF (-6.09, 4th worst behind MIN -9.37, PHI -9.00, CGY -7.07; per game -0.61). Sh% 9.0 (league 11.3). GF/60 23rd vs xGF/60 12th.
By danger: high 10 G on 6.75 xG (+3.25, 52.6% conv vs 35.5% expected) | medium 8 G on 17.67 xG (-9.67, 5.5% vs 12.2% expected; league 11.8%) | low 9 on 8.67 (+0.33).
  -> the entire deficit is medium danger. High danger and rebounds (8 G on 5.57 xG, +2.43) are ABOVE expected.
  MD on-goal rate 64% vs league 68%; MD sh% on shots that reach the net 9.6% vs league 17.3%.
  MD by distance: 0-9 ft 2/38 (5.05 xG), 10-19 3/39 (4.56), 20-29 4/36 (4.68), 30-39 0/34 (3.58, 26 on goal).
  MD by type: snap 2/48 (5.89 xG), wrist 5/46 (5.72), tip 2/30 (3.20), backhand 0/12, slap 0/6, deflection 0/4.
5on5: 18 on 20.77 (-2.77, 10th worst); 5on4: 6 on 9.19 (-3.19), MD 0 for 37 on 4.72 xG; other: 3 on 2.71.
Shot type all-sit: wrist 12/11.17 (+0.83) fine; snap 10/10.75; tips 3/4.70; backhand 1/3.24; slap 0/1.59.
Score state: tied 7 G on 12.09 xG (-5.09) = the whole gap; trailing -0.58, leading -0.11. Period 2: 8 on 12.12 (-4.12); period 3: 11 on 9.19 (+1.81).
Position: forwards -7.6 (LW -3.32, C -2.63, RW -1.61); defensemen +1.46 (Faulk 2 on 0.65, Wallinder 2 on 0.14).

Historical context (160 team-seasons 2021-22 to 2025-26, first 10 games):
- Overall GF-xGF -5.78 (shot-level): 27 of 160 starts were worse (~17th pctile). Mean -0.55, sd 5.63. Worst: 2022-23 FLA -14.47, 2023-24 WSH -13.70, 2023-24 SJS -13.29, 2024-25 EDM -12.31. So NOT historically extreme overall.
- Medium-danger G minus xG -8.86 (9 on 17.86, 6.1%): WORST of all 160. Next: 2022-23 NSH -8.32, 2021-22 TOR -7.69, 2024-25 EDM -6.83, 2025-26 CGY -6.33.
- 147 MD shots in 10 games is also the most of any DET start since 2021 (70-94 prior years) — volume is up, conversion collapsed.
- Persistence: corr(first-10 GF-xGF, rest-of-season GF-xGF per game) = 0.04. Bottom-quintile starters finished -1.7 per 82 the rest of the way; all teams -2.7; top quintile -1.0. Early finishing has ~zero predictive value.
- 2024-25 EDM -12.31 through 10 -> -4.19 over remaining 72; 2023-24 COL -10.85 -> +21.52; 2021-22 TOR -9.30 -> +26.65. But 2023-24 FLA -10.23 -> -29.19 and 2022-23 NSH -9.41 -> -34.48. Both tails exist.
- DET own starts: 2021 -2.23, 2022 +1.71, 2023 +7.39, 2024 -0.91, 2025 +3.21, 2026 -5.78.

Game log (goals exclude SO): NYR 0 on 1.72 (MD 0/5), WPG 2 on 4.77 (MD 0/16), OTT 5 on 3.57, SEA 3 on 3.63 (MD 0/15), MTL 0 on 3.57 (MD 0/20), NJD 4 on 2.25, PHI 2 on 3.63, SJS 3 on 3.16, SEA 3 on 2.56, VAN 5 on 3.92.
  The three regulation losses NYR/WPG/MTL: 2 goals on 10.06 xG, 0 for 41 on medium-danger shots (5.25 xG). Fowler (MTL rookie) 30 saves on 2.13 xG; Garand (NYR) 23 on 1.38.

Goalies faced: collectively .910 vs DET (301 SOG, 27 GA, 22.70 xGA, GSAx -4.30). Those same nine goalies vs everyone else: .883, GSAx -42.4 (Lankinen .802, Ersson .794, Fowler .852, Allen .890). Detroit has faced a weak goalie slate and still shoots 9.0%. Fowler and Garand pitched shutouts vs DET and are -3.7 / -4.6 GSAx otherwise.

Shooters, all situations (G / ixG, diff): DeBrincat 6/5.24 +0.76 | Raymond 3/4.79 -1.79 | Arvidsson 4/4.45 -0.45 | Brandsegg-Nygård 2/3.89 -1.89 | Finnie 4/2.67 +1.33 | Copp 1/2.23 -1.23 | Larkin 1/1.88 -0.88 (8 GP, 4.5% on 22 SOG) | Rasmussen 1/1.30 | Mazur 0/0.97 | Dries 0/0.97 | Seider 0/0.96 (17 SOG) | Faulk 2/0.65 +1.35 | Wallinder 2/0.14 +1.86.
  Medium danger by shooter: DeBrincat 3/23 (2.84 xG) | Raymond 0/23 (2.68) | Arvidsson 0/20 (2.53) | Copp 0/14 (1.71) | Finnie 2/10 | Brandsegg-Nygård 1/16 (1.90) | Larkin 0/8 (0.96).
  Raymond + Arvidsson + Copp + Larkin: 0 goals on 65 MD shots, 41 on net, 7.88 xG.
  Prior two seasons: DeBrincat +11.0 (1.16 G/xG), Raymond +7.8 (1.18), Faulk +6.1, Arvidsson +0.9, Seider +0.8, Larkin -3.7 (0.94), Compher -5.6, Finnie -6.2 (0.68, one season), Kasper -6.8, Rasmussen -9.9 (0.63), Copp -13.2 (0.59).
  League context: no Red Wing is among the 15 biggest individual under-finishers (Eriksson Ek -4.87 leads). Detroit's gap is spread across the lineup, not one player.

Cost: ~9.7 goals below expected on medium-danger shots alone ≈ 3 standings points at ~3 goals per point. Overall -6.1 ≈ 2 points.
Shape for this section: lead with the medium-danger split (worst in five years of 10-game starts), show that high-danger and rebounds are fine, then the goalie slate, then the shooters. Historical persistence (r = .04) belongs in the sustainability section, not here.

---
# 2026-10-23 CORRECTION + "how do they fix medium danger" analysis
MoneyPuck re-banded its xG model for 2026-27: league MD shots per team-game 8.2 (2025-26) -> 12.1 (2026-27); HD 3.1 -> 2.3; share of MD shots from 30+ ft 9% -> 18%. Cross-season comparisons must be RATIO-based (G/xG, conv %, volume relative to that season's league), not raw G-xG or raw counts.
CORRECTED historical claims (160 ten-game starts, 2021-22 to 2025-26):
- MD finishing G/xG 0.50 (9 on 17.86): 9 of 160 starts were worse (~6th pctile). Worst: 2023-24 SJS 0.25, 2025-26 CGY 0.32, 2022-23 NSH 0.32, 2021-22 SEA 0.40, 2024-25 EDM 0.47. Say "bottom ten of 160," NOT "worst ever."
- MD conversion 6.1%: 8 of 160 worse.
- MD volume 1.22x league: 17 of 160 higher. DET prior years 0.82, 0.84, 1.06, 0.93, 1.14. Say "about 20% more medium-danger shots than league average," NOT "most ever."
- HD volume 0.78x league (1.80/gm vs 2.30): 24 of 160 lower. MD:HD ratio 8.2 vs league 5.2.
- All-shot G/xG 0.82: 32 of 160 worse (~20th pctile).
Persistence: team MD finishing (G-xG) yoy r = .25 (24-25 -> 25-26); team all-shot finishing .26; shooter MD G/xG (>=40 MD shots both years, n=166) .24. ~6% of variance is repeatable.

Where the MD deficit sits (shot-level, DET 2026, 147 MD shots):
- Set shots (5s+ since last event): 9 on 14.95 xG, 7.3% conv; league converts these BEST (14.9% last season, 12.2% this). 2-5s: 0 for 22. So the gap is on the most convertible shot type -> noise signal.
- Middle lane (|y|<5 ft): 0 for 46 on 6.03 xG (league 14.3%). 23 of those are tips, 10 on net, 0 goals. Arvidsson 7, Copp 5, Finnie 5, Rasmussen 5 (0 on net), Dries 4.
- 30+ ft: 0 for 34 on 3.58 xG, 26 on net. 23% of MD shots vs league 18% (4th highest; sd 4%). Raymond 9, DeBrincat 9, Arvidsson 4. 21 snap shots. 15 on the PP, 12 at 5v5, 5 at 3v3. League converts 30+ MD at 8.9% vs 13.3% inside 30.
- Straight-on (<15 deg): 0 for 37 on 4.64.
- Last event HIT: 0 for 25, only 44% on net. Last event BLOCK: 0 for 27.
- On-goal rate 64% vs league 68% (DET 71% last season). Across teams corr(MD conv, on-goal%) = .33; corr with quick-release share -.29; with 30ft+ share -.09.
- Shot quality within band: avg xG .122 vs league .126; 56% of DET MD shots in the .08-.12 tercile vs league 50%.
- Rebounds: 4% of DET MD shots vs league 12%. xRebound 13.1, actual 14 (fine). Goalie froze 16 (x 14.4).
- Shooter class (prior 2-yr G/ixG): proven >1.05 (DeBrincat, Raymond, Faulk) 48 shots 4 G 5.74 xG | average (Larkin, Arvidsson, Seider, Kolesar) 33 shots 0 G 4.15 xG | under <.85 (Copp, Finnie, Compher, Kasper, Rasmussen) 33/3/3.90 | rookies (Brandsegg-Nygård, Mazur, Dries, ASP, A. Johansson) 33/2/4.08. Rookie+under share 45% vs league 37% (9th highest).
- PP MD: 38 shots, 1 G (DeBrincat), 4.80 xG. DeBrincat 10, Raymond 9, Arvidsson 6. 15 of 38 from 30+ ft, 13 from 20s. Flank shots. PP HD: 8 shots, 4 G.
- Shot type MD: snap 2/48 (league 14.8%), wrist 5/46 (13.6%), tip 2/30 (8.5%), backhand 0/12, slap 0/6, deflection 0/4.

Lever sizing per 10 games (rough): regression of MD conv from 6.1% to ~12% = +8.7 G. HD volume to league (1.80 -> 2.30/gm = +5 shots x ~35%) = +1.75 G. On-goal 64 -> 68% (+6 SOG x 17%) = +1 G. Cutting 30+ share to league (7 fewer long shots, redistributed inside) ≈ +0.3 G. Regression dwarfs every coaching lever.
Quotes (Detroit Hockey Now, Bob Duff, Oct 18): McLellan on Raymond: "Obviously, he doesn't have a hot stick." / "there's going to be a lot of pressure put on DeBrincat and Raymond in particular, to finish and produce." / players "get so focused on the goal – I got to get a goal, I got to, I got to – that some of the other things don't go real well." Raymond: "I feel like I'm getting a lot of looks and creating a lot of chances. So as long as I can keep doing that, I know it'll go in." 11 roster players without a goal as of Oct 18.

---
# 2026-10-25 update: after 1-4 L at CGY (Oct 24). 11 GP, 4-4-3, 11 pts, 22nd by points, GF 29 GA 34 GD -5.
Data: raw/2026-10-25 (MoneyPuck 2026 teams/skaters/goalies; NHL standings 2026-10-25 via dated endpoint, /standings/now returned empty 3x). Shot-level shots_2026 refreshed (14,926 rows). Site nightly ran 12:00Z 10/25 and includes CGY: radar finishing 3.2 (rank 31), goaltending 51.6, attacking 58.1, defending 80.6, possession 77.4, PP 100.0 (1st), PK 32.3; xgPointsPerSeason 100.9; MoneyPuck proj 90.6 pts / 26.2% playoffs. Top 3 still CAR/BOS/EDM.
CGY game: 1 G on 2.78 xG, 29 SOG, MD 1/11 (1.33), HD 0/2; Cooley .966 vs DET (.898 otherwise). PK gave up 3 (PK GA 12 on 7.73 xGA season).

Team all-sit: 28 GF on 35.86 xGF = -7.86, 2nd worst (MIN -10.99, PHI -7.78). Sh% 8.5 (30th; league 11.4). GF/60 25th vs xGF/60 14th (adj 15th). CF/60 7th, SOG/60 8th, MD/60 7th, HD/60 26th.
Danger: high 10 on 7.43 (+2.57, 47.6% vs 35.4%) | medium 9 on 19.00 (-10.00, 5.8% vs 12.2%; league 11.6%) | low 9 on 9.44 (-0.44). Rebounds 8 G on 35 (shot-level 8 on 6.40 xG, +1.60). PP MD 0 for 39 on 4.98. 5on5 19 on 22.74 (-3.74, 7th worst). 5on4 6 on 9.90.
MD on-goal 65% vs 68%; MD sh% on net 9.8% vs 17.1%. 30-39 ft still 0/34. Middle lane 1/52 (6.75 xG). Set shots 5s+ 9/132 (6.8%). After HIT 0/28, after BLOCK 0/29.
Score state: tied 7 on 12.93 (-5.93); trailing -1.51; leading -0.11. P1 -3.57, P2 -4.18, P3 +1.07. Forwards -8.95 (C -3.19, LW -3.82, RW -1.94), D +1.08.
Four regulation losses (NYR, WPG, MTL, CGY): 3 G on 12.84 xG, MD 1 for 52 (6.58 xG).
Goalies faced: .915 vs DET (330/28/24.86, GSAx -3.14); same ten vs others .881, GSAx -54.2. Cooley .966/.898, Fowler 1.000/.878, Garand 1.000/.881.
Percentiles (DET / top3 avg): finishing 3.2/86.0 (rank 31) | GSAx 51.6/48.4 (+0.98, 16th) | 5v5 xGF/60 58.1/65.6 (14th) | 5v5 xGA/60 80.6/74.2 (7th) | CF% 80.6/59.1 (7th; site shows 77.4) | PP xGF/60 100/66.7 (1st, 9.80) | PK xGA/60 32.3/54.8 (22nd) | PK GA-xGA 3.2/26.9 (31st, -4.27) | adj 5v5 xG% 54.8 (51.6%, 15th) | raw 5v5 xG% 53.0 (11th).
xG-Pythag .542 = 11th (was 13th). Counterfactual: finishing to avg +7.1, PK results to avg +4.3 -> GD -5 becomes about +6.
Schedule: opp pts% .525 vs league .555 -> NOW soft by record too (CGY .400). Opp all-sit xG% .468 (league .498); adj 5v5 .469 (median .510, Q1 .454). 7 of 11 at home.
Goalies: Gibson all .867, GSAx -4.23 (8 GP); 5v5 .909 +0.67; PK .633, 11 GA on 4.99 xGA, -6.01. Tarasov .940 +5.08 (4 GP). Postava 1 GP.
Skaters: DeBrincat 6/5.48 | Raymond 3/4.94 (-1.94; 8.8%; MD 0/23) | Arvidsson 4/4.81 (MD 0/20) | Brandsegg-Nygård 2/3.98 (-1.98) | Copp 2/2.89 (scored vs CGY; MD 1/15) | Finnie 4/2.87 | Larkin 1/2.46 (9 GP, 3.6% on 28 SOG; MD 0/12) | Rasmussen 1/1.42 | Seider 0/1.02 on 20 SOG | Mazur, Dries 0/0.97 | Faulk 2/0.68 | Wallinder 2/0.20. Raymond+Arvidsson+Copp+Larkin MD: 1 for 70, 8.48 xG. No DET skater in league bottom 15 (Eriksson Ek -4.98 leads).
Shooter class MD: proven 4/49 (5.88) | average (Larkin, Arvidsson, Seider, Kolesar) 0/37 (4.68) | under 4/38 | rookies 2/34. Rookie+under 46% (11th).
Historical, 11-game windows, ratio-based (160 team-seasons): MD G/xG 0.52 -> 7 of 160 worse; MD conv 6.3% -> 7 worse; all-shot G/xG 0.79 -> 20 worse; HD volume 0.72x league -> 21 lower. (MD volume ratio moved 1.22x -> 1.08x with the window change; quote MD/60 rank 7th instead.)
Lever sizing per 11 games: MD conv to 12% = +9.0 G; HD volume to league (1.82 -> 2.43/gm) = +2.3; on-goal 65 -> 68% = +0.8; 30ft+ share 22 -> 18% = +0.3.
Claim status after CGY: (1) still overstated but now three elite traits (possession 7th, 5v5 defending 7th, PP generation 1st); (2) strengthens: GD -5 -> ~+6 at league-avg finishing+PK, Pythag 11th; PK is now a results problem too (31st GA-xGA); (3) schedule soft by record AND quality now; (4) unchanged; finishing pace -60 per 84; MoneyPuck 90.6.

---
# 2026-10-27 update: after 4-3 SO W at EDM (Oct 26). 12 GP, 5-4-3, 13 pts, 17th by points, GF 33 GA 37 GD -4 (NHL; MoneyPuck GF 31 on 38.96 xGF, GA 35 on 35.69). Road trip 2-1-1. Next: Oct 29 vs CHI.
Reframe (Mark, Oct 27): lead with the Edmonton positives, then finishing and the PK as what keeps results from matching process; every season-long metric compared against the good and bad in the Edmonton game.
Data: raw/2026-10-27 (MoneyPuck 2026 teams/skaters/goalies; NHL standings via dated endpoint; club schedule; boxscore + landing JSON for 2026020187). shots_2026 refreshed (15,620 rows); EDM game present as game_id 20187 but carries NO BLOCK rows for either team (NHL box: DET blocked 11, EDM blocked 14), so MoneyPuck attempt shares for this game are unblocked-only. Site nightly ran 12:00Z 10/27 and includes EDM. Top 3 by points CAR/BOS/EDM (MIN tied with EDM at 18; the site radar used CAR/BOS/MIN).

EDM game, official: DET 4-3 SO. Podkolzin EV 6:10 P1 (Draisaitl centering pass, double deflection off Podkolzin's then Mazur's skate); Arvidsson PP 8:35 P2 (Raymond cross-ice feed, one-timer from the left circle); Howard PP 4:18 P3 (Brandsegg-Nygård tripping); Finnie EV 4:48 P3 (Arvidsson dug it out behind the net, putaway at the right pad); Dach EV tip 16:32 P3 (Shea point shot); Larkin 6v5 18:43 P3 (loose puck at the top of the crease, five-hole, Postava pulled); Raymond SO winner. PP 1/4, PK 2/3. Postava first NHL start 24/27 + 3/3 in the SO (recap says 25 saves); third DET goalie in 25 years to win his first start (Mrazek 2013, Howard 2005). Jarry 25/28. SOG 28-27 DET.
EDM game, MoneyPuck: DET 3 G on 3.10 xG (-0.10), 29 SOG, 42 unblocked attempts; EDM 3 on 2.71, 28 SOG, 45 unblocked. 5v5 xG 1.97-1.06 = 65.0% (4th best of the season behind VAN 66.3, WPG 65.8, PHI 65.2); unblocked attempts 30-28 at 5v5; all-sit attempts with NHL blocks 56-56. HD: DET 0/2 (0.96 xG; Arvidsson 7 ft wrist off the net, Arvidsson 5 ft rebound saved); EDM 0 HD shots. MD: DET 2/11 (1.33 xG, 9 on net): Arvidsson 28 ft PP snap (.126), Larkin 10 ft wrist, middle lane, after a block (.134). LD: 1/29 (Finnie 8 ft wrist, .042, 30-degree angle, 1 s after a takeaway). Inside 10 ft: 9 shots 2 G (season 90 shots, 13 G on 13.92 xG). Rasmussen 4 MD shots from 7-14 ft, all on net, 0 G. Raymond MD 0/1 (27 ft, missed). 30ft+ MD: 1 (Larkin 32 ft slap, saved); season 0/35. PP: 5 attempts, 0.51 xG, 1 G; season PP xGF/60 fell 9.80 -> 9.26, rank 1st -> 5th. PK: EDM 13 attempts, 1.21 xGA, 1 GA across 3 kills (~12 xGA/60 vs season 8.67); Postava 6/7 on PP shots. 3v3: DET 2 attempts 0.26, EDM 4 attempts 0.44 (Bouchard slot save with 9 s left). Postava MP line 28 SOG / 3 GA / 2.71 xGA = -0.29 GSAx. Jarry .897 vs DET, .853 vs everyone else.
Mark's recollection check: he remembered no MD goals and buried HD chances. MoneyPuck says the reverse by band (2 MD goals, 0 HD goals). By location his read holds: two of three goals came from inside 10 ft (Finnie 8, Larkin 10); the model grades them low/medium for angle and sequence, and the two shots it calls high danger (Arvidsson, 5 and 7 ft) did not go in. Write "they scored at the net," not "they finished high-danger chances."

Season vs EDM (for the new lead section): 5v5 xG% 54.0 (9th) | 65.0. 5v5 CF% 54.0 (8th) | 51.7 unblocked, 50.0 with NHL blocks. 5v5 xGA/60 2.13 (4th) | 1.06 xGA in the game, 0 HD against (season 5v5 HD against/60 1.42, 12th). Finishing -7.96 (31st) | -0.10. Sh% 8.7 (31st) | 10.3. MD conv 11/167 6.6% (MP summary; shot-level 12/169 7.1%) | 2/11. HD conv 10/23 43.5% | 0/2. Inside 10 ft 13/90 | 2/9. MD 30ft+ 0/35 | 0/1. PP 7 G on 10.41 xG, 9.26/60 5th | 1 for 4 on 0.51 xG. PK 13 GA on 8.95 xGA, 8.67/60 26th, GA-xGA 29th | 1 GA on 1.21 xGA. GSAx +0.69 17th | Postava -0.29.
Record splits (12 GP): G-xG >= -0.2 (OTT, NJD, SJS, SEA2, VAN, EDM) 4-0-2; under: 1-4-1. 5v5 xG% >= 55 (WPG, OTT, SEA1, PHI, VAN, CGY, EDM) 4-3-0; under 50 (NYR, MTL, NJD, SJS, SEA2) 1-0-3; 50-55 (NYR 50.0) counted in the >=50 bucket as 0-1-0. Eight points from the seven dominant games, five from the five outplayed ones.

Team season ranks (12 GP): finishing -7.96 31st (MIN -13.1, PHI -7.78); sh% 8.66 31st (league 11.4); GF/60 28th vs xGF/60 15th; adj 5v5 xG% 52.7% 13th, raw 54.0% 9th. CF/60 9th, SOG/60 9th, MD/60 8th, HD/60 26th. 5v5 xGA/60 2.13 4th (was 7th). 5v5 CF% 8th. PP xGF/60 9.26 5th, PP GF/60 6.22 23rd. PK xGA/60 8.67 26th, PK GA/60 12.6 25th, PK GA-xGA -4.05 29th. GSAx +0.69 17th. 5v5 GF-xGF -4.71 26th. HD GF-xGF +1.62 13th; MD -9.34 31st; LD -0.24 14th.
Danger (MP summary): HD 23 / 8.38 / 10 (+1.62, 43.5%; xG/shot 36.4%; league actual 34.7%) | MD 167 / 20.34 / 11 (-9.34, 6.6% vs 12.2% expected; league 11.7%) | LD 348 / 10.24 / 10 (-0.24) | all 538 / 38.96 / 31. Shot-level: MD 12 on 20.53, HD 9 on 8.03, rebounds 8 on 7.17 (+0.83). MD on-goal 66% vs 68%; MD sh% on net 10.8% vs 17.2%. 30-39 ft 0/35 (27 on net; Raymond 9, DeBrincat 9; 21 snap; 15 PP). Middle lane 2/55 (7.05; Copp, Larkin); 28 tips, 14 on net, 0 G. Set shots 5s+ 11/142 (7.7%); 2-5 s 1/26. After HIT 0/30 (14 on net); after BLOCK 1/31; after FAC 3/36. PP MD 2/44 (5.55 xG; DeBrincat, Arvidsson; 15 from 30+ with 0 G; 20s band 2/15). Score state: tied 7 on 13.58 (-6.58), trailing -0.97, leading -0.11. P1 -3.98, P2 -5.10, P3 +2.56. Forwards -8.90 (L -4.35, C -2.33, R -2.22), D +0.93.
Four regulation losses unchanged: 3 G on 12.84 xG, MD 1/52.
Goalies faced (11): .914 vs DET (359/31/26.99, GSAx -4.01); same eleven vs others .882, GSAx -63.0. Jarry .897/.853, Cooley .966/.904, Fowler 1.000/.906, Garand 1.000/.881, Lankinen .839/.802, Ersson .861/.794.
Percentiles (DET / top-3 CAR-BOS-EDM avg): finishing 3.2/86.0 (31st) | GSAx 48.4/47.3 (17th) | 5v5 xGF/60 58.1/64.5 (14th) | 5v5 xGA/60 90.3/74.2 (4th) | CF% 77.4/58.1 (8th) | PP xGF/60 87.1/68.8 (5th) | PK xGA/60 19.4/60.2 (26th) | PK GA-xGA 9.7/31.2 (29th) | adj 5v5 xG% 61.3 (13th). Site radar (top3 CAR/BOS/MIN): finishing 3.2, goaltending 48.4, attacking 58.1, defending 90.3, possession 77.4, PP 87.1, PK 19.4.
xG-Pythag .544 = 10th. Counterfactual: finishing to avg +8.0, PK results to avg +4.1 -> GD -4 becomes about +8.
Schedule (regular season only): opp pts% .542 vs league .557 (EDM .750 is the first top-tier opponent); opp adj 5v5 xG% .469 vs median .505, Q1 .451; 7 of 12 games vs teams under .460 (WPG, SEA x2, PHI, SJS, VAN, CGY). 7 of 12 at home.
Goalies: Gibson all .867, GSAx -4.23 (8 GP); 5v5 .909 +0.67; PK .633, 11 GA on 4.99. Tarasov .940 +5.08 (4 GP). Postava 2 GP .889 -0.29.
Skaters (all-sit G/ixG): DeBrincat 6/5.69 (+0.31; MD 2/25) | Arvidsson 5/6.02 (-1.02; MD 1/21; HD 2/6) | Raymond 3/5.24 (-2.24; 8.1% on 37 SOG; MD 0/24) | Brandsegg-Nygård 2/3.98 (-1.98; MD 1/16) | Larkin 2/3.03 (10 GP; 6.3% on 32; MD 1/16) | Copp 2/2.96 (MD 1/16) | Finnie 5/2.91 (+2.09; MD 2/12) | Rasmussen 1/1.89 (MD 1/12) | Seider 0/1.04 on 23 SOG | Mazur 0/0.99, Dries 0/0.97 | Faulk 2/0.75. Raymond+Arvidsson+Copp+Larkin MD: 3 for 77 (9.41 xG); two of the three came in Edmonton. No DET skater in league bottom 15 (Eriksson Ek -5.58 leads).
Shooter class MD: proven 4/51 (6.08) | average (Larkin, Arvidsson, Seider, Kolesar) 2/42 (5.34) | under 4/42 (4.91) | rookies 2/34 (4.19). Rookie+under 45% (10th).
Historical, 12-game windows, ratio-based (160 team-seasons): MD G/xG 0.58 -> 8 of 160 worse; MD conv 7.1% -> 8 worse; all-shot G/xG 0.80 -> 17 worse; HD volume 0.67x league -> 22 lower. MD volume 0.99x league in the window; quote MD/60 rank 8th.
Lever sizing per 12 games: MD conv to 12% = +8.3; HD volume to league (1.83 -> 2.42/gm) = +2.5; on-goal 66 -> 68% = +0.6; 30ft+ share 21 -> 18% = +0.2.
Quotes (NHL.com recap, Gerry Moddejonge, Oct 26): McLellan: "I'm really proud of the group, we responded well after what happened in Calgary. We checked well, kept some pretty good offensive players in check for the most part. The penalty kill did a really good job, and Postava." Arvidsson: "We played as a five-man unit and we helped each other out, and 'Posty' was unbelievable in net... Obviously, they're really good offensively and I think we shut them down really good." Babcock: "I thought they were better than us in the second... I thought their goalie made real good saves on our power play." Postava: "It's amazing, I feel like a kid."
Claim status after EDM: (1) still overstated; elite traits now 5v5 defending (4th) and possession (8th), PP generation slipped 1st -> 5th after a 0.51 xG power-play night; (2) holds: GD -4 -> ~+8 at league-avg finishing + PK results, Pythag 10th, PK 26th process / 29th results; (3) holds but softer by record (.542 vs .557), still bottom-quartile by quality; (4) unchanged; finishing pace -56 per 84; MoneyPuck 91.5 pts / 29.9% (preseason 88.6 / 25.5%); site xG-points pace 101.0 (10th); actual pace 91.
Larkin goal, why MoneyPuck graded it medium (.134) from 10 ft dead center: MoneyPuck's model is probability-based, not location-based. Inputs that pushed it down: lastEvent BLOCK 25 s earlier, speedFromLastEvent 0.5 ft/s (puck effectively stationary from the model's view), shotRebound 0, shotRush 0. The model never sees the goalie's position or that the puck was loose at Jarry's feet; 6v5 does not hurt it (league 6v5 same-spot avg xG .21). League 2026-27, wrist shots 8-12 ft under 15 degrees: 106 shots, avg xG .169, actual conv 17.9%; non-rebound 79 shots avg .182, conv 22.8%; non-rebound with last event 10+ s ago avg .174, conv 16.3%. Only 12% of all 8-12 ft shots clear .20; those are mostly rebounds (36%) or quick plays (median 3 s since last event). By a location-based definition (NST home-plate inner zone) it is a high-danger shot. Article phrasing: "high danger by location, medium by the model" or just "at the net."

# 2026-10-29 update: league ranks refreshed, Detroit idle since EDM (Oct 26)

Mark flagged the site radar moving (finishing 3.2 -> 6.5, PK 19.4 -> 25.8). Detroit did not play Oct 27-28; every move is other teams playing (CHI tonight, Oct 29). Raw pull in raw/2026-10-29/ (teams, skaters, goalies, standings). Site dashboard.json regenerated 2026-10-29T12:10Z, commit 3b2cca6.

Method note: the site's radar percentile = share of the OTHER 31 teams strictly worse (pipeline/build_site_data.py pct_rank). Ties do not count as worse, so tied teams share the better rank. My earlier sort-based ranks differed on tied metrics (CF% and xG% are rounded to 2 decimals in MoneyPuck, so ties are common). scripts/ranks.py now uses the site method; all 7 radar values reproduce exactly. Use ranks.py <raw dir> <top3 by pts> <top3 site>.

Standings Oct 29: 12 GP 5-4-3 13 pts, 21st in the league (was 17th on Oct 27), 8th of 8 Atlantic, 13th East. Top 3 by points = CAR 22, EDM 20, MIN 20 (BOS 19). Site radar top3 = CAR, MIN, EDM (points then regulation wins), now the same set as top-3 by points.

Radar / rank table, Oct 29 vs Oct 27 (DET raw unchanged except MoneyPuck model drift):
| metric | DET | rank Oct 29 | pctl Oct 29 | pctl Oct 27 | top3 avg Oct 29 |
| finishing GF-xGF | -8.01 | 30th | 6.5 | 3.2 | 51.6 (EDM +15.4 drags it) |
| sh% | 8.68 | 29th | 9.7 | 3.2 | 63.4 |
| GF/60 all | 2.51 | 27th | 16.1 | 12.9 | |
| xGF/60 all | 3.16 | 15th | 54.8 | 54.8 | |
| GSAx | +0.69 | 19th | 41.9 | 48.4 | 51.6 |
| 5v5 xGF/60 | 2.51 | 16th | 51.6 | 58.1 | 63.4 |
| 5v5 xGA/60 | 2.13 | 4th | 90.3 | 90.3 | 81.7 |
| 5v5 CF% | 54.0 | T-6th | 77.4 | 77.4 | 67.7 |
| 5v5 xG% raw | 54.0 | T-7th | 77.4 | 71.0 | |
| 5v5 xG% adj | 52.7 | 13th | 61.3 | 61.3 | |
| 5v5 CF/60 | 57.9 | 9th | 74.2 | 71.0 | |
| 5v5 SOG/60 | 27.2 | 9th | 74.2 | 74.2 | |
| 5v5 MD/60 | 10.45 | 13th | 61.3 | 64.5 | |
| 5v5 HD/60 | 1.22 | 28th | 12.9 | 12.9 | |
| 5v5 HDA/60 | 1.42 | 10th | 71.0 | | |
| PP xGF/60 | 9.24 | 6th | 83.9 | 87.1 | 86.0 |
| PP GF/60 | 6.23 | 21st | 35.5 | 29.0 | |
| PK xGA/60 | 8.67 | 24th | 25.8 | 19.4 | 67.7 (NYI 8.68, SEA 8.75 passed DET going the wrong way) |
| PK GA/60 | 12.60 | 26th | 19.4 | 22.6 | |
| PK GA-xGA | +4.05 | 29th | 9.7 | 9.7 | 38.7 |
| HD GF-xGF | +1.62 | 12th | 64.5 | 61.3 | |
| MD GF-xGF | -9.35 | 31st | 3.2 | 3.2 | TBL -9.36 is the only team worse |
| LD GF-xGF | -0.27 | 14th | 58.1 | 58.1 | |
| xG Pythag win% | .544 | 11th | 67.7 | 71.0 | |
Finishing bottom: MIN -13.0, PHI -9.3, DET -8.0, WPG -8.0, CHI -7.1. PK GA-xGA bottom: VGK 5.38, UTA 4.95, EDM 4.21, DET 4.05.
MoneyPuck drift without a game: DET xGF 38.96 -> 39.01, PP xGF/60 9.26 -> 9.24. Say "about" on anything to two decimals.

Projection: MoneyPuck 91.8 pts / 29.9% playoffs (Oct 27: 91.5 / 29.9%; preseason 88.6 / 25.5%). Site xG-points pace 101.0, 15th in the league (10th on Oct 27). Site xgPoints 14.4 vs actual 13 (-1.4). Next game swing: reg win +0.6 pts / +2.1% odds, reg loss -1.4 / -4.8%.

Artifact v7 carries all of the above (header 21st, comparison table ranks, claims, percentile table with Oct 29 / Oct 27 columns, intro check HD/60 28th, finishing para 3rd worst, PP para, projection). Shot-level sections untouched: Detroit's shots did not change; league shot baselines move only slightly.

## PK save percentage, Postava in EDM vs Gibson season (asked 2026-10-29)
Shot-level, game 20187, DET shorthanded (all 5v4): 13 EDM attempts, 7 on goal, 1 GA (Howard snap, 24 ft, .152) -> Postava .857 on the kill; 0.83 xG on the 7 on-goal shots, 1.21 on all 13. Hyman 8 ft (.192) and RNH tip 5 ft (.152) were the two best saves.
Postava season 4on5 (MoneyPuck goalies.csv): 8 SOG, 1 GA, 1.38 xGA, .875 (one shot came in the VAN relief).
Gibson season 4on5: 30 SOG, 11 GA, 4.99 xGA, .633 (all shorthanded strengths at shot level: 32 SOG, 11 GA, .656). Tarasov 4on5: 12 SOG, 1 GA, .917.
League PK sv% 2026-27 to date, shot level, on-goal shots with shooter up a skater: .841 (n=1,555).

## PK process with goaltending removed (asked 2026-10-29, Oct 29 teams.csv, 4on5)
| metric | DET | lg avg | median | DET rank (1 best) |
| xGA/60 | 8.67 | 7.69 | 7.56 | 24 |
| attempts against/60 | 110.5 | 96.2 | 93.9 | 26 |
| SOG against/60 | 48.5 | 48.5 | 47.9 | 18 |
| HD shots against/60 | 2.91 | 5.19 | 5.41 | 5 |
| MD shots against/60 | 46.5 | 37.1 | 38.2 | 29 |
| xG per SOG against | .179 | .159 | .158 | 28 |
| PK minutes per game | 5.16 | 4.87 | 4.77 | 21 |
| xGA per game | 0.75 | 0.62 | 0.61 | 27 |
| GA/60 | 12.60 | 8.12 | 7.79 | 26 |
| PK sv% | .740 | .840 | .840 | 29 |
DET 4on5: 61.9 min, 8.95 xGA, 13 GA, 50 SOG against.
Decomposition of the ~5 excess PK goals (13 GA vs ~8 at league GA/60 on DET's minutes): chances above league rate on DET's minutes ~1.0 goal; extra PK time (5.16 vs 4.87 min/game) ~0.45; goaltending (.740 vs .840 on 50 SOG) ~5.0 (overlaps; GA-xGA is 4.05). Read: process is bottom-third, not broken; goaltending is most of the damage. Shape: lots of attempts and medium-danger looks (bottom 4), very few high-danger (top 5), so the kill keeps shooters out of the crease but lets them shoot a lot from the second layer. PK persistence r=.11 across years, so the process rank is also soft.

## Penalties taken, 2025-26 vs 2026-27 (asked 2026-10-29; MoneyPuck teams.csv, raw/2026-10-29/teams_2025.csv added)
| | 2025-26 (82 GP) | rank (1 = most) | 2026-27 (12 GP) | rank | league 25-26 -> 26-27 |
| PK min/game (4on5) | 4.00 | 30 | 5.16 | 12 | 4.51 -> 4.87 |
| PP min/game (5on4) | 4.81 | 7 | 5.62 | 4 | 4.51 -> 4.86 |
| net PK minus PP | -0.81 | 32 (best in NHL) | -0.46 | 21 | 0 |
| penalties taken/game | 3.52 | 12 | 4.42 | 4 | 3.49 -> 3.86 |
| penalties drawn/game | 3.17 | 27 | 4.33 | 8 | 3.49 -> 3.87 |
| PIM taken/game | 7.52 | 17 | 9.83 | 5 | 7.79 -> 8.72 |
Totals: 25-26 328 PK min, 289 penalties, 617 PIM; 26-27 61.9 PK min, 53 penalties, 118 PIM.
Read: PK time up 29% vs league up 8%. Last year they were the 3rd least-shorthanded team and had the league's best special-teams time margin; this year 12th most shorthanded. Extra PK time vs last year's rate = 1.16 min/game x 12 = 13.9 min ~ 2.0 xGA at this year's 8.67/60. Note MoneyPuck penaltiesAgainst counts all infractions incl. offsetting/misconducts, so counts run above PK opportunities. League-wide rates are higher in October, so expect some of this to fall with the league.

## Gibson PK save % by season (asked 2026-10-29; MoneyPuck goalies.csv 4on5, files goalies_2024.csv / goalies_2025.csv added to raw/2026-10-29/)
| season | team | GP | PK SOG | GA | xGA | sv% | GSAx | rank among goalies w/ 60+ PK SOG | league PK sv% |
| 2024-25 | ANA | 29 | 82 | 15 | 14.46 | .817 | -0.54 | 50/61 | .854 |
| 2025-26 | DET | 57 | 195 | 30 | 32.73 | .846 | +2.73 | 44/67 | .856 |
| 2026-27 | DET | 8 | 30 | 11 | 4.99 | .633 | -6.01 | 58/61 (min 8 SOG) | .840 |
Context: his two prior years are a slightly below-average PK sv% but at-or-above expected on xG (shots he faces on the kill are dangerous). Last year he was +2.7 GSAx on the kill. Talbot DET 25-26 PK .849, -2.0; Talbot 24-25 .791, -7.1. Lyon 25-26 BUF .890 +5.7. Tarasov 24-25 CBJ .900, 25-26 FLA .884. 30 PK shots is ~15% of a Gibson season; .633 vs his .846 last year is about 6 goals of noise.

## 2026-10-29 article status
Draft reviewed (artifact Ndm7m61urQjvzfjB6Wyqn3, 25 edits, 24 approved + F06 as Mark's smaller fix) and applied to the Google Doc tab t.47n1rz9w3qbp; export matches research/style/finishing-final-expected-2026-10-29.txt. Article NOT yet built on the site. Two hyperlinks in the Doc: ESPN Larkin story on "waiting on the sidelines", site predictions post on "just 75 points". Aging claims to recheck at build time: "Monday night's", "tonight" (CHI, Oct 29), 12th-most PK minutes, 30th in finishing, Larkin status.
