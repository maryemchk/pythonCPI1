def lireliste(n):
    l=[]
    for i in range(n):
        print('donner l element numero ',i+1)
        l.append(input())
    print(l)
    return(l)

def sousliste(l1,l2):
    l3=[]
    
    for i in range(len(l1)):
            for j in range(len(l2)):
                if l2[j]==l1[i]:
                     l3.append(l2[j])
               
    if len(l2)==len(l3):
        return(True)
    else:
        return(False)
while True :
    b=int(input('donner la longueur de la liste 1='))
    liste1=lireliste(b)
    c=int(input('donner la longueur de la liste 2='))
    liste2=lireliste(c)
    if len(liste2)<len(liste1):
        break


a=sousliste(liste1,liste2)
print(a)
if a==True :
    print('la liste 2 existe dans la liste 1')
else: 
    print('laliste 2 n existe pas dans la liste 1')