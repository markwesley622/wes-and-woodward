// RSS feed: every published article, newest first, built from the same list as /news-sitemap.xml.
// Feed readers read it directly; the Buttondown newsletter (src/lib/follow.js) watches it and emails
// subscribers when a new item appears. Rebuilt on every deploy.
import { ARTICLES, articleUrl, SITE } from '../lib/articles.js';

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const rfc822 = (iso) => new Date(iso).toUTCString();

export function GET() {
  const all = [...ARTICLES].sort((a, b) => new Date(b.published) - new Date(a.published));
  const items = all.map((a) => `    <item>
      <title>${esc(a.title)}</title>
      <link>${articleUrl(a.slug)}</link>
      <guid isPermaLink="true">${articleUrl(a.slug)}</guid>
      <pubDate>${rfc822(a.published)}</pubDate>
      <description>${esc(a.description)}</description>
    </item>`).join('\n');
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Wes &amp; Woodward</title>
    <link>${SITE}/analysis/</link>
    <description>Detroit Red Wings analysis, by the numbers. One item per article.</description>
    <language>en-us</language>
    <lastBuildDate>${rfc822(all[0].published)}</lastBuildDate>
    <atom:link href="${SITE}/rss.xml" rel="self" type="application/rss+xml" />
    <image>
      <url>${SITE}/icon-192.png</url>
      <title>Wes &amp; Woodward</title>
      <link>${SITE}/</link>
    </image>
${items}
  </channel>
</rss>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' } });
}
