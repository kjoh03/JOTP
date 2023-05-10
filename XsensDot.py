import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
import glob
import os
import pwd
import math
import csv

class DropDownMenu:
    def __init__(self,root,dropdownlist,defaultoption,rownumber=0,columnnumber=0):
        clicked = StringVar()
        clicked.set(defaultoption)
        self.clicked = clicked
        drop = OptionMenu(root,self.clicked,*dropdownlist).grid(row=rownumber,column=columnnumber)

def event_list():
    directory = '/Users/'+pwd.getpwuid(os.getuid())[0]+'/Desktop/XsensData'
    os.chdir(directory)
    lis = next(os.walk('.'))[1]
    return lis

def player_list(event):
    directory = '/Users/'+pwd.getpwuid(os.getuid())[0]+'/Desktop/XsensData/'+event
    os.chdir(directory)

    lis = glob.glob('*.csv')
    for i in range(len(lis)):
        lis[i] = lis[i].split('.')[0]
    return lis

def select():
    global event
    event = stringvar.get()
    root1.destroy()

def event_dict(event,playerlist):
    PlayerDict = {}
    for player in playerlist:
        PlayerDict[player] = pd.read_csv('/Users/'+pwd.getpwuid(os.getuid())[0]+'/Desktop/XsensData/'+event+'/'+player+'.csv',skiprows = 11)
        accelscalar = []
        for i in range(len(PlayerDict[player][PlayerDict[player].columns[5]].tolist())):
            accelscalar.append(math.sqrt(PlayerDict[player][PlayerDict[player].columns[5]].tolist()[i]**2+PlayerDict[player][PlayerDict[player].columns[6]].tolist()[i]**2+PlayerDict[player][PlayerDict[player].columns[7]].tolist()[i]**2))
        PlayerDict[player + ' Accel Scalar List'] = accelscalar
        average = sum(PlayerDict[player + ' Accel Scalar List'])/len(PlayerDict[player + ' Accel Scalar List'])
        PlayerDict[player+' Average Acceleration'] = average
        PlayerDict[player+ 'Max Acceleration'] = max(PlayerDict[player + ' Accel Scalar List'])        
        print(player+'`s data complete....')
    return PlayerDict

def plot_accel_scalar():
    if root.grid_slaves(row=0,column=0)[0]['text'] == 'All Players':
        for player in playerlist:
            plt.plot(PlayerDict[player + ' Accel Scalar List'],label = player)
    else:
        plt.plot(PlayerDict[root.grid_slaves(row=0,column=0)[0]['text'] + ' Accel Scalar List'],label = root.grid_slaves(row=0,column=0)[0]['text'])
    plt.legend(loc="upper left")
    plt.show()

def plot_accel_components():
    if root.grid_slaves(row=0,column=0)[0]['text'] == 'All Players':
        for player in playerlist:
            plt.plot(PlayerDict[player][PlayerDict[player].columns[5]].tolist(),label = player+' X Component')
            plt.plot(PlayerDict[player][PlayerDict[player].columns[6]].tolist(),label = player+' Y Component')
            plt.plot(PlayerDict[player][PlayerDict[player].columns[7]].tolist(),label = player+' Z Component')
    else:
        player = root.grid_slaves(row=0,column=0)[0]['text']
        plt.plot(PlayerDict[player][PlayerDict[player].columns[5]].tolist(),label = player+' X Component')
        plt.plot(PlayerDict[player][PlayerDict[player].columns[6]].tolist(),label = player+' Y Component')
        plt.plot(PlayerDict[player][PlayerDict[player].columns[7]].tolist(),label = player+' Z Component')
        plt.legend()#loc="upper left")
    plt.show()

def print_important_stats():
    for player in playerlist:
        print(player+'`s average acceleration: '+str(round(PlayerDict[player+' Average Acceleration'],2))+' m/s^2')
        print(player+'`s max acceleration: '+str(round(PlayerDict[player+ 'Max Acceleration'],2))+' m/s^2')


if __name__ == '__main__':
    eventlist = event_list()

    root1 = Tk()
    frame = Frame(root1)
    root1.title('Welcome')
    frame.grid()
    label = Label()
    label.grid
    root1.geometry('200x200')
    label = Label(root1,text='Select Event').pack()
    stringvar = StringVar()
    stringvar.set('Event')
    teammenu = OptionMenu(root1,stringvar,*eventlist).pack()
    mybutton = Button(root1,text='Select', command=select).pack()
    root1.mainloop()
    
    print('Loading... (May take some time to crunch data)')    
    playerlist = player_list(event)
    PlayerDict = event_dict(event,playerlist)

    root = Tk()
    frame = Frame(root)
    root.title(event)
    frame.grid()
    root.geometry('500x500')

    DropDownMenu(root,['All Players']+playerlist,'All Players',0,0)
    mybutton = Button(root,text='Accel. Scalar', command=plot_accel_scalar).grid(row=1,column=0)
    mybutton = Button(root,text='Accel. Components', command=plot_accel_components).grid(row=2,column=0)
    mybutton = Button(root,text='Important Stats', command=print_important_stats).grid(row=3,column=0)


    '''
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





    '''   
    df = pd.read_csv('/Users/'+pwd.getpwuid(os.getuid())[0]+'/Desktop/XsensData/20220127_Kean+Welke/Kean.csv', skiprows = 7)
    df2 = pd.read_csv('/Users/'+pwd.getpwuid(os.getuid())[0]+'/Desktop/XsensData/20220127_Kean+Welke/Welke.csv', skiprows = 7)
#    plt.plot(df['Acc_X'].tolist(),label = 'Kean')
#    plt.plot(df['Acc_Y'].tolist())
#    plt.plot(df['Acc_Z'].tolist())
    
    accelscalarkean = []
    accelscalarwelke = []
    for i in range(len(df['Acc_X'].tolist())):
        accelscalarkean.append(math.sqrt(df['Acc_X'].tolist()[i]**2+df['Acc_Y'].tolist()[i]**2+df['Acc_Z'].tolist()[i]**2))
        accelscalarwelke.append(math.sqrt(df2['Acc_X'].tolist()[i]**2+df2['Acc_Y'].tolist()[i]**2+df2['Acc_Z'].tolist()[i]**2))

    averageaccelkean = sum(accelscalarkean)/len(accelscalarkean)
    averageaccelwelke = sum(accelscalarwelke)/len(accelscalarwelke)
    print(averageaccelkean)
    print(max(accelscalarkean))
    print(averageaccelwelke)
    print(max(accelscalarwelke))

    
#    plt.plot(df2['Acc_X'].tolist(), Label = 'Welke')
    plt.plot(accelscalarkean,label='Kean')
    plt.plot(accelscalarwelke,label='Welke')

    plt.legend(loc="upper left")
    plt.show()

#    print((sum(df['FreeAcc_X'].tolist()))/(len(df['FreeAcc_X'].tolist())))
#    print(len(df['FreeAcc_X'].tolist()))

    lis1 = []
    for ele in df['FreeAcc_X'].tolist():
        lis1.append(abs(ele))

    lis2 = []
    for ele in df['FreeAcc_Y'].tolist():
        lis2.append(abs(ele))

    lis3 = []
    for ele in df['FreeAcc_Z'].tolist():
        lis3.append(abs(ele))

    print(sum(lis1)/len(lis1))
    print(sum(lis2)/len(lis2))
    print(sum(lis3)/len(lis3))

    
    plt.plot(lis1)
#    plt.plot(lis2)
#    plt.plot(lis3)
    plt.show()
    '''

'''

averageaccellucas = sum(accelscalarlucas)/len(accelscalarlucas)
averageacceljeremy = sum(accelscalarjeremy)/len(accelscalarjeremy)
averageaccelhoyt = sum(accelscalarhoyt)/len(accelscalarhoyt)
averageaccelkean = sum(accelscalarkean)/len(accelscalarkean)

print(averageaccellucas)
print(max(accelscalarlucas))
print(averageacceljeremy)
print(max(accelscalarjeremy))
print(averageaccelhoyt)
print(max(accelscalarhoyt))
print(averageaccelkean)
print(max(accelscalarkean))

plt.plot(accelscalarlucas,label='Lucas')
plt.plot(accelscalarjeremy,label='Jeremy')
plt.plot(accelscalarhoyt,label='Hoyt')
plt.plot(accelscalarkean,label='Kean')
plt.legend(loc="upper left")
plt.show()

'''
