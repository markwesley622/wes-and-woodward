import re, sys
sys.path.insert(0,'.')
from _kit import INK, INK2, INK3, HAIR

def edit(fn, pairs):
    s = open(fn).read()
    for old, new in pairs:
        assert s.count(old) >= 1, f'{fn}: not found -> {old[:70]!r}'
        s = s.replace(old, new)
    open(fn, 'w').write(s)
    print(f'  {fn}')

print('stripping eyebrows:')

# ---- section-page eyebrows sitting above a Doto title ----
edit('Team.dc.html', [(
  '<p class="lbl" style="margin: 0 0 26px; color: ' + INK + ';">Detroit Red Wings &nbsp;·&nbsp; 2025&ndash;26</p>\n        ', '')])
edit('Players.dc.html', [(
  '<p class="lbl" style="margin: 0 0 22px; color: ' + INK + ';">Player database</p>\n          ', '')])
edit('Glossary.dc.html', [(
  '<p class="lbl" style="margin: 0 0 26px; color: ' + INK + ';">Plain English</p>\n        ', '')])
edit('Articles.dc.html', [(
  '<p class="lbl" style="margin: 0 0 26px; color: ' + INK + ';">Everything written here</p>\n        ', '')])

# ---- Articles: card kickers above headlines (subject already lives in the tag row) ----
edit('Articles.dc.html', [
  ('            <span class="lbl" style="font-size: 8px;">{{feature.kicker}}</span>\n', ''),
  ('''            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px; flex-wrap: wrap;">
              <span class="lbl" style="font-size: 8px;">{{a.kicker}}</span>
            </div>
''', ''),
])

# ---- Column: category moves down into the byline row ----
edit('Column.dc.html', [
  ('<p class="lbl" style="margin: 0 0 22px; color: ' + INK + ';">Forwards &nbsp;·&nbsp; Finishing</p>\n      ', ''),
  ('''<span class="lbl" style="color: ''' + INK + ''';">Mark Wesley</span>
        <span style="width: 3px; height: 3px; background: ''' + INK3 + '''; border-radius: 50%;"></span>
        <span class="lbl">April 14, 2026</span>''',
   '''<span class="lbl" style="color: ''' + INK + ''';">Mark Wesley</span>
        <span style="width: 3px; height: 3px; background: ''' + INK3 + '''; border-radius: 50%;"></span>
        <span class="lbl">Forwards &nbsp;·&nbsp; Finishing</span>
        <span style="width: 3px; height: 3px; background: ''' + INK3 + '''; border-radius: 50%;"></span>
        <span class="lbl">April 14, 2026</span>'''),
])

# ---- Player: the descriptor moves below the name ----
edit('Player.dc.html', [
  ('''<p class="lbl" style="margin: 0 0 16px; color: ''' + INK + ''';">Right wing &nbsp;·&nbsp; 2025&ndash;26 &nbsp;·&nbsp; 82 games</p>
          <h1 class="dot" style="font-size: 54px;">Alex DeBrincat</h1>''',
   '''<h1 class="dot" style="font-size: 54px;">Alex DeBrincat</h1>
          <p class="mono" style="margin: 16px 0 0; font-size: 12.5px; color: ''' + INK2 + ''';">Right wing &nbsp;·&nbsp; 2025&ndash;26 &nbsp;·&nbsp; 82 games</p>'''),
])

# ---- Main: pillar + reference-row eyebrows ----
edit('Main.dc.html', [
  ('          <span class="lbl" style="font-size: 8px;">{{c.eyebrow}}</span>\n', ''),
  ('<h2 class="dot" style="font-size: 38px; margin: 16px 0 0;">{{c.title}}</h2>',
   '<h2 class="dot" style="font-size: 38px; margin: 0;">{{c.title}}</h2>'),
  ('          <span class="lbl" style="font-size: 8px;">Reference</span>\n', ''),
  ('          <span class="lbl" style="font-size: 8px;">Masthead</span>\n', ''),
  ('<h3 class="dot" style="font-size: 30px; margin: 14px 0 0;">Glossary</h3>',
   '<h3 class="dot" style="font-size: 30px; margin: 0;">Glossary</h3>'),
  ('<h3 class="dot" style="font-size: 30px; margin: 14px 0 0;">About</h3>',
   '<h3 class="dot" style="font-size: 30px; margin: 0;">About</h3>'),
])

# drop the now-unused eyebrow field from the data
s = open('Main.dc.html').read()
s = re.sub(r"\{ eyebrow: '[^']*', title:", "{ title:", s)
open('Main.dc.html','w').write(s)
print('  Main.dc.html — eyebrow field removed from renderVals')
