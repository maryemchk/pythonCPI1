from msilib.schema import RadioButton
from tkinter import *
window=Tk()
def facture():
    mylabel=Label(window,text='YOUR TICKET  =',bg='#FFFFF0')

    mylabel.grid()
    mylabelc=Label(window,text=a.get(),bg='#FFFFF0')
    mylabelb=Label(window,text=r.get(),bg='#FFFFF0')
    mylabeld=Label(window,text=s.get(),bg='#FFFFF0')
    
    
    mylabelc.grid()
    mylabelb.grid()
    mylabeld.grid()

l=["spiderman","ex-machina","omar","3000 nights","dachra","beauty and the beast ","A.I","intresteller","rescue dawn","joker","paterson","nightingale","dune","grevity","mad max"]
scrollbar = Scrollbar(window)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(window, yscrollcommand = scrollbar.set )
for line in range(len(l)):
   mylist.insert(END, l[line])

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )





window.title("salle de cinema")
window.config(background='#FFFFF0')
window.geometry("360x480")
window.iconbitmap('.\Desktop\pyth-cpi1\cinee.ico')

    

mylabel1=Label(window,text='WELCOME!',bg='#FFFFF0').grid(row=17,column=0)


mylabelcc=Label(window,text='select your position please:',bg='#FFFFF0').grid(row=18,column=0)

a=StringVar()
a.get()

Radiobutton(window,text='in the middle',variable=a,value='middle',bg='#FFFFF0').grid()
Radiobutton(window,text='on the left  ',variable=a,value='on the left ',bg='#FFFFF0').grid()
Radiobutton(window,text='on the right ',variable=a,value='on the right',bg='#FFFFF0').grid()
Radiobutton(window,text='in the back  ',variable=a,value='in the back',bg='#FFFFF0').grid()

mylabel2=Label(window,text='select your state please:',bg='#FFFFF0').grid(row=6,column=0)

r= StringVar()

r.get()

Radiobutton(window,text='student',variable=r,value='student',bg='#FFFFF0').grid()
Radiobutton(window,text='not a student ',variable=r,value='not student',bg='#FFFFF0').grid()

mylabelbill=Label(window,text='enter the number of tickets please:',bg='#FFFFF0').grid(row=29,column=0)
s = Spinbox(window, from_=0, to=10)
s.get()
s.grid()



mybutton=Button(window,text='quit',command=quit,fg='#8B2323',bg='#CDC8B1')
mybutton.grid()
mybutton=Button(window,text='valider',command=facture,fg='#8B2323',bg='#CDC8B1')
mybutton.grid()

 




window.mainloop()

