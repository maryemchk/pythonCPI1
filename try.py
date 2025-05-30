especes=["virginica","setosa","versicolor"]
print(type(especes))
print(especes)
print(especes[0])
print(especes[2])
print(len(especes))
#largeur et longeur des sépales et des pétales
sepal=[0.45,12.3]
print(sepal)
petal=[1.45,14.5]
print(petal)
#les attributs de iris
iris=sepal+petal 
print(iris)
iris.append(especes[1])
print(iris)
#initialisation d'une liste vide
a=[]
a=a+[6]
print(a)
3
a.append(8)
print(a)
#ATTENTION : indices positifs et négatifs d'une liste
scores=[45,62,25,75,99,87,12,15,56,68]
print(len(scores))
scores[0] 
scores[5]
scores[len(scores)-1]
print(scores)
print(scores[len(scores)-1],scores[-1])
print(scores[len(scores)-2],scores[-2])
print(scores[len(scores)-3],scores[-3]) #!!!!!!!!!!
print(scores[0],scores[-len(scores)]) 
print(25 in scores)
print(71 in scores)
print(scores!=[])
print([1,2,3]==[1,2,3])
print(max(scores),min(scores),sum(scores)/len(scores))