while True:
    l=int(input(print('give the length of the list')))
    if l>0:
        break
lp=[]
ln=[]
for i in range(0,l):
    n=int(input(print('give a number')))
    if n>0:
        lp.append(n)
    elif n<=0:
        ln.append(n)

print(lp)
print(ln)
l1=[]
for i in range(0,len(lp)):

    l1.append(lp[i]**2)
print(l1)
l2=l1+ln
print(l2)


