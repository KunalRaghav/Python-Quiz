from Tkinter import *


def rais_fra(frame):
    frame.tkraise()

root = Tk()
root.resizable(0,0)
root.config(bg='green')
####parts of screen
#titlebar
f0=Frame(root,bg='green')
f0.pack()
Label(f0,text='QUIZ',bg='green',fg='black',font=('Arial 80 bold')).pack()
#maingame
c1=Canvas(root,bg='black')
c1.pack()
#productthanks
f1=Frame(root,bg='green')
f1.pack()
Label(f1,text='A KunalRaghav Product',bg='green',fg='black',font=('Arial 10 bold')).pack()
####frames
f2=Frame(c1,bg='black')
f2.grid(row=0,column=0,stick='nsew')
f3=Frame(c1,bg='black')
f3.grid(row=0,column=0,stick='nsew')
f4=Frame(c1,bg='black')
f4.grid(row=0,column=0,stick='nsew')
f5=Frame(c1,bg='black')
f5.grid(row=0,column=0,stick='nsew')
f6=Frame(c1,bg='black')
f6.grid(row=0,column=0,stick='nsew')
f7=Frame(c1,bg='black')
f7.grid(row=0,column=0,stick='nsew')
f8=Frame(c1,bg='black')
f8.grid(row=0,column=0,stick='nsew')
###welcome
wel=Label(f2,text='''WELCOME!!
START QUIZ''',fg='green',bg='black',font=('Arial 65 bold'),pady=55)
wel.pack()
Button(f2,text='START',bd=0,bg='green',font=('Arial 30 bold'),fg='black',relief='flat',activebackground='black',activeforeground='green',command=lambda: rais_fra(f3)).pack(side=BOTTOM)
###question1
q1=Label(f3,text='''Arrange the following elements in order of their
increasing ionization energies O, S, Se,Te, Po
''',fg='green',bg='black',font=('Arial 35 bold'))
q1.pack()
Button(f3,text='(a) Po,Te,Se,S,O',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f4)).pack()
Button(f3,text='(B)Se, Te, S, Po, O',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f3,text='(C) O, S, Se, Te, Po',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f3,text='(D)Te, O, S, Po, Se',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
##question2
q2=Label(f4,text='''The speeds of sound in air and sea-water are
given to be 340 m/s and 1440 m/s. resp. A ship sends a strong Signal
straight down and detects its echo after 1.5 secs. The depth
of the sea at that point is''',fg='green',bg='black',font=('Arial 30 bold'))
q2.pack()
Button(f4,text='(A)0.51 kms ',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f4,text='(B)2.16 kms',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f4,text='(c)1.08 kms',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f5)).pack()
Button(f4,text='(D)0.255 kms',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
##question3
q3=Label(f5,text='''The sum of all two digit numbers each of
which leaves remainder 3 when divided by 5 is''',fg='green',bg='black',font=('Arial 30 bold'))
q3.pack()
Button(f5,text='(A)1064',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f5,text='(B) 952',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f5,text='(C)1120',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f5,text='''(d) 999''',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f6)).pack()
##question4
q4=Label(f6,text='''Wings of birds and insects are''',fg='green',bg='black',font=('Arial 45 bold'))
q4.pack()
Button(f6,text='(A) Homologous organs',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f6,text='(b) Analogous organs',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f8)).pack()
Button(f6,text='(C) Paralogous organs',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
Button(f6,text='(D) vestigial organs',bd=0,fg='green',font=('Arial 30 bold'),bg='black',relief='flat',activebackground='green',activeforeground='black',command=lambda: rais_fra(f7)).pack()
##lose_screen
lose=Label(f7,pady=65,text='''You Lose''',fg='green',bg='black',font=('Arial 65 bold'))
lose.pack()
Button(f7,text='RESTART',bd=0,bg='green',font=('Arial 30 bold'),fg='black',relief='flat',activebackground='black',activeforeground='green',command=lambda: rais_fra(f2)).pack(side=BOTTOM)
##congo
congo=Label(f8,text='''Congratulations''',fg='green',bg='black',font=('Arial 65 bold'))
congo.pack()
Button(f8,text='Wanna Play Again??',bd=0,bg='green',font=('Arial 30 bold'),fg='black',relief='flat',activebackground='black',activeforeground='green',command=lambda: rais_fra(f2)).pack(side=BOTTOM)
rais_fra(f2)
root.title('Quiz')
root.wm_iconbitmap("LoggeR.ico")
root.mainloop()
