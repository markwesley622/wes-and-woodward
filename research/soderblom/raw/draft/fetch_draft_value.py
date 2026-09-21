import json, urllib.request, ssl, certifi, os, time
ctx=ssl.create_default_context(cafile=certifi.where())
def get(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),context=ctx,timeout=30) as r: return json.loads(r.read())
        except Exception as e: time.sleep(1.5)
    return None
out=[]
for yr in range(2008,2018):
    d=get(f'https://api-web.nhle.com/v1/draft/picks/{yr}/all')
    if not d: print('fail',yr); continue
    picks=d.get('picks',d)
    for p in picks:
        if p.get('round') in (2,3,4) or (p.get('round')==6):
            out.append(dict(year=yr, round=p['round'], overall=p['overallPick'], pid=p.get('playerId'), name=(f"{p['firstName']['default']} {p['lastName']['default']}" if p.get('firstName') else ''), pos=p.get('positionCode'), team=p.get('teamAbbrev')))
print(len(out),'picks')
for i,p in enumerate(out):
    if not p['pid']: continue
    l=get(f"https://api-web.nhle.com/v1/player/{p['pid']}/landing")
    if not l: continue
    ct=l.get('careerTotals',{}).get('regularSeason',{}) or {}
    p['gp']=ct.get('gamesPlayed',0); p['pts']=ct.get('points',0); p['g']=ct.get('goals',0)
    if i%50==0: print(i, p)
json.dump(out,open('draft/picks_2008_2017_r2346.json','w'),indent=0)
print('done')
