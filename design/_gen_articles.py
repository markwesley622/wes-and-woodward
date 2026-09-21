import sys; sys.path.insert(0,'.')
from _kit import *

body = topbar('Articles') + '''

  <div style="padding: 20px 64px 0;">
    <div style="display: grid; grid-template-columns: minmax(0, 1fr) 420px; gap: 12px; align-items: stretch;">
      <div class="panel" style="padding: 40px 44px 38px;">
        <p class="lbl" style="margin: 0 0 26px; color: ''' + INK + ''';">Everything written here</p>
        <h1 class="dot" style="font-size: 58px;">Articles</h1>
        <p style="font-size: 18px; line-height: 1.55; color: ''' + INK2 + '''; margin: 28px 0 0; max-width: 42em;">
          Deep dives, arguments, and whatever the data turned up that week. One feed, sorted newest first,
          filtered by subject rather than split by how quickly it expires &mdash; because none of it really does.
        </p>
      </div>
      <div style="background: ''' + GREY1 + '''; border-radius: 22px; padding: 34px 36px 32px; display: flex; flex-direction: column; justify-content: center;">
        <p class="lbl" style="margin: 0 0 14px; color: ''' + WHITE + ''';">Two datelines on every piece</p>
        <p style="margin: 0; font-size: 15px; line-height: 1.65; color: ''' + GREY4 + ''';">
          <span style="color: ''' + WHITE + ''';">Published</span> is when it was written.
          <span style="color: ''' + WHITE + ''';">Data through</span> is the last game in the numbers behind it.
          
          A two-year-old deep dive is still true; the dateline should say so rather than imply it has gone stale.
        </p>
      </div>
    </div>
  </div>

  <div style="padding: 12px 64px 0;">
    <div class="panel" style="padding: 22px 30px; display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
      <span class="lbl">Subject</span>
      <div style="display: flex; gap: 7px; flex-wrap: wrap;">
        <sc-for list="{{tags}}" as="t" hint-placeholder-count="6">
          <button class="lbl" onClick="{{t.pick}}" style="{{t.style}}">{{t.name}} <span style="opacity: 0.55;">{{t.n}}</span></button>
        </sc-for>
      </div>
    </div>
  </div>

  <!-- featured -->
  <sc-if value="{{showFeature}}" hint-placeholder-val="{{ true }}">
    <div style="padding: 12px 64px 0;">
      <a href="#" class="panel" style="padding: 40px 44px 38px; display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: 48px; align-items: end;">
        <div>
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 18px;">
            <span class="lbl" style="background: ''' + INK + '''; color: ''' + WHITE + '''; padding: 7px 13px; border-radius: 999px; font-size: 8px;">Featured</span>
          </div>
          <h2 class="hed" style="font-size: 42px; max-width: 22ch;">{{feature.hed}}</h2>
          <p style="margin: 20px 0 0; font-size: 17px; line-height: 1.55; color: ''' + INK2 + '''; max-width: 46em;">{{feature.dek}}</p>
          <div style="display: flex; gap: 7px; flex-wrap: wrap; margin-top: 22px;">
            <sc-for list="{{feature.tags}}" as="t" hint-placeholder-count="3">
              <span class="mono" style="font-size: 10px; color: ''' + INK2 + '''; background: ''' + INSET + '''; padding: 5px 11px; border-radius: 999px;">{{t}}</span>
            </sc-for>
          </div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 8px; align-items: flex-end; text-align: right;">
          <span class="mono" style="font-size: 11px; color: ''' + INK2 + ''';">{{feature.published}}</span>
          <span class="mono" style="font-size: 11px; color: ''' + INK3 + ''';">{{feature.data}}</span>
          <span class="lbl" style="font-size: 8px; margin-top: 10px;">{{feature.meta}}</span>
        </div>
      </a>
    </div>
  </sc-if>

  <!-- feed -->
  <div style="padding: 12px 64px 0;">
    <div style="display: flex; flex-direction: column; gap: 12px;">
      <sc-for list="{{items}}" as="a" hint-placeholder-count="5">
        <a href="#" class="panel" style="padding: 30px 34px 28px; display: grid; grid-template-columns: minmax(0, 1fr) 250px; gap: 40px; align-items: start;">
          <div>
            <h2 class="hed" style="font-size: 27px; margin-bottom: 12px;">{{a.hed}}</h2>
            <p style="margin: 0 0 18px; font-size: 15.5px; line-height: 1.55; color: ''' + INK2 + '''; max-width: 54em;">{{a.dek}}</p>
            <div style="display: flex; gap: 7px; flex-wrap: wrap;">
              <sc-for list="{{a.tags}}" as="t" hint-placeholder-count="3">
                <span class="mono" style="font-size: 10px; color: ''' + INK2 + '''; background: ''' + INSET + '''; padding: 5px 11px; border-radius: 999px;">{{t}}</span>
              </sc-for>
            </div>
          </div>
          <div style="display: flex; flex-direction: column; gap: 7px; align-items: flex-end; text-align: right;">
            <span class="mono" style="font-size: 11px; color: ''' + INK2 + ''';">{{a.published}}</span>
            <span class="mono" style="font-size: 11px; color: ''' + INK3 + ''';">{{a.data}}</span>
            <span class="lbl" style="font-size: 8px; margin-top: 8px;">{{a.meta}}</span>
          </div>
        </a>
      </sc-for>
    </div>
  </div>

''' + FOOTER

script = '''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { tag: 'All' };
  }

  all() {
    return [
      { feature: true,
        hed: 'Andrew Copp shot 19.8 expected goals and scored nine.',
        dek: 'The largest finishing shortfall on the roster, by a margin of four goals. Whether that is variance or something a coaching staff can act on decides how Detroit should use him next season.',
        tags: ['five-on-five', 'expected goals', 'andrew copp'],
        subjects: ['Five-on-five'],
        published: 'published apr 14 2026', data: 'data through apr 13', meta: '8 min read' },

      {         hed: 'Detroit needs a goaltender, and the numbers say which kind.',
        dek: 'Gibson was worth eleven and a half goals above expectation; his partner gave back thirteen. The tandem netted out below replacement. That is a solvable problem, and it is cheaper to solve than the forward group.',
        tags: ['offseason', 'goaltending', 'roster building'],
        subjects: ['Offseason', 'Goaltending'],
        published: 'published aug 20 2026', data: 'data through apr 15', meta: '9 min read' },

      {         hed: 'Gibson saved 11.7 goals. Talbot gave back 13.1.',
        dek: 'The same team, the same defence, the same shot quality against — and a twenty-five goal gap depending on who was in net.',
        tags: ['goaltending', 'gsax'],
        subjects: ['Goaltending'],
        published: 'published apr 10 2026', data: 'data through apr 9', meta: '7 min read' },

      {         hed: 'Three years on, what the DeBrincat trade actually bought.',
        dek: 'He led the roster in goals and points this season and finished four above what his shots were worth. Following every branch of the 2023 deal to where the pieces sit now, and what the whole thing has returned.',
        tags: ['trades', 'alex debrincat'],
        subjects: ['Trades'],
        published: 'published mar 2 2026', data: 'data through mar 1', meta: '11 min read' },

      {         hed: 'Edvinsson and Seider played 1,088 minutes at 55 percent.',
        dek: 'Detroit’s top pair out-expected the opposition 48.81 to 40.27 across seventy-one games together. Everything behind them is the argument.',
        tags: ['five-on-five', 'pairs', 'moritz seider'],
        subjects: ['Five-on-five'],
        published: 'published apr 4 2026', data: 'data through apr 2', meta: '6 min read' },

      {         hed: 'How to read an expected goal without being fooled by one.',
        dek: 'What the model sees, what it is deliberately blind to, and the four ways a single-season expected-goals number will mislead you if you let it.',
        tags: ['method', 'expected goals'],
        subjects: ['Method'],
        published: 'published feb 11 2026', data: 'no data dependency', meta: '11 min read' }
    ];
  }

  renderVals() {
    var self = this, st = this.state;
    var all = this.all();
    var names = ['All', 'Five-on-five', 'Goaltending', 'Offseason', 'Trades', 'Method'];

    var tags = names.map(function (name) {
      var on = st.tag === name;
      var n = name === 'All' ? all.length
        : all.filter(function (a) { return a.subjects.indexOf(name) !== -1; }).length;
      return {
        name: name, n: n,
        style: 'cursor: pointer; font-family: inherit; font-size: 9px; padding: 9px 15px; border-radius: 999px;'
          + ' border: 1px solid ' + (on ? '#141414' : '#c1c0bd') + ';'
          + ' background: ' + (on ? '#141414' : 'transparent') + ';'
          + ' color: ' + (on ? '#f2f1ef' : '#5f5e5b') + ';',
        pick: function () { self.setState({ tag: name }); }
      };
    });

    var list = st.tag === 'All' ? all
      : all.filter(function (a) { return a.subjects.indexOf(st.tag) !== -1; });

    // The featured slot is curation, not a category — it only stands while the
    // feed is unfiltered, so a subject view is a plain chronological list.
    var showFeature = st.tag === 'All';
    var feature = all[0];
    var items = showFeature ? list.slice(1) : list;

    return { tags: tags, showFeature: showFeature, feature: feature, items: items };
  }
}'''

open('Articles.dc.html','w').write(doc(1440, 2260, body, script))
print('Articles.dc.html written:', len(open('Articles.dc.html').read()))
