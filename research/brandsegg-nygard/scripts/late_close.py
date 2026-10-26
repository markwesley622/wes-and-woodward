"""Late-and-close usage share + game-11 linemates. usage: late_close.py RAW_DIR MBN_RAW_DIR"""
import json, sys, re, html, collections, urllib.request, ssl, certifi, os, time
RAW, MBNRAW = sys.argv[1], sys.argv[2]
ctx = ssl.create_default_context(cafile=certifi.where())
def get(url, path):
    if not os.path.exists(path):
        open(path, "wb").write(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), context=ctx, timeout=60).read()); time.sleep(0.3)
    return json.load(open(path))
def mmss(t): m, s = t.split(":"); return int(m)*60+int(s)
def abs_sec(p, t): return (p-1)*1200 + t if p <= 3 else 3600 + (p-4)*300 + t
def load_shifts_html(gid, roster, home_id, away_id, season):
    out = []; num = str(gid)[4:]
    for side, tid in (("TH", home_id), ("TV", away_id)):
        path = f"{RAW}/{side}{num}.HTM"
        if not os.path.exists(path):
            open(path, "wb").write(urllib.request.urlopen(urllib.request.Request(f"https://www.nhl.com/scores/htmlreports/{season}/{side}{num}.HTM", headers={"User-Agent": "Mozilla/5.0"}), context=ctx, timeout=60).read())
        t = open(path, encoding="utf-8", errors="replace").read()
        bysw = {r["sweaterNumber"]: pid for pid, r in roster.items() if r["teamId"] == tid}
        for part in re.split(r'<td[^>]*class="playerHeading[^"]*"[^>]*>', t)[1:]:
            head = html.unescape(re.sub(r"<[^>]+>", " ", part[:200])).strip(); m = re.match(r"(\d+)\s", head)
            if not m: continue
            pid = bysw.get(int(m.group(1)))
            if pid is None: continue
            for row in re.finditer(r'<tr[^>]*class="\s*(?:oddColor|evenColor)"[^>]*>(.*?)</tr>', part, flags=re.S):
                cells = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", row.group(1), flags=re.S)]
                if len(cells) < 5 or not cells[0].isdigit(): continue
                per = cells[1]; per = 4 if per == "OT" else int(per)
                out.append((pid, tid, per, mmss(cells[2].split("/")[0].strip()), mmss(cells[3].split("/")[0].strip())))
    return out
def game(gid, pid_me, team_ab, season, pbp_dir=None, sh_dir=None):
    p = get(f"https://api-web.nhle.com/v1/gamecenter/{gid}/play-by-play", (f"{pbp_dir}/{gid}.json" if pbp_dir and os.path.exists(f"{pbp_dir}/{gid}.json") else f"{RAW}/pbp_{gid}.json"))
    home_id, away_id = p["homeTeam"]["id"], p["awayTeam"]["id"]
    me_tid = home_id if p["homeTeam"]["abbrev"] == team_ab else away_id
    roster = {r["playerId"]: r for r in p["rosterSpots"]}
    shp = f"{sh_dir}/{gid}.json" if sh_dir and os.path.exists(f"{sh_dir}/{gid}.json") else f"{RAW}/sh_{gid}.json"
    d = get(f"https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId={gid}", shp)["data"]
    shifts = [(s["playerId"], s["teamId"], s["period"], mmss(s["startTime"]), mmss(s["endTime"])) for s in d if s.get("typeCode") == 517 and s.get("duration")]
    if len(shifts) < 100: shifts = load_shifts_html(gid, roster, home_id, away_id, season)
    on = collections.defaultdict(set)
    for pid, tid, per, st, en in shifts:
        for s in range(abs_sec(per, st), abs_sec(per, en)): on[s].add(pid)
    goals = [(abs_sec(e["periodDescriptor"]["number"], mmss(e["timeInPeriod"])), e["details"]["eventOwnerTeamId"]) for e in p["plays"] if e["typeDescKey"] == "goal"]
    def diff(sec): return sum((1 if tid == me_tid else -1) for t, tid in goals if t < sec)
    avail = mine = 0; mates = collections.Counter()
    for sec in range(3300, 3600):
        if abs(diff(sec)) <= 1:
            avail += 1
            if pid_me in on.get(sec, set()): mine += 1
    def sk(S, tid): return [x for x in S if roster.get(x, {}).get("teamId") == tid and roster[x]["positionCode"] != "G"]
    opp = away_id if me_tid == home_id else home_id
    for sec in range(0, 3600):
        S = on.get(sec, set())
        if pid_me in S and len(sk(S, me_tid)) == 5 and len(sk(S, opp)) == 5:
            for x in sk(S, me_tid):
                if x != pid_me: mates[f'{roster[x]["lastName"]["default"]}|{roster[x]["positionCode"]}'] += 1
    # score state at my points
    pts = []
    for e in p["plays"]:
        if e["typeDescKey"] == "goal" and pid_me in (e["details"].get("scoringPlayerId"), e["details"].get("assist1PlayerId"), e["details"].get("assist2PlayerId")):
            sec = abs_sec(e["periodDescriptor"]["number"], mmss(e["timeInPeriod"])); pts.append((e["timeInPeriod"], e["periodDescriptor"]["number"], "diff_before", diff(sec), e["situationCode"]))
    return dict(gid=gid, date=p["gameDate"], avail=avail, mine=mine, mates=mates.most_common(5), pts=pts, final=(p["homeTeam"]["abbrev"], p["homeTeam"]["score"], p["awayTeam"]["abbrev"], p["awayTeam"]["score"]))

# MBN both samples (reuse downloaded pbp/shifts)
games = json.load(open(f"{MBNRAW}/games.json"))
for season in ("20252026", "20262027"):
    A = M = 0
    for s, gid, dt, opp in games:
        if s != season: continue
        g = game(gid, 8484794, "DET", season, f"{MBNRAW}/pbp", f"{MBNRAW}/shifts"); A += g["avail"]; M += g["mine"]
        if g["pts"] or g["avail"]: print(" ", season, dt, opp, "avail", g["avail"], "mine", g["mine"], "pts", g["pts"])
    print("MBN", season, "late-close share", M, "/", A, "=", round(100*M/A, 1) if A else None)
# MBN game 11
g = game(2026020178, 8484794, "DET", "20262027"); print("MBN game 11", g["date"], g["final"], "5v5 mates (sec):", g["mates"], "late", g["mine"], "/", g["avail"])
# McKenna
gl = get("https://api-web.nhle.com/v1/player/8486067/game-log/20262027/2", f"{RAW}/mck_gl.json")["gameLog"]
A = M = 0
for x in sorted(gl, key=lambda x: x["gameDate"]):
    g = game(x["gameId"], 8486067, "TOR", "20262027"); A += g["avail"]; M += g["mine"]
    print("  MCK", x["gameDate"], x["opponentAbbrev"], "TOI", x["toi"], "avail", g["avail"], "mine", g["mine"], "top mates", g["mates"][:2])
print("McKenna late-close share", M, "/", A, "=", round(100*M/A, 1) if A else None)
