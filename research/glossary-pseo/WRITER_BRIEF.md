# Writer brief: Wes & Woodward glossary pages (batch of 10/9/2026)

You're writing glossary pages for wesandwoodward.com, Mark Wesley's Detroit Red Wings analytics publication.
One page per stat at `/glossary/<slug>/`. Mark wants all 58 stat pages plus the hub published in one deploy,
so every page has to be complete and gate-clean the first time. Ten writers are working in parallel on
different stats; stay inside your own files.

## Read first (all of it)
1. `research/glossary-pseo/TEMPLATE.md`: the slot list, data contract, title/meta/H1 rules, schema, voice
   targets (Barnwell lean) and gate. It is the spec. Follow it exactly.
2. `src/data/glossary/expected-goals.json`: the finished reference page. Match its shape, depth and voice.
3. `src/data/glossary-terms.json`: every term's `id`, `slug`, `name`, `abbr`, `category` and hover `short`.
   Use these slugs for your file names, `related[].slug` and `calculation.variants[].slug`. Your hero
   definition must agree with your term's `short`.
4. `research/glossary-pseo/stat_themes.json`: the keyword theme per stat `id` (`primary`, `supporting`,
   `status`, `primary_override`). Copy primary/supporting into `keywords`.

## Your files (write only these)
- `src/data/glossary/<slug>.json` for each assigned slug.
- `research/glossary-pseo/claims/<slug>.md`: the page's claims register (same table as TEMPLATE.md's
  expected-goals register: # | claim | source | verdict), then the voice metrics, then a "Proposed hover
  short" line ONLY if the current `short` in glossary-terms.json disagrees with your page (≤ 30 words, no
  colon, evergreen).
- New raw data you download goes in `research/glossary-pseo/raw/` under a new descriptive filename. Never
  overwrite an existing raw file.

Do NOT edit TEMPLATE.md, glossary-terms.json, anything in `src/lib`, `src/pages`, `src/layouts`,
`src/styles`, `pipeline/` or `data/`. Do NOT run `npm run build`, `astro build` or `astro dev` (the build
runs centrally once every page is in; parallel builds collide). Do NOT git commit or push.

## Keywords
- `status` theme / no_serp_overlap / single_keyword / data_intent: primary = the theme's `primary.keyword`,
  supporting = the `supporting[].keyword` list (empty when there is none).
- `status` no_volume (no primary): use a natural phrase "<stat name> in hockey" (or the abbreviation form
  people would type) as primary, supporting [], and set `keywords.source` to say there's no measured volume.
- Placement per TEMPLATE (gate checks it): primary in title, H1, meta and the first 100 words; each supporting
  keyword once in the body. Never stuff.

## Data and numbers
- Season numbers come from the completed 2025-26 season. MoneyPuck season files for 2025-26 are already in
  `research/glossary-pseo/raw/mp_{teams,skaters,goalies}_2025.csv` (downloaded 2026-10-09; MoneyPuck season
  "2025" = 2025-26; a `situation` column splits all / 5on5 / 5on4 / 4on5 / other). The skaters file carries
  faceoffs, hits, blocks, takeaways, giveaways, penalty minutes, penalties drawn, shots, points and more.
- For anything MoneyPuck lacks (power-play %, penalty-kill %, regulation wins, points %, official TOI, NHL
  shooting %, shutouts, quality starts), use the NHL stats API, e.g.
  `https://api.nhle.com/stats/rest/en/team/summary?cayenneExp=seasonId=20252026%20and%20gameTypeId=2`,
  `.../skater/summary?limit=-1&cayenneExp=...`, `.../goalie/summary?limit=-1&cayenneExp=...`, or
  `https://api-web.nhle.com/v1/standings/<date>`. Save what you use to `raw/`.
- Every computed number names its file and download date in `method`. Benchmarks need denominators
  ("the 32 teams", "327 forwards with 60+ GP").
- The 2026-27 season has just started (Detroit is 1-2-0). Make no claims about 2026-27 outside the live slot.
- Live slot: only the fields TEMPLATE.md lists as available today (dashboard tiles, team.json, skaters.json,
  goalies.json). If your stat isn't carried, omit `live` entirely. Say in your report what field you'd want.

## Facts
Every factual claim (history, who invented it, how a site defines or computes it, rule details) must be
verified against a primary or reputable source before it goes in: NHL.com / NHL rulebook / NHL stats
glossary, Hockey-Reference glossary, MoneyPuck, Evolving-Hockey, Hockey-Graphs, HockeyViz, Wikipedia only as
a pointer to primary sources. Use WebSearch and WebFetch (deferred tools: load with ToolSearch
`select:WebSearch,WebFetch`). Natural Stat Trick blocks automated fetches; cite what other sources confirm
about NST or leave it out. If you can't verify something, cut it. Never invent quotes, dates or numbers.

## Voice and copy
Barnwell-leaning voice per TEMPLATE.md "Voice" (claim-first sentences, every number with a baseline + source
+ so-what, contractions ≥ 28/1k, hedges and intensifiers ≤ 3/1k, no signpost openers). Banned: em dashes,
en dashes in season ranges (write 2025-26), payoff colons, "X, not Y" / "rather than" contrast frames, colons
or pipes in title/H1. Running prose roughly 900-1,500 words; a narrow stat can sit at the low end but every
slot is still filled. FAQ only for questions the page doesn't already answer (0-4). `reviewed`:
"2026-10-09", `status`: "gate-passed". `stat.category` = the term's category in glossary-terms.json.
`stat.short` is what reads naturally in the fixed H2s ("Where PIM comes from", "How Corsi is calculated");
use the main abbreviation, or the name when there isn't one.

Prose may link to `/team/` and to player pages. Only link a player whose page exists (see
`src/lib/pages.js` and `data/site/players/`); otherwise name him without a link.

## Gate (each page, before you report)
1. `python3 research/glossary-pseo/gate_glossary.py <slug>` → PASS.
2. `python3 research/glossary-pseo/voice/extract_prose.py <slug> > /tmp/<slug>.txt` then
   `python3 research/style/style_metrics.py --target barnwell_lean /tmp/<slug>.txt`: every metric in range
   (for a short page, note any metric the small sample pushes out and why).
3. `python3 ~/.claude/skills/ai-content-detection/scripts/analyze_text.py --input /tmp/<slug>.txt`: no
   contrast frames, payoff colons or unicode artifacts (metric-name n-grams are expected).
4. Claims register complete, every row SUPPORTED.
5. `python3 -c "import json; json.load(open('src/data/glossary/<slug>.json'))"` parses.

## Report back (short)
Per slug: gate PASS, words, the voice metrics that were hardest to hit, facts you cut because you couldn't
verify them, a proposed hover `short` if any, and live-slot fields you'd want added to the pipeline.
