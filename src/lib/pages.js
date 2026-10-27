// Which pages a player gets (Mark, 10/6). Every prospect has a prospect page at /prospects/<slug>/.
// A player has an NHL-level page at /players/<slug>/ when he is not a prospect, is on the NHL roster,
// or has played an NHL game this season. When both exist, his CURRENT status picks the canonical one:
// on the NHL roster -> the NHL page; otherwise -> the prospect page.
export const isProspect = (P) => !!(P.prospectStatus && P.prospectStatus.prospect);
export const onNhlRoster = (P) => !!(P.prospectStatus && P.prospectStatus.onNhlRoster);
export const playedNhlThisSeason = (P) => (Array.isArray(P.gameLog) && P.gameLog.length > 0) || (P.seasonLines || []).some((l) => l.league === 'NHL' && (l.gp || 0) > 0);
export const hasNhlPage = (P) => !isProspect(P) || onNhlRoster(P) || playedNhlThisSeason(P);
export const hasProspectPage = (P) => isProspect(P);
export const nhlPageIsCanonical = (P) => !isProspect(P) || onNhlRoster(P);
// The Players list (Mark, 10/12): only players who have played an NHL game for Detroit this season (detGames,
// pipeline/build_player.py). Edvinsson stays on it ahead of his first game because he is expected up soon; he drops
// off if he is traded (currentTeam is the NHL API's current team). Bernard-Docker came off the keep list on 10/27
// (Mark): his page waits for his first NHL game of the season, off the list and out of the sitemap.
const LIST_KEEP = new Set([8482762 /* Simon Edvinsson */]);
export const onPlayersList = (P) => hasNhlPage(P) && ((P.detGames ?? 0) > 0 || (LIST_KEEP.has(P.playerId) && P.currentTeam === 'DET'));
// Held off the index (Mark, 10/27): an NHL-template page for a player with no NHL game this season and no spot on
// the Players list (Bernard-Docker, the AHL call-ups) is noindex, which also keeps it out of the sitemap
// (astro.config.mjs reads the meta), until he plays. The kept players (Edvinsson) instead fall back to their most
// recent season (src/lib/seasons.js fallbackSeason).
export const heldOffIndex = (P) => hasNhlPage(P) && nhlPageIsCanonical(P) && !playedNhlThisSeason(P) && !onPlayersList(P);
export const canonicalPath = (P) => (nhlPageIsCanonical(P) ? `/players/${P.slug}/` : `/prospects/${P.slug}/`);
