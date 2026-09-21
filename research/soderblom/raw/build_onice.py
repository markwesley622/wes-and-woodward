"""Team-split on-ice numbers for Soderblom from NHL play-by-play + shift charts,
with MoneyPuck shot-level xG joined by (game, elapsed second, team)."""
import json, csv, os, glob
from collections import defaultdict, Counter
ME=8481725
MP='../../rasmussen/raw/mp'
def t2s(t): m,s=t.split(':'); return int(m)*60+int(s)

# MoneyPuck shots keyed by nhl game id
mp=defaultdict(list)
for yr in (2022,2024,2025):
    for r in csv.DictReader(open(f'{MP}/shots_{yr}.csv')):
        gid=int(f"{yr}0{int(r['game_id']):05d}") if len(r['game_id'])<=5 else int(r['game_id'])
        mp[gid].append(dict(t=int(r['time']),per=int(r['period']),team=r['teamCode'],xg=float(r['xGoal']),goal=int(float(r['goal'])),sog=int(float(r['shotWasOnGoal'])),shooter=int(float(r['shooterPlayerId'])) if r['shooterPlayerId'] else 0,ev=r['event'],hs=int(r['homeSkatersOnIce']),as_=int(r['awaySkatersOnIce']),dist=float(r['arenaAdjustedShotDistance'] or 0)))
print('mp games',len(mp))

games=[]
for f in sorted(glob.glob('nhl/pbp/*.json')):
    gid=int(os.path.basename(f)[:-5])
    g=json.load(open(f)); sh=json.load(open(f'nhl/shifts/{gid}.json'))['data']
    home=g['homeTeam']; away=g['awayTeam']
    pos={r['playerId']:r['positionCode'] for r in g['rosterSpots']}
    names={r['playerId']:f"{r['firstName']['default'][0]}. {r['lastName']['default']}" for r in g['rosterSpots']}
    teamof={r['playerId']:r['teamId'] for r in g['rosterSpots']}
    myteam=teamof.get(ME)
    if myteam is None: print('not in game',gid); continue
    myabbr=home['abbrev'] if myteam==home['id'] else away['abbrev']
    ishome= myteam==home['id']
    # shifts -> per-second on-ice (abs seconds; OT period 4 starts at 3600, 5 at 4800)
    maxt=0; shifts=[]
    for s in sh:
        if s['typeCode']!=517 or not s['startTime'] or not s['endTime']: continue
        base=(s['period']-1)*1200
        a=base+t2s(s['startTime']); b=base+t2s(s['endTime'])
        if b<=a: continue
        shifts.append((a,b,s['playerId'],s['teamId'])); maxt=max(maxt,b)
    on=[[] for _ in range(maxt+2)]      # start-inclusive, end-exclusive: TOI and faceoffs
    on2=[[] for _ in range(maxt+2)]     # start-exclusive, end-inclusive: shots/goals/hits (play stops at shift end)
    for a,b,p,t in shifts:
        for t_ in range(a,b): on[t_].append(p)
        for t_ in range(a+1,b+1): on2[t_].append(p)
    # per-second situation
    def situ2(t): return situ(t, on2)
    def situ(t, arr=None):
        ps=(arr if arr is not None else on)[t]; my=[p for p in ps if teamof.get(p)==myteam]; op=[p for p in ps if teamof.get(p)!=myteam]
        mysk=[p for p in my if pos.get(p)!='G']; opsk=[p for p in op if pos.get(p)!='G']
        myg=any(pos.get(p)=='G' for p in my); opg=any(pos.get(p)=='G' for p in op)
        if len(mysk)==5 and len(opsk)==5 and myg and opg: return '5v5'
        if not myg or not opg: return 'EN'
        if len(mysk)>len(opsk): return 'PP'
        if len(mysk)<len(opsk): return 'PK'
        return 'other'
    G=dict(gid=gid,date=g['gameDate'],team=myabbr,gtype=g['gameType'],opp=away['abbrev'] if ishome else home['abbrev'],home=ishome,
           toi=Counter(),team_toi=Counter(),mates=Counter(),opps=Counter(),
           cf=0,ca=0,ff=0,fa=0,xgf=0.0,xga=0.0,gf=0,ga=0,hdcf=0,hdca=0,
           team_cf=0,team_ca=0,team_xgf=0.0,team_xga=0.0,team_gf=0,team_ga=0,
           off_cf=0,off_ca=0,off_xgf=0.0,off_xga=0.0,off_gf=0,off_ga=0,
           fo=Counter(),fo_start=Counter(),hits=0,hits_taken=0,pen_taken=0,pen_drawn=0,tk=0,gv=0,blk=0,
           icf=0,iff=0,isog=0,ixg=0.0,ig=0,pts=0,pts_5v5=0,g_5v5=0,a1=0,a2=0,ixg_5v5=0.0,icf_5v5=0,shifts=0,ppo=0)
    for t in range(maxt):
        if not on[t]: continue
        s=situ(t); me_on= ME in on[t]
        G['team_toi'][s]+=1
        if me_on:
            G['toi'][s]+=1
            if s=='5v5':
                for p in on[t]:
                    if p==ME: continue
                    (G['mates'] if teamof.get(p)==myteam else G['opps'])[p]+=1
    G['shifts']=sum(1 for a,b,p,t in shifts if p==ME)
    mystarts=sorted(a for a,b,p,t in shifts if p==ME)
    # pbp events
    for e in g['plays']:
        d=e.get('details',{}) or {}
        per=e['periodDescriptor']['number']; t=(per-1)*1200+t2s(e['timeInPeriod'])
        if t>=len(on): t=len(on)-1
        k=e['typeDescKey']
        if k=='faceoff':
            me_on= ME in on[t]; s=situ(t) if on[t] else 'other'
        else:
            me_on= ME in on2[t]; s=situ2(t) if on2[t] else 'other'
        if k=='faceoff' and me_on:
            x=d.get('xCoord',0)
            # my defending side
            hds=e.get('homeTeamDefendingSide','left')
            my_def_left = (hds=='left') if ishome else (hds!='left')
            if abs(x)<26: z='N'
            else:
                z='D' if ((x<0) == my_def_left) else 'O'
            G['fo'][z]+=1
            if any(abs(t-a)<=1 for a in mystarts): G['fo_start'][z]+=1
        if k in ('shot-on-goal','missed-shot','blocked-shot','goal'):
            own=d.get('eventOwnerTeamId'); mine= own==myteam
            if s=='5v5':
                if me_on:
                    G['cf' if mine else 'ca']+=1
                    if k!='blocked-shot': G['ff' if mine else 'fa']+=1
                    if k=='goal': G['gf' if mine else 'ga']+=1
                else:
                    G['off_cf' if mine else 'off_ca']+=1
                    if k=='goal': G['off_gf' if mine else 'off_ga']+=1
                G['team_cf' if mine else 'team_ca']+=1
                if k=='goal': G['team_gf' if mine else 'team_ga']+=1
            if k=='goal' and ME in (d.get('scoringPlayerId'),d.get('assist1PlayerId'),d.get('assist2PlayerId')):
                G['pts']+=1
                if s=='5v5': G['pts_5v5']+=1
                if d.get('scoringPlayerId')==ME and s=='5v5': G['g_5v5']+=1
                if d.get('assist1PlayerId')==ME: G['a1']+=1
                if d.get('assist2PlayerId')==ME: G['a2']+=1
            if d.get('shootingPlayerId')==ME or (k=='goal' and d.get('scoringPlayerId')==ME):
                G['icf']+=1
                if k!='blocked-shot': G['iff']+=1
                if k in ('shot-on-goal','goal'): G['isog']+=1
                if k=='goal': G['ig']+=1
                if s=='5v5': G['icf_5v5']+=1
            if k=='blocked-shot' and d.get('blockingPlayerId')==ME: G['blk']+=1
        if k=='hit':
            if d.get('hittingPlayerId')==ME: G['hits']+=1
            if d.get('hitteePlayerId')==ME: G['hits_taken']+=1
        if k=='penalty':
            if d.get('committedByPlayerId')==ME: G['pen_taken']+=1
            if d.get('drawnByPlayerId')==ME: G['pen_drawn']+=1
        if k=='takeaway' and d.get('playerId')==ME: G['tk']+=1
        if k=='giveaway' and d.get('playerId')==ME: G['gv']+=1
    # MoneyPuck xG join (unblocked shots)
    for sh_ in mp.get(gid,[]):
        t=min(sh_['t'],len(on2)-1); me_on= ME in on2[t]; s=situ2(t) if on2[t] else 'other'
        mine= sh_['team']==myabbr
        if sh_['shooter']==ME:
            G['ixg']+=sh_['xg']
            if s=='5v5': G['ixg_5v5']+=sh_['xg']
        if s!='5v5': continue
        if me_on:
            G['xgf' if mine else 'xga']+=sh_['xg']
            if sh_['xg']>=0.2: G['hdcf' if mine else 'hdca']+=1
        else:
            G['off_xgf' if mine else 'off_xga']+=sh_['xg']
        G['team_xgf' if mine else 'team_xga']+=sh_['xg']
    G['mates_id']={str(p):v for p,v in G['mates'].items()}
    G['opps_id']={str(p):v for p,v in G['opps'].items()}
    G['mates']={names.get(p,p):v for p,v in G['mates'].most_common(8)}
    G['opps']={names.get(p,p):v for p,v in G['opps'].most_common(8)}
    for k in ('toi','team_toi','fo','fo_start'): G[k]=dict(G[k])
    games.append(G)
json.dump(games,open('onice_games.json','w'),indent=0)
print('built',len(games))
