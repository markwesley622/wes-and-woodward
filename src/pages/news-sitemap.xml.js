// Google News sitemap: every published article, newest first (Mark, 10/19: list them all, not just the last two
// days; Google's spec says it only reads entries under two days old, so older ones are harmless but inert).
// Rebuilt on every deploy, including the 5 AM nightly refresh. Listed in public/robots.txt and submitted in GSC.
import { ARTICLES, articleUrl } from '../lib/articles.js';

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export function GET() {
  const all = [...ARTICLES].sort((a, b) => new Date(b.published) - new Date(a.published));
  const urls = all.map((a) => `  <url>
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
