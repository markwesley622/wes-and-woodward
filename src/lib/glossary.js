// Glossary pages: one JSON per stat in src/data/glossary/<slug>.json (contract in research/glossary-pseo/TEMPLATE.md).
// This file resolves the "live" slot against the nightly pipeline output in data/site, so a stat page only
// names what it wants (a dashboard tile, or a skater/goalie field to rank on) and never carries numbers itself.
import fs from 'node:fs';
import path from 'node:path';
import dashboard from '../../data/site/dashboard.json';
import team from '../../data/site/team.json';
import skaters from '../../data/site/skaters.json';
import goalies from '../../data/site/goalies.json';
import { hasNhlPage, canonicalPath } from './pages.js';

const entries = import.meta.glob('../data/glossary/*.json', { eager: true, import: 'default' });
export const glossary = Object.values(entries).sort((a, b) => a.stat.name.localeCompare(b.stat.name));
export const glossarySlugs = new Set(glossary.map((g) => g.slug));

const SOURCES = { skaters, goalies, team, dashboard };

export const get = (obj, p) => p.split('.').reduce((o, k) => (o == null ? undefined : o[k]), obj);

const minus = '−';
export const fmt = (v, f) => {
  if (v == null || Number.isNaN(v)) return '–';
  switch (f) {
    case 'int': return String(Math.round(v));
    case 'num1': return Number(v).toFixed(1);
    case 'num2': return Number(v).toFixed(2);
    case 'pct1': return `${(v * 100).toFixed(1)}%`;
    case 'signed1': case 'signed2': {
      const d = f === 'signed1' ? 1 : 2, r = Number(v).toFixed(d);
      return Number(r) > 0 ? `+${r}` : Number(r) < 0 ? `${minus}${Math.abs(v).toFixed(d)}` : Number(0).toFixed(d);
    }
    case 'sv3': { const r = Number(v).toFixed(3); return r.startsWith('0') ? r.slice(1) : r; }   // 0.903 -> .903 (hockey save-percentage style)
    case 'mmss': { const t = Math.round(Number(v)); return `${Math.floor(t / 60)}:${String(t % 60).padStart(2, '0')}`; }   // seconds -> 20:00
    case 'hmm': { const t = Math.round(Number(v) / 60); return `${Math.floor(t / 60)}:${String(t % 60).padStart(2, '0')}`; }  // seconds -> hours:minutes
    default: return String(v);
  }
};

// player id -> page link, only when the player has an NHL-level page (same rule as the players index)
const dir = path.resolve('data/site/players');
const playerLinks = new Map();
for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.json'))) {
  const P = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
  if (hasNhlPage(P)) playerLinks.set(P.playerId, canonicalPath(P));
}

// Resolve a stat's live spec into render-ready numbers.
export function resolveLive(live) {
  if (!live) return null;
  const tiles = (live.tiles ?? []).map((t) => {
    if (t.tile) {
      const d = dashboard.tiles.find((x) => x.key === t.tile);
      if (!d) return null;
      const value = d.signed ? fmt(d.value, 'signed1') : d.unit === '%' ? `${d.value.toFixed(1)}%` : (Math.abs(d.value) < 20 ? d.value.toFixed(2) : d.value.toFixed(1));
      return { label: t.label ?? d.label, value, sub: d.rankLabel ?? '', note: d.note, top: d.rank != null && d.rank <= 8, bottom: d.rank != null && d.rank >= 25 };
    }
    const src = SOURCES[t.source];
    const v = get(src, t.path), rank = t.rankPath ? get(src, t.rankPath) : null;
    return { label: t.label, value: fmt(v, t.format), sub: rank ? `${ordinal(rank)} of 32` : (t.sub ?? ''), note: t.note };
  }).filter(Boolean);

  let leaders = null;
  if (live.leaders) {
    const L = live.leaders, rows = [...(SOURCES[L.source] ?? [])]
      .filter((r) => get(r, L.sort) != null)
      .sort((a, b) => (L.ascending ? 1 : -1) * (get(a, L.sort) - get(b, L.sort)))
      .slice(0, L.limit ?? 5);
    leaders = {
      caption: L.caption,
      columns: L.columns.map((c) => c.label),
      rows: rows.map((r) => ({ name: r.name, href: playerLinks.get(r.playerId) ?? null, cells: L.columns.map((c) => fmt(get(r, c.path), c.format)) })),
    };
  }

  const gp = dashboard.standings?.gamesPlayed ?? 0;
  const note = live.smallSample && gp < live.smallSample ? live.smallSampleNote.replace('{gp}', String(gp)) : null;
  const asOf = new Date(dashboard.generatedAt).toLocaleString('en-US', { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'America/Detroit' });
  return { intro: live.intro, tiles, leaders, note, asOf, season: dashboard.seasonLabel, gp, credit: live.credit ?? 'MoneyPuck' };
}

export const ordinal = (n) => { n = Number(n); const s = (10 <= n % 100 && n % 100 <= 20) ? 'th' : ({ 1: 'st', 2: 'nd', 3: 'rd' }[n % 10] || 'th'); return `${n}${s}`; };

// strip tags for schema text and meta
export const plain = (html) => html.replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
