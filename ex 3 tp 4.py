def verifierADN(ch):
        for i in range(len(ch)):
            if ch[i]=="a" or ch[i]=="t" or ch[i]=="c" or ch[i]=="g":
                return(True)
            else:
                return(False)



def saisirADN():
    while True :
        ch=input('donner une chaine  d ADN')
        if verifierADN(ch)==True:
            break
    return(ch)
        
def remplirlist():
    adns=[]
    adns=int(input('donner le nombre des chaines d ADN'))
    return(adns)

def creerdico(a,ch):
    d=dict()
    n=0
    for i in range (len(ch)):
        if ch[i]==a:
            n=n+1
            d[a]=n
    return(d)


l=["atcgta","cct","accc","agc"]
print(l)
c=input('donner une lettre=')
ch=str(l)
print(creerdico(c,ch))


    




   
