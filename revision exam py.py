l=[]
 
longg=int(input(print('give the length of the list please')))
i=0
while i<longg:
   
    a=int(input(print('element',i)))
    if a==0 or a==1:
        l.append(a)
    i=i+1
            
print(l)
l1=[]
for i in range(longg):
    for j in range(i):
        l1.append(1)
        if l1 in l:
         break
print(l1)


           




    
    
    
            
   
    
 



    