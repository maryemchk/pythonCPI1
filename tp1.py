print('ex1')
x=int(input("enter an integer please"))
y=int(input("enter a second integer please"))
aux=x
x=y
y=aux
print(x)
print(y)

x=float(input("enter a floating number please"))
y=float(input("enter a second floating number please"))
aux=x
x=y
y=aux
print(x)
print(y)

print('ex2')

from math import *
a=int(input("enter an integer please"))
f=int(input("enter a second integer please"))
print(sqrt(a*(1+(2/3)*pow((2*f/a),2))))
 
print('ex3')
 
a=int(input("how many hours u work a day?"))
b=int(input("how many years u v been working at this post ?"))
if b>=10:
    print("your salary per month=",a*25*30+35,"DT")
else :
    print("your salary per month=",a*25*30,"DT")

print('ex4')

age=int(input('enter your age please:'))
range1=(6,8)
range2=(8,10)
range3=(10,12)

if age in range1:
    print('poussin')
elif age in range2:
    print('pupille')
elif age in range3:
     print('minime')
elif age>12:
    print('cadet')
else :
    print('you won t get nothing :)')

print('ex5')

a=int(input("enter the first coef of the polynome"))
b=int(input("enter the second coef of the polynome"))
c=int(input("enter the third coef of the polynome"))
print('the polynome = '+str(a)+'x^2+'+str(b)+'x+'+str(c))
delta=pow(b,2)-4*a*c
if a==0:
    print('the unique solution =',-str(c)/str(b))
elif b==0 and (-c/a)>0:
    print ('solutions=',sqrt(-c/a),-sqrt(-c/a))
elif delta==0:
    print ('the unique solution =',-b/2*a)
elif delta>=0:
    print('solutions=',(-b-sqrt(delta))/2*a,(-b+sqrt(delta))/2*a)
else: print('pas de solutions')
    
    



