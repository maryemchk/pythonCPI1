def somdiv(n):
    s=0
    for i in range(1,n):
        if n %i==0:
            s=s+i
    return(s)

def estparfait(l):
    if somdiv(l)==l:
        return(True)
    else:
        return(False)
        
def estpremier(n):
    if somdiv(n)==1:
        return(True)
    else:
        return(False)
def estchanceux(a,n):

    if estpremier(a+n+n**2)==True:
        return (True)
    else:
        return(False)
parfaits=[]
chanceux=[]

for i in range(2,1001):
    if estparfait(i)==True:
        parfaits.append(i)
    elif estchanceux(i,100)==True:
        chanceux.append(i)

print('the list of perfect numbers=',parfaits)
print('the list of lucky numbers=',chanceux)





    
    


    