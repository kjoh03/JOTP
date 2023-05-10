from scipy.stats import poisson
import pandas as pd
import random
import xlwt


### A LIST OF ALL REMAINING FIXTURES TO SIMULATE
fixtureslist = [
    ('Prior Lake Typhoon','FC International'),
    ('St Paul Blackhawks 04 Red','Harambee HS Boys 1'),
    ('Sala Boys Black','JOTP LaMancha'),
    ('Prior Lake Typhoon','JOTP LaMancha'),
    ('St Paul Blackhawks 04 Red','KFA Boys'),
    ('JOTP Kiko','FC International'),
    ('JOTP Kaghani','JOTP Murciana'),
    ('Joga Bonito Rio','Sala Boys Blue'),
    ('JOTP Garganica','JOTP Girgentana'),
    ('JOTP Verata','Harambee HS Boys 1'),
    ('Blackhawks 2006 Black','Hawks')
    ]

### A LIST OF ALL TEAMS
teamslist = ['Blackhawks 2006 Black','FC International','Harambee HS Boys 1',
             'Hawks','Joga Bonito Rio','JOTP Garganica','JOTP Girgentana',
             'JOTP Kaghani','JOTP Kiko','JOTP LaMancha','JOTP Murciana',
             'JOTP Verata','KFA Boys','Prior Lake Typhoon','Sala Boys Black',
             'Sala Boys Blue','St Paul Blackhawks 04 Red']

### THIS FUNCTION IS JUST TO CREATE A DICTIONARY TO STORE INFO FOR THE LEAGUE TABLE
### DICTIONARIES ARE A VERY COOL PROGRAMMING TOOL THAT MAKES STORING INFO EASY
def League_Dict():
    LeagueDict = {}
    LeagueDict['Blackhawks 2006 Black'] = {}
    LeagueDict['Blackhawks 2006 Black']['GP'] = 9
    LeagueDict['Blackhawks 2006 Black']['GF'] = 68#82
    LeagueDict['Blackhawks 2006 Black']['GA'] = 55
    LeagueDict['Blackhawks 2006 Black']['Pts'] = 18
    LeagueDict['Blackhawks 2006 Black']['Opp Pts/Game'] = 1.40895

    LeagueDict['FC International'] = {}
    LeagueDict['FC International']['GP'] = 8
    LeagueDict['FC International']['GF'] = 52#58
    LeagueDict['FC International']['GA'] = 47#50
    LeagueDict['FC International']['Pts'] = 18
    LeagueDict['FC International']['Opp Pts/Game'] = 1.47396

    LeagueDict['Harambee HS Boys 1'] = {}
    LeagueDict['Harambee HS Boys 1']['GP'] = 8
    LeagueDict['Harambee HS Boys 1']['GF'] = 30
    LeagueDict['Harambee HS Boys 1']['GA'] = 62#64
    LeagueDict['Harambee HS Boys 1']['Pts'] = 3
    LeagueDict['Harambee HS Boys 1']['Opp Pts/Game'] = 1.77

    LeagueDict['Hawks'] = {}
    LeagueDict['Hawks']['GP'] = 9
    LeagueDict['Hawks']['GF'] = 34
    LeagueDict['Hawks']['GA'] = 74#97
    LeagueDict['Hawks']['Pts'] = 3
    LeagueDict['Hawks']['Opp Pts/Game'] = 1.508

    LeagueDict['Joga Bonito Rio'] = {}
    LeagueDict['Joga Bonito Rio']['GP'] = 9
    LeagueDict['Joga Bonito Rio']['GF'] = 69#76
    LeagueDict['Joga Bonito Rio']['GA'] = 54#58
    LeagueDict['Joga Bonito Rio']['Pts'] = 18
    LeagueDict['Joga Bonito Rio']['Opp Pts/Game'] = 1.2145

    LeagueDict['JOTP Garganica'] = {}
    LeagueDict['JOTP Garganica']['GP'] = 9
    LeagueDict['JOTP Garganica']['GF'] = 67#71
    LeagueDict['JOTP Garganica']['GA'] = 65#68
    LeagueDict['JOTP Garganica']['Pts'] = 15
    LeagueDict['JOTP Garganica']['Opp Pts/Game'] = 1.466

    LeagueDict['JOTP Girgentana'] = {}
    LeagueDict['JOTP Girgentana']['GP'] = 9
    LeagueDict['JOTP Girgentana']['GF'] = 30
    LeagueDict['JOTP Girgentana']['GA'] = 79#114
    LeagueDict['JOTP Girgentana']['Pts'] = 1
    LeagueDict['JOTP Girgentana']['Opp Pts/Game'] = 1.4568

    LeagueDict['JOTP Kaghani'] = {}
    LeagueDict['JOTP Kaghani']['GP'] = 9
    LeagueDict['JOTP Kaghani']['GF'] = 72#79
    LeagueDict['JOTP Kaghani']['GA'] = 38
    LeagueDict['JOTP Kaghani']['Pts'] = 24
    LeagueDict['JOTP Kaghani']['Opp Pts/Game'] = 1.5077

    LeagueDict['JOTP Kiko'] = {}
    LeagueDict['JOTP Kiko']['GP'] = 9
    LeagueDict['JOTP Kiko']['GF'] = 59#61
    LeagueDict['JOTP Kiko']['GA'] = 46#52
    LeagueDict['JOTP Kiko']['Pts'] = 15
    LeagueDict['JOTP Kiko']['Opp Pts/Game'] = 1.4012

    LeagueDict['JOTP LaMancha'] = {}
    LeagueDict['JOTP LaMancha']['GP'] = 8
    LeagueDict['JOTP LaMancha']['GF'] = 84#89
    LeagueDict['JOTP LaMancha']['GA'] = 42
    LeagueDict['JOTP LaMancha']['Pts'] = 24
    LeagueDict['JOTP LaMancha']['Opp Pts/Game'] = 1.4722

    LeagueDict['JOTP Murciana'] = {}
    LeagueDict['JOTP Murciana']['GP'] = 9
    LeagueDict['JOTP Murciana']['GF'] = 49
    LeagueDict['JOTP Murciana']['GA'] = 93#105
    LeagueDict['JOTP Murciana']['Pts'] = 4
    LeagueDict['JOTP Murciana']['Opp Pts/Game'] = 1.4614

    LeagueDict['JOTP Verata'] = {}
    LeagueDict['JOTP Verata']['GP'] = 9
    LeagueDict['JOTP Verata']['GF'] = 35
    LeagueDict['JOTP Verata']['GA'] = 74#80
    LeagueDict['JOTP Verata']['Pts'] = 3
    LeagueDict['JOTP Verata']['Opp Pts/Game'] = 1.767

    LeagueDict['KFA Boys'] = {}
    LeagueDict['KFA Boys']['GP'] = 9
    LeagueDict['KFA Boys']['GF'] = 76#87
    LeagueDict['KFA Boys']['GA'] = 52
    LeagueDict['KFA Boys']['Pts'] = 18
    LeagueDict['KFA Boys']['Opp Pts/Game'] = 1.4275

    LeagueDict['Prior Lake Typhoon'] = {}
    LeagueDict['Prior Lake Typhoon']['GP'] = 8
    LeagueDict['Prior Lake Typhoon']['GF'] = 44#53
    LeagueDict['Prior Lake Typhoon']['GA'] = 47
    LeagueDict['Prior Lake Typhoon']['Pts'] = 9
    LeagueDict['Prior Lake Typhoon']['Opp Pts/Game'] = 1.39

    LeagueDict['Sala Boys Black'] = {}
    LeagueDict['Sala Boys Black']['GP'] = 9
    LeagueDict['Sala Boys Black']['GF'] = 79#104
    LeagueDict['Sala Boys Black']['GA'] = 23
    LeagueDict['Sala Boys Black']['Pts'] = 27
    LeagueDict['Sala Boys Black']['Opp Pts/Game'] = 1.35185

    LeagueDict['Sala Boys Blue'] = {}
    LeagueDict['Sala Boys Blue']['GP'] = 9
    LeagueDict['Sala Boys Blue']['GF'] = 59#77
    LeagueDict['Sala Boys Blue']['GA'] = 46#55
    LeagueDict['Sala Boys Blue']['Pts'] = 15
    LeagueDict['Sala Boys Blue']['Opp Pts/Game'] = 1.4

    LeagueDict['St Paul Blackhawks 04 Red'] = {}
    LeagueDict['St Paul Blackhawks 04 Red']['GP'] = 8
    LeagueDict['St Paul Blackhawks 04 Red']['GF'] = 49
    LeagueDict['St Paul Blackhawks 04 Red']['GA'] = 59#64
    LeagueDict['St Paul Blackhawks 04 Red']['Pts'] = 6
    LeagueDict['St Paul Blackhawks 04 Red']['Opp Pts/Game'] = 1.88
    return LeagueDict


### NOW WE CALCULATE THE AVERAGE NUMBER OF GOALS PER GAME
def avg_goals_per_game(LeagueDict):
    AvgGoalsPerGame = 0
    for team in LeagueDict:
        AvgGoalsPerGame = AvgGoalsPerGame + LeagueDict[team]['GF']/(85-len(fixtureslist))
    return AvgGoalsPerGame

### WE'RE GONNA BE INTERESTED IN THE AVERAGE NUMBER OF POINTS AS WELL SO LETS CALCULATE THAT
def avg_points_per_game(LeagueDict):
    AvgPoints = 0
    for team in LeagueDict:
        AvgPoints = AvgPoints + LeagueDict[team]['Pts']/LeagueDict[team]['GP']/len(LeagueDict)
    return AvgPoints


### NOW WE WANT TO KNOW HOW GOOD A TEAM IS AT ATTACKING / DEFENDING COMPARED TO THE LEAGUE AVERAGE
### WE WILL CREATE AN "ATTACK SCORE" AND A "DEFENSIVE SCORE" AND ADD IT TO OUR DICTIONARY
def att_def_scores(LeagueDict,AvgGoalsPerGame,AvgPoints):
    for team in LeagueDict:
        LeagueDict[team]['Att Score'] = LeagueDict[team]['GF']/LeagueDict[team]['GP']/(AvgGoalsPerGame/2)*(LeagueDict[team]['Opp Pts/Game']/AvgPoints)
        LeagueDict[team]['Def Score'] = LeagueDict[team]['GA']/LeagueDict[team]['GP']/(AvgGoalsPerGame/2)*(2-LeagueDict[team]['Opp Pts/Game']/AvgPoints)

### NOW THAT WE HAVE ATTACK / DEFENSE SCORES, WE CAN USE THEM TO PREDICT AN OUTCOME BETWEEN TWO TEAMS
### HERE WE CALCULATE THE EXPECTED GOALS FOR TEAM 1 AND TEAM 2
def xG_calculator(team1,team2,LeagueDict,AvgGoalsPerGame):
    team1xG = 3.2696#LeagueDict[team1]['Att Score']*LeagueDict[team2]['Def Score']*(AvgGoalsPerGame/2)
    team2xG = 5.4378#LeagueDict[team2]['Att Score']*LeagueDict[team1]['Def Score']*(AvgGoalsPerGame/2)
    return team1xG,team2xG


### WE HAVE EVERYTHING WE NEED SO LETS START PREDICTING MATCHES!
### HERE IS MY CODE FOR FINDING THE PROBABILITIES TO PREDICT A MATCH
def match_prediction_df(team1xG,team2xG):
    df = pd.DataFrame()
    team1winprob = 0
    drawprob = 0
    team2winprob = 0
    x = 0
    while poisson.cdf(x,team2xG) < 0.9999:
        problist = []
        y = 0
        while poisson.cdf(y,team1xG) < 0.9999:
            problist.append(round(poisson.pmf(y,team1xG)*poisson.pmf(x,team2xG),3))
            if x<y:
                team1winprob+=poisson.pmf(y,team1xG)*poisson.pmf(x,team2xG)
            elif x==y:
                drawprob+=poisson.pmf(y,team1xG)*poisson.pmf(x,team2xG)
            else:
                team2winprob+=poisson.pmf(y,team1xG)*poisson.pmf(x,team2xG)
            y+=1
        df[x] = problist
        x+=1
    print(df.to_string())
    df.to_csv('file_name.csv')
    return (round(team1winprob,3),round(drawprob,3),round(team2winprob,3))

### HERE IS MY CODE TO PREDICT THE ACTUAL SCORELINE (VERY SIMILAR)
def predict_match_score(team1xG,team2xG):
    team1score = 0
    team2score = 0
    randomnumber1 = random.uniform(0,1)
    randomnumber2 = random.uniform(0,1)
    pmf1 = poisson.pmf(0,team1xG)
    for x in range(100):
        if randomnumber1<pmf1:
            team1score = x
            break
        else:
            pmf1 += poisson.pmf(x+1,team1xG)
    pmf2 = poisson.pmf(0,team2xG)
    for y in range(100):
        if randomnumber2<pmf2:
            team2score = y
            break
        else:
            pmf2 += poisson.pmf(y+1,team2xG)
    return team1score,team2score

### LETS SIMULATE THE WHOLE LEAGUE NOW
def predict_all_matches(fixtureslist,LeagueDict,AvgGoalsPerGame):
    for fixture in fixtureslist:
        xG = xG_calculator(fixture[0],fixture[1],LeagueDict,AvgGoalsPerGame)
#        prob = match_prediction_df(xG[0],xG[1])
#        print(fixture)
#        print(prob)
        score = predict_match_score(xG[0],xG[1])
        if score[0]>score[1]:
            LeagueDict[fixture[0]]['Pts'] += 3
            LeagueDict[fixture[0]]['GF'] += score[0]
            LeagueDict[fixture[0]]['GA'] += score[1]
            LeagueDict[fixture[1]]['GF'] += score[1]
            LeagueDict[fixture[1]]['GA'] += score[0]
        elif score[0]<score[1]:
            LeagueDict[fixture[1]]['Pts'] += 3
            LeagueDict[fixture[1]]['GF'] += score[1]
            LeagueDict[fixture[1]]['GA'] += score[0]
            LeagueDict[fixture[0]]['GF'] += score[0]
            LeagueDict[fixture[0]]['GA'] += score[1]
        else:
            LeagueDict[fixture[0]]['Pts'] += 1
            LeagueDict[fixture[1]]['Pts'] += 1
            LeagueDict[fixture[0]]['GF'] += score[0]
            LeagueDict[fixture[0]]['GA'] += score[1]
            LeagueDict[fixture[1]]['GF'] += score[1]
            LeagueDict[fixture[1]]['GA'] += score[0]
    return LeagueDict

### THIS FUNCTION FINALIZES THE SIMULATED LEAGUE TABLE IN A PANDAS DATAFRAME
def league_table_df(LeagueDict):
    leaguetabledf = pd.DataFrame()
    i = 0
    for team in LeagueDict:
        leaguetabledf.at[i,'Team'] = team
        leaguetabledf.at[i,'GF'] = LeagueDict[team]['GF']
        leaguetabledf.at[i,'GA'] = LeagueDict[team]['GA']
        leaguetabledf.at[i,'GD'] = LeagueDict[team]['GF']-LeagueDict[team]['GA']
        leaguetabledf.at[i,'Pts'] = LeagueDict[team]['Pts']
        i+=1
        leaguetabledf = leaguetabledf.sort_values(by = ['Pts','GD','GF'],ascending = False).reset_index(drop=True)
    print(leaguetabledf)
    leaguetabledf.to_csv('file_name.csv')
    indexlist = []
    for team in LeagueDict:
        indexlist.append(leaguetabledf.index[leaguetabledf.Team == team][0])
    return indexlist,leaguetabledf

def playoffs(leaguetabledf):
    ### SEMI FINAL 1
    xG = xG_calculator(leaguetabledf.at[0,'Team'],leaguetabledf.at[3,'Team'],LeagueDict,AvgGoalsPerGame)
    semi1 = predict_match_score(xG[0],xG[1])
    if semi1[0] > semi1[1]:
        finalist1 = leaguetabledf.at[0,'Team']
        thirdplace1 = leaguetabledf.at[3,'Team']
    elif semi1[0] < semi1[1]:
        finalist1 = leaguetabledf.at[3,'Team']
        thirdplace1 = leaguetabledf.at[0,'Team']
    else:
        finalist1 = random.choice([leaguetabledf.at[0,'Team'],leaguetabledf.at[3,'Team']])
        lis1 = [leaguetabledf.at[0,'Team'],leaguetabledf.at[3,'Team']]
        lis1.remove(finalist1)
        thirdplace1 = lis1[0]
    ### SEMI FINAL 2
    xG = xG_calculator(leaguetabledf.at[1,'Team'],leaguetabledf.at[2,'Team'],LeagueDict,AvgGoalsPerGame)
    semi2 = predict_match_score(xG[0],xG[1])
    if semi2[0] > semi2[1]:
        finalist2 = leaguetabledf.at[1,'Team']
        thirdplace2 = leaguetabledf.at[2,'Team']
    elif semi2[0] < semi2[1]:
        finalist2 = leaguetabledf.at[2,'Team']
        thirdplace2 = leaguetabledf.at[1,'Team']
    else:
        finalist2 = random.choice([leaguetabledf.at[1,'Team'],leaguetabledf.at[2,'Team']])
        lis2 = [leaguetabledf.at[1,'Team'],leaguetabledf.at[2,'Team']]
        lis2.remove(finalist2)
        thirdplace2 = lis2[0]
    ### THIRD PLACE GAME
    xG = xG_calculator(thirdplace1,thirdplace2,LeagueDict,AvgGoalsPerGame)
    thirdplacegame = predict_match_score(xG[0],xG[1])
    if thirdplacegame[0] > thirdplacegame[1]:
        third = thirdplace1
        fourth = thirdplace2
    elif thirdplacegame[0] < thirdplacegame[1]:
        third = thirdplace2
        fourth = thirdplace1
    else:
        third = random.choice([thirdplace1,thirdplace2])
        lis3 = [thirdplace1,thirdplace2]
        lis3.remove(third)
        fourth = lis3[0]
    ### FINALS
    xG = xG_calculator(finalist1,finalist2,LeagueDict,AvgGoalsPerGame)
    finals = predict_match_score(xG[0],xG[1])
    if finals[0] > finals[1]:
        first = finalist1
        second = finalist2
    elif finals[0] < finals[1]:
        first = finalist2
        second = finalist1
    else:
        first = random.choice([finalist1,finalist2])
        lis4 = [finalist1,finalist2]
        lis4.remove(first)
        second = lis4[0]
    i = 0
    for team in LeagueDict:
        if team == first:
            firstfinishes[i] +=1
        elif team == second:
            secondfinishes[i] +=1
        elif team == third:
            thirdfinishes[i] +=1
        elif team == fourth:
            fourthfinishes[i] +=1
        i+=1
    print(first)
    print(second)
    print(third)
    print(fourth)
    return firstfinishes,secondfinishes,thirdfinishes,fourthfinishes
firstfinishes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
secondfinishes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
thirdfinishes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
fourthfinishes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


### NOW THAT WE HAVE OUR FOUNDATION PROGRAMMED, WE CAN START TELLING IT WHAT TO DO
    
if __name__ == '__main__':      ### <----- THIS LINE STARTS OUR COMMANDS
    LeagueDict = League_Dict()
    AvgGoalsPerGame = avg_goals_per_game(LeagueDict)
    AvgPoints = avg_points_per_game(LeagueDict)

    att_def_scores(LeagueDict,AvgGoalsPerGame,AvgPoints)
#    predict_all_matches(fixtureslist,LeagueDict,AvgGoalsPerGame)
#    leaguetabledf = league_table_df(LeagueDict)[1]
#    playoffs1 = playoffs(leaguetabledf)

    xG = xG_calculator('St Paul Blackhawks 04 Red','KFA Boys',LeagueDict,AvgGoalsPerGame)
    print(xG)
    print(match_prediction_df(xG[0],xG[1]))
'''
    Blackhawks2006Black = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    FCInternational = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    HarambeeHSBoys1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Hawks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    JogaBonitoRio = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    JOTPGarganica = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    JOTPGirgentana = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    JOTPKaghani = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    JOTPKiko = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    JOTPLaMancha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    JOTPMurciana = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    JOTPVerata = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    KFABoys = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    PriorLakeTyphoon = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    SalaBoysBlack = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    SalaBoysBlue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    StPaulBlackhawks04Red = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for x in range(10000):
        LeagueDict = League_Dict()
        att_def_scores(LeagueDict,AvgGoalsPerGame,AvgPoints)
        predict_all_matches(fixtureslist,LeagueDict,AvgGoalsPerGame)
        df = league_table_df(LeagueDict)
        indice = df[0]
        leaguetabledf = df[1]
        playoffs1 = playoffs(leaguetabledf)
        print(x)
        
        Blackhawks2006Black[indice[0]] += 1
        FCInternational[indice[1]] += 1
        HarambeeHSBoys1[indice[2]] += 1
        Hawks[indice[3]] += 1
        JogaBonitoRio[indice[4]] += 1
        JOTPGarganica[indice[5]] += 1
        JOTPGirgentana[indice[6]] += 1
        JOTPKaghani[indice[7]] += 1
        JOTPKiko[indice[8]] += 1
        JOTPLaMancha[indice[9]] += 1
        JOTPMurciana[indice[10]] += 1
        JOTPVerata[indice[11]] += 1
        KFABoys[indice[12]] += 1
        PriorLakeTyphoon[indice[13]] += 1
        SalaBoysBlack[indice[14]] += 1
        SalaBoysBlue[indice[15]] += 1
        StPaulBlackhawks04Red[indice[16]] += 1
    print(playoffs1[0])
    print(playoffs1[1])
    print(playoffs1[2])
    print(playoffs1[3])
  
    placementdb = [Blackhawks2006Black,FCInternational,HarambeeHSBoys1,Hawks,JogaBonitoRio,JOTPGarganica,JOTPGirgentana,JOTPKaghani,JOTPKiko,JOTPLaMancha,JOTPMurciana,JOTPVerata,KFABoys,PriorLakeTyphoon,SalaBoysBlack,SalaBoysBlue,StPaulBlackhawks04Red]
    wb = xlwt.Workbook()
    newsheet = wb.add_sheet('yes')
    y = 0
    for team in teamslist:
        newsheet.write(y,0,team)
        x = 0
        for value in placementdb[y]:
            newsheet.write(y,x+1,placementdb[y][x])
            x+=1
        y+=1
    wb.save('/Users/keanjohansen/Desktop/simulation.xls')
'''

