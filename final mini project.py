from cProfile import label
from optparse import Values
from select import select
from tkinter import ttk
from tkinter import *

def open():
    
    
    top=Toplevel()
    
    top.title('YOUR CINEMA TICKET')
    top.config(background='#FFFFF0')
    top.geometry("400x400")
    Label(top,text='><YOUR TICKET ><',font=("Courier", 16, "italic"),bg='#FFFFF0').pack(expand=True)
    Label(top,text='your movie is :'+mycombo.get(),bg='#FFFFF0',font=("Roman", 11)).pack(expand=True)
    Label(top,text='the date of the movie projection:\n'+date.get(),bg='#FFFFF0',font=("Roman", 11)).pack(expand=True)
    Label(top,text='the place you chose:\n'+ a.get(),bg='#FFFFF0',font=("Roman", 11)).pack(expand=True)
    if r.get()=='student':
        Label(top,text='YEEEY!,you got a reduction of 30%',bg='#FFFFF0',font=("Roman", 11)).pack(expand=True)
    else:
        Label(top,text=s.get()+' tickets\n(PRICE:7dt per ticket) ',bg='#FFFFF0',font=("Roman", 11)).pack(expand=True)
    
    Label(top,text='the number of tickests= '+s.get(),bg='#FFFFF0',font=("Roman", 11)).pack(expand=True)
    Label(top,text='ENJOY THE SHOW ;)',font=("Roman", 11),bg='#FFFFF0').pack(side=LEFT)
    Button(top,text='DONE',command=quit,fg='#8B2323',bg='#CDC8B1').pack(expand=True)
    



 


window = Tk()
window.title("salle de cinema")
window.config(background='#FFFFF0')
window.geometry("400x400")
window.iconbitmap('C:/Users/21655/Desktop/python/cinee.ico')
mylabel1=Label(window,text='><WELCOME><',font=("Courier", 16, "italic"),bg='#FFFFF0',anchor=CENTER).pack(expand=True)
mylabel2=Label(window,text='select your movie:',font=("Roman", 11),bg='#FFFFF0').pack(expand=True)



l=["spiderman","ex-machina","omar","3000 nights","dachra","beauty and the beast ","A.I","intresteller","rescue dawn","joker","paterson","nightingale","dune","gravity","mad max"]


mycombo=ttk.Combobox(window,value=l,background='#FFFFF0')
mycombo.current()
mycombo.insert(0,'select a movie')


mycombo.pack(expand=True)


date_label=Label(window,text='enter the date please',font=("Roman", 11),bg='#FFFFF0')
date_label.pack()

date=Entry()
date.get()
date.insert(0,'dd/mm/yyyy')
date.pack()
a=StringVar()
a.get()
mylabel1=Label(window,text='select your position please:',font=("Roman", 11),bg='#FFFFF0').pack(expand=True)
Radiobutton(window,text='in the middle',variable=a,value='middle',bg='#FFFFF0').pack(expand=True)
Radiobutton(window,text='on the left  ',variable=a,value='on the left ',bg='#FFFFF0').pack(expand=True)
Radiobutton(window,text='on the right ',variable=a,value='on the right',bg='#FFFFF0').pack(expand=True)
Radiobutton(window,text='in the back  ',variable=a,value='in the back',bg='#FFFFF0').pack(expand=True)

mylabel2=Label(window,text='select your state please:',font=("Roman", 11),bg='#FFFFF0').pack(expand=True)

r= StringVar()
r.get()
Radiobutton(window,text='student',variable=r,value='student',bg='#FFFFF0').pack(expand=True)
Radiobutton(window,text='not a student ',variable=r,value='not student',bg='#FFFFF0').pack(expand=True)

mylabelbill=Label(window,text='enter the number of tickets please:',font=("Roman", 11),bg='#FFFFF0').pack(expand=True)
s = Spinbox(window, from_=0, to=10)
s.get()
s.pack()


mybutton=Button(window,text='quit',command=quit,fg='#8B2323',bg='#CDC8B1')
mybutton.pack()
mybutton=Button(window,text='validate',fg='#8B2323',bg='#CDC8B1',command=open)
mybutton.pack()


window.mainloop()

    












