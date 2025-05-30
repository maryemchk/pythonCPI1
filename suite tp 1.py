from tkinter import *


# DEFINITIONS DES FONCTIONS

def boutonFourreTout():

    fenetre.destroy()

    return(0)


# CORPS PRINCIPAL DU PROGRAMME

fenetre = Tk()

fenetre.title("NOM DE VOTRE PROGRAMME")

fenetre.geometry("500x400")


bouRouge = Button(fenetre, text="FILE", fg="white", bg="red", command = boutonFourreTout)

bouVert = Button(fenetre, text="EDIT EDIT EDIT", fg="white", bg="green", command = boutonFourreTout)


# - - - - - C'est sur cette zone qu'on définit une Frame - - - -

zone2 = Frame(fenetre, bg='#777777')

bouBleua = Button(zone2, text="RUN", fg="white", bg="#BBBB55", command = boutonFourreTout)

bouBleub = Button(zone2, text="RUN", fg="white", bg='#BBBB77', command = boutonFourreTout)

bouBleuc = Button(zone2, text="RUN", fg="white", bg='#BBBB99', command = boutonFourreTout)


bouNoir = Button(fenetre, text="QUIT", fg="white", bg="black", command = boutonFourreTout)


bouRouge.pack(fill=X, ipady=10, padx=10,pady=10)

bouVert.pack(fill=X, ipady=20, padx=10,pady=10)


zone2.pack(fill=Y, padx=10,pady=10)

bouBleua.pack(side=LEFT, fill=Y, ipady=30, padx=10,pady=10)

bouBleub.pack(side=LEFT, fill=Y, ipady=30, padx=10,pady=10)

bouBleuc.pack(side=LEFT, fill=Y, ipady=30, padx=10,pady=10)


bouNoir.pack(fill=X, ipady=60, padx=10,pady=10)


fenetre.mainloop()



