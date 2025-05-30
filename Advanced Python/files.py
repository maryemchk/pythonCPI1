file =[1,2,3,4,5,6,7]

def est_vide(f):
    return len(f)==0

def defiler(f):
    if not est_vide(f):
        element=f.pop(0)
        print("L'element enlevé est :",element)
    else:
        print("La file est vide")

def sommet(f):
    if not est_vide(f):
        return f[len(f)-1]

def enfiler(f,x):
    if not est_vide(f):
        f.append(x)
    
defiler(file)