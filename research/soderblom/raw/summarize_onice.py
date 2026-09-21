import json, csv
from collections import Counter, defaultdict
games=json.load(open('onice_games.json'))
gl={}
for f in ('20222023_2','20242025_2','20252026_2','20252026_3'):
    for g in json.load(open(f'nhl/gamelog_{f}.json'))['gameLog']: gl[g['gameId']]=g
def season_of(gid): return int(str(gid)[:4])
# MP skaters per season for QoC/QoT proxy: 5v5 TOI/GP and position
mpsk={}
for yr in (2022,2024,2025):
    d={}
    for r in csv.DictReader(open(f'../../rasmussen/raw/mp/skaters_{yr}.csv')):
        if r['situation']=='5on5': d[r['playerId']]=dict(toi_gp=float(r['icetime'])/60/max(1,int(r['games_played'])),pos=r['position'],name=r['name'],xgpct=float(r['onIce_xGoalsPercentage']))
    mpsk[yr]=d
def split_key(g):
    yr=season_of(g['gid']); return f"{yr}-{str(yr+1)[2:]} {g['team']}{' PO' if g['gtype']==3 else ''}"
S=defaultdict(list)
for g in games: S[split_key(g)].append(g)
out={}
def m(gs,k): return sum(g[k] for g in gs)
def toi(gs,s): return sum(g['toi'].get(s,0) for g in gs)/60
for key,gs in S.items():
    yr=season_of(gs[0]['gid']); sk=mpsk[yr]
    n=len(gs); t5=toi(gs,'5v5'); tpp=toi(gs,'PP'); tpk=toi(gs,'PK'); tall=sum(sum(g['toi'].values()) for g in gs)/60
    team_pp=sum(g['team_toi'].get('PP',0) for g in gs)/60; team_pk=sum(g['team_toi'].get('PK',0) for g in gs)/60; team5=sum(g['team_toi'].get('5v5',0) for g in gs)/60
    # nhl gamelog TOI check
    nhl_toi=sum(int(gl[g['gid']]['toi'].split(':')[0])*60+int(gl[g['gid']]['toi'].split(':')[1]) for g in gs)/60
    cf,ca,ff,fa,xgf,xga,gf,ga=[m(gs,k) for k in ('cf','ca','ff','fa','xgf','xga','gf','ga')]
    ocf,oca,oxgf,oxga,ogf,oga=[m(gs,k) for k in ('off_cf','off_ca','off_xgf','off_xga','off_gf','off_ga')]
    off5=team5-t5
    fo=Counter(); fos=Counter()
    for g in gs: fo.update(g['fo']); fos.update(g['fo_start'])
    mates=Counter(); opps=Counter()
    for g in gs: mates.update({k:v for k,v in g['mates_id'].items()}); opps.update({k:v for k,v in g['opps_id'].items()})
    def wavg(c, fwd_only):
        num=den=0
        for p,v in c.items():
            r=sk.get(p)
            if not r: continue
            if fwd_only and r['pos'] not in ('C','L','R'): continue
            if not fwd_only and r['pos']!='D': continue
            num+=v*r['toi_gp']; den+=v
        return num/den if den else None
    def top(c,k=6):
        return [(sk.get(p,{}).get('name',p), round(v/60,1), round(100*v/60/t5,1)) for p,v in c.most_common(k)]
    pct=lambda a,b: round(100*a/(a+b),1) if a+b else None
    r60=lambda v,t: round(60*v/t,2) if t else None
    out[key]=dict(GP=n, toi_gp=round(tall/n,2), nhl_toi_gp=round(nhl_toi/n,2), toi5_gp=round(t5/n,2), pp_gp=round(tpp/n,2), pk_gp=round(tpk/n,2),
        pp_share=round(100*tpp/team_pp,1) if team_pp else None, pk_share=round(100*tpk/team_pk,1) if team_pk else None,
        cf=cf,ca=ca,cf_pct=pct(cf,ca), cf60=r60(cf,t5), ca60=r60(ca,t5), ff_pct=pct(ff,fa),
        xgf=round(xgf,2),xga=round(xga,2),xgf_pct=pct(xgf,xga), xgf60=r60(xgf,t5), xga60=r60(xga,t5),
        gf=gf,ga=ga,gf_pct=pct(gf,ga), hdcf=m(gs,'hdcf'),hdca=m(gs,'hdca'),
        off_cf_pct=pct(ocf,oca), off_xgf_pct=pct(oxgf,oxga), off_gf_pct=pct(ogf,oga), off_xgf60=r60(oxgf,off5), off_xga60=r60(oxga,off5),
        rel_cf=round(pct(cf,ca)-pct(ocf,oca),1), rel_xgf=round(pct(xgf,xga)-pct(oxgf,oxga),1),
        ozs_pct=pct(fo['O'],fo['D']), fo=dict(fo), ozs_start_pct=pct(fos['O'],fos['D']), fo_start=dict(fos),
        icf=m(gs,'icf'), iff=m(gs,'iff'), isog=m(gs,'isog'), ig=m(gs,'ig'), ixg=round(m(gs,'ixg'),2), icf60_5v5=r60(m(gs,'icf_5v5'),t5), ixg60_5v5=r60(m(gs,'ixg_5v5'),t5),
        pts=m(gs,'pts'), pts_5v5=m(gs,'pts_5v5'), g_5v5=m(gs,'g_5v5'), p60_5v5=r60(m(gs,'pts_5v5'),t5), a1=m(gs,'a1'), a2=m(gs,'a2'),
        hits=m(gs,'hits'), hits60=r60(m(gs,'hits'),tall), hits_taken=m(gs,'hits_taken'), pen_taken=m(gs,'pen_taken'), pen_drawn=m(gs,'pen_drawn'), tk=m(gs,'tk'), gv=m(gs,'gv'), blk=m(gs,'blk'),
        shifts_gp=round(m(gs,'shifts')/n,1),
        qot_f=round(wavg(mates,True),2) if wavg(mates,True) else None, qot_d=round(wavg(mates,False),2) if wavg(mates,False) else None,
        qoc_f=round(wavg(opps,True),2) if wavg(opps,True) else None, qoc_d=round(wavg(opps,False),2) if wavg(opps,False) else None,
        top_mates=top(mates,8), top_opps=top(opps,6))
json.dump(out,open('onice_splits.json','w'),indent=1)
for k,v in out.items():
    print('\n==',k)
    for kk,vv in v.items():
        if kk not in ('top_mates','top_opps','fo','fo_start'): print(f"  {kk}={vv}",end='')
    print('\n  mates',v['top_mates']); print('  opps',v['top_opps'])
