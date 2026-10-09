// Hover definitions. Every stat label on the site (table headers, tile eyebrows, .tip spans) that matches a
// label below gets the glossary card on hover: the term's short definition from src/data/glossary-terms.json and,
// once that stat has a glossary page, a "Full definition" link. Base.astro inlines termCards + LABELS and
// annotates the page client-side, so new tables pick definitions up without per-page wiring. An element can
// also opt in explicitly with data-term="<id>", or out with data-term="none".
import TERMS from '../data/glossary-terms.json';
import { glossarySlugs } from './glossary.js';

// normalized label text -> term id (lowercase, "−" as "-", single spaces)
export const LABELS = {
  // counting stats
  'gp': 'gp', 'games': 'gp', 'games played': 'gp',
  'g': 'goals', 'goals': 'goals',
  'a': 'assists', 'assists': 'assists',
  'p': 'points', 'pts': 'points', 'points': 'points', 'goals · assists · points': 'points',
  '+/-': 'plus-minus', 'plus-minus': 'plus-minus',
  'pim': 'pim',
  'toi': 'toi', 'time on ice': 'toi',
  's': 'sog', 'sog': 'sog',
  'blk': 'blocks',
  'ppp': 'ppg', 'ppg': 'ppg', 'shg': 'shg', 'gwg': 'gwg',
  'fo%': 'fo-pct', 'sh%': 'sh-pct',
  // goalies
  'sv%': 'sv-pct', 'save percentage': 'sv-pct',
  'gaa': 'gaa', 'so': 'shutout', 'w': 'goalie-record', 'l': 'goalie-record', 'otl': 'goalie-record',
  'ga': 'saves', 'sa': 'saves',
  'gsax': 'gsax', 'goals saved above expected': 'gsax', 'goaltending': 'gsax', 'goaltending, goals saved above expected': 'gsax',
  // team
  'regulation wins': 'regulation-wins', 'rw': 'regulation-wins', 'p%': 'pts-pct',
  // expected goals family
  'xg': 'xg', 'xgf': 'xg', 'xga': 'xg', 'xgf%': 'xg', 'xg%': 'xg', '5v5 xg%': 'xg', '5v5 xg share': 'xg',
  '5v5 expected-goal share': 'xg', '5v5 xg share, score & venue adjusted': 'xg', 'power play xg per 60': 'xg',
  'penalty kill xg against per 60': 'xg', 'pp xg per 60': 'xg', 'pk xga per 60': 'xg', 'attacking': 'xg', 'defending': 'xg',
  'power play': 'xg', 'penalty kill': 'xg',
  'ixg': 'ixg', 'individual xg': 'ixg',
  'finishing': 'gax', 'finishing, goals above expected': 'gax',
  'cf%': 'corsi', 'possession': 'corsi',
  // site terms
  'w-value': 'w-value', 'pctl': 'percentile', 'percentiles': 'percentile', 'same-year pct.': 'percentile',
  'game score': 'game-score', 'game score, average': 'game-score',
};

export const termCards = Object.fromEntries(TERMS.filter((t) => t.short).map((t) => [t.id, {
  n: t.name, a: (t.abbr ?? []).find((x) => x.toLowerCase() !== t.name.toLowerCase()) ?? '', d: t.short,
  h: glossarySlugs.has(t.slug) ? `/glossary/${t.slug}/` : null,
}]));
