import sys, os, json, datetime as dt; sys.path.insert(0,'.')
from _kit import *

# Home = the glance page. ONE standalone hero block above the fold previews the Team
# dashboard from ../data/site/dashboard.json; everything under it is navigation into
# articles, player pages and the full team page.
D = json.load(open('../data/site/dashboard.json'))
S, X, P, T, NG = D['standings'], D['deserved'], D['projected'], D['tiles'], D['nextGame']

# PREVIEW_GAME=41 renders the in-season state for layout review: 2025-26 standings
# through that game, with the season's final points standing in for the projection.
PREVIEW = int(os.environ.get('PREVIEW_GAME', '0') or 0)
if PREVIEW:
    R = json.load(open('../data/site/results.json'))[:PREVIEW]
    w = sum(r['result'] == 'W' for r in R); l = sum(r['result'] == 'L' for r in R); o = sum(r['result'] == 'OTL' for r in R)
    S = dict(S, gamesPlayed=len(R), wins=w, losses=l, otLosses=o, points=2 * w + o,
             pointPctg=(2 * w + o) / (2 * len(R)), goalFor=sum(r['goalsFor'] for r in R),
             goalAgainst=sum(r['goalsAgainst'] for r in R), goalDifferential=sum(r['goalsFor'] - r['goalsAgainst'] for r in R),
             streak='W2', lastTen='6-3-1')
    P = {'available': True, 'points': P.get('finalPoints', 92.0)}
    D['seasonState'] = 'in_season'
    NG = dict(NG, date=R[-1]['date'], opponent='TOR', home=True)

def ordinal(n):
    n = int(n); suf = 'th' if 10 <= n % 100 <= 20 else {1:'st',2:'nd',3:'rd'}.get(n % 10, 'th')
    return f'{n}{suf}'
def signed(v, d=1):
    return ('+' if v > 0 else ('−' if v < 0 else '')) + f'{abs(v):.{d}f}'
def pct3(v):
    return f'.{round(v*1000):03d}'
def mdy(iso):
    return dt.date.fromisoformat(iso).strftime('%b %-d')
def ghost(w, h=9, op='0.30', col=INK3):
    return f'<div style="height: {h}px; width: {w}; border-radius: 999px; background: {col}; opacity: {op};"></div>'
def ghost_lines(widths, h=9, gap=7, op='0.30'):
    rows = ''.join('\n            ' + ghost(w, h, op) for w in widths)
    return ('<div style="display: flex; flex-direction: column; gap: %spx;">%s\n          </div>' % (gap, rows))

# dark-panel palette
CELL = '#222120'; HAIR_D = '#3a3936'; TXT = WHITE; TXT2 = '#b9b8b5'; TXT3 = '#8a8986'

# Reference-only annotations for the canvas. They never ship: ANNOTATIONS=0 strips them,
# and the Astro port must not carry them. Mark 9/21: "as long as those eyebrows are just
# there for my reference it's okay, but I don't want those visible once the site publishes."
ANNOTATIONS = os.environ.get('ANNOTATIONS', '1') != '0'
def note(text):
    if not ANNOTATIONS:
        return ''
    return (f'<span class="dc-note mono" style="font-size: 11px; color: {INK2}; border: 1px dashed {INK3}; border-radius: 999px; padding: 3px 10px;">'
            f'<span class="lbl" style="font-size: 8px; color: {RED}; margin-right: 6px;">design note</span>{text}</span>')

season = D['seasonLabel'].replace('-', '&ndash;')
state = D['seasonState']
rebuilt = dt.datetime.fromisoformat(D['generatedAt']).astimezone().strftime('%b %-d, %H:%M').lower()
vs = lambda g: 'vs' if g['home'] else 'at'
if state == 'offseason':
    nxt = f'{season} final'
    if NG:
        nxt += f" &nbsp;&middot;&nbsp; {NG['season'][:4]}&ndash;{NG['season'][6:]} opens {mdy(NG['date'])} {vs(NG)} {NG['opponent']}"
elif state == 'preseason':
    nxt = f'{season} &nbsp;&middot;&nbsp; opens {mdy(NG["date"])} {vs(NG)} {NG["opponent"]}' if NG else season
else:
    nxt = f'{season} &nbsp;&middot;&nbsp; next: {vs(NG)} {NG["opponent"]} {mdy(NG["date"])}' if NG else season

wc = S['wildcard']
if state == 'offseason':
    wc_note = 'season complete'
elif wc is None or wc == 0:
    wc_note = 'division spot'
else:
    wc_note = 'in a playoff spot' if wc <= 2 else f'{wc - 2} out'

def lbl(t, color=TXT3, size=10):
    return f'<span class="lbl" style="font-size: {size}px; color: {color};">{t}</span>'

def cell(k, v, sub=None, note=None, vsize=36, vcolor=TXT, subcolor=RED, pad='16px 18px 14px'):
    subl = f'<span class="mono" style="font-size: 12.5px; font-weight: 600; color: {subcolor};">{sub}</span>' if sub else ''
    notel = f'<span class="mono" style="font-size: 11px; color: {TXT3}; line-height: 1.4;">{note}</span>' if note else ''
    return f"""
          <div style="background: {CELL}; border-radius: 16px; padding: {pad}; display: flex; flex-direction: column; gap: 7px; min-width: 0;">
            {lbl(k)}
            <span class="mono" style="font-size: {vsize}px; font-weight: 500; letter-spacing: -0.04em; line-height: 1; color: {vcolor};">{v}</span>
            {subl}{notel}
          </div>"""

# ---- record column
record = f"""
        <div style="display: flex; flex-direction: column; justify-content: space-between; min-width: 0;">
          <div>
            {lbl('Record', RED, 11)}
            <p class="mono" style="margin: 10px 0 0; font-size: 116px; font-weight: 500; letter-spacing: -0.06em; line-height: 0.9; color: {TXT}; white-space: nowrap;">{S['wins']}&ndash;{S['losses']}&ndash;{S['otLosses']}</p>
            <p class="mono" style="margin: 14px 0 0; font-size: 17px; color: {TXT2};"><span style="color: {RED}; font-weight: 600; font-size: 24px;">{S['points']} pts</span> &nbsp;&middot;&nbsp; {pct3(S['pointPctg'])} &nbsp;&middot;&nbsp; {S['goalFor']}&ndash;{S['goalAgainst']} ({signed(S['goalDifferential'], 0)})</p>
          </div>
          <p class="mono" style="margin: 16px 0 0; font-size: 12px; color: {TXT3};">{S['gamesPlayed']} gp &nbsp;&middot;&nbsp; {S['regulationWins']} rw &nbsp;&middot;&nbsp; streak {S['streak'] or '&mdash;'} &nbsp;&middot;&nbsp; last ten {S['lastTen'] or '&mdash;'}</p>
        </div>"""

places = f"""
        <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px;">
          {cell(S['division']['name'] + ' Division', ordinal(S['division']['place']), note=f"of {S['division']['teams']}", vsize=40)}
          {cell(S['conference']['name'] + ' Conference', ordinal(S['conference']['place']), note=f"of {S['conference']['teams']}", vsize=40)}
        </div>"""

# ---- progress toward MoneyPuck's projected points
gp, pts = S['gamesPlayed'], S['points']
if P.get('available') and P.get('points'):
    proj = P['points']; pace = pts / gp * 82 if gp else 0; delta = pace - proj
    scale = max(proj, pace) * 1.06
    fill = pts / scale * 100; pace_w = max(0, pace - pts) / scale * 100; tick = proj / scale * 100
    verdict = 'outperforming the projection' if delta >= 0.5 else 'underperforming the projection' if delta <= -0.5 else 'tracking the projection'
    head = f'<span class="mono" style="font-size: 34px; font-weight: 500; letter-spacing: -0.04em; line-height: 1; color: {RED};">{pts}</span><span class="mono" style="font-size: 15px; color: {TXT2}; margin-left: 10px;">of {proj:.0f} projected &nbsp;&middot;&nbsp; {gp} of 82 gp</span>'
    bar = f"""
            <div style="position: relative; height: 12px; border-radius: 999px; background: {HAIR_D}; margin: 12px 0 4px;">
              <div style="position: absolute; left: 0; top: 0; bottom: 0; width: {fill:.2f}%; border-radius: 999px; background: {RED};"></div>
              <div style="position: absolute; left: {fill:.2f}%; top: 0; bottom: 0; width: {pace_w:.2f}%; border-radius: 0 999px 999px 0; background: {RED}; opacity: 0.35;"></div>
              <div style="position: absolute; left: {tick:.2f}%; top: -6px; bottom: -6px; width: 2px; background: {TXT};"></div>
            </div>
            <div style="position: relative; height: 14px;"><span class="lbl" style="position: absolute; left: {tick:.2f}%; transform: translateX(-50%); font-size: 9px; color: {TXT2}; white-space: nowrap;">projection {proj:.0f}</span></div>"""
    under = f'<p class="mono" style="margin: 6px 0 0; font-size: 13px; color: {TXT};">pacing to <span style="font-weight: 600;">{pace:.0f} pts</span> &nbsp;&middot;&nbsp; <span style="color: {RED}; font-weight: 600;">{signed(delta, 1)}</span> &nbsp;&middot;&nbsp; {verdict}</p>'
else:
    when = f"before the opener {mdy(NG['date'])}" if NG else 'once the season opens'
    head = ghost('200px', 26, '0.25', TXT3)
    bar = f'<div style="height: 16px; border-radius: 999px; background: {HAIR_D}; margin: 16px 0 6px;"></div><div style="height: 14px;"></div>'
    under = f'<p class="mono" style="margin: 8px 0 0; font-size: 12px; color: {TXT3};">moneypuck publishes its projection {when} &nbsp;&middot;&nbsp; pace and verdict render from game one</p>'
progress = f"""
        <div style="background: {CELL}; border-radius: 16px; padding: 14px 18px 14px; display: flex; flex-direction: column; justify-content: space-between;">
          <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px;">
            {lbl("Progress toward MoneyPuck&rsquo;s projected points")}
            <div style="display: flex; gap: 14px;">
              {lbl('<span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:' + RED + ';margin-right:5px;vertical-align:middle;"></span>banked', TXT3, 9)}
              {lbl('<span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:' + RED + ';opacity:.35;margin-right:5px;vertical-align:middle;"></span>on pace for', TXT3, 9)}
              {lbl('<span style="display:inline-block;width:2px;height:10px;background:' + TXT + ';margin-right:5px;vertical-align:middle;"></span>projection', TXT3, 9)}
            </div>
          </div>
          <div style="margin-top: 10px;">{head}</div>{bar}{under}
        </div>"""

# ---- by expected goals (xG-Pythagorean)
dpa = X['pointsAboveExpected']
def place_line(n, name):
    return (f'<span style="display: flex; align-items: baseline; gap: 8px;"><span class="mono" style="font-size: 30px; font-weight: 500; letter-spacing: -0.04em; line-height: 1; color: {TXT};">{ordinal(n)}</span>'
            f'<span class="lbl" style="font-size: 9px; color: {TXT3};">{name}</span></span>')
xg_place = f'<span style="display: flex; flex-direction: column; gap: 6px;">{place_line(X["divisionPlace"], S["division"]["name"])}{place_line(X["conferencePlace"], S["conference"]["name"])}</span>'
xg = f"""
        <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; align-content: stretch;">
          {cell('xG win share', f"{X['xgWinPct']*100:.1f}%", sub=f"actual {S['wins']/max(1,S['gamesPlayed'])*100:.1f}%", note='xG-pythagorean, all situations', vsize=40)}
          {cell('xG points', f"{X['xgPoints']:.1f}", sub=f"actual {S['points']} &nbsp;&middot;&nbsp; {signed(dpa)}", note='loser points at the league rate', vsize=40)}
          {cell('xG place', xg_place, sub=f"actual {ordinal(S['division']['place'])} &nbsp;&middot;&nbsp; {ordinal(S['conference']['place'])}", note=f"all 32 teams on xG points &nbsp;&middot;&nbsp; {ordinal(X['leaguePlace'])} in the nhl", vsize=30)}
        </div>"""

# ---- six ranked tiles
def fmt(t):
    v = t['value']
    if t.get('signed'): return signed(v, 1)
    if t['unit'] == '%': return f'{v:.1f}%'
    return f'{v:.2f}' if isinstance(v, float) and abs(v) < 20 else f'{v:.1f}'
short = {'xg_share_5v5': '5v5 xG share', 'xg_share_5v5_adj': 'Adj. xG share', 'finishing': 'Finishing',
         'gsax': 'Goalie GSAx', 'pp_xgf60': 'PP xG per 60', 'pk_xga60': 'PK xGA per 60'}
NOTE = {'xg_share_5v5': 'moneypuck, five-on-five', 'xg_share_5v5_adj': 'score &amp; venue adj.', 'finishing': 'G minus xG, all situations', 'gsax': 'saved above expected', 'pp_xgf60': '5v4, xG generated', 'pk_xga60': '4v5, lower is better'}
KEEP = ('xg_share_5v5', 'finishing', 'pp_xgf60', 'pk_xga60')
tiles = ''.join(cell(short[t['key']], fmt(t), sub=t['rankLabel'], note=NOTE[t['key']], vsize=34, subcolor=(RED if t['rank'] <= 10 else TXT2), pad='14px 16px 12px') for t in T if t['key'] in KEEP)
ranked = f"""
        <div>
          <div style="display: flex; justify-content: space-between; align-items: baseline; margin: 0 2px 8px;">
            {lbl('The numbers behind a paywall elsewhere', TXT2, 10)}
            {lbl('league rank, 1 is best &nbsp;&middot;&nbsp; red = top ten', TXT3, 9)}
          </div>
          <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px;">{tiles}
          </div>
        </div>"""

hero = f"""
  <!-- the glance block: one standalone preview of the Team dashboard, above the fold -->
  <div style="padding: 10px 64px 0;">
    <div style="background: {GREY1}; border-radius: 22px; padding: 22px 26px 22px; display: flex; flex-direction: column; gap: 10px;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 24px; padding: 0 4px 4px;">
        <span class="lbl" style="font-size: 11px; color: {TXT2};"><span style="color: {RED};">Detroit Red Wings</span> &nbsp;&middot;&nbsp; {nxt}</span>
        <a href="#" class="lbl" style="font-size: 10px; color: {RED}; white-space: nowrap;">Full team dashboard &rarr;</a>
      </div>
      <div style="display: grid; grid-template-columns: 600px minmax(0, 1fr); gap: 10px; align-items: stretch;">
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <div style="background: {CELL}; border-radius: 16px; padding: 18px 22px 16px; display: flex; flex: 1;">{record}</div>
          {xg}
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
          {progress}
          {places}
          {ranked}
        </div>
      </div>
      <div style="display: flex; justify-content: space-between; align-items: baseline; padding: 2px 4px 0;">
        {lbl('rebuilt ' + rebuilt + ' &nbsp;&middot;&nbsp; nhl api &middot; moneypuck', TXT3, 9)}
        {lbl(X['method'].split(';')[0].lower(), TXT3, 9)}
      </div>
    </div>
  </div>
"""

# ============================================================ below the hero
SK = json.load(open('../data/site/skaters.json'))

# ---- three player cards. The proprietary value score (out of 100) is not built yet, so
# the score slot is a ghost and the three players are a stand-in: top three by game score.
def portrait_static(goals, ixg, cols=14, dot=9, gap=3):
    exp = int(round(ixg))
    def grid(n, style):
        cells = ''.join(f'<span style="width: {dot}px; height: {dot}px; border-radius: 50%; {style}"></span>' for _ in range(n))
        return f'<div style="display: grid; grid-template-columns: repeat({cols}, {dot}px); gap: {gap}px;">{cells}</div>'
    return (f'<div style="display: flex; flex-direction: column; gap: 10px;">'
            f'{lbl("Scored &nbsp;" + str(goals), INK2, 8)}{grid(goals, "background: " + RED + ";")}'
            f'{lbl("Expected &nbsp;" + str(exp), INK2, 8)}{grid(exp, "border: 1.2px solid " + INK3 + "; box-sizing: border-box;")}</div>')

POS = {'C': 'Centre', 'L': 'Left wing', 'R': 'Right wing', 'D': 'Defence'}
def player_card(p):
    f5 = p.get('fiveOnFive') or {}
    stats = [('GP', p['gamesPlayed']), ('G', p['goals']), ('A', p['assists']), ('P', p['points']),
             ('ixG', f"{p['ixG']:.1f}" if p.get('ixG') is not None else '&mdash;'),
             ('5v5 xG%', f"{f5['onIceXgPct']*100:.0f}" if f5 else '&mdash;')]
    stat_html = ''.join(f'<div style="display: flex; flex-direction: column; gap: 5px;">{lbl(k, INK3, 8)}<span class="mono" style="font-size: 17px; font-weight: 600; color: {INK};">{v}</span></div>' for k, v in stats)
    return f"""
      <a href="#" style="background: {WHITE}; border-radius: 22px; padding: 26px 28px 24px; display: flex; flex-direction: column; gap: 20px; min-width: 0;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 16px;">
          <div style="min-width: 0;">
            <h3 class="dot" style="font-size: 26px; margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{p['name']}</h3>
            <p class="lbl" style="margin: 8px 0 0; font-size: 9px; color: {INK2};">{POS.get(p['position'], p['position'])} &nbsp;&middot;&nbsp; {season}</p>
          </div>
          <div style="flex: none; width: 74px; height: 74px; border-radius: 50%; border: 2px solid {RED}; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px;">
            {ghost('30px', 16, '0.30')}
            <span class="lbl" style="font-size: 7.5px; color: {RED};">/ 100</span>
          </div>
        </div>
        {portrait_static(p['goals'], p.get('ixG') or 0)}
        <div style="margin-top: auto; border-top: 1px solid {HAIR}; padding-top: 16px; display: flex; justify-content: space-between; gap: 10px;">{stat_html}</div>
        <span class="lbl" style="font-size: 9px; color: {RED};">Full player page &rarr;</span>
      </a>"""

top3 = sorted([p for p in SK if p.get('gameScore') is not None], key=lambda p: -p['gameScore'])[:3]
players = f"""
  <div style="padding: 34px 64px 0;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 24px; margin: 0 0 14px;">
      <h2 class="hed" style="font-size: 30px;">Top Red Wings</h2>
      <span style="display: flex; align-items: baseline; gap: 16px;">{note('value score out of 100, proprietary, in development; cards ordered by game score until it ships')}<a href="#" class="lbl" style="font-size: 9px; color: {RED}; white-space: nowrap;">Entire roster &rarr;</a></span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;">{''.join(player_card(p) for p in top3)}
    </div>
  </div>
"""

# ---- three featured articles: one pinned, two most recent
def article_card(kind):
    pinned = kind == 'Pinned'
    tag = f'<span class="lbl" style="font-size: 8px; color: {RED};">&#9679; Pinned</span>' if pinned else f'<span class="lbl" style="font-size: 8px; color: {INK2};">Latest</span>'
    return f"""
      <a href="#" style="background: {WHITE}; border-radius: 22px; padding: 26px 28px 24px; display: flex; flex-direction: column; gap: 16px; min-height: 250px; {'border: 1px solid ' + RED + ';' if pinned else ''}">
        {tag}
        {ghost_lines(['92%', '70%'], 19, 9)}
        {ghost_lines(['100%', '84%', '58%'], 8, 7, '0.22')}
        <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: baseline;">
          {ghost('110px', 8, '0.30')}
          <span class="lbl" style="font-size: 9px; color: {RED};">Read &rarr;</span>
        </div>
      </a>"""
articles = f"""
  <div style="padding: 34px 64px 0;">
    <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 24px; margin: 0 0 14px;">
      <h2 class="hed" style="font-size: 30px;">Analysis</h2>
      <span style="display: flex; align-items: baseline; gap: 16px;">{note('one pinned, two most recent')}<a href="#" class="lbl" style="font-size: 9px; color: {RED};">All articles &rarr;</a></span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;">{article_card('Pinned')}{article_card('Latest')}{article_card('Latest')}
    </div>
  </div>
"""

# ---- top five prospects. The pipeline ranking is not built and no public source lists the
# system with a league and club, so the rows are slots.
def prospect_row(i):
    return f"""
      <div style="display: grid; grid-template-columns: 56px minmax(0, 1fr) 160px 120px 90px; align-items: center; gap: 18px; padding: 16px 0; border-top: 1px solid {HAIR};">
        <span class="dot" style="font-size: 26px; color: {RED if i == 1 else INK};">{i:02d}</span>
        {ghost_lines([('62%', '48%')[i % 2]], 14, 0)}
        {ghost('72%', 8, '0.30')}
        {ghost('60%', 8, '0.30')}
        <div style="display: flex; justify-content: flex-end;">{ghost('42px', 14, '0.30')}</div>
      </div>"""
prospects = f"""
  <div style="padding: 34px 64px 0;">
    <div style="background: {WHITE}; border-radius: 22px; padding: 28px 34px 22px;">
      <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 24px; margin: 0 0 18px;">
        <div>
          <h2 class="hed" style="font-size: 30px;">Top Prospects</h2>
          <p style="margin: 10px 0 0;">{note('prospect ranking in development; counting stats in the league they were produced in, no cross-league xG')}</p>
        </div>
        <a href="#" class="lbl" style="font-size: 9px; color: {RED}; white-space: nowrap;">In the System &rarr;</a>
      </div>
      <div style="display: grid; grid-template-columns: 56px minmax(0, 1fr) 160px 120px 90px; gap: 18px; padding: 0 0 10px;">
        {lbl('Rank', INK3, 8)}{lbl('Player', INK3, 8)}{lbl('Club &nbsp;&middot;&nbsp; league', INK3, 8)}{lbl('Age &nbsp;&middot;&nbsp; drafted', INK3, 8)}<span style="text-align: right;">{lbl('Score', INK3, 8)}</span>
      </div>{''.join(prospect_row(i) for i in range(1, 6))}
    </div>
  </div>
"""

body = topbar(None) + hero + players + articles + prospects + '\n\n' + FOOTER

script = '''class Component extends DCLogic {
  renderVals() { return {}; }
}'''

OUTFILE = os.environ.get('OUTFILE', 'Main.dc.html')
open(OUTFILE,'w').write(doc(1440, 2150, body, script))
print(OUTFILE, '— glance home:', len(open(OUTFILE).read()))
