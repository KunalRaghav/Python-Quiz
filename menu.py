from tkinter import Tk,Frame,Button,Label,BOTTOM,mainloop
import os
menu=Tk()
frame=Frame()
frame.config(bg='black')
frame.grid(row=0,column=0)
frame1=Frame()
frame1.config(bg='black')
frame1.grid(row=1,column=0)
menu.resizable(0,0)
#button fuctions
class button:
    def __init__(self,menu,a,b,c,d):

        self=Button(menu,bg='green',font=('Arial 30 bold'),fg='black',text=a,relief='flat',activebackground='black',activeforeground='green',command=b,padx=25,pady=25,bd=0)
        self.grid(row=c,column=d)

#configurations
menu.title("Menu")
menu.wm_iconbitmap("Logger.ico")
menu.config(bg='black')
#Options
title=Label(frame,text='Menu',bg='black',fg='green',font=('Arial 60 bold'))
title.pack()
Quiz=button(frame1,'Quiz',lambda:os.startfile('quiz.py'),0,0)
Brick=button(frame1,'Brick Breaker','',1,1)
Label(frame1,text='''A KunalRaghav Product''',bg='black',fg='green',font=('Arial 18 bold')).grid(row=0,column=1)
Label(frame1,text='''More Games
Coming Soon ''',bg='black',fg='green',font=('Arial 17 bold')).grid(row=1,column=0)
mainloop()