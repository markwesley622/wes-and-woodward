import sys; sys.path.insert(0,'.')
from _kit import *

s = open('Column.dc.html').read()

# ---- replace the trailing-off ending with the argument the piece is actually for ----
old_tail = '''          <p style="margin: 0; font-size: 17.5px; line-height: 1.65;">
            He simply did not score them, and that is the part where the numbers stop being able to help&hellip;
          </p>
        </div>'''
assert s.count(old_tail) == 1, 'tail not found'

dumbbell = '''        <div style="display: flex; flex-direction: column; gap: 11px;">
          <sc-for list="{{dumbbell}}" as="d" hint-placeholder-count="9">
            <div style="display: grid; grid-template-columns: 150px minmax(0, 1fr) 108px; gap: 16px; align-items: center;">
              <span class="mono" style="font-size: 11px; text-align: right; color: {{d.nameColor}};">{{d.name}}</span>
              <div title="{{d.title}}" style="position: relative; height: 18px;">
                <div class="track" style="position: absolute; left: 0; right: 0; top: 8px; height: 2px;"></div>
                <div style="{{d.link}}"></div>
                <div style="{{d.expDot}}"></div>
                <div style="{{d.actDot}}"></div>
              </div>
              <span class="mono" style="font-size: 11px; text-align: right; color: ''' + INK2 + ''';">{{d.readout}}</span>
            </div>
          </sc-for>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 14px; padding-top: 12px; border-top: 1px solid ''' + HAIR + ''';">
          <span class="lbl" style="font-size: 8px;">0%</span>
          <span class="lbl" style="font-size: 8px;">10%</span>
          <span class="lbl" style="font-size: 8px;">20%</span>
        </div>
        <div style="display: flex; gap: 20px; margin-top: 13px;">
          <span class="lbl" style="font-size: 8px; display: flex; align-items: center; gap: 6px;"><span style="width: 9px; height: 9px; border-radius: 50%; background: transparent; border: 1.5px solid ''' + INK3 + '''; display: inline-block; box-sizing: border-box;"></span>What the shots were worth</span>
          <span class="lbl" style="font-size: 8px; display: flex; align-items: center; gap: 6px;"><span style="width: 9px; height: 9px; border-radius: 50%; background: ''' + GREY1 + '''; display: inline-block;"></span>What he actually shot</span>
        </div>'''

new_tail = '''          <p style="margin: 0; font-size: 17.5px; line-height: 1.65;">
            He simply did not score them. So the question worth eight minutes of your time is not whether the
            gap exists &mdash; it plainly does &mdash; but where it came from.
          </p>
        </div>

        <div class="panel" style="padding: 34px 40px 32px;">
          <h2 class="hed" style="font-size: 32px; margin-bottom: 20px;">Skill, or luck?</h2>
          <p style="margin: 0 0 20px; font-size: 17.5px; line-height: 1.65;">
            Start with the shape of his shooting. Copp took 115 shots on goal this season &mdash; the fewest of any
            forward who played a regular shift. Those 115 shots were worth 19.83 expected goals, which works out
            to 17.2 percent per shot. That is the highest figure on the roster, and it is not close: DeBrincat
            sat at 12.9, Larkin at 14.7.
          </p>
          <p style="margin: 0 0 20px; font-size: 17.5px; line-height: 1.65;">
            So the story is not a player firing pucks from the perimeter and hoping. It is the opposite. Copp
            shot rarely and almost exclusively from dangerous places, and converted 7.8 percent of them.
          </p>
        </div>

''' + figure(
    'What the shots were worth, against what he shot',
    'expected and actual shooting percentage &nbsp;·&nbsp; skaters with 100+ shots on goal',
    dumbbell,
    'Dumbbell &nbsp;·&nbsp; moneypuck + nhl api &nbsp;·&nbsp; all situations',
    pad='30px 34px 24px') + '''

        <div class="panel" style="padding: 34px 40px 32px;">
          <p style="margin: 0 0 20px; font-size: 17.5px; line-height: 1.65;">
            Three things fall out of that chart, and they point in different directions.
          </p>
          <p style="margin: 0 0 20px; font-size: 17.5px; line-height: 1.65;">
            <span style="font-weight: 600;">The sample is small enough to be nearly meaningless.</span> One
            hundred and fifteen shots is not a finishing sample; it is a rumour of one. Individual shooting
            talent takes something on the order of five hundred shots before the signal outruns the noise, which
            is to say two or three full seasons of Copp&rsquo;s volume. On sample size alone, the honest prior is
            that most of this reverses.
          </p>
          <p style="margin: 0 0 20px; font-size: 17.5px; line-height: 1.65;">
            <span style="font-weight: 600;">He is not alone, and that is the interesting part.</span> Finnie and
            Kasper sit immediately behind him, both underperforming by roughly five points of shooting
            percentage, and both with expected rates well above the roster median. Three players missing the
            same way is either a coincidence across three small samples, or it is telling you something about
            the kind of chance Detroit generates &mdash; scrambles, deflections and second efforts in tight, which
            a shot model tends to value generously and a shooter converts less often than the model implies.
          </p>
          <p style="margin: 0; font-size: 17.5px; line-height: 1.65;">
            <span style="font-weight: 600;">Which leaves a residue that might be real.</span> Copp&rsquo;s career
            shooting percentage is the number that would settle this, and one season of data cannot supply it.
            My read: perhaps three of the ten and a half goals are a genuine finishing deficiency, the rest is
            sample and model generosity. That is a guess with a direction, not a measurement &mdash; and I would
            rather say so than dress it up.
          </p>
        </div>

        <div style="background: ''' + GREY1 + '''; border-radius: 22px; padding: 30px 34px 28px;">
          <p class="lbl" style="margin: 0 0 16px; color: ''' + WHITE + ''';">What would actually settle it</p>
          <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px;">
            <sc-for list="{{settle}}" as="x" hint-placeholder-count="3">
              <div>
                <p class="mono" style="margin: 0 0 8px; font-size: 12px; font-weight: 600; color: ''' + WHITE + ''';">{{x.k}}</p>
                <p style="margin: 0; font-size: 13.5px; line-height: 1.55; color: ''' + GREY4 + ''';">{{x.v}}</p>
              </div>
            </sc-for>
          </div>
        </div>'''

s = s.replace(old_tail, new_tail)

# ---- data for the new figure ----
old_ret = '''    return {
      gax: gax,'''
new_ret = '''    // Dumbbell: expected shooting % (hollow) against actual (solid), 0-20% scale.
    var shooters = [
      ['Andrew Copp', 115, 7.83, 17.24], ['Emmitt Finnie', 120, 10.83, 16.00],
      ['Marco Kasper', 131, 6.87, 11.76], ['Patrick Kane', 169, 9.47, 9.76],
      ['Dylan Larkin', 229, 14.85, 14.74], ['Ben Chiarot', 103, 4.85, 4.20],
      ['Moritz Seider', 187, 5.35, 4.01], ['Alex DeBrincat', 287, 14.29, 12.85],
      ['Lucas Raymond', 173, 14.45, 11.27]
    ];
    var dumbbell = shooters.map(function (r) {
      var name = r[0], shots = r[1], act = r[2], exp = r[3];
      var px = function (v) { return Math.min(v / 20, 1) * 100; };
      var a = px(act), e = px(exp);
      var lo = Math.min(a, e), hi = Math.max(a, e);
      var over = act >= exp;
      var focus = name === 'Andrew Copp';
      var dot = function (pos, style) {
        return 'position: absolute; top: 50%; left: ' + pos + '%; transform: translate(-50%, -50%);'
          + ' width: 10px; height: 10px; border-radius: 50%; box-sizing: border-box; ' + style;
      };
      return {
        name: name,
        nameColor: focus ? '#141414' : '#5f5e5b',
        link: 'position: absolute; top: 50%; transform: translateY(-50%); height: 2px; left: ' + lo
          + '%; width: ' + (hi - lo) + '%; background: ' + (over ? RED : '#141414') + '; opacity: 0.45;',
        expDot: dot(e, 'background: #e7e6e3; border: 1.5px solid #91908d;'),
        actDot: dot(a, 'background: ' + (over ? RED : '#141414') + ';'),
        readout: act.toFixed(1) + ' / ' + exp.toFixed(1) + '%',
        title: name + ' — ' + shots + ' shots · shot ' + act.toFixed(1)
          + '%, worth ' + exp.toFixed(1) + '%'
      };
    });

    return {
      gax: gax,
      dumbbell: dumbbell,
      settle: [
        { k: 'A career baseline', v: 'Several seasons of Copp’s own shooting percentage, which one year of data cannot supply.' },
        { k: 'Shot location detail', v: 'Where each of the 115 attempts came from, to test whether the model is over-crediting chances in tight.' },
        { k: 'A teammate control', v: 'Whether Finnie and Kasper regress next season too. If all three do, it was the chances, not the shooters.' }
      ],'''
assert s.count(old_ret) == 1, 'return block not found'
s = s.replace(old_ret, new_ret)

# taller now
s = s.replace('"$preview":{"width":1440,"height":2560}', '"$preview":{"width":1440,"height":3760}')

open('Column.dc.html','w').write(s)
print('Column.dc.html patched:', len(s))
