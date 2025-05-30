from timeit import repeat


equipe1=str(input(print('give the name of the first team')))
equipe2=str(input(print('give the name of the second team')))
lstbuts=[]
n=int(input(print("if the number of buts =0 enter 0 else enter the number of buts")))
if n==0:
    print('the match ended 0_0 for both teams')
else:
    for i in range(n):
        tg=str(input(print('enter the team who shoot a goal')))
        lstbuts.append(tg)
print(lstbuts)
j=0
for i in range(0,n):
    if equipe1==lstbuts[i]:
        j+=1
    
if (n-j==j):
    print('equals')
elif n-j<j:
    print(equipe1)
else:
    print(equipe2)

    

