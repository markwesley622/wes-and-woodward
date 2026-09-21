# Shared design kit for the Wes & Woodward artboards.
# Minimal-digital-clean: flat neutral field, pill geometry, mono numerals,
# dot-matrix display type. Wings red appears ONLY inside data visualisations.

FIELD='#d7d6d3'; SURFACE='#e7e6e3'; INSET='#cbcac7'; WHITE='#f2f1ef'
INK='#141414'; INK2='#5f5e5b'; INK3='#91908d'; HAIR='#c1c0bd'
RED='#ce1126'; DOWN='#4a4845'

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Doto:wght@400;600;800&'
         'family=IBM+Plex+Mono:wght@400;500;600&'
         'family=Space+Grotesk:wght@400;500;600;700&display=swap">')

HELMET = FONTS + '''
  <style>
    body { margin: 0; background: ''' + FIELD + '''; color: ''' + INK + ''';
           font-family: 'Space Grotesk', ui-sans-serif, system-ui, sans-serif;
           -webkit-font-smoothing: antialiased; }
    a { color: ''' + INK + '''; text-decoration: none; }
    a:hover { color: ''' + INK2 + '''; }
    .mono { font-family: 'IBM Plex Mono', ui-monospace, SFMono-Regular, monospace;
            font-variant-numeric: tabular-nums; font-feature-settings: 'tnum' 1; }
    .dot  { font-family: 'Doto', 'IBM Plex Mono', monospace; font-weight: 800;
            letter-spacing: 0.06em; text-transform: uppercase; line-height: 1; margin: 0; }
    .lbl  { font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 10px;
            font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase;
            color: ''' + INK3 + '''; }
    .hed  { font-family: 'Space Grotesk', ui-sans-serif, sans-serif; font-weight: 600;
            line-height: 1.06; letter-spacing: -0.025em; text-wrap: balance; margin: 0; }
    .panel { background: ''' + SURFACE + '''; border-radius: 22px; }
    .track { background: ''' + INSET + '''; border-radius: 999px; position: relative; }
  </style>'''

def topbar(active):
    """Wordmark left, pill nav right. Active pill is solid black."""
    items = ['Team', 'Players', 'Articles', 'Glossary', 'About']
    pills = []
    for it in items:
        if it == active:
            st = 'background: ' + INK + '; color: ' + WHITE + '; border: 1px solid ' + INK + ';'
        else:
            st = 'background: transparent; color: ' + INK2 + '; border: 1px solid ' + HAIR + ';'
        pills.append(
            '<a class="lbl" href="#" style="' + st +
            ' font-size: 9px; padding: 10px 15px; border-radius: 999px; white-space: nowrap;">' + it + '</a>')
    # Lockup mirrors src/layouts/Base.astro: Doto WW monogram (offset shadow) + Doto wordmark + mono tagline.
    mono = open('ww-monogram-shadow.svg').read().replace('fill="#ce1126"', 'fill="' + RED + '"').replace('fill="#141414"', 'fill="' + INK + '"')
    mono = mono.replace('<svg ', '<svg style="height: 46px; width: auto; display: block;" ', 1)
    head = ('  <div style="display: flex; justify-content: space-between; align-items: center; gap: 36px; padding: 22px 64px 18px;">\n'
            '    <a href="#" style="display: flex; align-items: center; gap: 16px;">' + mono +
            '<span style="display: flex; flex-direction: column; gap: 4px;">'
            '<span class="dot" style="font-size: 22px;">Wes <span style="color: ' + RED + ';">&amp;</span> Woodward</span>'
            '<span class="lbl" style="font-size: 9px; color: ' + INK3 + ';">Detroit Red Wings analytics</span></span></a>\n'
            '    <div style="display: flex; gap: 7px;">\n')
    tail = '\n    </div>\n  </div>'
    return head + '\n'.join('      ' + p for p in pills) + tail

FOOTER = ('''  <div style="padding: 30px 64px 44px;">
    <div class="panel" style="padding: 24px 28px; display: flex; justify-content: space-between; gap: 40px; align-items: center;">
      <p style="margin: 0; font-size: 13px; color: ''' + INK2 + '''; line-height: 1.6; max-width: 62em;">
        Wes &amp; Woodward is an independent publication and is not affiliated with the Detroit Red Wings or
        the National Hockey League. Data from the NHL API, MoneyPuck, HockeyStatCards and Natural Stat Trick, Evolving-Hockey and Elite Prospects; dashboards rebuild nightly.
      </p>
      <span class="lbl" style="white-space: nowrap;">&copy; 2026</span>
    </div>
  </div>''')

def doc(preview_w, preview_h, body, script_body, props_extra=''):
    props = '{"$preview":{"width":%d,"height":%d}%s}' % (preview_w, preview_h, props_extra)
    return ('''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>''' + HELMET + '''
</helmet>

<div style="width: ''' + str(preview_w) + '''px; background: ''' + FIELD + ''';">
''' + body + '''
</div>
</x-dc>

<script data-dc-script data-props=\'''' + props + '''\'>
''' + script_body + '''
</script>
</body>
</html>
''')

# Diverging bar helpers, emitted into each artboard's JS.
BAR_JS = """    var RED = '""" + RED + """', DOWN = '""" + DOWN + """';
    // Diverging fill around a centre line. Sign is carried by SIDE as well as
    // colour, so the pair stays readable without relying on hue alone.
    function diverge(value, scale, thickness) {
      var half = Math.min(Math.abs(value) / scale, 1) * 50;
      var css = 'position: absolute; top: 0; bottom: 0; border-radius: 999px; ';
      return value >= 0
        ? css + 'left: 50%; width: ' + half + '%; background: ' + RED + ';'
        : css + 'right: 50%; width: ' + half + '%; background: ' + DOWN + ';';
    }
"""

# ---------------------------------------------------------------- analog viz
# Monochrome instrument idiom: hairlines with dot terminals, capsule bars,
# dot grids, inverted panels. Wings red is the single highlight inside a figure.
GREY1='#141414'; GREY2='#4a4845'; GREY3='#7c7b78'; GREY4='#a8a7a4'; GREY5='#cbcac7'

def figure(title, sub, inner, slug, invert=False, pad='26px 28px 20px'):
    """Figure block: title, one-line subtitle, plot, tiny mono slug strip."""
    bg   = GREY1 if invert else SURFACE
    tx   = WHITE if invert else INK
    sx   = INK3  if invert else INK2
    slugc= '#4a4845' if invert else '#a8a7a4'
    return ('''      <div style="background: ''' + bg + '''; border-radius: 22px; padding: ''' + pad + ''';">
        <p style="margin: 0 0 3px; font-size: 15px; font-weight: 600; color: ''' + tx + '''; letter-spacing: -0.01em;">''' + title + '''</p>
        <p class="mono" style="margin: 0 0 22px; font-size: 11px; color: ''' + sx + ''';">''' + sub + '''</p>
''' + inner + '''
        <p class="lbl" style="margin: 18px 0 0; font-size: 8px; color: ''' + slugc + ''';">''' + slug + '''</p>
      </div>''')

# Lollipop row: hairline out from a centre line, dot terminal.
LOLLIPOP_JS = """
    // Lollipop: a hairline out from the centre line with a dot terminal.
    // Side encodes sign, so the red/graphite pair never carries meaning alone.
    function lollipop(value, scale, opts) {
      opts = opts || {};
      var h = Math.min(Math.abs(value) / scale, 1) * 50;
      var up = value >= 0;
      var col = up ? (opts.up || '#ce1126') : (opts.down || '#141414');
      var side = up ? 'left: 50%;' : 'right: 50%;';
      var stem = 'position: absolute; top: 50%; transform: translateY(-50%); height: 2px; '
        + side + ' width: ' + h + '%; background: ' + col + '; opacity: 0.55;';
      var dotSide = up ? 'left: calc(50% + ' + h + '%);' : 'right: calc(50% + ' + h + '%);';
      var d = opts.dot || 9;
      var dot = 'position: absolute; top: 50%; ' + dotSide
        + ' width: ' + d + 'px; height: ' + d + 'px; border-radius: 50%; background: ' + col
        + '; transform: translate(' + (up ? '-50%' : '50%') + ', -50%);';
      return { stem: stem, dot: dot, color: col };
    }

    // Barcode: one hairline per observation, height scaled, dot at the tip.
    function barcode(value, scale, height, opts) {
      opts = opts || {};
      var h = Math.min(Math.abs(value) / scale, 1) * (height / 2 - 5);
      var up = value >= 0;
      var col = opts.color || (up ? '#ce1126' : '#141414');
      var stem = 'position: absolute; left: 50%; transform: translateX(-50%); width: 1.5px; '
        + 'background: ' + col + '; opacity: 0.5; height: ' + h + 'px; '
        + (up ? 'bottom: 50%;' : 'top: 50%;');
      var dot = 'position: absolute; left: 50%; transform: translateX(-50%); '
        + 'width: 5px; height: 5px; border-radius: 50%; background: ' + col + '; '
        + (up ? 'bottom: calc(50% + ' + h + 'px - 2.5px);' : 'top: calc(50% + ' + h + 'px - 2.5px);');
      return { stem: stem, dot: dot };
    }
"""

# ------------------------------------------------------------- data portrait
# A player's likeness, drawn from his own numbers. Two dot grids: goals scored
# (solid) against individual expected goals (hollow). Unique per player,
# generated from the pipeline, and carries no image rights at all.
def portrait(size=186):
    return ('''        <div style="width: ''' + str(size) + '''px; background: ''' + INSET + '''; border-radius: 22px; padding: 18px 18px 16px; box-sizing: border-box;">
          <p class="lbl" style="margin: 0 0 8px; font-size: 8px; color: ''' + INK2 + ''';">Scored &nbsp;{{portrait.goals}}</p>
          <div style="display: grid; grid-template-columns: repeat(14, 1fr); gap: 3px; margin-bottom: 14px;">
            <sc-for list="{{portrait.scored}}" as="d" hint-placeholder-count="41">
              <div style="aspect-ratio: 1; border-radius: 50%; background: ''' + RED + ''';"></div>
            </sc-for>
          </div>
          <p class="lbl" style="margin: 0 0 8px; font-size: 8px; color: ''' + INK2 + ''';">Expected &nbsp;{{portrait.expected}}</p>
          <div style="display: grid; grid-template-columns: repeat(14, 1fr); gap: 3px;">
            <sc-for list="{{portrait.model}}" as="d" hint-placeholder-count="37">
              <div style="aspect-ratio: 1; border-radius: 50%; background: transparent; border: 1.2px solid ''' + INK3 + '''; box-sizing: border-box;"></div>
            </sc-for>
          </div>
        </div>''')

PORTRAIT_JS = """
    // Data portrait: one dot per goal, one hollow dot per expected goal.
    function makePortrait(goals, ixg) {
      var expected = Math.round(ixg);
      return {
        goals: String(goals),
        expected: String(expected),
        scored: new Array(goals).fill(0),
        model: new Array(expected).fill(0)
      };
    }
"""
