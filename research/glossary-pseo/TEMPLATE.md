# Glossary page template (one page per stat)

Spec for the W&W stat glossary at `/glossary/<slug>/`. Written 2026-10-09. One JSON file per stat in
`src/data/glossary/<slug>.json`; `src/pages/glossary/[slug].astro` renders every page from the same
fixed slot list, and `src/lib/glossary.js` fills the live Red Wings slot from the nightly pipeline. The
worked example is `expected-goals.json` (live at `/glossary/expected-goals/` once pushed).

Same rule as the Bluevine international and FLORA art-styles families: **one skeleton, only the fills
change.** Headings are built by the page from `stat.short`, never written in the JSON, so no page can
drift structurally. Extra per-stat material goes inside an existing slot, never into a new H2.

## Slot list (fixed order)

| # | Slot | H2 (built from `short`) | Purpose | Length | Data | Keyword variants it absorbs |
|---|---|---|---|---|---|---|
| 1 | Hero | (H1) | Kicker `Glossary · {category} stat`, H1, the **definition** (the answer passage), dek, quick-facts tiles, on-page jump list | Definition 40-70 words, 2-3 sentences, sentence 1 stands alone. Dek 2 sentences | Static | "what is X in hockey", "what does X mean in hockey", "X meaning hockey", "X hockey" (definitional) |
| 1b | Quick facts | (none, tiles under the hero) | Also-called names, unit/scale, league average, best and worst of last season, who publishes it, which source W&W uses | 4 or 8 tiles; value ≤ 12 chars, sub ≤ 60 | Static, benchmarks computed from the dated research pull | abbreviation and alias queries ("xgf hockey stat", "sat hockey") |
| 2 | Origin | Where {short} comes from | Who invented it, when it went mainstream, who publishes it now, what raw data it's built from | 3-4 paragraphs | Static, every fact sourced | "who invented corsi", history queries |
| 3 | Calculation | How {short} is calculated | Inputs list, formula rows, a worked example with round numbers (labelled as such), what's excluded, the variant definitions (for/against/share/individual) | Intro 1 para, 3-7 inputs, 2-5 formulas, example 3-5 sentences, 2-5 variants | Static | "how is X calculated", "X formula", "how to calculate X", the for/against/% variants ("xga hockey", "cf%") |
| 4 | Meaning | What {short} tells you | What it measures, the benchmarks with numbers (average, best, worst, Detroit, plus a player scale where the stat has one), what it predicts | 3-4 paragraphs | Static, numbers from the dated research pull | "what is a good X", "X average" |
| 5 | Uses | How analysts use {short} | 2-4 uses, each an H3 + one paragraph with a real Red Wings or league example and a number | 60-110 words each | Static | "X vs goals", applied queries |
| 6 | Live | {short} on the Red Wings | This season's team tiles (value + league rank) and a Red Wings leaderboard on the stat, as-of stamp, small-sample note | Intro 1-2 sentences; 2-4 tiles; 5-8 rows | **Pipeline JSON**, rebuilt nightly (see below) | "nhl X", "X leaders", "red wings X", "X nhl" (data intent) |
| 7 | Limits | What {short} can't tell you | 3-6 named blind spots, each H3 + 1-2 sentences, sourced | 30-70 words each | Static | "is X a good stat", "X problems" |
| 8 | Related | Related stats | 3-6 cards to sibling pages, each with a one-line "X vs Y" difference | 1 line each | Static; cards link only when the sibling JSON exists, otherwise render greyed | "X vs Y" |
| 9 | FAQ | Questions | Only People Also Ask questions whose answer is NOT already on the page. Zero is fine | 0-4, answers 2-4 sentences | Static | leftover PAA |
| 10 | Sources | Sources | Numbered sources (label, publisher, what it supports), method note for computed numbers, last-reviewed date | as needed | Static | n/a |

The FAQ answers may not restate the body (same rule as the on-page "green copy" rule). If a PAA question
is answered above, the FAQ drops it; if the slot ends up empty, the section and the FAQPage schema are not
rendered.

## Data contract (`src/data/glossary/<slug>.json`)

```jsonc
{
  "slug": "expected-goals",             // stat's full name, lowercase, hyphenated. Not the keyword (themes change; URLs shouldn't)
  "status": "draft",                     // draft | gate-passed | approved | live
  "reviewed": "2026-10-09",              // ISO; feeds dateModified and the "Last reviewed" line
  "stat": { "name": "Expected goals", "short": "xG", "abbr": "xG", "aliases": ["xGF", "..."], "category": "Advanced", "plural": false },
                                         // short: what reads in the H2s. Mixed-case abbreviations (xG, GSAx) keep their case; words and
                                         // all-caps abbreviations uppercase. Single letters read badly (use "goals", not "G"). plural: true
                                         // switches the H2 verbs ("Where hits come from").
                                         // category: Skater | Goalie | Team | Advanced (hub grouping)
  "keywords": { "primary": "...", "supporting": ["..."], "source": "stat_themes.json ..." },
                                         // copied from research/glossary-pseo/stat_themes.json for this stat
  "seo": { "title": "...", "description": "...", "h1": "..." },
  "hero": { "definition": "html", "dek": "html" },
  "facts": [ { "label": "...", "value": "...", "sub": "..." } ],          // 4 or 8
  "origin": [ "html paragraph", "..." ],
  "calculation": { "intro": ["html"], "inputs": ["..."], "formulas": [ { "label": "...", "expr": "..." } ],
                   "example": "html", "after": ["html"], "variants": [ { "term": "xGF", "def": "...", "slug": "optional-sibling" } ] },
  "meaning": [ "html paragraph" ],
  "uses": [ { "title": "...", "html": "..." } ],
  "live": {                               // omit entirely for a stat the pipeline doesn't carry yet
    "intro": "...",
    "tiles": [ { "tile": "xg_share_5v5" },                                        // a dashboard.json tile by key
               { "label": "...", "source": "team", "path": "situations.5on5.corsiPct", "format": "pct1", "rankPath": "leagueRanks.corsiPct_5on5" } ],
    "leaders": { "source": "skaters|goalies", "sort": "ixG", "ascending": false, "limit": 8, "caption": "...",
                 "columns": [ { "label": "ixG", "path": "ixG", "format": "num2" } ] },
    "smallSample": 20, "smallSampleNote": "Detroit has played {gp} games. ..."
  },
  "limits": [ { "title": "...", "html": "..." } ],
  "related": [ { "slug": "corsi", "name": "Corsi", "abbr": "CF%", "vs": "one line" } ],
  "faq": [ { "q": "...", "a": "..." } ],   // 0-4
  "sources": [ { "label": "...", "publisher": "...", "url": "...", "note": "what it supports" } ],
  "method": "how every computed number on the page was computed, with the download date"
}
```

Formats for live cells: `int`, `num1`, `num2`, `pct1` (0.6 → 60.0%), `signed1`, `signed2` (U+2212 minus), `sv3` (0.903 → .903, save-percentage style), `mmss` (seconds → 20:00), `hmm` (seconds → hours:minutes for season totals). `live.credit` sets the "Data:" line under the live slot (default "MoneyPuck"; e.g. "NHL API and MoneyPuck").

Season length: 2025-26 was 82 games; the new CBA makes 2026-27 84 games (NHL.com). Tie any "82" to 2025-26 or say "a full season".

### How the live slot is wired

`src/lib/glossary.js` imports `data/site/dashboard.json`, `team.json`, `skaters.json` and `goalies.json`
(all rebuilt by the nightly refresh) and resolves the stat's `live` spec at build time:

- `{ "tile": key }` pulls a ready-made tile (label, value, league rank) from `dashboard.tiles`. Current keys:
  `xg_share_5v5`, `xg_share_5v5_adj`, `finishing`, `gsax`, `pp_xgf60`, `pk_xga60`.
- `{ source, path, format, rankPath }` reads any field from `team.json` (e.g. `situations.5on5.corsiPct`,
  rank `leagueRanks.corsiPct_5on5`).
- `leaders` sorts `skaters.json` or `goalies.json` on any field (dotted paths work: `fiveOnFive.ixgPer60`) and
  links each name to the player's canonical page through `src/lib/pages.js`.
- The as-of stamp is `dashboard.generatedAt`; the small-sample note appears while Detroit's games played is
  under `smallSample`.

Because the nightly GitHub Action rebuilds the site after the refresh, the live slot updates with no edit to
the stat JSON. A stat whose numbers the pipeline doesn't yet carry (e.g. high-danger chances, zone starts)
ships without `live`, and the slot disappears; add the field to `pipeline/build_site_data.py` first, then the
`live` spec.

Fields available today: skaters `gamesPlayed goals assists points shots shootingPct toiPerGame ixG
goalsAboveExpected gameScore fiveOnFive.{icetimeMinutes,onIceXgPct,onIceCorsiPct,ixgPer60}`; goalies
`gamesPlayed gamesStarted wins losses otLosses savePct gaa shutouts gsax`; team `record.*`,
`situations.{all,5on5,5on4,4on5}.{xGoalsPct,corsiPct,xGoalsFor,xGoalsAgainst,goalsFor,goalsAgainst,iceTime}`,
`leagueRanks.{xGoalsPct_5on5,corsiPct_5on5,xGoalsFor_5on4}`.

## Title, meta, H1

- **Title** (`seo.title`, ≤ 60 chars before the site suffix): the primary keyword first where it reads
  naturally, joined with a real word ("and", "for", "with"). No colon, and no pipe inside `seo.title`. The page
  appends the suffix ` | Wes & Woodward` (Mark 10/9: keep the brand suffix, split it with a pipe).
- **Meta description** ≤ 160 chars: what the stat is in one clause, then what the page covers, ending on the
  Red Wings' live numbers.
- **H1**: the stat's name with its abbreviation, carrying the primary keyword. No colon. It need not repeat
  the title.
- Keyword placement (gated by `gate_glossary.py`): primary in title, H1, meta and the first 100 words; each
  supporting keyword once in the body. "Present" means the exact phrase, or the keyword's words in order with
  only stopwords between them ("xGF in hockey" satisfies "xgf hockey"); for word-order flips that read
  badly as an exact phrase, all of the keyword's words in one sentence also passes. Never stuff.
- H2s are template-fixed and carry `short` (the abbreviation), so the stat's name is in every H2.

## Schema

The page passes these nodes to `Base.astro`, which adds Organization, WebSite and the BreadcrumbList
(Home → Glossary → stat; `glossary` was added to Base's breadcrumb sections):

- `WebPage` (@id = URL, `about` → the term, `dateModified` = `reviewed`)
- `DefinedTerm` (@id `URL#term`, name, `alternateName` = aliases, `termCode` = abbr, `description` = the
  definition, `inDefinedTermSet` → `/glossary/#set`)
- `DefinedTermSet` (@id `/glossary/#set`); the hub page lists every term in `hasDefinedTerm`
- `FAQPage` only when `faq` is non-empty

## Internal links

- Kicker links to the hub `/glossary/` (`src/pages/glossary/index.astro`, grouped by category).
- Related cards and `calculation.variants[].slug` link to sibling pages only when the sibling JSON exists
  (no dead links while the family is being built).
- Player names in the live table link to canonical player pages; prose links to player pages and to `/team/`
  where the example lives there.
- Mark 10/9: Glossary lives in the global footer, not the header nav. Stat labels across the site get a hover
  card with the term's `short` definition from `src/data/glossary-terms.json` and a "Full definition" link once
  that stat's page exists (so every new glossary page needs its `short` written there too).

## Copy rules

W&W professional register in the Barnwell-leaning voice below: claim-first sentences, every number with a
baseline and a source, contractions, varied sentence length. No em dashes. Season
ranges with a hyphen (2025-26), matching the article copy. No colon in title or H1. No "X, not Y" frames.
Worked examples with invented round numbers say so. Every factual claim goes in the page's claims register
below with a source, and every computed number names its file and download date in `method`.

## Voice (Mark 10/9: "leaning a bit more towards the barnwell end of the spectrum")

Every glossary page is written to Mark's style analysis (`research/style/`, memory
`wes-woodward-prose-style-target`), pulled toward Bill Barnwell and away from Simmons: detail-dense, dry,
claim-first, fewer one-liners and less first person. It's a reference page in a publication's voice, so the
tone is Barnwell's explainer register, never a column's.

**Measure it.** `python3 research/glossary-pseo/voice/extract_prose.py <slug> > x.txt` pulls the running prose
(hero definition and dek, origin, calculation intro/example/after, meaning, uses, limits, FAQ answers; the
variant definitions and live-slot UI lines are excluded because they're short by design), then
`python3 research/style/style_metrics.py --target barnwell_lean x.txt`. The target block lives in
`research/style/baseline.json` as `barnwell_lean`; the original `target` (Simmons tone + Barnwell detail) is
unchanged for Mark's columns.

| Metric | Mark (2 columns) | Simmons | Barnwell | **Glossary target** |
|---|---|---|---|---|
| Sentence length, mean | 18.0-21.5 | 15.2 | 21.1 | **17-21** |
| Sentence length, SD | 8.4-9.7 | 14.2 | 10.5 | **≥ 10** |
| Short sentences (≤ 6 words) | 2-7% | 32% | 6.5% | **6-15%** |
| Long sentences (≥ 30 words) | 9-21% | 13% | 23% | **≤ 20%** |
| Words per paragraph | 89-91 | 63 | 79 | **55-85** |
| One-sentence paragraphs | 3-6% | 27% | 6% | **5-12%** |
| Contractions per 1k | 9-13 | 34 | 35 | **≥ 28** |
| "I/me/my" per 1k | 2-8 | 18 | 3.5 | **≤ 6** (usually 0 on a glossary page) |
| "you" per 1k | 3-4 | 11 | 5.3 | **3-8** |
| Questions per 1k | 0.4-3.4 | 12.6 | 2.9 | **1-5** (asked and answered at once) |
| Parentheses per 1k | 3-5 | 15.5 | 4.7 | **3-8** |
| Intensifiers per 1k | 5-7 | 2.3 | 2.8 | **≤ 3** |
| Transition openers | 15-18% | 7% | 4.5% | **≤ 5%** |
| Numbers per 1k | 44-51 | 43 | 33 | **30-55** (benchmarks make these pages number-dense) |
| Hedges per 1k | 4.6-5.8 | 2.5 | 2.8 | **≤ 3** |

**The moves that make it Barnwell, beyond the numbers:**
- Topic sentence states the claim, then the evidence ("Hockey's version of expected goals is 22 years old.").
- Every number gets a baseline, a named source and a so-what: Detroit's 2.38 is "a tick below the middle of
  the pack" next to the median team's 2.47; McDavid's 43.6 is "about two and a half times the median forward."
- Base rates with denominators ("the fifth-largest shortfall among the league's 940 skaters"; "for scale,
  the league took 112,096 unblocked attempts in 2025-26 alone").
- Parentheticals carry context numbers and asides; a question appears only when the next sentence answers it
  ("Why trust a model over the scoreboard? Because of what it predicts.").
- Dry asides over jokes, and a short sentence after a long run to land the point ("That's a finishing problem.").
- Possessives and contractions read naturally ("the Wings'", "it's", "doesn't"); "Detroit" and "the Wings"
  carry most references, "the Red Wings" sparingly.

**Banned:** em dashes; payoff colons (a list-intro colon before the inputs list is fine); "X, not Y" and
"rather than" contrast frames; signpost openers ("When it comes to", "In terms of", "It may come as no
surprise", "To round out"); hedges (may, might, likely, potentially, seems) and intensifiers (actually,
significantly, really, very); the "also" tic; new facts that aren't in the claims register.

**Hover definitions** (`src/data/glossary-terms.json` → `short`): 1-2 sentences, ≤ 30 words, plain text, no
colons. Say what the stat counts, then why it matters or where it misleads. Keep them evergreen: no
season-specific numbers (they'd go stale between page reviews). A term with a page must agree with that page's
hero definition.

**expected-goals.json, 10/9 rewrite (running prose, `--target barnwell_lean`):**

| Metric | Before | After | Target |
|---|---|---|---|
| Words | 1,337 | 1,433 | |
| Sentence mean / SD | 16.9 / 9.6 | 18.1 / 10.2 | 17-21 / ≥ 10 |
| Short / long sentences | 11% / 11% | 13% / 15% | 6-15% / ≤ 20% |
| Words per paragraph | 53 | 57 | 55-85 |
| One-sentence paragraphs | 4% | 12% | 5-12% |
| Contractions per 1k | 17.2 | 28.6 | ≥ 28 |
| Questions / parentheses per 1k | 0.0 / 1.5 | 1.4 / 6.3 | 1-5 / 3-8 |
| Intensifiers / hedges / transition openers | 0 / 0 / 0% | 0 / 0 / 0% | ≤ 3 / ≤ 3 / ≤ 5% |
| Numbers per 1k | 50.1 | 51.6 | 30-55 |

Every metric lands inside the target. `gate_glossary.py expected-goals` passes. ai-content-detection
`analyze_text.py`: nothing flagged; the before version carried `uniform_sentence_runs`, the after version
doesn't. The remaining hints (`uniform_paragraph_structure`, `repeated_ngrams`) come from the fixed template
and metric names, as expected. Before copy saved at `research/glossary-pseo/voice/expected-goals.before.json`.

## Gate (before a page ships)

1. `python3 research/glossary-pseo/gate_glossary.py <slug>`: slots, title/meta/H1 rules, keyword placement, dashes.
1b. Voice: `extract_prose.py <slug>` + `style_metrics.py --target barnwell_lean`; every metric in range (see Voice).
2. ai-content-detection `analyze_text.py --input <body.md>` on the extracted body: no contrast frames, no
   payoff colons, no unicode artifacts. Metric-name n-grams ("five on five", "goals above expected") are expected.
3. Claims register complete: every row SUPPORTED by the cited source.
4. `npx astro build` passes; render at 1440 and 390 wide (no horizontal scroll).
5. Do not push without Mark: a push to main deploys the live site.

## Build order for the family

Themes come from `stat_themes.json` (29 themed stats + 6 primary-only). Build in descending primary volume,
but publish related-stat clusters together so the cards light up (xG → ixG → goals above expected → GSAx;
Corsi → Fenwick → PDO; save percentage → GAA → GSAA). Stats with no measurable volume still get a page if
the site uses the stat (the template is the glossary's job, not only search's), but last.

## Open questions for Mark

- Resolved 10/9: suffix stays, split with a pipe (` | Wes & Woodward`); Glossary goes in the global footer;
  stat labels get hover definitions with a "Full definition" link; copy leans Barnwell (Voice section).
- The xG page uses MoneyPuck's 2025-26 file as published on 10/9/2026. MoneyPuck rebuilt its model for
  2026-27 and reports AUC for both versions on 2023-24 through 2025-26; whether the downloadable 2025-26
  season file was re-scored with the new model isn't stated. Benchmarks should be re-pulled when that's clear.

## Claims register: expected-goals.json

| # | Claim (as written or paraphrased) | Source | Verdict |
|---|---|---|---|
| 1 | Average team scored 3.08 goals a game in 2025-26 | W&W calc: 8,086 goals / (32 × 82), MoneyPuck 2025-26 teams file (all situations) | SUPPORTED (computed) |
| 2 | Every shot worth between 0 and 1 | Definition (a probability); MoneyPuck about: "predicts the probability of each shot being a goal" | SUPPORTED |
| 3 | Average unblocked attempt 0.073 xG in 2025-26 | W&W calc: 8,222 xG / 112,096 unblocked attempts, MoneyPuck teams file | SUPPORTED (computed) |
| 4 | 5v5 xGF%: Colorado 56.9 (1st), Carolina 56.3 (2nd), Chicago 42.4 (last), Detroit 48.8 (21st) | W&W calc xGF/(xGF+xGA) at 5on5, MoneyPuck teams file | SUPPORTED (computed) |
| 5 | 5v5 xGF/60 range 2.13 to 3.03 (Colorado), median 2.47, Detroit 2.38 | W&W calc xGF / (iceTime/3600) at 5on5 | SUPPORTED (computed) |
| 6 | 327 forwards with 60+ GP; median ixG 17.3, top 10% ≥ 29.7; McDavid 43.6 led; DeBrincat 36.9, 5th, only Red Wing in top 15 (Larkin 18th) | W&W calc, MoneyPuck skaters file, all situations | SUPPORTED (computed) |
| 7 | Ryder, 2004, "Shot Quality", HockeyAnalytics.com, 2002-03 data, distance/type/rebound, study of shots a team allowed ("22 years old" = 2004 to 2026) | Ryder PDF; arXiv 2511.07703 lit review; Evolving-Hockey history; HockeyStats Medium | SUPPORTED |
| 8 | Sprigings and Toumi, Hockey-Graphs, October 2015; past ~20 games xG beat score-adjusted Corsi and goals at predicting future goals ("didn't catch on for another 11 years" = 2004 to 2015) | Hockey-Graphs 2015-10-01 (bylines DTMAboutHeart and asmean); HockeyStats Medium names them | SUPPORTED |
| 9 | Emmanuel Perry's model on Corsica, 2016 | Evolving-Hockey history (link dated 2016/03/03) | SUPPORTED |
| 10 | MoneyPuck built by Peter Tanner | MoneyPuck about, Contributors | SUPPORTED |
| 11 | Evolving-Hockey (Josh and Luke Younggren), four models: EV, PP, SH offense, empty net; XGBoost | Evolving-Hockey model write-up | SUPPORTED |
| 12 | Natural Stat Trick and HockeyStats publish xG | NST team table columns xGF/xGA/xGF%; HockeyStats methodology page | SUPPORTED |
| 13 | All start from NHL play-by-play with shot type and rink coordinates | Evolving-Hockey variable list (coords_x/y, shot types) | SUPPORTED |
| 14 | MoneyPuck rebuilt for 2026-27, random sample of 289,000+ shots, 2023-24 to 2025-26, gradient boosting | MoneyPuck about | SUPPORTED |
| 15 | MoneyPuck inputs: location, shot type, last event (what/where/seconds), TOI of both teams, skaters per side, off-wing, empty net | MoneyPuck about | SUPPORTED |
| 16 | Shot types wrist/slap/snap/backhand/tip/deflection/wraparound | Evolving-Hockey shot-type variables | SUPPORTED |
| 17 | Blocked shots excluded because the NHL logs the location of the block | Evolving-Hockey model write-up + glossary | SUPPORTED |
| 18 | xG counts the same shots as Fenwick | Evolving-Hockey glossary (xGF = goal probability of all Fenwick shots); NST (Fenwick = unblocked attempts) | SUPPORTED |
| 19 | xGF / xGA / xGF% / ixG definitions | MoneyPuck glossary; Evolving-Hockey glossary; NST formula pattern | SUPPORTED |
| 20 | Detroit 2025-26 5v5: 142 GF on 161.1 xGF (−19.1); only NJD (−33.6), NYI (−20.7), VAN (−20.7) worse; 170 GA on 169.2 xGA | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |
| 21 | DeBrincat 41 on 36.9 (+4.1); Copp 9 on 19.8 (−10.8), 5th-largest shortfall of 940 skaters; Caufield 51 on 33.7 best | W&W calc, MoneyPuck skaters file | SUPPORTED (computed) |
| 22 | One season of finishing carries a lot of luck | MoneyPuck about, shooting talent section | SUPPORTED |
| 23 | GSAx = expected goals against minus goals allowed | MoneyPuck glossary | SUPPORTED |
| 24 | Team page uses GSAx for goaltending; runs an xG standings table nightly | `data/site/dashboard.json` radar + `deserved` table, `src/pages/team.astro` | SUPPORTED |
| 25 | Public models don't see passes; EH's 2-on-1 cross-crease example; HockeyStats has no royal-road pass data, uses proxy features | Evolving-Hockey write-up; HockeyStats methodology | SUPPORTED |
| 26 | MoneyPuck base model and EH model exclude shooting skill; MoneyPuck publishes a shooting-talent-adjusted version | MoneyPuck about + glossary; Evolving-Hockey write-up | SUPPORTED |
| 27 | MoneyPuck demo flags a slap shot recorded closer than it was | MoneyPuck about, flurry section | SUPPORTED |
| 28 | No goalie positioning or screens in MoneyPuck's or EH's published feature lists | MoneyPuck about (components); EH variable list | SUPPORTED (by omission from both lists) |
| 29 | MoneyPuck, EH and HockeyStats train their own models | Each site's methodology page | SUPPORTED |
| 30 | FAQ: MoneyPuck uses skaters-per-side and empty net; EH separate models per situation; Team page splits by situation | MoneyPuck about; EH write-up; `src/pages/team.astro` SIT list | SUPPORTED |
| 31 | FAQ: 2025-26 5v5 G minus xGF: MTL +23.4, BUF +23.0, BOS +22.1, NJD −33.6 | W&W calc, MoneyPuck teams file | SUPPORTED (computed) |

| 32 | "for scale, the league took 112,096 unblocked attempts in 2025-26 alone" (calculation intro) | Same calc as row 3, MoneyPuck teams file | SUPPORTED (computed) |
| 33 | McDavid's 43.6 ixG is "about two and a half times the median forward" (17.3) | 43.6 / 17.3 = 2.52, from row 6 | SUPPORTED (computed) |
| 34 | Caufield "plus-17.3" | 51 − 33.7, from row 21 | SUPPORTED (computed) |
| 35 | Detroit's 5v5 xGF/60 of 2.38 is "a tick below the middle of the pack" (median 2.47) | Row 5 | SUPPORTED (computed) |
| 36 | Detroit "didn't have the finishing to cover the gap" in 2025-26 | Row 20 (142 GF on 161.1 xGF at 5v5) | SUPPORTED (computed) |

Computed rows come from `research/glossary-pseo/raw/mp_{teams,skaters}_2025.csv` (MoneyPuck season "2025" =
2025-26), downloaded 2026-10-09.
