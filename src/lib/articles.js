// Every published article in one place: the article pages build their NewsArticle node from here, and
// /news-sitemap.xml lists every one of them, newest first.
// Times are the real publish / last-content-edit times (the commits that shipped the copy), with their offset.
// `modified` moves only when the words or the charts change, never for a markup-only commit.
// `description` is the meta description and the dek on /analysis/; `thumb` picks the line-art thumbnail (ArticleThumb.astro);
// the one `featured` article is pinned to the top of /analysis/, everything else runs newest first.
import predictions from '../../data/site/articles/predictions-2026-27-copy.json';
import twoWay from '../../data/site/articles/two-way-forwards-copy.json';
import kasper from '../../data/site/articles/marco-kasper-copy.json';
import larkin from '../../data/site/articles/dylan-larkin-copy.json';
import rasmussen from '../../data/site/articles/michael-rasmussen-mt-rushmore-copy.json';
import fs from 'node:fs';
import path from 'node:path';

export const SITE = 'https://wesandwoodward.com';

// the byline (Mark, 10/16: "Mark Wesley"). Base.astro carries this node into any page that references it.
export const AUTHOR = { '@type': 'Person', '@id': `${SITE}/about/#author`, name: 'Mark Wesley', url: `${SITE}/about/`,
  worksFor: { '@id': `${SITE}/#org` }, knowsAbout: ['Detroit Red Wings', 'hockey analytics', 'expected goals'] };

export const ARTICLES = [
  { slug: '2026-27-predictions', title: predictions.title, published: '2026-10-02T16:19:22-07:00', modified: '2026-10-09T11:50:32-07:00', featured: true, thumb: 'puck',
    description: 'Five hundred simulated seasons with Dylan Larkin and five hundred without, one of each played out game by game, and a prediction.' },
  { slug: 'two-way-forwards', title: twoWay.title, published: '2026-10-07T12:32:59-07:00', modified: '2026-10-09T11:50:32-07:00', thumb: 'flip',
    description: 'Detroit built its forward group around compete and defensive responsibility. Three seasons of 5v5 scoring, the teams that made the archetype work, and where this roster was really headed.' },
  { slug: 'marco-kasper-year-three', title: kasper.title, published: '2026-10-13T10:58:35-07:00', modified: '2026-10-13T10:58:35-07:00', thumb: 'ghost',
    description: 'Marco Kasper’s second season was worse than a sophomore slump. What the comps, the luck and the projections say he needs in year three.' },
  { slug: 'dylan-larkin-checked-out', title: larkin.title, published: '2026-10-17T16:07:03-07:00', modified: '2026-10-17T16:07:03-07:00', thumb: 'seventyone',
    description: 'Dylan Larkin’s first five games since his trade request, measured against every five-game stretch of his career. The giveaways, the takeaways, the shots and what his speed says.' },
  { slug: 'michael-rasmussen-mt-rushmore', title: rasmussen.title, published: '2026-10-19T14:24:03-07:00', modified: '2026-10-19T14:24:03-07:00', thumb: 'rushmore',
    description: 'Forty-seven forwards have gone 400 minutes without a point since the NHL started tracking ice time. Four kept a real role the whole way. Michael Rasmussen is one of them, and by goals scored with him on the ice, the worst.' },
];

export const article = (slug) => ARTICLES.find((a) => a.slug === slug);
export const articleUrl = (slug) => `${SITE}/analysis/${slug}/`;

// Google wants the lead image in 16:9, 4:3 and 1:1 (scripts/og_images.py renders all three plus the 1200x630 link preview)
// (only files that exist; before the script has run for a new article it falls back to the link-preview image)
export const articleImages = (slug) => {
  const have = ['16x9', '4x3', '1x1'].filter((r) => fs.existsSync(path.resolve(`public/og/${slug}-${r}.png`)));
  return have.length ? have.map((r) => `${SITE}/og/${slug}-${r}.png`) : [`${SITE}/og/${slug}.png`];
};

// the date line under each headline: "Analysis · October 7, 2026 · Updated October 9"
const day = (iso, opts) => new Date(iso).toLocaleDateString('en-US', { timeZone: 'America/Detroit', ...opts });
export const dateline = (a) => {
  const pub = day(a.published, { month: 'long', day: 'numeric', year: 'numeric' });
  const upd = day(a.modified, { month: 'long', day: 'numeric', year: 'numeric' });
  return upd === pub ? pub : `${pub} · Updated ${day(a.modified, { month: 'long', day: 'numeric' })}`;
};
export const pubDay = (a) => day(a.published, { month: 'long', day: 'numeric', year: 'numeric' });

// the article node for Base's @graph. NewsArticle, not Article: these are dated, time-sensitive pieces on the
// current team (Google News and Top stories read the type, the times and the images from here).
export const newsArticle = (slug, { description, about = [], keywords = [], wordCount } = {}) => {
  const a = article(slug), url = articleUrl(slug);
  return {
    '@type': 'NewsArticle', '@id': `${url}#article`, url, mainEntityOfPage: url,
    headline: a.title, description, image: articleImages(slug),
    datePublished: a.published, dateModified: a.modified, inLanguage: 'en-US',
    author: { '@id': AUTHOR['@id'] }, publisher: { '@id': `${SITE}/#org` }, isPartOf: { '@id': `${SITE}/#website` },
    about, articleSection: 'Analysis', keywords, ...(wordCount ? { wordCount } : {}),
  };
};
