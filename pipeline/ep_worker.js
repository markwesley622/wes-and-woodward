// In-page EliteProspects worker. Paste/run on any eliteprospects.com tab in Mark's logged-in Chrome
// (claude-in-chrome javascript_tool). Pulls tasks from pipeline/ep_receiver.py, fetches each EP page
// with the session cookies, extracts the embedded __NEXT_DATA__ and POSTs a compact record back.
// Stop with: window.__ww.running = false. Status: window.__ww.
(() => {
  if (window.__ww && window.__ww.running) return 'already running';
  const SERVER = 'http://127.0.0.1:8765';
  const W = (window.__ww = { running: true, done: 0, err: 0, last: null, started: Date.now(), concurrency: 3, gapMs: 700 });
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const DROP = new Set(['flagUrl', 'logo', '__typename', 'imageUrl', 'teamLogoUrl', 'biographyAsHTML', 'links', 'agencies', 'playerHighlights', 'playerQuotes']);
  const slim = (o) => JSON.parse(JSON.stringify(o ?? null, (k, v) => (DROP.has(k) ? undefined : v)));
  const list = (o) => (Array.isArray(o) ? o : o && typeof o === 'object' ? Object.values(o).find((v) => Array.isArray(v)) || [] : []);
  const nextData = (html) => {
    const m = html.match(/<script id="__NEXT_DATA__"[^>]*>([\s\S]*?)<\/script>/);
    if (!m) throw new Error('no __NEXT_DATA__');
    return JSON.parse(m[1]).props.pageProps;
  };
  const pid = (path) => (String(path || '').match(/\/player\/(\d+)\//) || [])[1] || null;

  const extract = {
    player(html) {
      const pp = nextData(html);
      const pd = pp.playerData || {};
      return {
        player: slim(pd.player),
        draftRanking: slim(pd.playerDraftRanking),
        styles: slim(pd.playerStyles),
        seasons: list(pp.initialLeagueStats && pp.initialLeagueStats.playerStats).map((s) => ({
          season: s.season && s.season.slug, team: s.teamName, teamPath: s.team && s.team.eliteprospectsUrlPath, league: s.leagueName,
          leaguePath: s.league && s.league.eliteprospectsUrlPath, status: s.status, role: s.playerRole, contract: s.contractType,
          reg: slim(s.regularStats), post: slim(s.postseasonStats), postType: s.postseasonType,
        })),
        careerTotals: slim(pp.initialCareerTotals),
        gameLog: { season: pp.initialGameLog && pp.initialGameLog.season, games: list(pp.initialGameLog && pp.initialGameLog.gameLogs).map(slim) },
        awards: slim(pp.initialAwards),
        transactions: slim(pp.initialTransactions),
        fetchedAt: Date.now(),
      };
    },
    draft(html) {
      const pp = nextData(html);
      const doc = new DOMParser().parseFromString(html, 'text/html');
      const table = [...doc.querySelectorAll('table')].find((t) => /OVERALL/.test((t.querySelector('thead') || {}).innerText || t.querySelector('thead')?.textContent || ''));
      const rows = [];
      if (table) for (const tr of table.querySelectorAll('tbody tr')) {
        const td = [...tr.querySelectorAll('td')];
        if (td.length < 8) continue;
        const a = td[2].querySelector('a[href*="/player/"]');
        const txt = (x) => (x.textContent || '').trim().replace(/\s+/g, ' ');
        rows.push({ overall: parseInt(txt(td[0]).replace('#', ''), 10), team: txt(td[1]), name: txt(td[2]).replace(/\s*\([^)]*\)\s*$/, ''),
          pos: (txt(td[2]).match(/\(([^)]*)\)\s*$/) || [])[1] || null, playerId: pid(a && a.getAttribute('href')),
          nhl: { seasons: +txt(td[3]) || 0, gp: +txt(td[4]) || 0, g: +txt(td[5]) || 0, a: +txt(td[6]) || 0, tp: +txt(td[7]) || 0, pim: +txt(td[8]) || 0 } });
      }
      let picks = null;
      const walk = (o, d = 0) => { if (picks || !o || d > 5) return; if (Array.isArray(o) && o.length > 30 && o[0] && typeof o[0] === 'object' && 'overall' in o[0]) { picks = o; return; } if (typeof o === 'object') for (const k in o) walk(o[k], d + 1); };
      walk(pp);
      return { year: pp.year, picks: (picks || []).map((p) => ({ overall: p.overall, round: p.round, year: p.year, playerId: p.player && p.player.id, name: p.player && p.player.name, pos: p.player && p.player.position, nationality: p.player && p.player.nationality && p.player.nationality.slug, team: p.team && p.team.name })), table: rows, fetchedAt: Date.now() };
    },
    league(html) {
      const pp = nextData(html);
      const st = (pp.skaterStats && pp.skaterStats.stats) || (pp.goalieStats && pp.goalieStats.stats) || {};
      return { league: pp.leagueSlug, season: pp.seasonSlug, age: pp.age, position: pp.position, pageInfo: slim(st.pageInfo), totalCount: st.totalCount,
        rows: list(st.edges || st).map((e) => ({ playerId: e.player && e.player.id, name: e.player && e.player.name, pos: e.player && e.player.detailedPosition, rights: slim(e.player && e.player.nhlRights),
          team: e.teamName, league: e.leagueName, reg: slim(e.regularStats), post: slim(e.postseasonStats), total: slim(e.totalStats) })), fetchedAt: Date.now() };
    },
    system(html) {
      const pp = nextData(html);
      const d = pp.data || {};
      const f = (x) => ({ id: pid(x.player && x.player.eliteprospectsUrlPath), name: x.player && x.player.name, pos: ((x.player && x.player.detailedPosition) || []).join('/'), status: x.player && x.player.gameStatus,
        lines: (x.stats || []).map((s) => ({ team: s.teamName, league: s.leagueName, status: s.status, reg: slim(s.regularStats) })) });
      return { skaters: list(d.skaters).map(f), goalies: list(d.goalies).map(f), fetchedAt: Date.now() };
    },
    team(html) {
      const pp = nextData(html);
      return { title: (html.match(/<title>([^<]*)<\/title>/) || [])[1], data: slim(pp.data || pp), fetchedAt: Date.now() };
    },
  };

  const post = (path, body) => fetch(SERVER + path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });

  async function one(t, i) {
    await sleep(i * W.gapMs);
    try {
      const res = await fetch(t.url, { credentials: 'include' });
      if (res.status !== 200) throw new Error('HTTP ' + res.status);
      const html = await res.text();
      const data = extract[t.type](html);
      await post('/save', { task: t, data });
      W.done++; W.last = t.key;
    } catch (e) {
      W.err++; W.lastError = String(e) + ' @ ' + t.url;
      await post('/error', { task: t, error: String(e) });
      if (/HTTP (429|403|5\d\d)/.test(String(e))) { W.backoffUntil = Date.now() + 90000; await sleep(90000); }
    }
  }

  (async () => {
    while (W.running) {
      let tasks = [];
      try { tasks = (await (await fetch(SERVER + '/next?n=' + W.concurrency)).json()).tasks || []; } catch (e) { W.lastError = 'server: ' + e; await sleep(15000); continue; }
      if (!tasks.length) { await sleep(10000); continue; }
      await Promise.all(tasks.map(one));
      await sleep(W.gapMs);
    }
  })();
  return 'started';
})();
