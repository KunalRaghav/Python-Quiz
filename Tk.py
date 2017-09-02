from Tkinter import *
import tkMessageBox
import os

def passcheck():
    cu=u.get()
    cp=p.get()
    ru='user'
    rp='123456'
    if cu!=ru or cp!=rp:
        tkMessageBox.showinfo('Invalid','Username or Password didn\'t match ')
    else:
        os.startfile('menu.py')
        root.destroy()
root=Tk()
root.resizable(0,0)
root.title("LogR")
#Username
ent=u=Entry(root,fg='black',bg='green',relief='flat',bd=1)
ent.place(x=150,y=10)
#password
ent2=p=Entry(root,show='*',fg='black',bg='green',relief='flat',bd=1)
ent2.place(x=150,y=40)
#labels
lbl=Label(root,text="Username",bg='black',fg='green', font=('Arial 10 bold')).place(x=10,y=10)
lbl2=Label(root,text="Password",bg='black',fg='green', font=('Arial 10 bold')).place(x=10,y=40)
bttn=Button(root,relief='flat',bd=1,text="Log In",fg="green",bg='black',activebackground='green',activeforeground='black',command=passcheck,font=('Arial 8 bold')).place(x=122,y=70)
#Configurations
root.geometry("300x115")
root.configure(background="black")
root.wm_iconbitmap("Logger.ico")
lbl3=Label(root,text="A KunalRaghav Product",bg='black',fg='green').place(x=155,y=95)


root.mainloop()



