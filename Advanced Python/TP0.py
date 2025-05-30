# partie1 :Exercice Python : Structures de Données Avancées
#Liste (list)

import numpy as np 
import random

nombres = np.random.randint(1, 101, 10)
print(nombres)

print(max(nombres))
print(min(nombres))

nombres_tries = np.sort(nombres)[::-1]
print(nombres_tries)

i= 9
nbr=np.array(nombres)
while i>=0:  
    if nombres[i] % 2 == 0:
        nbr=np.delete(nbr,i)
    i=i-1
print(nbr)

summ=0
for i in nbr:
    summ=summ+i**2

print(summ)

#Tableau (array)
tableau_1 = np.random.randint(1, 101, 10)
print(tableau_1)

tableau_2 = np.random.randint(1, 101, 10)
print(tableau_2)

tableau_sum = np.concatenate((tableau_1, tableau_2))
print(tableau_sum)
print(max(tableau_sum))


#Ensemble (set)
ensemble_1 = set(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10))
ensemble_2 = set(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10))

commun=ensemble_1.intersection(ensemble_2)
print(ensemble_1)
print(ensemble_2)

print(commun)

ensemble_3=set()
for x in ensemble_1 :
    if x not in ensemble_2 :
        ensemble_3.add(x)
print(ensemble_3)

#Dictionnaire (dict)

etudiants={"maryem":90,"refka":20,"nada":50,"chava":0,"dalel":10}


print(etudiants)
n=0
et=None

for i ,j in etudiants.items():
    if j>n:
        n=j
        et=i
print(et)    

moy=0
for i  in etudiants.values():
   moy=moy+i
print(moy/5)    

basse=100
eb=None
for i,j  in etudiants.items():
   if j<basse:
       basse=j
       eb=i


print(eb)
del(etudiants[eb])
print(etudiants)

##Partie II :
#Partie 1 : Listes et Tableaux
import numpy as np
nombres = np.random.randint(low=1, high=1001, size=100).tolist()
tableau = np.array(nombres)
print(nombres)

def tri_rapide(tab1):
    if len(tab1) <= 1:
        return tab1
    m = tab1[len(tab1) // 2]  # Utilisez // pour la division entière
    g = []
    d = []
    e = []

    for i in range(len(tab1)):
        if tab1[i] < m:
            g.append(tab1[i])
        elif m == tab1[i]:
            e.append(tab1[i])
        else:
            d.append(tab1[i])

    return tri_rapide(g) + e + tri_rapide(d)
def recherche_Binaire(liste,element):
  debut=0
  fin=len(liste)-1
  m=(debut+fin)//2
  while debut<fin:
    if liste[m]==element:
      return m;
    elif liste[m]>element:
      fin=m-1
    else:
      debut=m+1
      m=debut+fin
    return -1

tab = tri_rapide(tableau )
print(tab)
print("la médiane des nombres dans la liste triée : ",tab[len(tab)//2])
t=recherche_Binaire(nombres,5)
print(t)


#Partie 2 : Ensembles

ensemble_A = set(random.randint(1,501) for _ in range(10))
ensemble_B = set(random.randint(1,501) for _ in range(10))

print(ensemble_A)
print(ensemble_B)
ensemble_C=ensemble_A.intersection(ensemble_B)

ensemble_3=set()
for x in ensemble_A :
    if x not in ensemble_B :
        ensemble_3.add(x)
print(ensemble_3)

if ensemble_C== ensemble_B:
    print ("L'ensemble B est dans A ")
else:
    print('l\'ensemble B n\'est pas dans l\'ensemble A')


#Partie 3 : Dictionnaires:

dictionnaire_notes = {
    "salma": 85,
    "salem": 92,
    "sawsen": 78,
    "sirine": 49,
    "salim": 96,
    "salima": 88,
    "sinda": 70,
    "sofiane": 91,
    "samir": 45,
    "lousif": 89
}
print(dictionnaire_notes)
#calcule de moyenne :
moy=0

for n in dictionnaire_notes.values():
  moy=moy+n
moy=moy/10
print("la moyenne des notes des élèves :",moy)
#le nom de l'élève ayant la note la plus élevée
nm=0
em=None
for e,n in dictionnaire_notes.items():
  if n>nm:
    nm=n
    em=e
print("le nom de l'élève ayant la note la plus élevée :",em)
# les élèves ayant obtenu une note en dessous de la moyenne
elv_supp=[]
for e,n in dictionnaire_notes.items():
  if n<moy:
    elv_supp.append(e)
for e in elv_supp :
 del dictionnaire_notes[e]

print(dictionnaire_notes)

#Partie 4 : Challenge Supplémentaire
def factorielle(n):
  if(n==0 or n==1):
    return 1
  else :
    return (n*factorielle(n-1))
print("(factorielle(1)=",factorielle(1))
print("(factorielle(5)=",factorielle(5))

def nombreCombinaison(n,k):
  if k == 0 or k == n:
        return 1
  else:
    return nombreCombinaison(n-1,k-1)+nombreCombinaison(n-1,k)
print("le nombre de façons différentes de choisir 5 éléments parmi les 10 éléments de nombres : ",nombreCombinaison(10,5))
