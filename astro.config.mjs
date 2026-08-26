import { defineConfig } from 'astro/config';

// Until the custom domain is wired up, the site lives at
// markwesley622.github.io/wes-and-woodward (project pages), so `base` is set.
// When wesandwoodward.com lands: site -> 'https://wesandwoodward.com',
// base -> '/', and add public/CNAME containing "wesandwoodward.com".
export default defineConfig({
  site: 'https://markwesley622.github.io',
  base: '/wes-and-woodward',
});
