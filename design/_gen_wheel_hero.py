"""Prototype: Augustus-style homepage hero with the Red Wings wheel as a 3D object.
Standalone HTML (no Astro) for judging the motion before it touches src/. Query ?p=0..1 freezes scroll progress for screenshots."""
import json, math, re, datetime
D = json.load(open('data/site/dashboard.json'))
P = json.load(open('design/wheel-parts.json'))
wordmark = open('brand/wes-and-woodward-wordmark-black.svg').read()
wordmark = re.sub(r'<svg ', '<svg class="wm" ', wordmark, count=1).replace('fill="#000000"', 'fill="currentColor"')
S, X, T = D['standings'], D['deserved'], D['tiles']
def ordinal(n): return f"{n}{'th' if 10<=n%100<=20 else {1:'st',2:'nd',3:'rd'}.get(n%10,'th')}"
nxt = D.get('nextGame') or {}
banner = (f"Next: {nxt.get('label','')}" if nxt.get('label') else f"{D['seasonLabel']} final · {S['wins']}–{S['losses']}–{S['otLosses']} · {S['points']} pts · {ordinal(S['division']['place'])} in the Atlantic")
# tread layers: N rings along z, circumferential grooves where a layer is skipped
import os
N, STEP = int(os.environ.get('N','30')), int(os.environ.get('STEP','5'))
OUT = os.environ.get('OUT','design/wheel-hero.html')
C = 2*math.pi*415
blocks = 48; dash = C/blocks*0.72; gap = C/blocks - dash
layers = []
for i in range(1, N+1):
    if i in (10, 20): continue
    layers.append(f'<svg class="tl" viewBox="0 0 840 840" style="transform:translateZ({-i*STEP}px)"><circle cx="420" cy="420" r="415" fill="none" stroke="currentColor" stroke-width="1.2" vector-effect="non-scaling-stroke" stroke-dasharray="{dash:.2f} {gap:.2f}" stroke-dashoffset="{(1 if 10<i<20 else 0)*C/blocks/2:.2f}"/></svg>')
layers.insert(0, '<svg class="tl" viewBox="0 0 840 840" style="transform:translateZ(-1px)"><circle cx="420" cy="420" r="415" fill="none" stroke="currentColor" stroke-width="1.6" vector-effect="non-scaling-stroke"/></svg>')
layers.append(f'<svg class="tl" viewBox="0 0 840 840" style="transform:translateZ({-N*STEP-1}px)"><circle cx="420" cy="420" r="415" fill="none" stroke="currentColor" stroke-width="1.6" vector-effect="non-scaling-stroke"/></svg>')
tread = "\n".join(layers)
tiles = [t for t in T if t['key'] in ('xg_share_5v5','finishing','pp_xg60','pk_xga60')] or T[:4]
tile_html = "".join(f'<div class="tile"><span class="eb">{t["label"]}</span><span class="num">{t["value"]}{t["unit"] if t["unit"]!="%" else "%"}</span><span class="sub{" red" if t["rank"]<=10 else ""}">{t["rankLabel"]}</span></div>' for t in tiles)
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wes &amp; Woodward — wheel hero prototype</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap">
<style>
:root{{--paper:#e9e8e5;--ink:#141414;--red:#ce1126;--rule:#c9c8c4;--mute:#6b6a67;--shell:1312px;--gutter:24px}}
*{{box-sizing:border-box}} html{{scroll-behavior:auto}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:'Space Grotesk',system-ui,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
a{{color:inherit;text-decoration:none}}
.mono{{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase}}
.shell{{max-width:var(--shell);margin:0 auto;padding:0 var(--gutter)}}
.banner{{background:var(--red);color:#fff;text-align:center;padding:7px 12px;font-size:12px}}
.banner .mono{{text-transform:none;letter-spacing:0;font-size:12px}}
.hdr{{position:relative;z-index:6;background:var(--paper)}}
.top{{display:flex;align-items:center;justify-content:space-between;height:64px;border-bottom:1px solid var(--rule)}}
.wm{{height:30px;width:auto;display:block;color:var(--ink)}}
.nav{{display:flex;gap:28px}} .nav a:hover{{color:var(--red)}}
.cta{{background:var(--ink);color:#fff;padding:9px 14px;border-radius:3px;font-size:12px}}
/* hero */
.hero{{position:relative;height:calc(100vh - 94px);min-height:640px;border-bottom:1px solid var(--rule)}}
.hero .shell{{position:relative;height:100%}}
.stamp{{position:absolute;left:var(--gutter);top:22px;color:var(--mute)}} .stamp i{{display:block;width:5px;height:5px;background:var(--red);margin-bottom:8px}}
.h1{{position:absolute;left:var(--gutter);top:96px;margin:0;font-weight:600;font-size:clamp(64px,9.6vw,146px);line-height:.86;letter-spacing:-.035em;text-transform:uppercase;z-index:3;pointer-events:none}}
.h1 span{{display:block}} .h1 .l2{{padding-left:.12em}} .h1 .l3{{padding-left:1.05em}} .h1 .star{{color:var(--red)}}
.foot{{position:absolute;left:var(--gutter);right:var(--gutter);bottom:18px;display:flex;justify-content:space-between;color:var(--mute);z-index:3}}
/* wheel */
.stage{{position:absolute;right:-6vw;top:-6vh;transform:translateY(var(--ty,0px));will-change:transform;width:min(1040px,86vw);aspect-ratio:1;perspective:1900px;perspective-origin:50% 40%;z-index:1}}
.wheel{{position:absolute;inset:0;transform-style:preserve-3d;transform:rotateX(var(--tilt,0deg));will-change:transform}}
.face,.back,.tread{{position:absolute;inset:0;transform-style:preserve-3d}}
.face svg,.back svg,.tl{{position:absolute;inset:0;width:100%;height:100%;display:block}}
.spin{{transform-box:fill-box;transform-origin:center;transform:rotate(var(--spin,0deg))}}
.tread{{transform:rotate(var(--spin,0deg));color:var(--ink);opacity:var(--tread,0.35)}}
.back{{transform:translateZ(calc(-1px * {N*STEP}))}}
.face{{transform:translateZ(0.5px)}}
/* sections */
.sec{{position:relative;z-index:2;padding:56px 0;border-bottom:1px solid var(--rule)}}
.eb{{display:block;color:var(--mute)}} .eb::before{{content:"// "}}
.sec h2{{margin:0 0 28px;font-weight:600;font-size:clamp(34px,4.4vw,56px);line-height:.95;letter-spacing:-.03em;text-transform:uppercase}} .sec h2::before{{content:"// ";color:var(--red)}}
.viewall{{display:flex;justify-content:flex-start;margin-top:22px}} .viewall a{{display:inline-flex;align-items:center;gap:8px;border-bottom:1px solid var(--ink);padding-bottom:4px}} .viewall a:hover{{color:var(--red);border-color:var(--red)}}
.plist{{border-top:1px solid var(--rule)}} .prow{{display:grid;grid-template-columns:56px 1fr 1fr 120px;align-items:center;gap:16px;padding:16px 0;border-bottom:1px solid var(--rule)}} .prow .rk{{font-size:28px;font-weight:600;letter-spacing:-.02em}} .prow .ghost{{width:70%}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--rule);border-left:1px solid var(--rule)}}
.tile{{background:var(--paper);padding:18px 18px 22px;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule);display:flex;flex-direction:column;gap:8px;min-height:150px}}
.tile .num{{font-size:44px;font-weight:600;letter-spacing:-.03em;line-height:1;margin-top:auto}} .tile .num.big{{font-size:96px}}
.tile .sub{{font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--mute)}} .tile .sub.red,.red{{color:var(--red)}}
.tile.wide{{grid-column:span 2}}
.row3{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.card{{background:var(--paper);border:1px solid var(--rule);padding:18px;min-height:220px;display:flex;flex-direction:column;justify-content:space-between}}
.card.pin{{border-color:var(--red)}} .card h3{{margin:10px 0 0;font-size:22px;font-weight:600;letter-spacing:-.02em;line-height:1.1}}
.ghost{{background:#dcdbd7;border-radius:3px;height:14px;width:60%}}
footer{{padding:36px 0 60px;color:var(--mute);font-size:12px;line-height:1.6}}
@media (max-width:900px){{.grid{{grid-template-columns:repeat(2,1fr)}}.row3{{grid-template-columns:1fr}}.stage{{right:-30vw;top:34vh;width:150vw}}.hero{{height:100vh}}.nav{{display:none}}}}
@media (prefers-reduced-motion:reduce){{.wheel{{transform:rotateX(28deg)!important}}}}
</style></head><body>
<div class="banner mono">{banner}</div>
<div class="hdr"><div class="shell"><div class="top">
  <a href="#" aria-label="Wes and Woodward, home">{wordmark}</a>
  <nav class="nav mono"><a href="#">Team</a><a href="#">Players</a><a href="#">Analysis</a><a href="#">Prospects</a><a href="#">About</a></nav>
  <a class="cta mono" href="#">Subscribe</a>
</div></div></div>
<section class="hero"><div class="shell">
  <div class="stamp mono"><i></i><span id="clock">—</span><br>Detroit, MI</div>
  <h1 class="h1"><span class="l1">Detroit</span><span class="l2">hockey,</span><span class="l3">by the numbers<span class="star">*</span></span></h1>
  <div class="stage" aria-hidden="true"><div class="wheel" id="wheel">
    <div class="back"><svg viewBox="{P['viewBox']}"><path fill="none" stroke="var(--ink)" stroke-width="1.6" vector-effect="non-scaling-stroke" d="{P['tire']}"/><path class="spin" fill="none" stroke="var(--ink)" stroke-width="1.6" vector-effect="non-scaling-stroke" d="{P['spokes']}"/></svg></div>
    <div class="tread">{tread}</div>
    <div class="face"><svg viewBox="{P['viewBox']}"><path fill="none" stroke="var(--ink)" stroke-width="1.6" vector-effect="non-scaling-stroke" d="{P['tire']}"/><path class="spin" fill="none" stroke="var(--ink)" stroke-width="1.6" vector-effect="non-scaling-stroke" d="{P['spokes']}"/></svg></div>
  </div></div>
  <div class="foot mono"><span>*expected goals, not vibes</span><span>nhl api · moneypuck · rebuilt {D['generatedAt'][:10]}</span></div>
</div></section>
<section class="sec"><div class="shell">
  <h2>Team dashboard</h2>
  <div class="grid">
    <div class="tile wide"><span class="eb mono">Record</span><span class="num big">{S['wins']}–{S['losses']}–{S['otLosses']}</span><span class="sub"><span class="red">{S['points']} pts</span> · {S['pointPctg']:.3f} · {S['goalFor']}–{S['goalAgainst']} ({S['goalDifferential']:+d}) · last ten {S['lastTen']}</span></div>
    <div class="tile"><span class="eb mono">{S['division']['name']} Division</span><span class="num">{ordinal(S['division']['place'])}</span><span class="sub">of {S['division']['teams']} · {ordinal(X['divisionPlace'])} by expected goals</span></div>
    <div class="tile"><span class="eb mono">{S['conference']['name']} Conference</span><span class="num">{ordinal(S['conference']['place'])}</span><span class="sub">of {S['conference']['teams']} · {ordinal(X['conferencePlace'])} by expected goals</span></div>
    <div class="tile"><span class="eb mono">xG win share</span><span class="num">{X['xgWinPct']*100:.1f}%</span><span class="sub">actual {S['wins']/max(1,S['gamesPlayed'])*100:.1f}%</span></div>
    <div class="tile"><span class="eb mono">xG points</span><span class="num">{X['xgPoints']:.1f}</span><span class="sub">actual {S['points']} · {X['pointsAboveExpected']:+.1f}</span></div>
    <div class="tile"><span class="eb mono">xG place, NHL</span><span class="num">{ordinal(X['leaguePlace'])}</span><span class="sub">actual {ordinal(S['league']['place'])} of 32</span></div>
    <div class="tile"><span class="eb mono">Regulation wins</span><span class="num">{S['regulationWins']}</span><span class="sub">{S['gamesPlayed']} gp · streak {S['streak']}</span></div>
    {tile_html}
  </div>
  <div class="viewall mono"><a href="#">View all team stats &rarr;</a></div>
</div></section>
<section class="sec"><div class="shell"><h2>Analysis</h2>
  <div class="row3"><div class="card pin"><span class="eb mono">Pinned</span><h3>What the numbers say about the Rasmussen extension</h3><div class="ghost"></div></div><div class="card"><span class="eb mono">Column</span><h3>Is Sandin-Pellikka's competition really soft?</h3><div class="ghost"></div></div><div class="card"><span class="eb mono">Column</span><h3>The Söderblom trade, on ice</h3><div class="ghost"></div></div></div>
  <div class="viewall mono"><a href="#">View all analysis &rarr;</a></div>
</div></section>
<section class="sec"><div class="shell"><h2>Top Red Wings</h2>
  <div class="row3"><div class="card"><div class="ghost"></div><h3>—</h3></div><div class="card"><div class="ghost"></div><h3>—</h3></div><div class="card"><div class="ghost"></div><h3>—</h3></div></div>
  <div class="viewall mono"><a href="#">View all players &rarr;</a></div>
</div></section>
<section class="sec"><div class="shell"><h2>Top Prospects</h2>
  <div class="plist"><div class="prow"><span class="rk">1</span><div class="ghost"></div><div class="ghost" style="width:45%"></div><span class="sub mono" style="color:var(--mute)">—</span></div><div class="prow"><span class="rk">2</span><div class="ghost"></div><div class="ghost" style="width:45%"></div><span class="sub mono" style="color:var(--mute)">—</span></div><div class="prow"><span class="rk">3</span><div class="ghost"></div><div class="ghost" style="width:45%"></div><span class="sub mono" style="color:var(--mute)">—</span></div><div class="prow"><span class="rk">4</span><div class="ghost"></div><div class="ghost" style="width:45%"></div><span class="sub mono" style="color:var(--mute)">—</span></div><div class="prow"><span class="rk">5</span><div class="ghost"></div><div class="ghost" style="width:45%"></div><span class="sub mono" style="color:var(--mute)">—</span></div></div>
  <div class="viewall mono"><a href="#">View all prospects &rarr;</a></div>
</div></section>
<footer><div class="shell">Wes &amp; Woodward is an independent publication and is not affiliated with the Detroit Red Wings or the NHL. Data: NHL API, MoneyPuck, HockeyStatCards, Natural Stat Trick, Evolving-Hockey, Elite Prospects.</div></footer>
<script>
(()=>{{
  const wheel=document.getElementById('wheel'), hero=document.querySelector('.hero');
  const q=new URLSearchParams(location.search); const fixed=q.has('p')?parseFloat(q.get('p')):null; const fixedSy=q.has('sy')?parseFloat(q.get('sy')):null;
  if(fixedSy!==null){{ document.body.style.marginTop=(-fixedSy)+'px'; }}
  if(q.has('hero')) document.querySelector('.hero').style.height=q.get('hero')+'px';
  if(q.has('y')) addEventListener('load',()=>scrollTo(0,parseFloat(q.get('y'))));
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const TILT_MAX=74, ROLL=420; let t0=performance.now();
  function frame(now){{
    const range=hero.offsetHeight-innerHeight*0.35;
    const sy=fixedSy!==null?fixedSy:(fixed!==null?fixed*range:scrollY);
    const p=Math.min(1,Math.max(0,sy/range));
    const stage=document.querySelector('.stage');
    stage.style.setProperty('--ty',(0.55*Math.min(sy,1.5*hero.offsetHeight)).toFixed(1)+'px');
    const tilt=6+p*(TILT_MAX-6);
    const spin=reduce?0:((now-t0)/1000*4 + p*ROLL);
    wheel.style.setProperty('--tilt',tilt.toFixed(2)+'deg');
    wheel.style.setProperty('--spin',spin.toFixed(2)+'deg');
    wheel.style.setProperty('--tread',Math.min(1,0.18+p*2.2).toFixed(3));
    if(!reduce && sy<2.2*hero.offsetHeight) requestAnimationFrame(frame);
  }}
  requestAnimationFrame(frame);
  addEventListener('scroll',()=>{{ requestAnimationFrame(frame); }},{{passive:true}});
  const clock=document.getElementById('clock');
  const tick=()=>{{ clock.textContent=new Date().toLocaleTimeString('en-US',{{hour:'numeric',minute:'2-digit',timeZone:'America/Detroit'}}); }};
  tick(); setInterval(tick,30000);
}})();
</script>
</body></html>'''
open(OUT,'w').write(html)
print("wrote", OUT, len(html), "bytes;", len(layers), "tread layers")
