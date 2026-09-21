import sys; sys.path.insert(0,'.')
from _kit import *

pctl_plot = '''        <div style="display: flex; flex-direction: column; gap: 20px;">
          <sc-for list="{{pctls}}" as="p" hint-placeholder-count="2">
            <div style="display: grid; grid-template-columns: 210px minmax(0, 1fr) 92px; gap: 20px; align-items: center;">
              <div style="text-align: right;">
                <span class="mono" style="font-size: 12px; font-weight: 600; display: block;">{{p.metric}}</span>
                <span class="mono" style="font-size: 10.5px; color: ''' + INK2 + ''';">{{p.value}}</span>
              </div>
              <div title="{{p.title}}" style="position: relative; height: 24px;">
                <div class="track" style="position: absolute; left: 0; right: 0; top: 10px; height: 4px;"></div>
                <div style="position: absolute; left: 50%; top: 0; bottom: 0; width: 1px; background: ''' + INK3 + ''';"></div>
                <div style="{{p.stem}}"></div>
                <div style="{{p.dot}}"></div>
              </div>
              <span class="mono" style="font-size: 13px; font-weight: 500; text-align: right;">{{p.readout}}</span>
            </div>
          </sc-for>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 18px; padding-top: 12px; border-top: 1px solid ''' + HAIR + ''';">
          <span class="lbl" style="font-size: 8px;">0th</span>
          <span class="lbl" style="font-size: 8px;">50th &mdash; league average</span>
          <span class="lbl" style="font-size: 8px;">100th</span>
        </div>'''

body = topbar('Players') + '''

  <div style="padding: 20px 64px 0;">
    <div class="panel" style="padding: 34px 40px 34px;">
      <p class="lbl" style="margin: 0 0 24px;"><a href="#" style="color: ''' + INK3 + ''';">Players</a> &nbsp;/&nbsp; <a href="#" style="color: ''' + INK3 + ''';">Red Wings</a> &nbsp;/&nbsp; <span style="color: ''' + INK + ''';">Alex DeBrincat</span></p>
      <div style="display: grid; grid-template-columns: 186px minmax(0, 1fr); gap: 36px; align-items: center;">
''' + portrait(186) + '''
        <div>
          <p class="lbl" style="margin: 0 0 16px; color: ''' + INK + ''';">Right wing &nbsp;·&nbsp; 2025&ndash;26 &nbsp;·&nbsp; 82 games</p>
          <h1 class="dot" style="font-size: 54px;">Alex DeBrincat</h1>
          <p style="font-size: 17px; line-height: 1.55; color: ''' + INK2 + '''; margin: 22px 0 0; max-width: 50em;">
            Detroit&rsquo;s leading scorer, and the only skater on the roster to clear forty goals. He put 287
            shots on goal for 36.87 expected &mdash; the heaviest individual load on the team &mdash; and finished four
            above what those attempts were worth.
          </p>
          <p class="mono" style="margin: 18px 0 0; font-size: 11px; color: ''' + INK3 + ''';">
            portrait: one solid dot per goal scored, one hollow dot per expected goal
          </p>
        </div>
      </div>
    </div>
  </div>

  <div style="padding: 12px 64px 0;">
    <div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px;">
      <sc-for list="{{hero}}" as="h" hint-placeholder-count="6">
        <div class="panel" style="padding: 22px 22px 20px; display: flex; flex-direction: column; gap: 8px;">
          <span class="lbl" style="font-size: 8px;">{{h.k}}</span>
          <span class="mono" style="font-size: 32px; font-weight: 500; letter-spacing: -0.045em; line-height: 1;">{{h.v}}</span>
          <span class="mono" style="font-size: 10px; color: ''' + INK2 + '''; line-height: 1.4;">{{h.note}}</span>
        </div>
      </sc-for>
    </div>
  </div>

  <div style="padding: 12px 64px 0;">
    <div style="display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 12px; align-items: start;">
      <div style="display: flex; flex-direction: column; gap: 12px;">
''' + figure('Where he ranks', 'league forwards with 300+ five-on-five minutes', pctl_plot,
             'Lollipop &nbsp;·&nbsp; moneypuck &nbsp;·&nbsp; 5v5 only', pad='30px 34px 26px') + '''

        <div class="panel" style="padding: 30px 34px 28px;">
          <p style="margin: 0 0 3px; font-size: 15px; font-weight: 600;">Line combinations</p>
          <p class="mono" style="margin: 0 0 22px; font-size: 11px; color: ''' + INK2 + ''';">five-on-five &nbsp;·&nbsp; the only situation moneypuck publishes line data for</p>
          <div style="display: grid; grid-template-columns: minmax(0, 1fr) 56px 70px 66px 60px 60px; padding: 0 0 12px; border-bottom: 1px solid ''' + INK + ''';">
            <span class="lbl" style="font-size: 8px;">Line</span>
            <span class="lbl" style="font-size: 8px; text-align: right;">GP</span>
            <span class="lbl" style="font-size: 8px; text-align: right;">TOI</span>
            <span class="lbl" style="font-size: 8px; text-align: right;">xGF%</span>
            <span class="lbl" style="font-size: 8px; text-align: right;">GF</span>
            <span class="lbl" style="font-size: 8px; text-align: right;">GA</span>
          </div>
          <sc-for list="{{lines}}" as="l" hint-placeholder-count="2">
            <div style="display: grid; grid-template-columns: minmax(0, 1fr) 56px 70px 66px 60px 60px; align-items: baseline; padding: 15px 0; border-bottom: 1px solid ''' + HAIR + ''';">
              <span style="font-size: 15px; font-weight: 500;">{{l.name}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{l.gp}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{l.toi}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; font-weight: 600;">{{l.xgf}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{l.gf}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{l.ga}}</span>
            </div>
          </sc-for>
        </div>
      </div>

      <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="background: ''' + GREY1 + '''; border-radius: 22px; padding: 24px 26px 22px;">
          <p class="lbl" style="margin: 0 0 16px; color: ''' + WHITE + ''';">What the numbers say</p>
          <sc-for list="{{machine}}" as="m" hint-placeholder-count="3">
            <p style="margin: 0 0 14px; font-size: 13px; line-height: 1.55; color: ''' + GREY4 + ''';">{{m}}</p>
          </sc-for>
        </div>
        <div class="panel" style="padding: 24px 26px 20px;">
          <p class="lbl" style="margin: 0 0 16px; color: ''' + INK + ''';">Season line</p>
          <sc-for list="{{season}}" as="s" hint-placeholder-count="8">
            <div style="display: flex; justify-content: space-between; gap: 12px; align-items: baseline; padding: 9px 0; border-bottom: 1px solid ''' + HAIR + ''';">
              <span class="mono" style="font-size: 10.5px; color: ''' + INK2 + ''';">{{s.k}}</span>
              <span class="mono" style="font-size: 13px; font-weight: 500;">{{s.v}}</span>
            </div>
          </sc-for>
        </div>
        <div class="panel" style="padding: 24px 26px 20px;">
          <p class="lbl" style="margin: 0 0 14px; color: ''' + INK + ''';">Written about him</p>
          <a href="#" style="padding: 12px 0; border-bottom: 1px solid ''' + HAIR + '''; display: block;">
            <span style="font-size: 15px; font-weight: 500; line-height: 1.3; display: block;">The forty-goal season nobody argued about</span>
            <span class="lbl" style="font-size: 8px;">Analysis &nbsp;·&nbsp; April 2</span>
          </a>
          <a href="#" style="padding: 12px 0; display: block;">
            <span style="font-size: 15px; font-weight: 500; line-height: 1.3; display: block;">The DeBrincat trade tree</span>
            <span class="lbl" style="font-size: 8px;">Analysis &nbsp;·&nbsp; Evergreen</span>
          </a>
        </div>
      </div>
    </div>
  </div>

''' + FOOTER

script = '''class Component extends DCLogic {
  renderVals() {
''' + LOLLIPOP_JS + PORTRAIT_JS + '''
    var RED = '#ce1126';
    function row(metric, value, p) {
      var l = lollipop(p - 50, 50, { up: RED, down: '#141414', dot: 11 });
      return { metric: metric, value: value, stem: l.stem, dot: l.dot,
               readout: Math.round(p) + 'th pct',
               title: metric + ' — ' + p.toFixed(1) + 'th percentile among league forwards' };
    }
    return {
      portrait: makePortrait(41, 36.87),
      pctls: [
        row('Expected goals per 60', '0.88 at five-on-five', 87.3),
        row('On-ice xG share', '53% at five-on-five', 70.3)
      ],
      hero: [
        { k: 'Goals', v: '41', note: 'team high' },
        { k: 'Assists', v: '44', note: 'third on the team' },
        { k: 'Points', v: '85', note: 'team high' },
        { k: 'Expected goals', v: '36.9', note: 'heaviest shot load' },
        { k: 'Above expected', v: '+4.1', note: 'finished over model' },
        { k: 'Shooting', v: '14.3%', note: '287 shots on goal' }
      ],
      lines: [
        { name: 'DeBrincat · Compher · Kane', gp: '32', toi: '120.7', xgf: '58%', gf: '8', ga: '8' },
        { name: 'DeBrincat · Copp · Kane', gp: '47', toi: '500.1', xgf: '52%', gf: '30', ga: '14' }
      ],
      machine: [
        'Leads the roster in goals (41), points (85) and individual expected goals (36.87).',
        'Finished 4.13 goals above expectation — second on the team, behind Raymond and ahead of Sandin-Pellikka.',
        'His most-used line (with Copp and Kane) out-scored its expectation badly: 30 goals for on 21.23 expected across 500 minutes. Treat that as unrepeatable.'
      ],
      season: [
        { k: 'games played', v: '82' },
        { k: 'goals — assists — points', v: '41 — 44 — 85' },
        { k: 'shots on goal', v: '287' },
        { k: 'shooting percentage', v: '14.3%' },
        { k: 'ice time per game', v: '18:30' },
        { k: 'individual expected goals', v: '36.87' },
        { k: 'goals above expected', v: '+4.13' },
        { k: 'game score', v: '87.36' }
      ]
    };
  }
}'''

open('Player.dc.html','w').write(doc(1440, 1620, body, script))
print('Player.dc.html rebuilt:', len(open('Player.dc.html').read()))
