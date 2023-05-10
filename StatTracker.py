import numpy as np
import pandas as pd
import os
import pwd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Slider, Button, RadioButtons
import math
from tkinter import *
import tkinter as tk
from datetime import datetime
from datetime import timedelta  

global starttime
starttime = datetime.now()

### FUTSAL
def draw_futsal_pitch(figsize=(9, 6.75)):
    rect = patches.Rectangle((-11, -38), 122, 92, linewidth=0.1,edgecolor='r', facecolor='tan', zorder=0)

    fig, ax = plt.subplots(1, figsize=figsize)
    ax.add_patch(rect)
    plt.plot([-10, -10, 10, 10, -10], 
            [0, 20, 20, 0, 0], color='white')
    plt.plot([-1.5, -1.5, 1.5, 1.5], 
            [0, -.9, -.9, 0], color='white')
    left_arc = patches.Arc([-1.5, 0], 9, 12, theta1=90, theta2=180, color='white')
    ax.add_patch(left_arc)
    right_arc = patches.Arc([1.5, 0], 9, 12, theta1=0, theta2=90, color='white')
    ax.add_patch(right_arc)
    plt.plot([-1.5, 1.5], 
            [6, 6], color='white')
    plt.plot([-.25, .25], 
            [10, 10], color='white')
    centre_circle = patches.Circle([0, 20], 3, edgecolor='white', facecolor='tan')
    ax.add_patch(centre_circle)
   
    plt.xlim(-11, 11)
    plt.ylim(21, -1)
    plt.axis('off')    

    return fig, ax
### FUTSAL END

def draw_soccer_pitch(figsize=(9, 6.75)):
    """
    Function that plots a scaled soccer pitch of length 120*90 metres which 
    are the maximum dimensions allowed by FIFAs "Laws Of The Game"
    """
    rect = patches.Rectangle((-38.5, -38.5), 122, 92, linewidth=0.1,edgecolor='r', facecolor='green', zorder=0)

    fig, ax = plt.subplots(1, figsize=figsize)
    ax.add_patch(rect)
    plt.plot([-3.66, -3.66], 
            [0, -5], color='white')
    plt.plot([3.66, 3.66],
            [0, -10], color='white')
    plt.plot([-37.5, -37.5, -37.5, 37.5, 37.5, -37.5], 
            [0, 0, 45, 45, 0, 0], color='white')
    plt.plot([-20.26, -20.26, 20.26, 20.26], 
            [0, 16.5, 16.5, 0], color='white')
    plt.plot([-9.26, -9.26, 9.26, 9.26], 
            [0, 5.5, 5.5, 0], color='white')

    plt.plot([-.5, .5],[10.97, 10.97], color='white')
    
    centre_circle = patches.Circle([0, 45], 10, edgecolor='white', facecolor='green')
    ax.add_patch(centre_circle)

    left_arc = patches.Arc([0, 10.97], 18.3, 18.3, theta1=37.5, theta2=142.5, color='white')
    ax.add_patch(left_arc)
    
    '''
    # Secondary pitch markings, ie penalty spots, centre circle etc
    
    centre_circle = patches.Circle([60, 45], 9.15, edgecolor='white', facecolor='darkgreen')
    ax.add_patch(centre_circle)
    
    left_arc = patches.Arc([16.5, 45], 9.15, 16, theta1=270.0, theta2=90.0, color='white')
    ax.add_patch(left_arc)
    right_arc = patches.Arc([103.5, 45], 9.15, 16, theta1=90.0, theta2=270.0, color='white')
    ax.add_patch(right_arc)

    bl_corner = patches.Arc([0, 0], 2.5, 2.5, theta1=0.0, theta2=90.0, color='white')
    tl_corner = patches.Arc([0, 90], 2.5, 2.5, theta1=270.0, color='white')
    br_corner = patches.Arc([120, 0], 2.5, 2.5, theta1=90.0, theta2=180.0, color='white')
    tr_corner = patches.Arc([120, 90], 2.5, 2.5, theta1=180.0, theta2=270.0,color='white')
    ax.add_patch(bl_corner)
    ax.add_patch(tl_corner)
    ax.add_patch(br_corner)
    ax.add_patch(tr_corner)
    '''    
    plt.xlim(-38.5, 38.5)
    plt.ylim(46, -1)
    plt.axis('off')    
    return fig, ax

def select():
    global team1
    global half
    global year
    global opponent
    team1 = stringvar.get()
    half = stringvar2.get()
    year = stringvar3.get()
    opponent = root.grid_slaves(row=1,column=1)[0].get()
    global dfrow
    dfrow = []
    if half == '2nd Half':
        username = pwd.getpwuid(os.getuid())[0]
        df = pd.read_csv('/Users/'+username+'/Desktop/Stat Tracker/'+team1+'/'+year+'/'+team1+' vs '+opponent+'.csv')
        for index, rows in df.iterrows():
            my_list =[rows.Name, rows.Event, rows.Time,rows.x, rows.y, rows.xG, rows.Assist, rows.get('Shot Distance')]
            dfrow.append(my_list)
            print(dfrow)

    root.destroy()


def onclick(event):
    y, x = event.xdata, event.ydata     # awkwardly switched because I rotated the field
    circle = plt.Circle((event.xdata,event.ydata),.25,color='red') #.25 radius for outdoor
    ax.add_patch(circle)
    fig.canvas.draw()
#    xG_tracker_subplot(df,fig1,ax1)
    Event(x,y)

def xG_Calculator(x,y):
#    distance = math.sqrt(x**2+y**2)
    x = abs(x)
    goalconstant = (7.32/2)**2  #7.32 outdoor goal 3 indoor
    if goalconstant > x**2+y**2:
        theta = math.atan((7.32*x)/(x**2+y**2-goalconstant))+math.pi   #7.32 outdoor goal 3 indoor
    else:
        theta = math.atan((7.32*x)/(x**2+y**2-goalconstant))   #7.32 outdoor goal 3 indoor
    xG = 1/(1+math.exp(4.03-2.53*theta-.12*x-.11*x*theta+.0069*x**2))
    return xG

def shot_distance(x,y):
    distance = math.sqrt(x**2+y**2)
    return distance

'''
def xG_tracker_subplot(df,fig1,ax1):
    plt.close(fig1)
    fig1,ax1 = plt.subplots()
    index = []
    xG = []
    totalxG = 0
    for i in range(len(df.index)):
        index.append(i+1)
        totalxG += df.at[i,'xG']
        xG.append(totalxG)
    plt.scatter(index,xG)
    plt.show()
'''

class DropDownMenu:
    def __init__(self,root,dropdownlist,defaultoption,rownumber=0,columnnumber=0):
        clicked = StringVar()
        clicked.set(defaultoption)
        self.clicked = clicked
        drop = OptionMenu(root,self.clicked,*dropdownlist).grid(row=rownumber,column=columnnumber)

class Event:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.root = Tk()
        self.frame = Frame(self.root)
        self.root.title('Event')
        self.label = Label()
        self.label.grid
        self.root.geometry('200x150')
        DropDownMenu(self.root,playerlist,'Choose Player')
        DropDownMenu(self.root,['Goal','Shot','Penalty Goal','Penalty Miss'],'Choose Event',1,0)
        DropDownMenu(self.root,assistlist,'Who Assisted?',2,0)
        mybutton = Button(self.root,text='Save', command=self.save_event).grid(row=3,column=0)
        self.root.mainloop()
    '''
    def save_event(self):
        if self.root.grid_slaves(row=1,column=0)[0]['text'] == 'Penalty Goal' or self.root.grid_slaves(row=1,column=0)[0]['text'] == 'Penalty Miss':
            xG = 0.76
        else:
            xG = xG_Calculator(self.x,self.y)
        time = get_time()
        distance = shot_distance(self.x,self.y)
        dfrow.append([self.root.grid_slaves(row=0,column=0)[0]['text'],self.root.grid_slaves(row=1,column=0)[0]['text'],str(time).split(".")[0][-5:],self.x,self.y,round(xG,2),self.root.grid_slaves(row=2,column=0)[0]['text'],distance])
        df = pd.DataFrame(dfrow,columns = ['Name','Event','Time','x','y','xG','Assist','Shot Distance'])
        print(df)
        username = pwd.getpwuid(os.getuid())[0]
        df.to_csv('/Users/'+username+'/Desktop/Stat Tracker/'+team1+' Matches '+year+'/Match xG Dataframe.csv',index=False,header=True)
        self.root.destroy()
    '''
    def save_event(self):
        if self.root.grid_slaves(row=1,column=0)[0]['text'] == 'Penalty Goal' or self.root.grid_slaves(row=1,column=0)[0]['text'] == 'Penalty Miss':
            xG = 0.76
        else:
            xG = xG_Calculator(self.x,self.y)
        time = get_time()
        distance = shot_distance(self.x,self.y)
        dfrow.append([self.root.grid_slaves(row=0,column=0)[0]['text'],self.root.grid_slaves(row=1,column=0)[0]['text'],str(time).split(".")[0][-5:],self.x,self.y,round(xG,2),self.root.grid_slaves(row=2,column=0)[0]['text'],distance])
        df = pd.DataFrame(dfrow,columns = ['Name','Event','Time','x','y','xG','Assist','Shot Distance'])
        print(df)
        username = pwd.getpwuid(os.getuid())[0]
        df.to_csv('/Users/'+username+'/Desktop/Stat Tracker/'+team1+'/'+year+'/'+team1+' vs '+opponent+'.csv',index=False,header=True)
        self.root.destroy()

def update_title(axes):
    axes.set_title(str(datetime.now()-starttime).split(".")[0])
    axes.figure.canvas.draw()
    
def get_time():
    eventtime = datetime.now()
    if half == '2nd Half':
        gametime = eventtime - starttime + timedelta(minutes=45)
    else:
        gametime = eventtime - starttime
    print(gametime)
    return gametime
   
def player_list(team,year):
    if team == 'Joy AC':
        if year == '2022':
            playerlist = ['Opponent Player','#2 Vukota Mastilovic','#3 Marco Corona Duran','#4 Noah Kantorowicz','#6 Martin Browne Jr','#8 Philip Caputo','#10 Whitney Browne','#11 Bennett Kouame','#12 Marshall Urban','#13 Luca Guarin','#14 Brian Kallman','#18 Dimitri Nair','#19 Mika Folstad','#22 David Riera','#24 Zinedine Kroeten','#28 Simeon Friesen','#29 Gabriel Eduarte','Henry Elias','Diego Paulin','Griffin Price','Jonathan Robles','#0 Tucker Mann','#1 Gage Steiner']
            assistlist = ['Unassisted','Opponent Player','#2 Vukota Mastilovic','#3 Marco Corona Duran','#4, Noah Kantorowicz','#6 Martin Browne Jr','#8 Philip Caputo','#10 Whitney Browne','#11 Bennett Kouame','#12 Marshall Urban','#13 Luca Guarin','#14 Brian Kallman','#18 Dimitri Nair','#19 Mika Folstad','#22 David Riera','#24 Zinedine Kroeten','#28 Simeon Friesen','#29 Gabriel Eduarte','Henry Elias','Diego Paulin','Griffin Price','Jonathan Robles','#0 Tucker Mann','#1 Gage Steiner']
        elif year == '2021':
            playerlist = ['Opponent Player','#2 Devan DiGrado','#3 Marco Corona Duran','#4 Noah Kantorowicz','#5 Vukota Mastilovic','#6 David Riera','#7 Zinedine Kroeten','#8 Aiden Cavanaugh','#9 Darley Florvil','#10 Whitney Browne','#11 Emmanuel Iwe','#12 Marshall Urban','#14 Philip Caputo','#15 Otis Anderson','#16 Xavier Zengue','#17 Denilson Ramos','#18 Dennis Mensah','#19 Mika Folstad','#20 Jorge Radilla','#21 Luis Martinez Rojas','#22 Dimitri Nair','#23 Liam Vance','#24 Martin Browne Jr','#27 Abduselam Regassa','#28 Gabriel Eduarte','#29 Diego Paulin','#1 Dawson Fairchild','#0 Tucker Mann','#30 Ayuub Ahmed','Andrei Gotsmanov','Siddiq Madson-Keita','Henry Elias']
            assistlist = ['Unassisted','Opponent Player','#2 Devan DiGrado','#3 Marco Corona Duran','#4 Noah Kantorowicz','#5 Vukota Mastilovic','#6 David Riera','#7 Zinedine Kroeten','#9 Darley Florvil','#10 Whitney Browne','#11 Emmanuel Iwe','#12 Marshall Urban','#14 Philip Caputo','#15 Otis Anderson','#16 Xavier Zengue','#18 Dennis Mensah','#19 Mika Folstad','#20 Jorge Radilla','#21 Luis Martinez Rojas','#22 Dimitri Nair','#23 Liam Vance','#24 Martin Browne Jr','#27 Abduselam Regassa','#28 Gabriel Eduarte','#29 Diego Paulin','#1 Dawson Fairchild','#0 Tucker Mann','#30 Ayuub Ahmed','Andrei Gotsmanov','Siddiq Madson-Keita','Henry Elias']
    elif team == 'Joy LaMancha':
        playerlist = ['Opponent Player','Phil','Gabe','Henry','Mika','Luca','Siddiq','Bennett','Dimi','Andrew','Diego','Jack','Diego GK']
        assistlist = ['Unassisted','Opponent Player','Phil','Gabe','Henry','Mika','Luca','Siddiq','Bennett','Dimi','Andrew','Diego','Jack','Diego GK']
    elif team == 'Joy U19':
        playerlist = ['Opponent Player','Adri','Henry','Michael','Phil','Mika','Victor','Elsini','Hassan','Oliver','Josiah','Noah','Sean','Isaiah','Carlitos','Yonas','Minoli','Gabe','Bennett','Sebe','Zekiah']
        assistlist = ['Unassisted','Opponent Player','Adri','Henry','Michael','Phil','Mika','Victor','Elsini','Hassan','Oliver','Josiah','Noah','Sean','Isaiah','Carlitos','Yonas','Minoli','Gabe','Bennett','Sebe','Zekiah']                 
    elif team == 'Joy Kaghani':
        playerlist = ['Opponent Player','Wilton','Si','Luca','Jack','Eric','Johnny','Manny','Max','Liam']
        assistlist = ['Unassisted','Opponent Player','Wilton','Si','Luca','Jack','Eric','Johnny','Manny','Max','Liam']
    elif team == 'Joy Tennessee Fainting':
        playerlist = ['Opponent Player','Alanna','Dare','Allison','Iman','Riana','Sami','Aliviah','Sam','Ari','Caitlyn']
        assistlist = ['Unassisted','Opponent Player','Alanna','Dare','Allison','Iman','Riana','Sami','Aliviah','Sam','Ari','Caitlyn']
    elif team == 'Joy 06':
        playerlist = ['Opponent Player','Nico', 'Tyler', 'Oliver', 'Isaiah', 'Will', 'Luca','Benji', 'Mikey', 'Kai', 'Eric', 'Makai', 'John', 'Leo', 'Lucas', 'Johnny','Jeremy'] 
        assistlist = ['Unassisted','Opponent Player','Nico', 'Tyler', 'Oliver', 'Isaiah', 'Will', 'Luca','Benji', 'Mikey', 'Kai', 'Eric', 'Makai', 'John', 'Leo', 'Lucas', 'Johnny','Jeremy'] 
    elif team == 'Cornell Mens Soccer':
        if year == '2021':
            playerlist = ['Opponent Player','#2 Gaurab Khadka','#3 Greg Pappadakis','#4 Emerson Roy','#5 Thomas Hamborg','#6 Drew Bruck','#7 Cian McNamara','#8 Nolan Zeger','#9 Aria Dehshid','#10 Owen Smith','#11 Andrew Lopez','#12 Galen Westervelt','#14 Sam Brueck','#15 Zach Miller','#16 Jonas Ricke','#17 Vance Wicker','#18 Mardoche Ntonku','#19 Justin Howe','#20 Brian Gin','#21 George Archer','#22 Blake Soto','#23 Bryce Scott','#24 Aron Mawia','#27 Federico Polidori','#28 Eddie Garces','#0 Will Bickel','#1 Jeremy Spina','#32 Mateo Ramirez']
            assistlist = ['Unassisted','Opponent Player','#2 Gaurab Khadka','#3 Greg Pappadakis','#4 Emerson Roy','#5 Thomas Hamborg','#6 Drew Bruck','#7 Cian McNamara','#8 Nolan Zeger','#9 Aria Dehshid','#10 Owen Smith','#11 Andrew Lopez','#12 Galen Westervelt','#14 Sam Brueck','#15 Zach Miller','#16 Jonas Ricke','#17 Vance Wicker','#18 Mardoche Ntonku','#19 Justin Howe','#20 Brian Gin','#21 George Archer','#22 Blake Soto','#23 Bryce Scott','#24 Aron Mawia','#27 Federico Polidori','#28 Eddie Garces','#0 Will Bickel','#1 Jeremy Spina','#32 Mateo Ramirez']
        elif year == '2022':
            playerlist = ['Opponent Player','#2 Gaurab Khadka','#3 Greg Pappadakis','#4 Emerson Roy','#5 Thomas Hamborg','#6 Drew Bruck','#7 Cian McNamara','#8 Nolan Zeger','#9 Mardoche Ntonku','#10 Owen Smith','#11 Andrew Lopez','#12 Galen Westervelt','#13 Zach Miller','#14 Sam Brueck','#15 Ian Schilling','#16 Jonas Ricke','#17 Vance Wicker','#18 Brenton Duboise','#19 Matthew Welton','#20 Blake Soto','#21 George Archer','#23 Bryce Scott','#24 Aron Mawia','#25 Lewis Page','#26 Edu Aldrete','#27 Aidan Lerch','#28 Eddie Garces','#0 Will Bickel','#1 Jeremy Spina','#41 Floris Huiskers']
            assistlist = ['Unassisted','Opponent Player','#2 Gaurab Khadka','#3 Greg Pappadakis','#4 Emerson Roy','#5 Thomas Hamborg','#6 Drew Bruck','#7 Cian McNamara','#8 Nolan Zeger','#9 Mardoche Ntonku','#10 Owen Smith','#11 Andrew Lopez','#12 Galen Westervelt','#13 Zach Miller','#14 Sam Brueck','#15 Ian Schilling','#16 Jonas Ricke','#17 Vance Wicker','#18 Brenton Duboise','#19 Matthew Welton','#20 Blake Soto','#21 George Archer','#23 Bryce Scott','#24 Aron Mawia','#25 Lewis Page','#26 Edu Aldrete','#27 Aidan Lerch','#28 Eddie Garces','#0 Will Bickel','#1 Jeremy Spina','#41 Floris Huiskers']
    return playerlist,assistlist



if __name__ == '__main__':
    teamlist = ['Cornell Mens Soccer','Joy AC','Joy U19','Joy LaMancha','Joy Tennessee Fainting','Joy Kaghani','Joy 06']
    yearlist = ['2021','2022']
    
    root = Tk()
    frame = Frame(root)
    root.title('Welcome')
    frame.grid()
    label = Label()
    label.grid
    root.geometry('200x200')
    label = Label(root,text='Select Team').grid(row=0,column=0)
    label = Label(root,text='Write Opponent').grid(row=0,column=1)
    stringvar = StringVar()
    stringvar.set('Team')
    stringvar2 = StringVar()
    stringvar2.set('Half')
    stringvar3 = StringVar()
    stringvar3.set('Year')
    text = Entry(root,bd = 5).grid(row=1,column=1)
    
    teammenu = OptionMenu(root,stringvar,*teamlist).grid(row=1,column=0)
    half = OptionMenu(root,stringvar2,*['1st Half','2nd Half']).grid(row=2,column=0)
    yearselect = OptionMenu(root,stringvar3,*yearlist).grid(row=3,column=0)
    mybutton = Button(root,text='Select', command=select).grid(row=5,column=0)
    root.mainloop()


    
    team = player_list(team1,year)
    playerlist = team[0]
    assistlist = team[1]

    Event()
#    fig,ax = draw_futsal_pitch()
    fig,ax = draw_soccer_pitch()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    timer = fig.canvas.new_timer(interval=1000)
    timer.add_callback(update_title, ax)
    timer.start()
    plt.show()



#    playerlist = ['Kean Johansen','Ted Kroeten','Hannah Wehrman','Lioul Minas','Andrei Gotsmanov']

#    playerlist = ['Opponent Player','Phil','Gabe','Henry','Mika','Luca','Siddiq','Bennett','Dimi','Andrew','Diego','Jack','Diego GK']
#    assistlist = ['Unassisted','Opponent Player','Phil','Gabe','Henry','Mika','Luca','Siddiq','Bennett','Dimi','Andrew','Diego','Jack','Diego GK']

#    playerlist = ['Opponent Player','Wilton','Si','Luca','Jack','Eric','Johnny','Manny','Max','Liam']
#    assistlist = ['Unassisted','Opponent Player','Wilton','Si','Luca','Jack','Eric','Johnny','Manny','Max','Liam']

#    playerlist = ['Opponent Player','Alanna','Dare','Allison','Iman','Riana','Sami','Aliviah','Sam','Ari','Caitlyn']
#    assistlist = ['Unassisted','Opponent Player','Alanna','Dare','Allison','Iman','Riana','Sami','Aliviah','Sam','Ari','Caitlyn']

#    playerlist = ['Opponent Player','#2 Devan DiGrado','#3 Marco Corona Duran','#4 Noah Kantorowicz','#5 Vukota Mastilovic','#6 David Riera','#7 Zinedine Kroeten','#8 Aiden Cavanaugh','#9 Darley Florvil','#10 Whitney Browne','#11 Emmanuel Iwe','#12 Marshall Urban','#14 Philip Caputo','#15 Otis Anderson','#16 Xavier Zengue','#17 Denilson Ramos','#18 Dennis Mensah','#19 Mika Folstad','#20 Jorge Radilla','#21 Luis Martinez Rojas','#22 Dimitri Nair','#23 Liam Vance','#24 Martin Browne Jr','#27 Abduselam Regassa','#28 Gabriel Eduarte','#29 Diego Paulin','#1 Dawson Fairchild','#0 Tucker Mann','#30 Ayuub Ahmed','Andrei Gotsmanov','Siddiq Madson-Keita','Henry Elias']
#    assistlist = ['Unassisted','Opponent Player','#2 Devan DiGrado','#3 Marco Corona Duran','#4 Noah Kantorowicz','#5 Vukota Mastilovic','#6 David Riera','#7 Zinedine Kroeten','#9 Darley Florvil','#10 Whitney Browne','#11 Emmanuel Iwe','#12 Marshall Urban','#14 Philip Caputo','#15 Otis Anderson','#16 Xavier Zengue','#18 Dennis Mensah','#19 Mika Folstad','#20 Jorge Radilla','#21 Luis Martinez Rojas','#22 Dimitri Nair','#23 Liam Vance','#24 Martin Browne Jr','#27 Abduselam Regassa','#28 Gabriel Eduarte','#29 Diego Paulin','#1 Dawson Fairchild','#0 Tucker Mann','#30 Ayuub Ahmed','Andrei Gotsmanov','Siddiq Madson-Keita','Henry Elias']

#    playerlist = ['Opponent Player','Adri','Henry','Michael','Victor','Elsini','Hassan','Oliver','Josiah','Noah','Sean','Isaiah','Carlitos','Yonas','Minoli','Gabe','Bennett','Sebe','Zekiah']
#    assistlist = ['Unassisted','Opponent Player','Adri','Henry','Michael','Victor','Elsini','Hassan','Oliver','Josiah','Noah','Sean','Isaiah','Carlitos','Yonas','Minoli','Gabe','Bennett','Sebe','Zekiah']                 

#    playerlist = ['Opponent Player','Nico', 'Tyler', 'Oliver', 'Isaiah', 'Will', 'Luca','Benji', 'Mikey', 'Kai', 'Eric', 'Makai', 'John', 'Leo', 'Lucas', 'Johnny','Jeremy'] 
#    assistlist = ['Unassisted','Opponent Player','Nico', 'Tyler', 'Oliver', 'Isaiah', 'Will', 'Luca','Benji', 'Mikey', 'Kai', 'Eric', 'Makai', 'John', 'Leo', 'Lucas', 'Johnny','Jeremy'] 


#    df = pd.DataFrame([[1,2,.8],[2,4,.6]],columns=['x','y','xG'])

#    xG_tracker_subplot(df)



