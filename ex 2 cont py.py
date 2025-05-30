n=int(input(print('give a number n please')))
while True:
    num=int(input(print('give a number of ',n,'please')))
    strr=str(input(print('give a string of length',n,'please')))
    if len(strr)==n and len(str(num))==n:
        break
print(num,strr)
liste=list(str(num))

liste2=list(strr)
print(liste)
print(liste2)
k=[]
for i in range(n):
    k.append(int(liste[i]))
    k.append(liste2[i])
print(k)




