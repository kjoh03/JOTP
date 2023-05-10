from tkinter import *
import tkinter as tk
import StatTracker as ST
from datetime import datetime
import matplotlib.pyplot as plt
import math

### TEST, DOES NOT WORK

class StatTrackerapp(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        container = Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in (StartPage,PageOne):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
#        label = Label(self,text = 'Home')
#        label.pack(pady = 10, padx = 10)
        button1 = Button(self,text = 'Enter',command=run_stat_tracker_)#lambda:controller.show_frame(PageOne))
        button1.pack()

class PageOne(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        label = Label(self,text = 'Page 1')
        label.pack(pady = 10, padx = 10)
        button1 = Button(self,text = 'Return',command=lambda:controller.show_frame(StartPage))
        button1.pack()

def run_stat_tracker_():
#    Event()
    fig,ax = ST.draw_soccer_pitch()
    cid = fig.canvas.mpl_connect('button_press_event', lambda:ST.onclick)
    timer = fig.canvas.new_timer(interval=1000)
    timer.add_callback(ST.update_title, ax)
    timer.start()
    plt.show()

        
app = StatTrackerapp()
app.mainloop()
