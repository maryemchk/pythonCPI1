def entierpos3():
    while True :
        n=int(input('give a number '))
        if n>0 and len(str(n))==3:
            break
    return(n)


def armstrong(n):
    if (n //100)**3+((n%100)//10)**3+((n%100)%10)**3==n:
        return(True)
    else:
        return(False)

def listedarms():
    l=[]
    for i in range(100,1000):
         if armstrong(i)==True:
             l.append(i)
    return(l)

a=entierpos3()
print(armstrong(a))
print(listedarms())
            

    


