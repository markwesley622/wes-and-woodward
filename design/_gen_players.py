import sys; sys.path.insert(0,'.')
from _kit import *

RGRID = '206px 40px 44px 44px 44px 48px 58px 62px 70px 58px 64px minmax(0, 1fr)'
SGRID = '206px 44px 52px 74px 96px minmax(0, 1fr) 48px 44px 44px 48px'

body = topbar('Players') + '''

  <div style="padding: 20px 64px 0;">
    <div class="panel" style="padding: 38px 44px 34px;">
      <div style="display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 48px; align-items: end;">
        <div>
          <p class="lbl" style="margin: 0 0 22px; color: ''' + INK + ''';">Player database</p>
          <h1 class="dot" style="font-size: 56px;">Players</h1>
          <p style="font-size: 17px; line-height: 1.55; color: ''' + INK2 + '''; margin: 24px 0 0; max-width: 46em;">
            Everyone in the organisation, in two groups: the professional roster and the players developing
            below it. Click any name for that player&rsquo;s page.
          </p>
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px; align-items: flex-end;">
          <span class="mono" style="font-size: 11px; color: ''' + INK2 + ''';">rebuilt apr 16 2026 · 03:12 et</span>
        </div>
      </div>

      <div style="display: flex; gap: 8px; margin-top: 32px;">
        <sc-for list="{{tabs}}" as="t" hint-placeholder-count="2">
          <button onClick="{{t.pick}}" style="{{t.style}}">
            <span style="font-size: 15px; font-weight: 600; letter-spacing: -0.01em;">{{t.name}}</span>
            <span class="mono" style="font-size: 11px; opacity: 0.62;">{{t.count}}</span>
          </button>
        </sc-for>
      </div>
    </div>
  </div>

  <!-- ROSTER -->
  <sc-if value="{{isRoster}}" hint-placeholder-val="{{ true }}">
    <div>
      <div style="padding: 12px 64px 0;">
        <div class="panel" style="padding: 22px 30px; display: flex; justify-content: space-between; align-items: center; gap: 32px;">
          <div style="display: flex; align-items: center; gap: 14px;">
            <span class="lbl">Position</span>
            <div style="display: flex; gap: 7px;">
              <sc-for list="{{filters}}" as="f" hint-placeholder-count="3">
                <button class="lbl" onClick="{{f.pick}}" style="{{f.style}}">{{f.name}}</button>
              </sc-for>
            </div>
          </div>
          <div style="display: flex; align-items: center; gap: 20px;">
            <span class="lbl" style="font-size: 8px; display: flex; align-items: center; gap: 7px;"><span style="width: 8px; height: 8px; border-radius: 50%; background: ''' + RED + '''; display: inline-block;"></span>Above the 50th percentile</span>
            <span class="lbl" style="font-size: 8px; display: flex; align-items: center; gap: 7px;"><span style="width: 8px; height: 8px; border-radius: 50%; background: ''' + GREY1 + '''; display: inline-block;"></span>Below</span>
            <span class="lbl" style="font-size: 8px; display: flex; align-items: center; gap: 7px;"><span style="width: 8px; height: 8px; border-radius: 50%; background: transparent; border: 1.5px solid ''' + INK3 + '''; display: inline-block; box-sizing: border-box;"></span>Sample too small</span>
          </div>
        </div>
      </div>

      <div style="padding: 12px 64px 0;">
        <div class="panel" style="padding: 10px 30px 26px;">
          <div style="display: grid; grid-template-columns: ''' + RGRID + '''; align-items: center; padding: 16px 0 14px; border-bottom: 1px solid ''' + INK + ''';">
            <sc-for list="{{headers}}" as="h" hint-placeholder-count="12">
              <button onClick="{{h.sort}}" title="{{h.title}}" class="lbl" style="{{h.style}}">{{h.text}}</button>
            </sc-for>
          </div>
          <sc-for list="{{rows}}" as="r" hint-placeholder-count="18">
            <div style="display: grid; grid-template-columns: ''' + RGRID + '''; align-items: center; padding: 11px 0; border-bottom: 1px solid ''' + HAIR + ''';">
              <a href="#" style="font-size: 14.5px; font-weight: 500;">{{r.name}} &rarr;</a>
              <span class="mono" style="font-size: 11px; color: ''' + INK3 + '''; text-align: center;">{{r.pos}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{r.gp}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{r.g}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{r.a}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; font-weight: 600;">{{r.p}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{r.ixg}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{r.gax}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{r.xgpct}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{r.cf}}</span>
              <span class="mono" style="font-size: 12.5px; text-align: right; color: ''' + INK2 + ''';">{{r.per60}}</span>
              <div style="display: flex; align-items: center; gap: 14px; padding-left: 22px;">
                <div title="{{r.pctlTitle}}" style="position: relative; height: 16px; flex-grow: 1;">
                  <div style="position: absolute; left: 50%; top: 0; bottom: 0; width: 1px; background: ''' + HAIR + ''';"></div>
                  <div style="{{r.stem}}"></div>
                  <div style="{{r.dot}}"></div>
                </div>
                <span class="mono" style="font-size: 11.5px; width: 34px; text-align: right; color: ''' + INK2 + ''';">{{r.pctl}}</span>
              </div>
            </div>
          </sc-for>
          <p class="mono" style="margin: 18px 0 0; font-size: 10.5px; color: ''' + INK2 + '''; line-height: 1.7; max-width: 82em;">
            Showing 18 of 29. ixG individual expected goals, all situations &nbsp;·&nbsp; G&minus;ixG goals above
            expected &nbsp;·&nbsp; 5v5 xG% share of expected goals on ice &nbsp;·&nbsp; CF% share of shot attempts
            &nbsp;·&nbsp; ixG/60 expected goals per sixty minutes. A hollow dot marks a skater under three
            hundred five-on-five minutes &mdash; ranked, but not to be trusted.
          </p>
        </div>
      </div>
    </div>
  </sc-if>

  <!-- SYSTEM -->
  <sc-if value="{{isSystem}}" hint-placeholder-val="{{ false }}">
    <div>
      <div style="padding: 12px 64px 0;">
        <div style="background: ''' + GREY1 + '''; border-radius: 22px; padding: 30px 34px 28px;">
          <p class="lbl" style="margin: 0 0 14px; color: ''' + WHITE + ''';">Why this table looks different</p>
          <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 40px;">
            <p style="margin: 0; font-size: 15px; line-height: 1.65; color: ''' + GREY4 + ''';">
              No public expected-goals model covers the AHL, the CHL, the NCAA or the European leagues.
              MoneyPuck is NHL-only. So there is no honest way to show xG, GSAx or league percentiles for a
              player in the system, and this page does not pretend otherwise &mdash; it shows counting stats,
              the league they were produced in, and nothing implying they are comparable across leagues.
            </p>
            <p style="margin: 0; font-size: 15px; line-height: 1.65; color: ''' + GREY4 + ''';">
              A twenty-goal season in the OHL and a twenty-goal season in the AHL are not the same
              achievement, and the only public way to bridge them is NHL-equivalency translation, which is a
              blunt instrument with published factors. If it appears here it will be labelled as an estimate
              and defined in the <a href="#" style="color: ''' + WHITE + '''; border-bottom: 1px solid ''' + GREY2 + ''';">glossary</a>.
            </p>
          </div>
        </div>
      </div>

      <div style="padding: 12px 64px 0;">
        <div class="panel" style="padding: 10px 30px 30px;">
          <div style="display: grid; grid-template-columns: ''' + SGRID + '''; align-items: center; padding: 16px 0 14px; border-bottom: 1px solid ''' + INK + ''';">
            <span class="lbl" style="font-size: 9px;">Player</span>
            <span class="lbl" style="font-size: 9px; text-align: center;">Pos</span>
            <span class="lbl" style="font-size: 9px; text-align: right;">Age</span>
            <span class="lbl" style="font-size: 9px; text-align: right;">Drafted</span>
            <span class="lbl" style="font-size: 9px;">League</span>
            <span class="lbl" style="font-size: 9px;">Club</span>
            <span class="lbl" style="font-size: 9px; text-align: right;">GP</span>
            <span class="lbl" style="font-size: 9px; text-align: right;">G</span>
            <span class="lbl" style="font-size: 9px; text-align: right;">A</span>
            <span class="lbl" style="font-size: 9px; text-align: right;">P</span>
          </div>
          <sc-for list="{{ghosts}}" as="gh" hint-placeholder-count="5">
            <div style="display: grid; grid-template-columns: ''' + SGRID + '''; align-items: center; padding: 13px 0; border-bottom: 1px solid ''' + HAIR + '''; opacity: 0.38;">
              <div style="height: 9px; background: ''' + INK3 + '''; border-radius: 999px; width: {{gh.w}};"></div>
              <div></div><div></div><div></div>
              <div style="height: 9px; background: ''' + INK3 + '''; border-radius: 999px; width: 54px;"></div>
              <div style="height: 9px; background: ''' + INK3 + '''; border-radius: 999px; width: 88px;"></div>
              <div></div><div></div><div></div><div></div>
            </div>
          </sc-for>

          <div style="margin-top: 26px; border: 1px dashed ''' + INK3 + '''; border-radius: 18px; padding: 28px 32px 26px;">
            <p style="margin: 0 0 6px; font-size: 17px; font-weight: 600;">Not wired up yet</p>
            <p style="margin: 0 0 20px; font-size: 14.5px; line-height: 1.6; color: ''' + INK2 + '''; max-width: 62em;">
              The NHL API has a prospects endpoint, but it returns biography only &mdash; no league, no club, no
              stats &mdash; and Detroit&rsquo;s list currently comes back empty. Filling this table needs a second
              source. The candidates, in order of how well they fit an independent publication:
            </p>
            <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;">
              <sc-for list="{{sources}}" as="s" hint-placeholder-count="3">
                <div style="background: ''' + INSET + '''; border-radius: 16px; padding: 18px 20px 17px;">
                  <p class="mono" style="margin: 0 0 7px; font-size: 12.5px; font-weight: 600;">{{s.name}}</p>
                  <p style="margin: 0 0 10px; font-size: 13px; line-height: 1.5; color: ''' + INK2 + ''';">{{s.what}}</p>
                  <p class="lbl" style="margin: 0; font-size: 8px;">{{s.catch}}</p>
                </div>
              </sc-for>
            </div>
          </div>
        </div>
      </div>
    </div>
  </sc-if>

''' + FOOTER

script = '''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { tab: 'Roster', key: 'p', dir: -1, pos: 'All' };
  }

  data() {
    return [
      ['Alex DeBrincat','R',82,41,44,85,36.87,4.13,0.53,0.51,0.884,70.3,true],
      ['Lucas Raymond','L',80,25,51,76,19.49,5.51,0.49,0.51,0.596,39.2,true],
      ['Dylan Larkin','C',74,34,33,67,33.76,0.24,0.47,0.50,0.659,24.3,true],
      ['Moritz Seider','D',82,10,50,60,7.50,2.50,0.55,0.53,0.172,84.0,true],
      ['Patrick Kane','R',67,16,41,57,16.50,-0.50,0.52,0.50,0.691,63.9,true],
      ['Andrew Copp','C',79,9,34,43,19.83,-10.83,0.51,0.50,0.730,56.2,true],
      ['James van Riemsdyk','L',72,15,16,31,19.23,-4.23,0.48,0.47,0.804,31.1,true],
      ['Emmitt Finnie','C',82,13,17,30,19.20,-6.20,0.49,0.49,0.798,39.2,true],
      ['J.T. Compher','L',82,11,17,28,12.07,-1.07,0.47,0.46,0.588,24.3,true],
      ['Simon Edvinsson','D',72,9,16,25,6.37,2.63,0.51,0.52,0.189,60.3,true],
      ['Axel Sandin-Pellikka','D',68,7,14,21,3.51,3.49,0.46,0.50,0.161,17.7,true],
      ['Marco Kasper','C',81,9,10,19,15.41,-6.41,0.50,0.50,0.807,47.2,true],
      ['Ben Chiarot','D',82,5,10,15,4.33,0.67,0.45,0.46,0.167,11.4,true],
      ['Mason Appleton','C',65,6,8,14,6.06,-0.06,0.44,0.47,0.389,8.8,true],
      ['Michael Rasmussen','C',64,6,8,14,9.88,-3.88,0.48,0.45,0.650,31.1,true],
      ['Albert Johansson','D',82,3,8,11,2.90,0.10,0.47,0.46,0.137,27.8,true],
      ['Justin Faulk','D',17,5,3,8,7.85,-2.85,0.45,0.47,0.218,11.4,true],
      ['Nate Danielson','C',28,2,5,7,4.11,-2.11,0.49,0.48,0.660,39.2,false]
    ];
  }

  renderVals() {
''' + LOLLIPOP_JS + '''
    var self = this, st = this.state;

    var tabs = [
      { name: 'Red Wings', count: '29 players', key: 'Roster' },
      { name: 'In the system', count: 'prospects', key: 'System' }
    ].map(function (t) {
      var on = st.tab === t.key;
      return {
        name: t.name, count: t.count,
        style: 'cursor: pointer; display: flex; flex-direction: column; gap: 5px; align-items: flex-start;'
          + ' font-family: inherit; text-align: left; padding: 16px 26px; border-radius: 18px;'
          + ' border: 1px solid ' + (on ? '#141414' : '#c1c0bd') + ';'
          + ' background: ' + (on ? '#141414' : 'transparent') + ';'
          + ' color: ' + (on ? '#f2f1ef' : '#5f5e5b') + ';',
        pick: function () { self.setState({ tab: t.key }); }
      };
    });

    var IDX = { name: 0, pos: 1, gp: 2, g: 3, a: 4, p: 5, ixg: 6, gax: 7, xgpct: 8, cf: 9, per60: 10, pctl: 11 };
    var cols = [
      { key: 'name',  text: 'Player',  align: 'left',   title: 'Sort by name' },
      { key: 'pos',   text: 'Pos',     align: 'center', title: 'Sort by position' },
      { key: 'gp',    text: 'GP',      align: 'right',  title: 'Games played' },
      { key: 'g',     text: 'G',       align: 'right',  title: 'Goals' },
      { key: 'a',     text: 'A',       align: 'right',  title: 'Assists' },
      { key: 'p',     text: 'P',       align: 'right',  title: 'Points' },
      { key: 'ixg',   text: 'ixG',     align: 'right',  title: 'Individual expected goals' },
      { key: 'gax',   text: 'G−ixG',   align: 'right',  title: 'Goals above expected' },
      { key: 'xgpct', text: '5v5 xG%', align: 'right',  title: 'On-ice share of expected goals' },
      { key: 'cf',    text: 'CF%',     align: 'right',  title: 'On-ice share of shot attempts' },
      { key: 'per60', text: 'ixG/60',  align: 'right',  title: 'Expected goals per sixty minutes' },
      { key: 'pctl',  text: 'Percentile', align: 'left', pad: true, title: 'Rank among league regulars' }
    ];

    var headers = cols.map(function (c) {
      var active = st.key === c.key;
      return {
        text: c.text + (active ? (st.dir === -1 ? ' ↓' : ' ↑') : ''),
        title: c.title,
        style: 'cursor: pointer; user-select: none; background: transparent; border: 0; padding: 0;'
          + ' font-family: inherit; font-size: 9px; text-align: ' + c.align + ';'
          + ' color: ' + (active ? '#141414' : '#91908d') + ';' + (c.pad ? ' padding-left: 22px;' : ''),
        sort: function () {
          self.setState({ key: c.key,
            dir: st.key === c.key ? -st.dir : (c.key === 'name' || c.key === 'pos' ? 1 : -1) });
        }
      };
    });

    var filters = ['All', 'Forwards', 'Defence'].map(function (name) {
      var on = st.pos === name;
      return {
        name: name,
        style: 'cursor: pointer; font-family: inherit; font-size: 9px; padding: 9px 16px; border-radius: 999px;'
          + ' border: 1px solid ' + (on ? '#141414' : '#c1c0bd') + ';'
          + ' background: ' + (on ? '#141414' : 'transparent') + ';'
          + ' color: ' + (on ? '#f2f1ef' : '#5f5e5b') + ';',
        pick: function () { self.setState({ pos: name }); }
      };
    });

    var list = this.data().filter(function (r) {
      if (st.pos === 'Forwards') return r[1] !== 'D';
      if (st.pos === 'Defence') return r[1] === 'D';
      return true;
    });
    var i = IDX[st.key];
    list = list.slice().sort(function (a, b) {
      var x = a[i], y = b[i];
      if (typeof x === 'string') return st.dir * x.localeCompare(y);
      return st.dir * (x - y);
    });

    var rows = list.map(function (r) {
      var pctl = r[11], ok = r[12], d = pctl - 50;
      var l = lollipop(d, 50, { up: '#ce1126', down: '#141414', dot: 9 });
      var dot = ok ? l.dot : l.dot.replace('background: ' + l.color + ';',
        'background: transparent; border: 1.5px solid #91908d; box-sizing: border-box;');
      return {
        name: r[0], pos: r[1], gp: r[2], g: r[3], a: r[4], p: r[5],
        ixg: r[6].toFixed(1),
        gax: (r[7] > 0 ? '+' : '−') + Math.abs(r[7]).toFixed(1),
        xgpct: (r[8] * 100).toFixed(1),
        cf: (r[9] * 100).toFixed(1),
        per60: r[10].toFixed(2),
        pctl: ok ? pctl.toFixed(0) : pctl.toFixed(0) + '*',
        stem: ok ? l.stem : l.stem.replace('opacity: 0.55;', 'opacity: 0.25;'),
        dot: dot,
        pctlTitle: r[0] + ' — ' + pctl.toFixed(1) + 'th percentile'
          + (ok ? '' : ' (under 300 five-on-five minutes)')
      };
    });

    return {
      tabs: tabs,
      isRoster: st.tab === 'Roster',
      isSystem: st.tab === 'System',
      headers: headers, rows: rows, filters: filters,
      ghosts: [{ w: '140px' }, { w: '116px' }, { w: '152px' }, { w: '124px' }, { w: '134px' }],
      sources: [
        { name: 'Elite Prospects',
          what: 'The canonical prospect database — every league, every season, draft and contract status.',
          catch: 'Commercial licence · redistribution restricted' },
        { name: 'HockeyTech / LeagueStat',
          what: 'Powers the AHL and the three CHL leagues directly. Covers most of the system in one shape.',
          catch: 'API key required · terms apply · no NCAA or europe' },
        { name: 'League sites, one by one',
          what: 'NCAA, SHL, Liiga and the rest, pulled individually and normalised here.',
          catch: 'Free · brittle · the most work to maintain' }
      ]
    };
  }
}'''

open('Players.dc.html','w').write(doc(1440, 1900, body, script))
print('Players.dc.html written:', len(open('Players.dc.html').read()))
