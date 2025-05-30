import time
import numpy as np 
import matplotlib.pyplot

def Perf_pop_Inter(n,k):
    l=[[1 for _ in range(n+1)] for _ in range(k)]
    print(l)
    for i in l:
        l[i].pop(i)
    print(l)




Perf_pop_Inter(2,5)