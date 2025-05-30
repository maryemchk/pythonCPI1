


n=int(input("give the length of the dict"))
d={}
for i in range(n):
    a=input(print('give the key '))
    b=input(print('give the value'))
    d[a]=b


print(d)
for i in list(d.keys()):
    d[d.pop(i)]=i
print(d)
