from itertools import combinations
data = [{"A", "C", "D"}, {"B", "C", "E"}, {"A", "B", "C", "E"}, {"B", "E"}]
minSup = 2

def create(L,i):
    s=set()
    for key in L:
        for elements in key:
            s.add(elements)
    return list(combinations(s,i))

def exist(Subset,Set):
    for i in Subset:
        if i not in Set:
            return False
    return True

def fill(c,data):
    new={}
    for i in data:
        for j in c:
         if exist(j,i):
            if j not in new:
                new[j] = 1
            else:
                new[j] += 1
    return new

def update(c,minsup):
    aux=c.copy()
    for i in aux.keys():
        if aux[i]<minsup:
            c.pop(i)
    return c


def apriori (data,minSup):
    C = {}
    L = set()
    LF=set()
    for i in data:
        for elements in i:
            L.add(elements)
    i=0
    while(len(L)!=0):
        LF=L.copy()
        i+=1
        C = create(L,i)
        C= fill(C,data)
        L=update(C,minSup)
    return LF

print (apriori(data,2))
