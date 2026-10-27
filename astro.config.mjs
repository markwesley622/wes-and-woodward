import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import fs from 'node:fs';
import { ARTICLES } from './src/lib/articles.js';

// The sitemap lists canonical URLs only. A prospect with both an NHL page and a prospect page points one at the
// other (src/lib/pages.js), so read each built page's canonical link (the sitemap is written after the pages)
// and leave out any page whose canonical is somewhere else, and any page marked noindex (a player's past seasons,
// which only exist for the season dropdown to fetch).
const dist = new URL('./dist/', import.meta.url);
const selfCanonical = (page) => {
  try {
    const html = fs.readFileSync(new URL(`.${new URL(page).pathname}index.html`, dist), 'utf8');
    if (/<meta name="robots" content="[^"]*noindex/.test(html)) return false;
    const m = html.match(/<link rel="canonical" href="([^"]+)"/);
    return !m || m[1] === page;
  } catch { return true; }
};

// Custom domain live since 2026-09-21: DNS (four A records + www CNAME, DNS-only) is on
// Cloudflare; GitHub Pages has the domain set and public/CNAME keeps it pinned per deploy.
// markwesley622.github.io/wes-and-woodward now redirects here.
// lastmod (Mark, 10/27): real change dates so Google can tell a refreshed page from one it already has. Articles carry
// their own `modified` (src/lib/articles.js); player pages their data file's updatedAt (moves only when the values move);
// prospect pages the prospect build date; home and team the dashboard build; glossary pages their `reviewed` date.
// The index pages take the newest date of what they list. Anything else (about) goes out without a lastmod.
const readJson = (rel) => JSON.parse(fs.readFileSync(new URL(rel, import.meta.url), 'utf8'));
const listJson = (rel) => fs.readdirSync(new URL(rel, import.meta.url)).filter((f) => f.endsWith('.json')).map((f) => readJson(`${rel}${f}`));
const iso = (d) => (d ? new Date(d).toISOString() : undefined);
const newest = (ds) => { const t = ds.filter(Boolean).map((d) => Date.parse(d)).filter((n) => !Number.isNaN(n)); return t.length ? new Date(Math.max(...t)).toISOString() : undefined; };
let lastmods = null;
const lastmodMap = () => {
  const m = new Map();
  const articles = ARTICLES.map((a) => { m.set(`/analysis/${a.slug}/`, iso(a.modified)); return a.modified; });
  m.set('/analysis/', newest(articles));
  const players = listJson('./data/site/players/').map((P) => { m.set(`/players/${P.slug}/`, iso(P.updatedAt)); m.set(`/prospects/${P.slug}/`, iso(P.updatedAt)); return P.updatedAt; });
  m.set('/players/', newest(players));
  try { const built = readJson('./data/site/prospects.json').built; const d = built && iso(`${built}T12:00:00-04:00`);
    for (const P of listJson('./data/site/prospects/')) if (P.slug) m.set(`/prospects/${P.slug}/`, newest([d, m.get(`/prospects/${P.slug}/`)]));
    m.set('/prospects/', d); } catch {}
  try { const d = iso(readJson('./data/site/dashboard.json').generatedAt); m.set('/', d); m.set('/team/', d); } catch {}
  const glossary = listJson('./src/data/glossary/').map((g) => { const d = g.reviewed && iso(`${g.reviewed}T12:00:00-04:00`); m.set(`/glossary/${g.slug}/`, d); return d; });
  m.set('/glossary/', newest(glossary));
  return m;
};

export default defineConfig({
  site: 'https://wesandwoodward.com',
  base: '/',
  integrations: [sitemap({
    filter: selfCanonical,
    serialize(item) {
      lastmods ??= lastmodMap();                     // built once, after the pages exist
      const lastmod = lastmods.get(new URL(item.url).pathname);
      return lastmod ? { ...item, lastmod } : item;
    },
  })],
});
