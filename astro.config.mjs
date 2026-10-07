import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import fs from 'node:fs';

// The sitemap lists canonical URLs only. A prospect with both an NHL page and a prospect page points one at the
// other (src/lib/pages.js), so read each built page's canonical link (the sitemap is written after the pages)
// and leave out any page whose canonical is somewhere else.
const dist = new URL('./dist/', import.meta.url);
const selfCanonical = (page) => {
  try {
    const html = fs.readFileSync(new URL(`.${new URL(page).pathname}index.html`, dist), 'utf8');
    const m = html.match(/<link rel="canonical" href="([^"]+)"/);
    return !m || m[1] === page;
  } catch { return true; }
};

// Custom domain live since 2026-09-21: DNS (four A records + www CNAME, DNS-only) is on
// Cloudflare; GitHub Pages has the domain set and public/CNAME keeps it pinned per deploy.
// markwesley622.github.io/wes-and-woodward now redirects here.
export default defineConfig({
  site: 'https://wesandwoodward.com',
  base: '/',
  integrations: [sitemap({ filter: selfCanonical })],
});
