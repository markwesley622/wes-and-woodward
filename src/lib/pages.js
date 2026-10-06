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
export const canonicalPath = (P) => (nhlPageIsCanonical(P) ? `/players/${P.slug}/` : `/prospects/${P.slug}/`);
