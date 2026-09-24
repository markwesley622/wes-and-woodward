import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Custom domain live since 2026-09-21: DNS (four A records + www CNAME, DNS-only) is on
// Cloudflare; GitHub Pages has the domain set and public/CNAME keeps it pinned per deploy.
// markwesley622.github.io/wes-and-woodward now redirects here.
export default defineConfig({
  site: 'https://wesandwoodward.com',
  base: '/',
  integrations: [sitemap()],
});
