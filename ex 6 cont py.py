ch=input(print('give a string aman'))
liste=list(ch)
print(liste)
l1=[]
for i in range(0,len(ch)):
    n=liste.count(ch[i])
    if (n==1):
        l1.append((len(ch)+1))
    else:
        l1.append(n)

print(l1)
a=min(l1)
p=l1.index(a)
if a!=(len(ch)+1):
    print(liste[p])
else:
    print("n'existe pas")


























   



