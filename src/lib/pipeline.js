// Pipeline Rankings table on prospect pages (Mark, 10/15): the prospect plus the two ranked above him and the
// two below (a five-row window that slides inward at the top and bottom of the list). Each row shows this
// season's main line (league, Network NHLe coefficient, counting stats) and rank movement against the
// start-of-season ranking that pipeline/build_prospects.py keeps in data/site/prospect_ranks_start.json.
import fs from 'node:fs';
import path from 'node:path';
import { hasProspectPage, canonicalPath } from './pages.js';

const PIPE = JSON.parse(fs.readFileSync(path.resolve('data/site/prospects.json'), 'utf8'));
const RANKED = PIPE.prospects.filter((x) => x.rank != null).sort((a, b) => a.rank - b.rank);

// nhlId -> the player's canonical page (the NHL page while a roster prospect is up, else the prospect page)
const links = new Map();
const dir = path.resolve('data/site/players');
for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json'))) {
  const P = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
  if (hasProspectPage(P)) links.set(P.playerId, canonicalPath(P));
}

// the main line: most games among lines in leagues with a coefficient (EP sorts lines by games); a player with
// nothing this season falls back to last season's league, flagged, with no stats
const mainLine = (x) => {
  const cur = (x.currentLines || []).filter((l) => l.coef != null);
  if (cur.length) return { ...cur[0], also: cur.slice(1).map((l) => l.league), now: true };
  const last = (x.lastLines || []).filter((l) => l.coef != null);
  return last.length ? { league: last[0].league, team: last[0].team, coef: last[0].coef, now: false } : null;
};

export const pipelineSize = RANKED.length;
export const rankStartDate = RANKED.find((x) => x.rankStartDate)?.rankStartDate ?? null;

export function pipelineWindow(rank, size = 5) {
  if (rank == null) return [];
  const i = RANKED.findIndex((x) => x.rank === rank);
  if (i < 0) return [];
  const half = Math.floor(size / 2);
  const lo = Math.max(0, Math.min(i - half, RANKED.length - size));
  return RANKED.slice(lo, lo + size).map((x) => ({
    rank: x.rank, name: x.name, nhlId: x.nhlId, group: x.group, position: x.position,
    href: links.get(x.nhlId) ?? null,
    line: mainLine(x),
    move: x.rankStart != null ? x.rankStart - x.rank : null,   // positive = climbed
  }));
}
