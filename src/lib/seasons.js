// Past Detroit seasons for the season dropdown on NHL player pages (Mark, 10/12), built by
// pipeline/build_player_seasons.py into data/site/players/seasons/<playerId>/<season>.json. Each one renders at
// /players/<slug>/<2024-25>/ (noindex, out of the sitemap) only so the dropdown can fetch it and swap it in on
// the player's own URL.
import fs from 'node:fs';
import path from 'node:path';

const dash = (label) => `${label.slice(0, 4)}–${label.slice(5)}`;

export const pastSeasons = (P) => {
  const dir = path.resolve(`data/site/players/seasons/${P.playerId}`);
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((f) => f.endsWith('.json')).map((f) => JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8')))
    .sort((a, b) => b.season.localeCompare(a.season));
};

// the dropdown: the current season (the page itself) first, then each past Detroit season, newest first
export const seasonMenu = (P) => [
  { key: P.season, label: dash(P.seasonLabel), href: `/players/${P.slug}/` },
  ...pastSeasons(P).map((S) => ({ key: S.season, label: dash(S.seasonLabel), href: `/players/${P.slug}/${S.seasonLabel}/` })),
];
