// Google News sitemap: articles published in the last two days (Google ignores older entries). Rebuilt on every
// deploy, including the 5 AM nightly refresh, so pieces roll off on their own. Listed in public/robots.txt.
import { ARTICLES, articleUrl } from '../lib/articles.js';

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export function GET() {
  const cutoff = Date.now() - 2 * 24 * 60 * 60 * 1000;
  const recent = ARTICLES.filter((a) => new Date(a.published).getTime() >= cutoff);
  const urls = recent.map((a) => `  <url>
    <loc>${articleUrl(a.slug)}</loc>
    <news:news>
      <news:publication><news:name>Wes &amp; Woodward</news:name><news:language>en</news:language></news:publication>
      <news:publication_date>${a.published}</news:publication_date>
      <news:title>${esc(a.title)}</news:title>
    </news:news>
  </url>`).join('\n');
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
${urls}
</urlset>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
}
