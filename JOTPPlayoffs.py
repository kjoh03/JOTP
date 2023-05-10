from scipy.stats import poisson
import pandas as pd
import random
import JOTPFutsalLeague as JOTPFL
import xlwt

def League_Dict():
    LeagueDict = {}
    LeagueDict['Sala Boys Black'] = {}
    LeagueDict['Sala Boys Black']['GP'] = 9
    LeagueDict['Sala Boys Black']['GF'] = 89#118
    LeagueDict['Sala Boys Black']['GA'] = 26
    LeagueDict['Sala Boys Black']['Pts'] = 30
    LeagueDict['Sala Boys Black']['Opp Pts/Game'] = 1.49

    LeagueDict['JOTP LaMancha'] = {}
    LeagueDict['JOTP LaMancha']['GP'] = 10
    LeagueDict['JOTP LaMancha']['GF'] = 100#105
    LeagueDict['JOTP LaMancha']['GA'] = 61#65
    LeagueDict['JOTP LaMancha']['Pts'] = 27
    LeagueDict['JOTP LaMancha']['Opp Pts/Game'] = 1.59
    
    LeagueDict['JOTP Kaghani'] = {}
    LeagueDict['JOTP Kaghani']['GP'] = 10
    LeagueDict['JOTP Kaghani']['GF'] = 83#91
    LeagueDict['JOTP Kaghani']['GA'] = 42
    LeagueDict['JOTP Kaghani']['Pts'] = 27
    LeagueDict['JOTP Kaghani']['Opp Pts/Game'] = 1.35
    
    LeagueDict['FC International'] = {}
    LeagueDict['FC International']['GP'] = 10
    LeagueDict['FC International']['GF'] = 65#71
    LeagueDict['FC International']['GA'] = 59#62
    LeagueDict['FC International']['Pts'] = 22
    LeagueDict['FC International']['Opp Pts/Game'] = 1.45
    return LeagueDict


def playoffs(team1,team2,team3,team4,LeagueDict,AvgGoalsPerGame):
    ### SEMI FINAL 1
    xG = JOTPFL.xG_calculator(team1,team4,LeagueDict,AvgGoalsPerGame)
    semi1 = JOTPFL.predict_match_score(xG[0],xG[1])
    if semi1[0] > semi1[1]:
        finalist1 = team1
        thirdplace1 = team4
    elif semi1[0] < semi1[1]:
        finalist1 = team4
        thirdplace1 = team1
    else:
        finalist1 = random.choice([team1,team4])
        lis1 = [team1,team4]
        lis1.remove(finalist1)
        thirdplace1 = lis1[0]
    ### SEMI FINAL 2
    xG = JOTPFL.xG_calculator(team2,team3,LeagueDict,AvgGoalsPerGame)
    semi2 = JOTPFL.predict_match_score(xG[0],xG[1])
    if semi2[0] > semi2[1]:
        finalist2 = team2
        thirdplace2 = team3
    elif semi2[0] < semi2[1]:
        finalist2 = team3
        thirdplace2 = team2
    else:
        finalist2 = random.choice([team2,team3])
        lis2 = [team2,team3]
        lis2.remove(finalist2)
        thirdplace2 = lis2[0]
    ### THIRD PLACE GAME
    xG = JOTPFL.xG_calculator(thirdplace1,thirdplace2,LeagueDict,AvgGoalsPerGame)
    thirdplacegame = JOTPFL.predict_match_score(xG[0],xG[1])
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
    xG = JOTPFL.xG_calculator(finalist1,finalist2,LeagueDict,AvgGoalsPerGame)
    finals = JOTPFL.predict_match_score(xG[0],xG[1])
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
    return firstfinishes,secondfinishes,thirdfinishes,fourthfinishes

firstfinishes = [0,0,0,0]
secondfinishes = [0,0,0,0]
thirdfinishes = [0,0,0,0]
fourthfinishes = [0,0,0,0]

if __name__ == '__main__':
    LeagueDict = League_Dict()
    AvgGoalsPerGame = 13.4588
    AvgPoints = 1.47
    JOTPFL.att_def_scores(LeagueDict,AvgGoalsPerGame,AvgPoints)

    xG = JOTPFL.xG_calculator('Sala Boys Black','JOTP LaMancha',LeagueDict,AvgGoalsPerGame)
    print(xG)
    print(JOTPFL.match_prediction_df(xG[0],xG[1]))
    '''
    for i in range(10000):
        playoffs('Sala Boys Black','JOTP LaMancha','JOTP Kaghani','FC International',LeagueDict,AvgGoalsPerGame)
        print(i)
    print(firstfinishes)
    print(secondfinishes)
    print(thirdfinishes)
    print(fourthfinishes)
    '''
      
