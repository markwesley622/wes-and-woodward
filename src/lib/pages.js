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
// pipeline/build_player.py). Edvinsson and Bernard-Docker stay on it ahead of their first game because they are
// expected up soon; either one drops off if he is traded (currentTeam is the NHL API's current team).
const LIST_KEEP = new Set([8482762 /* Simon Edvinsson */, 8480879 /* Jacob Bernard-Docker */]);
export const onPlayersList = (P) => hasNhlPage(P) && ((P.detGames ?? 0) > 0 || (LIST_KEEP.has(P.playerId) && P.currentTeam === 'DET'));
export const canonicalPath = (P) => (nhlPageIsCanonical(P) ? `/players/${P.slug}/` : `/prospects/${P.slug}/`);
