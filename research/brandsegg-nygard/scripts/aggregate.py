import json, sys, collections
RAW, OUT = sys.argv[1], sys.argv[2]
res = json.load(open(f"{OUT}/onice_games.json"))
summary = {}
for s, games in res.items():
    n = len(games); A = collections.Counter(); X = collections.Counter(); st = collections.Counter(); per = collections.Counter(); sc = collections.Counter(); zs = collections.Counter(); ind = collections.Counter(); mates = collections.Counter()
    team55 = team_pp = team_pk = shifts = close_late = 0; qoc3 = qoc2 = qocb = qot = 0.0; ishots = []
    for g in games:
        for k, v in g["ev5v5"].items(): A[k] += v
        for k, v in g["xg"].items(): X[k] += v
        for k, v in g["toi_by_state"].items(): st[k] += v
        for k, v in g["per_toi"].items(): per[k] += v
        for k, v in g["score_toi"].items(): sc[k] += v
        for k, v in g["zs"].items(): zs[k] += v
        for k, v in g["ind"].items(): ind[k] += v
        for k, v in g["mates"].items(): mates[k] += v
        team55 += g["team_5v5"]; team_pp += g["team_pp"]; team_pk += g["team_pk"]; shifts += g["shifts"]; close_late += g["close_late_toi"]
        w = g["toi_by_state"].get("5v5", 0)
        qoc3 += g["qoc_top3F_share"]*w; qoc2 += g["qoc_top2D_share"]*w; qocb += g["qoc_bottom3F_share"]*w; qot += g["qot_top3F_share"]*w
        ishots += g["ishots"]
    t55 = st["5v5"]; tall = sum(st.values())
    def pct(a, b): return round(100*a/(a+b), 1) if a+b else None
    def p60(v, t): return round(60*v/(t/60), 2) if t else None
    off55 = team55 - t55
    S = dict(
        games=n, toi_per_gp=round(tall/60/n, 2), toi_5v5_per_gp=round(t55/60/n, 2), pp_toi_per_gp=round(st["PP"]/60/n, 2), pk_toi_per_gp=round(st["PK"]/60/n, 2),
        pp_share_of_team=round(100*st["PP"]/team_pp, 1) if team_pp else None, pk_share_of_team=round(100*st["PK"]/team_pk, 1) if team_pk else None, team_pp_min_per_gp=round(team_pp/60/n, 2),
        shifts_per_gp=round(shifts/n, 1), avg_shift_sec=round(tall/shifts, 1),
        period_share={k: round(100*v/tall, 1) for k, v in sorted(per.items())}, period3_toi_per_gp=round(per.get(3, 0)/60/n, 2),
        score_state_5v5_share={k: round(100*v/t55, 1) for k, v in sc.items()}, close_late_min_per_gp=round(close_late/60/n, 2),
        zone_starts=dict(zs), oZS_pct=pct(zs["O"], zs["D"]), oZS_share_all=round(100*zs["O"]/sum(zs.values()), 1),
        qoc_top3F_share=round(qoc3/t55, 3), qoc_top2D_share=round(qoc2/t55, 3), qoc_bottom3F_share=round(qocb/t55, 3), qot_top3F_share=round(qot/t55, 3),
        cf=A["CF"], ca=A["CA"], cf_pct=pct(A["CF"], A["CA"]), ff_pct=pct(A["FF"], A["FA"]), sf=A["SF"], sa=A["SA"], gf=A["GF"], ga=A["GA"],
        cf60=p60(A["CF"], t55), ca60=p60(A["CA"], t55), xgf=round(X["xGF"], 2), xga=round(X["xGA"], 2), xgf_pct=pct(X["xGF"], X["xGA"]), xgf60=p60(X["xGF"], t55), xga60=p60(X["xGA"], t55),
        off_cf_pct=pct(A["off_CF"], A["off_CA"]), off_xgf_pct=pct(X["off_xGF"], X["off_xGA"]), off_xgf60=p60(X["off_xGF"], off55), off_xga60=p60(X["off_xGA"], off55), off_gf=A["off_GF"], off_ga=A["off_GA"],
        on_sh_pct=round(100*A["GF"]/A["SF"], 1) if A["SF"] else None, on_sv_pct=round(100*(1-A["GA"]/A["SA"]), 1) if A["SA"] else None,
        ind=dict(ind), icf60_all=p60(ind["iCF"], tall), isog60_all=p60(ind["iSOG"], tall), icf60_5v5=p60(ind["iCF_5v5"], t55),
        ixg_all=round(X["ixg_all"], 2), ixg_5v5=round(X["ixg_5v5"], 2), ixg60_all=p60(X["ixg_all"], tall), ixg60_5v5=p60(X["ixg_5v5"], t55),
        hits60=p60(ind["hits"], tall), giveaways60=p60(ind["giveaways"], tall), takeaways60=p60(ind["takeaways"], tall),
        pp_xgf_on=round(X["pp_xGF_on"], 2),
        by_score={st_: dict(cf=A[st_+"_CF"], ca=A[st_+"_CA"], cf_pct=pct(A[st_+"_CF"], A[st_+"_CA"]), xgf=round(X[st_+"_xGF"],2), xga=round(X[st_+"_xGA"],2), xgf_pct=pct(X[st_+"_xGF"], X[st_+"_xGA"])) for st_ in ("lead","tied","trail")},
        top_mates={k: round(v/60, 1) for k, v in mates.most_common(10)},
    )
    # shot profile (MoneyPuck unblocked attempts)
    if ishots:
        ns = len(ishots); S["shots_mp"] = ns; S["avg_xg_per_shot"] = round(sum(x["xg"] for x in ishots)/ns, 3); S["avg_dist"] = round(sum(x["dist"] for x in ishots)/ns, 1)
        S["share_inside_25ft"] = round(100*sum(1 for x in ishots if x["dist"] <= 25)/ns, 1); S["share_rebound"] = round(100*sum(1 for x in ishots if x["rebound"] == "1")/ns, 1); S["share_rush"] = round(100*sum(1 for x in ishots if x["rush"] == "1")/ns, 1)
        S["shot_types"] = dict(collections.Counter(x["type"] for x in ishots)); S["hd_shots_0.1plus"] = sum(1 for x in ishots if x["xg"] >= 0.1); S["hd_xg_0.1plus"] = round(sum(x["xg"] for x in ishots if x["xg"] >= 0.1), 2)
        S["on_goal_share"] = round(100*sum(1 for x in ishots if x["onGoal"] in ("1","1.0"))/ns, 1)
    summary[s] = S
json.dump(summary, open(f"{OUT}/summary.json", "w"), indent=1)
keys = list(summary["20262027"].keys())
for k in keys:
    a, b = summary["20252026"].get(k), summary["20262027"].get(k)
    print(f"{k:24s} | {str(a):60s} | {str(b)}")
