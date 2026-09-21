#!/usr/bin/env python3
"""Derive every analysis JSON the brief and charts use, from the raw pulls.

Inputs (already in raw/):
  hsc/hsc_8484223.json         HockeyStatCards card + game logs (NST data, Luszczyszyn model)
  asp_gamelog_merged.json      HSC logs joined to the NHL API game log (dates, opponents)
  nhl/age20_d_cohort_onice.json  age-20 D cohort with MoneyPuck on-ice splits
  nhl/age20_cohort_careers.json  career totals for the cohort
  ../../../data/raw/moneypuck/*  the site pipeline's 2025-26 league + DET files
"""
import csv, json, pathlib, statistics

HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parents[2] / "data" / "raw" / "moneypuck"

out = {}

# --- 1. ASP season on-ice, all situations and 5v5 (MoneyPuck) ---
sk = list(csv.DictReader(open(SITE / "skaters.csv")))
def onice(row):
    ti = float(row["icetime"]) / 60
    gf, ga = float(row["OnIce_F_goals"]), float(row["OnIce_A_goals"])
    xgf, xga = float(row["OnIce_F_xGoals"]), float(row["OnIce_A_xGoals"])
    sf, sa = float(row["OnIce_F_shotsOnGoal"]), float(row["OnIce_A_shotsOnGoal"])
    return dict(gp=int(row["games_played"]), toi=ti, gf=gf, ga=ga, xgf=xgf, xga=xga,
                xgfPct=xgf / (xgf + xga) * 100, gfPct=gf / (gf + ga) * 100 if gf + ga else None,
                onIceShPct=gf / sf * 100, onIceSvPct=(1 - ga / sa) * 100,
                pdo=(gf / sf + (1 - ga / sa)) * 100,
                offIceXgfPct=float(row["offIce_xGoalsPercentage"]) * 100,
                relXgfPct=(float(row["onIce_xGoalsPercentage"]) - float(row["offIce_xGoalsPercentage"])) * 100)
out["asp_season"] = {r["situation"]: onice(r) for r in sk
                     if r["playerId"] == "8484223" and r["situation"] in ("all", "5on5")}

# --- 2. Detroit's defence, 5v5 (MoneyPuck season file; traded players are
#        listed once under their final team, so Faulk's row is STL+DET combined) ---
DMEN = ["Moritz Seider", "Simon Edvinsson", "Ben Chiarot", "Justin Faulk", "Albert Johansson",
        "Jacob Bernard-Docker", "Axel Sandin-Pellikka", "Travis Hamonic"]
out["det_d"] = [dict(name=r["name"], **onice(r)) for r in sk
                if r["name"] in DMEN and r["situation"] == "5on5"]

# --- 3. Pairings (DET-only file, so these are Detroit minutes) ---
ln = list(csv.DictReader(open(SITE / "lines_det.csv")))
pair = []
for r in ln:
    if r.get("position") != "pairing":
        continue
    ti = float(r["icetime"]) / 60
    if ti < 15:
        continue
    pair.append(dict(name=r["name"], toi=ti, gp=int(r["games_played"]),
                     xgfPct=float(r["xGoalsPercentage"]) * 100,
                     cfPct=float(r["corsiPercentage"]) * 100,
                     gf=float(r["goalsFor"]), ga=float(r["goalsAgainst"]),
                     xgf=float(r["xGoalsFor"]), xga=float(r["xGoalsAgainst"])))
pair.sort(key=lambda d: -d["toi"])
out["pairings"] = pair

# --- 4. Phase and month splits from the merged game log ---
rows = json.load(open(HERE / "asp_gamelog_merged.json"))
def agg(rs, label):
    n = len(rs); toi = sum(r["toi"] for r in rs)
    xgf = sum(r["xgf"] for r in rs); xga = sum(r["xga"] for r in rs)
    gf = sum(r["gf"] for r in rs); ga = sum(r["ga"] for r in rs)
    return dict(label=label, gp=n, toiPerGp=toi / n, xgf=xgf, xga=xga, gf=gf, ga=ga,
                xgfPct=xgf / (xgf + xga) * 100, gfPct=gf / (gf + ga) * 100 if gf + ga else None,
                gsPerGp=sum(r["gs"] for r in rs) / n,
                first=rs[0]["date"], last=rs[-1]["date"])
months = {}
for r in rows:
    months.setdefault(r["date"][:7], []).append(r)
out["months"] = [agg(rs, m) for m, rs in sorted(months.items())]
PHASES = [("Oct 9 - Nov 29: top-four minutes", "2025-10-01", "2025-11-30"),
          ("Dec: first demotion in ice time", "2025-12-01", "2025-12-31"),
          ("Jan 1 - Feb 4: the trough", "2026-01-01", "2026-02-05"),
          ("Feb 26 - Mar 6: post-Olympic break", "2026-02-06", "2026-03-31"),
          ("Apr 4 - 15: recalled", "2026-04-01", "2026-05-01")]
out["phases"] = [agg([r for r in rows if a <= r["date"] <= b], lbl) for lbl, a, b in PHASES]
out["halves"] = [agg(rows[:34], "first 34 games"), agg(rows[34:], "last 34 games")]

# --- 5. Age-20 cohort ---
coh = json.load(open(HERE / "age20_d_cohort_onice.json"))
car = json.load(open(HERE / "nhl" / "age20_cohort_careers.json"))
for c in coh:
    k = car.get(str(c["pid"]), {})
    c["careerGP"], c["careerP"] = k.get("gp"), k.get("p")
    c["ptsPer82"] = c["p"] / c["gp"] * 82
coh.sort(key=lambda c: c["pdo"])
out["cohort"] = coh
mature = [c for c in coh if int(c["season"][:4]) <= 2020]
def tier(lo, hi, label):
    g = [c for c in mature if lo < c["rel"] < hi]
    gp = [c["careerGP"] for c in g]
    return dict(label=label, n=len(g), medianCareerGP=statistics.median(gp),
                pct500=sum(1 for x in gp if x >= 500) / len(g) * 100,
                names=sorted(((c["name"], c["careerGP"]) for c in g), key=lambda t: -t[1]))
out["cohort_tiers"] = [tier(1.99, 99, "rel xGF% +2 or better"), tier(-2, 2, "rel xGF% between -2 and +2"),
                       tier(-99, -1.99, "rel xGF% -2 or worse")]
xs = [c["rel"] for c in mature]; ys = [c["careerGP"] for c in mature]
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
out["cohort_corr"] = dict(n=len(mature), r=sum((a - mx) * (b - my) for a, b in zip(xs, ys)) /
    ((sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys)) ** 0.5))

# --- 6. HockeyStatCards card ---
out["hsc"] = json.load(open(HERE / "hsc" / "hsc_8484223.json"))["card"]["ratings"]

json.dump(out, open(HERE / "analysis.json", "w"), indent=1)
print("wrote analysis.json:", ", ".join(out))

# --- 7. Evolving Hockey (subscriber data: cite and chart, never republish raw) ---
EH = HERE / "eh"
out["eh_percentiles"] = json.load(open(EH / "asp_eh_percentiles.json"))
out["eh_deployment"] = json.load(open(EH / "asp_deployment_by_date.json"))
qoc = json.load(open(HERE / "asp_qoc_by_game.json"))
qoc.sort(key=lambda r: r["date"])


def qagg(rs, label):
    w = sum(r["toi5v5"] for r in rs)
    return dict(label=label, gp=len(rs), toi5v5PerGp=w / len(rs),
                qoc=sum(r["qoc"] * r["toi5v5"] for r in rs) / w,
                first=rs[0]["date"], last=rs[-1]["date"])


out["qoc"] = dict(
    halves=[qagg(qoc[:34], "first 34 games"), qagg(qoc[34:], "last 34 games")],
    phases=[qagg([r for r in qoc if a <= r["date"] <= b], lbl) for lbl, a, b in
            [("Oct 9 - Nov 29", "2025-10-01", "2025-11-30"), ("December", "2025-12-01", "2025-12-31"),
             ("Jan 1 - Feb 4", "2026-01-01", "2026-02-05"), ("Feb 26 - Mar 6", "2026-02-06", "2026-03-31"),
             ("Apr 4 - 15 recall", "2026-04-01", "2026-05-01")]],
    games=qoc,
    meanCoverage=sum(r["coverage"] for r in qoc) / len(qoc))
xs = [r["toi"] for r in qoc]; ys = [r["qoc"] for r in qoc]
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
out["qoc"]["corrToiQoc"] = (sum((a - mx) * (b - my) for a, b in zip(xs, ys)) /
    ((sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys)) ** 0.5))

json.dump(out, open(HERE / "analysis.json", "w"), indent=1)
print("re-wrote analysis.json with EH:", ", ".join(out))
