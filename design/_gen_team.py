import sys; sys.path.insert(0,'.')
from _kit import *

sit_table = '''        <div style="display: grid; grid-template-columns: 150px 76px 70px 78px 78px 62px 62px 84px; padding: 0 0 12px; border-bottom: 1px solid ''' + INK + ''';">
          <span class="lbl" style="font-size: 8px;">Situation</span>
          <span class="lbl" style="font-size: 8px; text-align: right;">xGF%</span>
          <span class="lbl" style="font-size: 8px; text-align: right;">CF%</span>
          <span class="lbl" style="font-size: 8px; text-align: right;">xGF</span>
          <span class="lbl" style="font-size: 8px; text-align: right;">xGA</span>
          <span class="lbl" style="font-size: 8px; text-align: right;">GF</span>
          <span class="lbl" style="font-size: 8px; text-align: right;">GA</span>
          <span class="lbl" style="font-size: 8px; text-align: right;">Minutes</span>
        </div>
        <sc-for list="{{situations}}" as="s" hint-placeholder-count="4">
          <div style="display: grid; grid-template-columns: 150px 76px 70px 78px 78px 62px 62px 84px; align-items: center; padding: 15px 0; border-bottom: 1px solid ''' + HAIR + ''';">
            <div>
              <span style="font-size: 15px; font-weight: 500; display: block;">{{s.name}}</span>
              <span class="mono" style="font-size: 9.5px; color: ''' + INK3 + ''';">{{s.rank}}</span>
            </div>
            <span class="mono" style="font-size: 13px; text-align: right; font-weight: 600;">{{s.xgf}}</span>
            <span class="mono" style="font-size: 13px; text-align: right; color: ''' + INK2 + ''';">{{s.cf}}</span>
            <span class="mono" style="font-size: 13px; text-align: right; color: ''' + INK2 + ''';">{{s.xgfor}}</span>
            <span class="mono" style="font-size: 13px; text-align: right; color: ''' + INK2 + ''';">{{s.xgag}}</span>
            <span class="mono" style="font-size: 13px; text-align: right; color: ''' + INK2 + ''';">{{s.gf}}</span>
            <span class="mono" style="font-size: 13px; text-align: right; color: ''' + INK2 + ''';">{{s.ga}}</span>
            <span class="mono" style="font-size: 13px; text-align: right; color: ''' + INK2 + ''';">{{s.toi}}</span>
          </div>
        </sc-for>'''

barcode_plot = '''        <div style="display: flex; align-items: stretch; gap: 2px; height: 150px; padding: 0 2px;">
          <sc-for list="{{barcode}}" as="b" hint-placeholder-count="82">
            <div title="{{b.title}}" style="position: relative; flex-grow: 1; min-width: 0;">
              <div style="{{b.stem}}"></div>
              <div style="{{b.dot}}"></div>
            </div>
          </sc-for>
        </div>
        <div style="position: relative; height: 1px; background: #3a3936; margin-top: -75px;"></div>
        <div style="display: flex; justify-content: space-between; margin-top: 66px;">
          <span class="lbl" style="font-size: 8px; color: #7c7b78;">Oct 9</span>
          <div style="display: flex; gap: 16px;">
            <span class="lbl" style="font-size: 8px; color: #7c7b78; display: flex; align-items: center; gap: 6px;"><span style="width: 7px; height: 7px; border-radius: 50%; background: ''' + RED + '''; display: inline-block;"></span>Won</span>
            <span class="lbl" style="font-size: 8px; color: #7c7b78; display: flex; align-items: center; gap: 6px;"><span style="width: 7px; height: 7px; border-radius: 50%; background: ''' + WHITE + '''; display: inline-block;"></span>Lost</span>
          </div>
          <span class="lbl" style="font-size: 8px; color: #7c7b78;">Apr 15</span>
        </div>'''

waffle_plot = '''        <div style="display: grid; grid-template-columns: repeat(20, minmax(0, 1fr)); gap: 6px;">
          <sc-for list="{{waffle}}" as="d" hint-placeholder-count="100">
            <div title="{{d.title}}" style="{{d.style}}"></div>
          </sc-for>
        </div>
        <div style="display: flex; gap: 22px; margin-top: 18px;">
          <span class="lbl" style="font-size: 8px; display: flex; align-items: center; gap: 7px;"><span style="width: 9px; height: 9px; border-radius: 50%; background: ''' + RED + '''; display: inline-block;"></span>Detroit &mdash; 49</span>
          <span class="lbl" style="font-size: 8px; display: flex; align-items: center; gap: 7px;"><span style="width: 9px; height: 9px; border-radius: 50%; background: ''' + GREY2 + '''; display: inline-block;"></span>Opposition &mdash; 51</span>
        </div>'''

body = topbar('Team') + '''

  <div style="padding: 20px 64px 0;">
    <div style="display: grid; grid-template-columns: minmax(0, 1fr) 400px; gap: 12px; align-items: stretch;">
      <div class="panel" style="padding: 40px 44px 38px;">
        <p class="lbl" style="margin: 0 0 26px; color: ''' + INK + ''';">Detroit Red Wings &nbsp;·&nbsp; 2025&ndash;26</p>
        <h1 class="dot" style="font-size: 58px;">Team</h1>
        <p style="font-size: 18px; line-height: 1.55; color: ''' + INK2 + '''; margin: 28px 0 0; max-width: 42em;">
          Where the season actually went, in every game state. Rebuilt each night from the NHL API and
          MoneyPuck &mdash; no selection, no smoothing, and a league rank wherever the league publishes one.
        </p>
      </div>
      <div class="panel" style="padding: 30px 32px 28px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <p class="lbl" style="margin: 0 0 16px; color: ''' + INK + ''';">Record</p>
          <p class="mono" style="margin: 0 0 6px; font-size: 34px; font-weight: 500; letter-spacing: -0.04em;">41&ndash;31&ndash;10</p>
          <p class="mono" style="margin: 0; font-size: 13px; color: ''' + INK2 + ''';">92 points &nbsp;·&nbsp; .561</p>
        </div>
        <p class="mono" style="margin: 0; font-size: 11px; color: ''' + INK2 + '''; line-height: 1.6;">
          sixth in the division &nbsp;·&nbsp; fourth in the wild-card race<br>rebuilt apr 16 2026 · 03:12 et
        </p>
      </div>
    </div>
  </div>

  <div style="padding: 12px 64px 0;">
    <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px;">
      <sc-for list="{{tiles}}" as="t" hint-placeholder-count="5">
        <div class="panel" style="padding: 22px 22px 20px; display: flex; flex-direction: column; gap: 8px;">
          <span class="lbl" style="font-size: 8px;">{{t.k}}</span>
          <span class="mono" style="font-size: 28px; font-weight: 500; letter-spacing: -0.04em; line-height: 1;">{{t.v}}</span>
          <span class="mono" style="font-size: 10px; color: ''' + INK2 + '''; line-height: 1.4;">{{t.note}}</span>
        </div>
      </sc-for>
    </div>
  </div>

  <div style="padding: 12px 64px 0;">
''' + figure('Every situation, whole season',
             'share of expected goals by game state &nbsp;·&nbsp; minutes are real time on ice',
             sit_table,
             'Situational table &nbsp;·&nbsp; moneypuck &nbsp;·&nbsp; all strengths',
             pad='30px 34px 26px') + '''
  </div>

  <div style="padding: 12px 64px 0;">
''' + figure('Eighty-two games, as a barcode',
             'goal differential per game &nbsp;·&nbsp; in order, october to april',
             barcode_plot,
             'Season barcode &nbsp;·&nbsp; nhl api &nbsp;·&nbsp; all games',
             invert=True, pad='30px 34px 24px') + '''
  </div>

  <div style="padding: 12px 64px 0;">
    <div style="display: grid; grid-template-columns: minmax(0, 1fr) 520px; gap: 12px; align-items: start;">
''' + figure('One hundred expected goals at five-on-five',
             'how the season&rsquo;s even-strength chances split &nbsp;·&nbsp; one dot = one percent',
             waffle_plot,
             'Dot grid &nbsp;·&nbsp; moneypuck &nbsp;·&nbsp; 5v5 only',
             pad='30px 34px 26px') + '''

      <div class="panel" style="padding: 30px 34px 28px;">
        <p style="margin: 0 0 3px; font-size: 15px; font-weight: 600;">What this season was</p>
        <p class="mono" style="margin: 0 0 20px; font-size: 11px; color: ''' + INK2 + ''';">read alongside the table above</p>
        <p style="margin: 0 0 16px; font-size: 15.5px; line-height: 1.6; color: ''' + INK + ''';">
          Detroit was a league-average team at even strength and an elite one on the power play. The
          man advantage generated the third-most expected goals in the NHL and converted almost exactly on
          model &mdash; 51 goals against 53.73 expected.
        </p>
        <p style="margin: 0 0 22px; font-size: 15.5px; line-height: 1.6; color: ''' + INK + ''';">
          Five-on-five is where the season went. Eighteenth in expected-goal share, nineteenth in shot
          attempts, and 142 goals against 170 allowed in the state that makes up most of a hockey game.
        </p>
        <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px;">
          <sc-for list="{{ranks}}" as="r" hint-placeholder-count="3">
            <div style="background: ''' + INSET + '''; border-radius: 16px; padding: 16px 18px 15px;">
              <p class="lbl" style="margin: 0 0 8px; font-size: 8px;">{{r.k}}</p>
              <p class="mono" style="margin: 0; font-size: 20px; font-weight: 500;">{{r.v}}</p>
            </div>
          </sc-for>
        </div>
      </div>
    </div>
  </div>

''' + FOOTER

script = '''class Component extends DCLogic {
  renderVals() {
''' + BAR_JS + '''
    var games = [GAMES];
    var barcodeRows = games.map(function (g, i) {
      var diff = g[0], res = g[1], won = res === 'W';
      var b = barcode(diff, 7, 150, { color: won ? RED : '#f2f1ef' });
      return { stem: b.stem, dot: b.dot,
               title: 'Game ' + (i + 1) + ' — ' + (diff > 0 ? '+' : '') + diff + ' (' + res + ')' };
    });

    var waffle = [];
    for (var i = 0; i < 100; i++) {
      var mine = i < 49;
      waffle.push({
        title: mine ? 'Detroit — ' + (i + 1) + ' of 49' : 'Opposition',
        style: 'aspect-ratio: 1; border-radius: 50%; background: ' + (mine ? RED : '#4a4845') + ';'
      });
    }

    return {
      barcode: barcodeRows,
      waffle: waffle,
      tiles: [
        { k: 'Goals for', v: '241', note: 'nhl official' },
        { k: 'Goals against', v: '258', note: '−17 differential' },
        { k: '5v5 xG share', v: '49.0%', note: '18th in the nhl' },
        { k: 'Power play xGF', v: '3rd', note: '53.7 expected, 51 scored' },
        { k: 'Finishing', v: '−17.5', note: 'moneypuck: 239 of 256.5' }
      ],
      situations: [
        { name: 'All situations', rank: 'no league rank published', xgf: '50.0%', cf: '49.0%',
          xgfor: '256.45', xgag: '252.38', gf: '239', ga: '254', toi: '4,978.9' },
        { name: 'Five-on-five', rank: '18th xGF% · 19th CF%', xgf: '49.0%', cf: '49.0%',
          xgfor: '161.14', xgag: '169.16', gf: '142', ga: '170', toi: '4,065.4' },
        { name: 'Power play (5v4)', rank: '3rd in expected goals generated', xgf: '91.0%', cf: '89.0%',
          xgfor: '53.73', xgag: '5.40', gf: '51', ga: '4', toi: '394.2' },
        { name: 'Penalty kill (4v5)', rank: 'no league rank published', xgf: '9.0%', cf: '9.0%',
          xgfor: '4.54', xgag: '43.73', gf: '3', ga: '43', toi: '328.0' }
      ],
      ranks: [
        { k: '5v5 expected-goal share', v: '18th' },
        { k: '5v5 shot-attempt share', v: '19th' },
        { k: 'Power-play xG generated', v: '3rd' }
      ]
    };
  }
}'''

GAMES = open('_games.txt').read().strip()
script = script.replace('GAMES', GAMES)

open('Team.dc.html','w').write(doc(1440, 2760, body, script))
print('Team.dc.html written:', len(open('Team.dc.html').read()))
