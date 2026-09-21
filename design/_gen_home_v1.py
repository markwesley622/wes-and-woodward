import sys; sys.path.insert(0,'.')
from _kit import *

def ghost(w, h=9, op='0.30'):
    return ('<div style="height: %spx; width: %s; border-radius: 999px; background: %s; opacity: %s;"></div>'
            % (h, w, INK3, op))

def ghost_lines(widths, h=9, gap=7, op='0.30'):
    rows = ''.join('\n            ' + ghost(w, h, op) for w in widths)
    return ('<div style="display: flex; flex-direction: column; gap: %spx;">%s\n          </div>' % (gap, rows))

body = topbar(None) + '''

  <!-- what this is -->
  <div style="padding: 14px 64px 0;">
    <div style="background: ''' + GREY1 + '''; border-radius: 22px; padding: 46px 48px 42px;">
      <div style="display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 64px; align-items: end;">
        <div>
          <h1 class="dot" style="font-size: 60px; color: ''' + WHITE + ''';">Detroit Red Wings,<br>by the numbers</h1>
          <p style="margin: 30px 0 0; font-size: 18.5px; line-height: 1.6; color: ''' + GREY4 + '''; max-width: 44em;">
            Every figure is cited to its original source. This is meant for Red Wings fans who not only want to
            see what transpires on the ice, but also seek to understand how or why it happened. Articles come
            out regularly, and player and team dashboards are rebuilt nightly.
          </p>
        </div>
        <div style="display: flex; flex-direction: column; gap: 12px;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 12px 0; border-bottom: 1px solid #2e2d2b;">
            <span class="lbl" style="font-size: 8px; color: ''' + GREY3 + ''';">Open</span>
            <span class="mono" style="font-size: 12.5px; color: ''' + WHITE + ''';">NHL API · MoneyPuck</span>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; padding: 12px 0; border-bottom: 1px solid #2e2d2b;">
            <span class="lbl" style="font-size: 8px; color: ''' + GREY3 + ''';">Licensed</span>
            <span class="mono" style="font-size: 12.5px; color: ''' + WHITE + ''';">Evolving-Hockey · Elite Prospects</span>
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 12px 0; border-bottom: 1px solid #2e2d2b;">
            <span class="lbl" style="font-size: 8px; color: ''' + GREY3 + ''';">Last rebuilt</span>
            ''' + ghost('120px', 9, '0.45') + '''
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 12px 0; border-bottom: 1px solid #2e2d2b;">
            <span class="lbl" style="font-size: 8px; color: ''' + GREY3 + ''';">Season</span>
            ''' + ghost('86px', 9, '0.45') + '''
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- the three standing sections -->
  <div style="padding: 12px 64px 0;">
    <h2 class="hed" style="font-size: 36px; margin: 30px 0 18px;">Dive Deeper</h2>
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;">
      <sc-for list="{{pillars}}" as="c" hint-placeholder-count="3">
        <a href="#" class="panel" style="padding: 34px 36px 30px; display: flex; flex-direction: column;">
          <h3 class="dot" style="font-size: 34px; margin: 0;">{{c.title}}</h3>
          <p style="margin: 16px 0 0; font-size: 15.5px; line-height: 1.55; color: ''' + INK2 + ''';">{{c.blurb}}</p>
          <p style="margin: 14px 0 0; font-size: 14px; line-height: 1.55; color: ''' + INK3 + ''';">{{c.detail}}</p>

          <div style="margin: 24px 0 0; padding: 20px 22px; border: 1px dashed ''' + INK3 + '''; border-radius: 16px;">
            <p class="lbl" style="margin: 0 0 14px; font-size: 8px;">{{c.slot}}</p>
            <div style="display: flex; gap: 26px;">
              <sc-for list="{{c.stats}}" as="s" hint-placeholder-count="2">
                <div style="display: flex; flex-direction: column; gap: 7px;">
                  <span class="lbl" style="font-size: 8px;">{{s}}</span>
                  <div style="height: 15px; width: 62px; border-radius: 999px; background: ''' + INK3 + '''; opacity: 0.30;"></div>
                </div>
              </sc-for>
            </div>
          </div>

          <span class="lbl" style="color: ''' + INK + '''; margin-top: 22px;">{{c.cta}} &rarr;</span>
        </a>
      </sc-for>
    </div>
  </div>

  <!-- season figure slot -->
  <div style="padding: 12px 64px 0;">
    <div style="background: ''' + GREY1 + '''; border-radius: 22px; padding: 30px 34px 26px;">
      <p style="margin: 0 0 3px; font-size: 15px; font-weight: 600; color: ''' + WHITE + ''';">The season, game by game</p>
      <p class="mono" style="margin: 0 0 24px; font-size: 11px; color: ''' + INK3 + ''';">the signature figure &mdash; renders once a season is loaded</p>
      <div style="border: 1px dashed #3a3936; border-radius: 16px; height: 150px; display: flex; align-items: center; justify-content: center;">
        <span class="lbl" style="font-size: 8px; color: ''' + GREY3 + ''';">[ Season barcode ]</span>
      </div>
      <p class="lbl" style="margin: 18px 0 0; font-size: 8px; color: #4a4845;">Season barcode &nbsp;·&nbsp; nhl api &nbsp;·&nbsp; rebuilt nightly</p>
    </div>
  </div>

  <!-- articles -->
  <div style="padding: 12px 64px 0;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; margin: 22px 0 14px;">
      <h2 class="hed" style="font-size: 36px; margin: 0;">Latest Analysis</h2>
      <a class="lbl" href="#" style="color: ''' + INK + '''; border-bottom: 1px solid ''' + INK + '''; padding-bottom: 4px;">All articles &rarr;</a>
    </div>

    <a href="#" class="panel" style="padding: 38px 42px 36px; display: grid; grid-template-columns: minmax(0, 1fr) 250px; gap: 48px; align-items: end; margin-bottom: 12px; border: 1px dashed ''' + INK3 + ''';">
      <div>
        <span class="lbl" style="font-size: 8px;">[ Featured article ]</span>
        <div style="margin: 20px 0 0;">''' + ghost_lines(['86%','62%'], 24, 12) + '''</div>
        <div style="margin: 24px 0 0;">''' + ghost_lines(['74%','68%'], 9, 8) + '''</div>
      </div>
      <div style="display: flex; flex-direction: column; gap: 9px; align-items: flex-end;">
        ''' + ghost('116px') + '''
        ''' + ghost('92px') + '''
      </div>
    </a>

    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;">
      <sc-for list="{{stubs}}" as="s" hint-placeholder-count="3">
        <div class="panel" style="padding: 28px 30px 26px; border: 1px dashed ''' + INK3 + '''; display: flex; flex-direction: column; gap: 16px;">
          <span class="lbl" style="font-size: 8px;">{{s}}</span>
          <div style="display: flex; flex-direction: column; gap: 9px;">
            <div style="height: 17px; width: 92%; border-radius: 999px; background: ''' + INK3 + '''; opacity: 0.30;"></div>
            <div style="height: 17px; width: 64%; border-radius: 999px; background: ''' + INK3 + '''; opacity: 0.30;"></div>
          </div>
          <div style="display: flex; flex-direction: column; gap: 7px;">
            <div style="height: 8px; width: 100%; border-radius: 999px; background: ''' + INK3 + '''; opacity: 0.22;"></div>
            <div style="height: 8px; width: 78%; border-radius: 999px; background: ''' + INK3 + '''; opacity: 0.22;"></div>
          </div>
        </div>
      </sc-for>
    </div>
  </div>

  <!-- reference row -->
  <div style="padding: 12px 64px 0;">
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px;">
      <a href="#" class="panel" style="padding: 30px 34px 28px; display: flex; justify-content: space-between; align-items: flex-end; gap: 24px;">
        <div>
          <h3 class="dot" style="font-size: 30px; margin: 0;">Glossary</h3>
          <p style="margin: 14px 0 0; font-size: 14.5px; line-height: 1.55; color: ''' + INK2 + '''; max-width: 34em;">
            Every number used on this site, defined in plain English, with a worked example and a note on what
            it cannot tell you.
          </p>
        </div>
        <span class="lbl" style="color: ''' + INK + '''; white-space: nowrap;">Open &rarr;</span>
      </a>
      <a href="#" class="panel" style="padding: 30px 34px 28px; display: flex; justify-content: space-between; align-items: flex-end; gap: 24px;">
        <div>
          <h3 class="dot" style="font-size: 30px; margin: 0;">About</h3>
          <p style="margin: 14px 0 0; font-size: 14.5px; line-height: 1.55; color: ''' + INK2 + '''; max-width: 34em;">
            Who publishes this, how the data is built, and the standards every figure is held to before it
            appears on the site.
          </p>
        </div>
        <span class="lbl" style="color: ''' + INK + '''; white-space: nowrap;">Open &rarr;</span>
      </a>
    </div>
  </div>

''' + FOOTER

script = '''class Component extends DCLogic {
  renderVals() {
    return {
      pillars: [
        { title: 'Roster',
          blurb: 'The professional roster with individual expected goals, finishing, on-ice shares and league percentiles.',
          detail: 'Sortable on every column, and a page for each player.',
          slot: '[ live counts ]', stats: ['Skaters', 'Goaltenders'], cta: 'Open the roster' },
        { title: 'System',
          blurb: 'Every player in the organisation developing below the professional roster — which league, which club, and how they are producing against it.',
          detail: 'Counting stats only: no public expected-goals model covers these leagues.',
          slot: '[ live counts ]', stats: ['Players', 'Leagues'], cta: 'Open the system' },
        { title: 'Team',
          blurb: 'Record, goal differential and share of expected goals in all four game states, against the league distribution.',
          detail: 'With a league rank wherever the league publishes one.',
          slot: '[ live counts ]', stats: ['Record', '5v5 xG share'], cta: 'Open the dashboard' }
      ],
      stubs: ['[ Article ]', '[ Article ]', '[ Article ]']
    };
  }
}'''

open('Main.dc.html','w').write(doc(1440, 2260, body, script))
print('Main.dc.html — navigation shell:', len(open('Main.dc.html').read()))
