import json, urllib.request, ssl, certifi, os, time
ctx=ssl.create_default_context(cafile=certifi.where())
ids=[]
for f in ['gamelog_20222023_2.json','gamelog_20242025_2.json','gamelog_20252026_2.json','gamelog_20252026_3.json']:
    for g in json.load(open(f))['gameLog']: ids.append(g['gameId'])
print(len(ids),'games')
def get(url,out):
    if os.path.exists(out) and os.path.getsize(out)>1000: return
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),context=ctx,timeout=30) as r:
                open(out,'wb').write(r.read()); return
        except Exception as e:
            print('retry',url,e); time.sleep(2)
for gid in ids:
    get(f'https://api-web.nhle.com/v1/gamecenter/{gid}/play-by-play', f'pbp/{gid}.json')
    get(f'https://api.nhle.com/stats/rest/en/shiftcharts?cayenneExp=gameId={gid}', f'shifts/{gid}.json')
print('done', len(os.listdir('pbp')), len(os.listdir('shifts')))
