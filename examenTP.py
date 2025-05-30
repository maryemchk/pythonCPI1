


def miniscule(ch):

    for i in range(len(ch)):
        if(ord(ch[i]) >= 65 and ord(ch[i]) <= 90):
            s=ord(ch[i])+32
            ch[i]=chr(s)
    return(ch)


def crypto(ch):
    for i in range (len(ch)):
        if ch[i]=='z':
            ch[i]='A'
        elif ch[i]=='y':
            ch[i]='B'
         
        elif ch[i]=='z':
            ch[i]='C'
        else:
            ch[i]=chr(ord(ch[i])+3)
        return(ch)

def crypto_n(ch,n):
    for i in range (len(ch)):
        if ch[i]=='z':
            ch[i]=chr(ord('A')+n)
        elif ch[i]=='y':
            ch[i]=chr(ord('B')+n)
         
        elif ch[i]=='z':
            ch[i]=chr(ord('C')+n)
        else:
            ch[i]=chr(ord(ch[i])+n)
        return(ch)
         
def occurence(ch,ctr):
    somme=0
    for i in range(ch):
        if ctr in ch:
            somme=somme+1
    return(somme)





ch=input(print('donner une chaine en miniscule'))  
print(miniscule(ch))
print(crypto(ch))
n=int(input('donner un entier'))
print(crypto_n(ch,n))
c=input(print('donner un caractere'))
print(occurence(ch,c))

    