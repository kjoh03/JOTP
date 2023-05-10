import random
import pandas as pd

playoffteamlist = ['Australia','Peru','UAE','Costa Rica','New Zealand','Ukraine','Scotland','Wales']

teamlist = ['Qatar','Mexico','Senegal','Cameroon','Brazil','Netherlands','Iran','Canada',
    'Belgium','Denmark','Japan','Ecuador','France','Germany','Morocco','Saudi Arabia',
    'Argentina','Uruguay','Serbia','Ghana','England','Switzerland','Poland',
    'Spain','USA','South Korea','Portugal','Croatia','Tunisia']



def world_cup_dict():
    WCDict = {}
    WCDict['Qatar'] = {}
    WCDict['Qatar']['Elo'] = 1441.41
    WCDict['Mexico'] = {}
    WCDict['Mexico']['Elo'] = 1658.82
    WCDict['Senegal'] = {}
    WCDict['Senegal']['Elo'] = 1584.16
    WCDict['Cameroon'] = {}
    WCDict['Cameroon']['Elo'] = 1480.48
    WCDict['Brazil'] = {}
    WCDict['Brazil']['Elo'] = 1832.69
    WCDict['Netherlands'] = {}
    WCDict['Netherlands']['Elo'] = 1658.66
    WCDict['Iran'] = {}
    WCDict['Iran']['Elo'] = 1564.49
    WCDict['Canada'] = {}
    WCDict['Canada']['Elo'] = 1479
    WCDict['Belgium'] = {}
    WCDict['Belgium']['Elo'] = 1827
    WCDict['Denmark'] = {}
    WCDict['Denmark']['Elo'] = 1653.6
    WCDict['Japan'] = {}
    WCDict['Japan']['Elo'] = 1553.44
    WCDict['Ecuador'] = {}
    WCDict['Ecuador']['Elo'] = 1452.63
    WCDict['France'] = {}
    WCDict['France']['Elo'] = 1789.85
    WCDict['Germany'] = {}
    WCDict['Germany']['Elo'] = 1650.53
    WCDict['Morocco'] = {}
    WCDict['Morocco']['Elo'] = 1551.88
    WCDict['Saudi Arabia'] = {}
    WCDict['Saudi Arabia']['Elo'] = 1444.69
    WCDict['Argentina'] = {}
    WCDict['Argentina']['Elo'] = 1765.13
    WCDict['Uruguay'] = {}
    WCDict['Uruguay']['Elo'] = 1635.73
    WCDict['Serbia'] = {}
    WCDict['Serbia']['Elo'] = 1547.53
    WCDict['Ghana'] = {}
    WCDict['Ghana']['Elo'] = 1387.36
    WCDict['England'] = {}
    WCDict['England']['Elo'] = 1761.71
    WCDict['Switzerland'] = {}
    WCDict['Switzerland']['Elo'] = 1635.32
    WCDict['Poland'] = {}
    WCDict['Poland']['Elo'] = 1544.2
    WCDict['Spain'] = {}
    WCDict['Spain']['Elo'] = 1709.19
    WCDict['USA'] = {}
    WCDict['USA']['Elo'] = 1633.72
    WCDict['South Korea'] = {}
    WCDict['South Korea']['Elo'] = 1519.54
    WCDict['Portugal'] = {}
    WCDict['Portugal']['Elo'] = 1674.78
    WCDict['Croatia'] = {}
    WCDict['Croatia']['Elo'] = 1621.11
    WCDict['Tunisia'] = {}
    WCDict['Tunisia']['Elo'] = 1499.8
    WCDict['Australia'] = {}
    WCDict['Australia']['Elo'] =1462.29
    WCDict['Peru'] = {}
    WCDict['Peru']['Elo'] = 1562.32
    WCDict['UAE'] = {}
    WCDict['UAE']['Elo'] = 1356.99
    WCDict['Costa Rica'] = {}
    WCDict['Costa Rica']['Elo'] = 1503.09
    WCDict['New Zealand'] = {}
    WCDict['New Zealand']['Elo'] = 1206.07
    WCDict['Ukraine'] = {}
    WCDict['Ukraine']['Elo'] = 1535.08
    WCDict['Scotland'] = {}
    WCDict['Scotland']['Elo'] = 1472.66
    WCDict['Wales'] = {}
    WCDict['Wales']['Elo'] = 1588.08
    return WCDict

def predict_outcome(team1,team2):
    win1 = 1/(10**(-(WCDict[team1]['Elo']-WCDict[team2]['Elo'])/600)+1)
    num = random.random()
    if num < win1:
        winner = team1
    else:
        winner = team2
    return winner

def playoff_simulation():
    europlayoff1 = predict_outcome('Scotland','Ukraine')
    europlayoffwinner = predict_outcome('Wales',europlayoff1)
    asiaplayoff = predict_outcome('Australia','UAE')
    ICPlayoff1 = predict_outcome('Peru',asiaplayoff)
    ICPlayoff2 = predict_outcome('Costa Rica','New Zealand')
    return [europlayoffwinner,ICPlayoff1,ICPlayoff2]

def simulate_group(T1,T2,T3,T4):
    WCDict[T1]['Pts'] = 0
    WCDict[T2]['Pts'] = 0
    WCDict[T3]['Pts'] = 0
    WCDict[T4]['Pts'] = 0
    m11 = predict_outcome(T1,T2)
    m12 = predict_outcome(T3,T4)
    m21 = predict_outcome(T1,T3)
    m22 = predict_outcome(T2,T4)
    m31 = predict_outcome(T1,T4)
    m32 = predict_outcome(T2,T3)
    WCDict[m11]['Pts'] += 3
    WCDict[m12]['Pts'] += 3
    WCDict[m21]['Pts'] += 3
    WCDict[m22]['Pts'] += 3
    WCDict[m31]['Pts'] += 3
    WCDict[m32]['Pts'] += 3
    pts9 = []
    pts6 = []
    pts3 = []
    for team in [T1,T2,T3,T4]:
        if WCDict[team]['Pts'] == 9:
            pts6.append(team)
        elif WCDict[team]['Pts'] == 6:
            pts6.append(team)
        elif WCDict[team]['Pts'] == 3:
            pts3.append(team)
    if len(pts9) == 1:
        winner = pts9[0]
        if len(pts6) == 1:
            runnerup = pts6[0]
        elif len(pts6) == 0:
            runnerup = random.choice(pts3)
        else:
            runnerup = random.choice(pts6)
    else:
        if len(pts6) == 1:
            winner = pts6[0]
            runnerup = random.choice(pts3)
        elif len(pts6) == 2:
            winner = random.choice(pts6)
            pts6.remove(winner)
            runnerup = pts6[0]
        elif len(pts6) == 3:
            winner = random.choice(pts6)
            pts6.remove(winner)
            runnerup = random.choice(pts6)
    return winner,runnerup

def simulate_knockout(A1,A2,B1,B2,C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,H1,H2):
    qf = []
    sf = []
    f = []
    k1 = predict_outcome(A1,B2)
    k2 = predict_outcome(A2,B1)
    k3 = predict_outcome(C1,D2)
    k4 = predict_outcome(C2,D1)
    k5 = predict_outcome(E1,F2)
    k6 = predict_outcome(F1,E2)
    k7 = predict_outcome(G1,H2)
    k8 = predict_outcome(G2,H1)
    for team in (k1,k2,k3,k4,k5,k6,k7,k8):
        qf.append(team)
    q1 = predict_outcome(k1,k3)
    q2 = predict_outcome(k2,k4)
    q3 = predict_outcome(k5,k7)
    q4 = predict_outcome(k6,k8)
    for team in (q1,q2,q3,q4):
        sf.append(team)
    s1 = predict_outcome(q1,q3)
    s2 = predict_outcome(q2,q4)
    for team in (s1,s2):
        f.append(team)
    winner = predict_outcome(s1,s2)
    return winner,f,sf,qf

def predict_outcome_draws(team1,team2):
    ratingdif = WCDict[team1]['Elo']-WCDict[team2]['Elo']
    eloparam = 600
    drawparam = .8
    win1 = 10**(.5*ratingdif/eloparam)/(10**(.5*ratingdif/eloparam)+10**(-.5*ratingdif/eloparam)+drawparam)
    win2 = 10**(-.5*ratingdif/eloparam)/(10**(.5*ratingdif/eloparam)+10**(-.5*ratingdif/eloparam)+drawparam)
    draw = drawparam/(10**(.5*ratingdif/eloparam)+10**(-.5*ratingdif/eloparam)+drawparam)
    num = random.random()
    if num < win1:
        result = team1
    elif win1 <= num < win1+draw:
        result = 'Draw'
    else:
        result = team2
    return result

def simulate_group_draws(teams):
    WCDict[teams[0]]['Pts'] = 0
    WCDict[teams[1]]['Pts'] = 0
    WCDict[teams[2]]['Pts'] = 0
    WCDict[teams[3]]['Pts'] = 0
    x = 0
    y = 1
    while x<4:
        y = 1
        while y<4-x:
            result = predict_outcome_draws(teams[x],teams[y+x])
            if result == 'Draw':
                WCDict[teams[x]]['Pts'] += 1
                WCDict[teams[y+x]]['Pts'] += 1
            else:
                WCDict[result]['Pts'] += 3
            y+=1
        x+=1
    table = pd.DataFrame({'Team':teams,'Pts':[WCDict[teams[0]]['Pts'],WCDict[teams[1]]['Pts'],WCDict[teams[2]]['Pts'],WCDict[teams[3]]['Pts']]})
    table = table.sort_values('Pts', ascending = False)
    if table.iat[0,1] == table.iat[1,1] == table.iat[2,1] == table.iat[3,1]:
        lis = [table.iat[0,0],table.iat[1,0],table.iat[2,0],table.iat[3,0]]
        winner = random.choice(lis)
        lis.remove(winner)
        runnerup = random.choice(lis)
    elif table.iat[0,1] == table.iat[1,1] == table.iat[2,1]:
        lis = [table.iat[0,0],table.iat[1,0],table.iat[2,0]]
        winner = random.choice(lis)
        lis.remove(winner)
        runnerup = random.choice(lis)
    elif table.iat[0,1] == table.iat[1,1]:
        lis = [table.iat[0,0],table.iat[1,0]]
        winner = random.choice(lis)
        lis.remove(winner)
        runnerup = random.choice(lis)
    else:
        winner = table.iat[0,0]
        if table.iat[1,1] == table.iat[2,1] == table.iat[3,1]:
            lis = [table.iat[1,0],table.iat[2,0],table.iat[3,0]]
            runnerup = random.choice(lis)
        if table.iat[1,1] == table.iat[2,1]:
            lis = [table.iat[1,0],table.iat[2,0]]
            runnerup = random.choice(lis)
        else:
            runnerup = table.iat[1,0]
    return winner,runnerup



WCDict = world_cup_dict()
df = pd.DataFrame({'Team':teamlist+playoffteamlist,'R16':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'QF':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'SF':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'Final':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],'Winner':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
df.set_index('Team', inplace = True)



for i in range(10000):
    print(i)
    playoffteams = playoff_simulation()
    A = simulate_group_draws(['Qatar','Ecuador','Senegal','Netherlands'])
    B = simulate_group_draws(['England','Iran','USA',playoffteams[0]])
    C = simulate_group_draws(['Argentina','Saudi Arabia','Mexico','Poland'])
    D = simulate_group_draws(['France',playoffteams[1],'Denmark','Tunisia'])
    E = simulate_group_draws(['Spain',playoffteams[2],'Germany','Japan'])
    F = simulate_group_draws(['Belgium','Canada','Morocco','Croatia'])
    G = simulate_group_draws(['Brazil','Serbia','Switzerland','Cameroon'])
    H = simulate_group_draws(['Portugal','Ghana','Uruguay','South Korea'])
    bracket = simulate_knockout(A[0],A[1],B[0],B[1],C[0],C[1],D[0],D[1],E[0],E[1],F[0],F[1],G[0],G[1],H[0],H[1])
    for team in teamlist+playoffteams:
        if team in [A[0],A[1],B[0],B[1],C[0],C[1],D[0],D[1],E[0],E[1],F[0],F[1],G[0],G[1],H[0],H[1]]:
            df.loc[team]['R16']+=1
        if team in bracket[3]:
            df.loc[team]['QF']+=1
        if team in bracket[2]:
            df.loc[team]['SF']+=1
        if team in bracket[1]:
            df.loc[team]['Final']+=1
        if team in bracket[0]:
            df.loc[team]['Winner']+=1
    
df = df.sort_values('Winner', ascending = False)
print(df)


















'''
spain = 0
costarica = 0
germany = 0
japan = 0

for i in range(100000):
    result = simulate_group('France','Peru','Denmark','Tunisia')
    if result[0] == 'France' or result[1] == 'France':
        spain +=1
    if result[0] == 'Peru' or result[1] == 'Peru':
        costarica +=1
    if result[0] == 'Denmark' or result[1] == 'Denmark':
        germany +=1
    if result[0] == 'Tunisia' or result[1] == 'Tunisia':
        japan +=1

print(spain)
print(costarica)
print(germany)
print(japan)


'''




