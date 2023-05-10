from tkinter import *
import tkinter as tk
import os
import glob
import StatTrackerAnalysis as STA
import StatTracker as ST

'''
def player_list(team):
    if team == 'Joy AC':
        playerlist = ['Opponent Player','#2 Vukota Mastilovic','#3 Marco Corona Duran','#4, Noah Kantorowicz','#6 Martin Browne Jr','#8 Philip Caputo','#10 Whitney Browne','#11 Bennett Kouame','#12 Marshall Urban','#13 Luca Guarin','#14 Brian Kallman','#18 Dimitri Nair','#19 Mika Folstad','#22 David Riera','#24 Zinedine Kroeten','#28 Simeon Friesen','#29 Gabriel Eduarte','Henry Elias','Diego Paulin','Griffin Price','Jonathan Robles','#0 Tucker Mann','#1 Gage Steiner']
#2021        playerlist = ['Opponent Player','#2 Devan DiGrado','#3 Marco Corona Duran','#4 Noah Kantorowicz','#5 Vukota Mastilovic','#6 David Riera','#7 Zinedine Kroeten','#8 Aiden Cavanaugh','#9 Darley Florvil','#10 Whitney Browne','#11 Emmanuel Iwe','#12 Marshall Urban','#14 Philip Caputo','#15 Otis Anderson','#16 Xavier Zengue','#17 Denilson Ramos','#18 Dennis Mensah','#19 Mika Folstad','#20 Jorge Radilla','#21 Luis Martinez Rojas','#22 Dimitri Nair','#23 Liam Vance','#24 Martin Browne Jr','#27 Abduselam Regassa','#28 Gabriel Eduarte','#29 Diego Paulin','#1 Dawson Fairchild','#0 Tucker Mann','#30 Ayuub Ahmed','Andrei Gotsmanov','Siddiq Madson-Keita','Henry Elias']
    elif team == 'Joy LaMancha':
        playerlist = ['Opponent Player','Phil','Gabe','Henry','Mika','Luca','Siddiq','Bennett','Dimi','Andrew','Diego','Jack','Diego GK']
    elif team == 'Joy U19':
        playerlist = ['Opponent Player','Adri','Henry','Michael','Phil','Mika','Victor','Elsini','Hassan','Oliver','Josiah','Noah','Sean','Isaiah','Carlitos','Yonas','Minoli','Gabe','Bennett','Sebe','Zekiah']
    elif team == 'Joy Kaghani':
        playerlist = ['Opponent Player','Wilton','Si','Luca','Jack','Eric','Johnny','Manny','Max','Liam']
    elif team == 'Joy Tennessee Fainting':
        playerlist = ['Opponent Player','Alanna','Dare','Allison','Iman','Riana','Sami','Aliviah','Sam','Ari','Caitlyn']
    elif team == 'Joy 06':
        playerlist = ['Opponent Player','Nico', 'Tyler', 'Oliver', 'Isaiah', 'Will', 'Luca','Benji', 'Mikey', 'Kai', 'Eric', 'Makai', 'John', 'Leo', 'Lucas', 'Johnny','Jeremy'] 
    elif team == 'Cornell Mens Soccer':
        playerlist = ['Opponent Player','#2 Gaurab Khadka','#3 Greg Pappadakis','#4 Emerson Roy','#5 Thomas Hamborg','#6 Drew Bruck','#7 Cian McNamara','#8 Nolan Zeger','#9 Aria Dehshid','#10 Owen Smith','#11 Andrew Lopez','#12 Galen Westervelt','#14 Sam Brueck','#15 Zach Miller','#16 Jonas Ricke','#17 Vance Wicker','#18 Mardoche Ntonku','#19 Justin Howe','#20 Brian Gin','#21 George Archer','#22 Blake Soto','#23 Bryce Scott','#24 Aron Mawia','#27 Federico Polidori','#28 Eddie Garces','#0 Will Bickel','#1 Jeremy Spina','#32 Mateo Ramirez']
    return playerlist
'''
def match_list(team,year):
    directory = '/Users/keanjohansen/Desktop/Stat Tracker/'+team+'/'+year
    os.chdir(directory)
    lis = glob.glob('*.csv')
    for i in range(len(lis)):
        lis[i] = lis[i].split('.')[0]
    lis = ['All Matches']+lis
    return lis
    
class DropDownMenu:
    def __init__(self,root,dropdownlist,defaultoption,rownumber=0,columnnumber=0):
        clicked = StringVar()
        clicked.set(defaultoption)
        self.clicked = clicked
        drop = OptionMenu(root,self.clicked,*dropdownlist).grid(row=rownumber,column=columnnumber)

def xG_graphic():
    matchID = root.grid_slaves(row=1,column=0)[0]['text']
    if matchID == 'Choose Match':
        print('Please Select a Match')
        return ''
    if matchID == 'All Matches':
        matchlist1 = []
        for ele in matchlist:
            if not ele == 'All Matches':
                matchlist1.append(ele)
        for match in matchlist1:
            MatchDict = STA.match_stats(dfDict,match)
            STA.draw_xG_graphic(MatchDict,dfDict,match)
    else:
        MatchDict = STA.match_stats(dfDict,matchID)
        STA.draw_xG_graphic(MatchDict,dfDict,matchID)

def team_shot_chart():
    matchID = root.grid_slaves(row=1,column=0)[0]['text']
    if matchID == 'Choose Match':
        print('Please Select a Match')
        return ''
#    if matchID == 'All Matches':
#        print('Feature Not Available Right Now')
#        return ''
    if matchID == 'All Matches':
        matchlist2 = []
        for ele in matchlist:
            if not ele == 'All Matches':
                matchlist2.append(ele)
    else:
        matchlist2 = [matchID]
    shotdf = STA.read_all_data_to_one_df(dfDict,matchlist2)
    STA.shot_chart(shotdf,'no')

def player_shot_chart():
    player = root.grid_slaves(row=4,column=0)[0]['text']
    matchID = root.grid_slaves(row=4,column=1)[0]['text']
    if player == 'Choose Player':
        print('Please Select a Player')
        return ''
    if matchID == 'Choose Match':
        print('Please Select a Match')
        return ''
    if matchID == 'All Matches':
        matchlist2 = []
        for ele in matchlist:
            if not ele == 'All Matches':
                matchlist2.append(ele)
    else:
        matchlist2 = [matchID]
    shotdf = STA.read_all_data_to_one_df(dfDict,matchlist2)
    STA.individual_player_shot_charts(player,shotdf,'no')

def print_player_df():
    matchID = root.grid_slaves(row=4,column=1)[0]['text']
    if matchID == 'Choose Match':
        print('Please Select a Match')
        return ''
    if matchID == 'All Matches':
        matchlist3 = []
        for ele in matchlist:
            if not ele == 'All Matches':
                matchlist3.append(ele)
    else:
        matchlist3 = [root.grid_slaves(row=4,column=1)[0]['text']]
    TeamDict = STA.team_dict(team,year)
    TeamDict = STA.full_season_player_data(dfDict,TeamDict,matchlist3)
    STA.individual_performers_df(TeamDict)

def season_player_progression():
    if root.grid_slaves(row=4,column=0)[0]['text'] == 'Choose Player':
        print('Please Select a Player')
    else:
        STA.season_progression_graphic(root.grid_slaves(row=4,column=0)[0]['text'],dfDict,['Cornell Mens Soccer vs Luther','Cornell Mens Soccer vs Simpson','Cornell Mens Soccer vs Rockford','Cornell Mens Soccer vs Nebraska Wesleyan','Cornell Mens Soccer vs Bethel','Cornell Mens Soccer vs Coe','Cornell Mens Soccer vs Knox','Cornell Mens Soccer vs Central','Cornell Mens Soccer vs Ripon','Cornell Mens Soccer vs Grinnell','Cornell Mens Soccer vs Buena Vista','Cornell Mens Soccer vs Illinois College','Cornell Mens Soccer vs Lake Forest'])#['Cornell vs Luther','Cornell vs Coe','Cornell vs Rockford','Cornell vs Fontbonne','Cornell vs Simpson','Cornell vs Nebraska Wesleyan','Cornell vs Central','Cornell vs Monmouth','Cornell vs Coe (away)','Cornell vs Ripon','Cornell vs Iowa Wesleyan','Cornell vs Grinnell','Cornell vs Illinois College','Cornell vs Lake Forest','Cornell vs Knox','Cornell vs Lawrence'])

def select():
    global team
    global year
    team = stringvar.get()
    year = stringvar2.get()
    root.destroy()


if __name__ == '__main__':
    teamlist = ['Cornell Mens Soccer','Joy AC','Joy U19','Joy LaMancha','Joy Tennessee Fainting','Joy Kaghani','Joy 06']

    root = Tk()
    frame = Frame(root)
    root.title('Welcome')
    frame.grid()
    label = Label()
    label.grid
    root.geometry('200x200')
    label = Label(root,text='Select Team').grid(row=0,column=0)
    stringvar = StringVar()
    stringvar.set('Team')
    stringvar2 = StringVar()
    stringvar2.set('Year')
    teammenu = OptionMenu(root,stringvar,*teamlist).grid(row=1,column=0)
    year = OptionMenu(root,stringvar2,*['2021','2022']).grid(row=2,column=0)
    mybutton = Button(root,text='Select', command=select).grid(row=3,column=0)
    root.mainloop()



    
    playerlist = ST.player_list(team,year)[0]

    matchlist = match_list(team,year)
    dfDict = STA.read_data(team,year)


    
    root = Tk()
    frame = Frame(root)
    root.title('Stat Tracker Analysis')
    frame.grid()
    root.geometry('500x500')

    ### TEAM STATS
    label = Label(root,text = 'Team Stats',font=("Arial", 25))
    label.grid(row=0,column=0)
    DropDownMenu(root,matchlist,'Choose Match',1,0)
    mybutton = Button(root,text='xG Report', command=xG_graphic).grid(row=2,column=0)
    mybutton = Button(root,text='Shot Charts', command=team_shot_chart).grid(row=2,column=1)

    ### PLAYER STATS
    label = Label(root,text = 'Player Stats',font=("Arial", 25))
    label.grid(row=3,column=0)
    DropDownMenu(root,playerlist,'Choose Player',4,0)
    DropDownMenu(root,matchlist,'Choose Match',4,1)
    mybutton = Button(root,text='Shot Chart', command=player_shot_chart).grid(row=5,column=0)
    mybutton = Button(root,text='Print df', command=print_player_df).grid(row=5,column=1)
    mybutton = Button(root,text='Player Progression', command=season_player_progression).grid(row=6,column=0)




    
    '''
    DropDownMenu(positionlist,'Choose Position',0,1)
    DropDownMenu(minuteslist,'Minimum Minutes',0,2)
    DropDownMenu(statheadings,'Choose Stat',1,0)
    DropDownMenu(statheadings,'Choose Stat',1,1)
    DropDownMenu(statheadings,'Choose Stat',1,2)
    DropDownMenu(statheadings,'Choose Stat',1,3)
    DropDownMenu(statheadings,'Choose Stat',1,4)
    DropDownMenu(playerlist,'Choose Second Player',0,3)

    '''
    root.mainloop()

    


#    playerlist = ['#2 Devan DiGrado','#3 Marco Corona Duran','#4 Noah Kantorowicz','#5 Vukota Mastilovic','#6 David Riera','#7 Zinedine Kroeten','#8 Aiden Cavanaugh','#9 Darley Florvil','#10 Whitney Browne','#11 Emmanuel Iwe','#12 Marshall Urban','#14 Philip Caputo','#15 Otis Anderson','#16 Xavier Zengue','#17 Denilson Ramos','#18 Dennis Mensah','#19 Mika Folstad','#20 Jorge Radilla','#21 Luis Martinez Rojas','#22 Dimitri Nair','#23 Liam Vance','#24 Martin Browne Jr','#27 Abduselam Regassa','#28 Gabriel Eduarte','#29 Diego Paulin','#1 Dawson Fairchild','#0 Tucker Mann','#30 Ayuub Ahmed','Andrei Gotsmanov','Siddiq Madson-Keita','Henry Elias']
#    playerlist = ['Opponent Player','Phil','Gabe','Henry','Mika','Luca','Siddiq','Bennett','Dimi','Andrew','Diego','Jack','Diego GK']
#    playerlist = ['Opponent Player','Wilton','Si','Luca','Jack','Eric','Johnny','Manny','Max','Liam']
#    playerlist = ['Opponent Player','Alanna','Dare','Allison','Iman','Riana','Sami','Aliviah','Sam','Ari','Caitlyn']  
#    playerlist = ['Adri','Henry','Michael','Victor','Elsini','Hassan','Oliver','Josiah','Noah','Sean','Isaiah','Carlitos','Yonas','Minoli','Gabe','Bennett','Sebe','Zekiah']
#    playerlist = ['Opponent Player','Nico', 'Tyler', 'Oliver', 'Isaiah', 'Will', 'Luca','Benji', 'Mikey', 'Kai', 'Eric', 'Makai', 'John', 'Leo', 'Lucas', 'Johnny','Jeremy'] 
