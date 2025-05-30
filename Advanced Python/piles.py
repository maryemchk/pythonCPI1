pile=[0,1,2,3,4,5]


def est_vide(p):
    return len(p)==0

def depiler(p):
    if not est_vide(p):
        return p.pop()
    else:
        print("La pile est vide")

def sommet(p):
    if not est_vide(p):
        return p[-1]
    else:
        print("La pile est vide")

def empiler(p,x):
    p.append(x)
   
def longueur(p):
    return len(p)


      
   
print("la pile est vide :",est_vide(pile))
depiler(pile)
print(pile)
print("la sommet de la pile :",sommet(pile))
empiler(pile,9)
print(pile)
print("la longueur de la pile :",longueur(pile))
        

 




