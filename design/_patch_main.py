import sys; sys.path.insert(0,'.')
from _kit import *

s = open('Main.dc.html').read()
marker = FOOTER
assert s.count(marker) == 1, 'footer marker not unique'

entry = '''  <div style="padding: 12px 64px 0;">
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px;">
      <a href="#" class="panel" style="padding: 30px 34px 28px; display: flex; justify-content: space-between; align-items: flex-end; gap: 24px;">
        <div>
          <p class="lbl" style="margin: 0 0 14px; color: ''' + INK + ''';">Rebuilt nightly</p>
          <h3 class="dot" style="font-size: 34px;">Team</h3>
          <p style="margin: 14px 0 0; font-size: 14.5px; line-height: 1.55; color: ''' + INK2 + '''; max-width: 34em;">
            Every game state, every league rank, and the season as a barcode.
          </p>
        </div>
        <span class="lbl" style="color: ''' + INK + '''; white-space: nowrap;">Open &rarr;</span>
      </a>
      <a href="#" class="panel" style="padding: 30px 34px 28px; display: flex; justify-content: space-between; align-items: flex-end; gap: 24px;">
        <div>
          <p class="lbl" style="margin: 0 0 14px; color: ''' + INK + ''';">29 on the roster</p>
          <h3 class="dot" style="font-size: 34px;">Players</h3>
          <p style="margin: 14px 0 0; font-size: 14.5px; line-height: 1.55; color: ''' + INK2 + '''; max-width: 34em;">
            The professional roster and the players developing below it, each with their own page.
          </p>
        </div>
        <span class="lbl" style="color: ''' + INK + '''; white-space: nowrap;">Open &rarr;</span>
      </a>
    </div>
  </div>

'''
s = s.replace(marker, entry + marker)

# secondary reads now carry stream labels
s = s.replace("meta: 'Goaltending · 7 min'", "meta: 'Analysis · Goaltending · 7 min'")
s = s.replace("meta: 'Defence · 6 min'", "meta: 'Analysis · Defence · 6 min'")
s = s.replace("meta: 'Forwards · 8 min'", "meta: 'Analysis · Forwards · 8 min'")
s = s.replace('More from Wes &amp; Woodward', 'Latest analysis')

# frame is taller now
s = s.replace('"$preview":{"width":1440,"height":2180}', '"$preview":{"width":1440,"height":2420}')

open('Main.dc.html','w').write(s)
print('Main.dc.html patched:', len(s))
