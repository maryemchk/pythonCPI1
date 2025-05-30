import time 
import numpy as np
import matplotlib.pyplot as plt

def Perf_pop_Last(n,k):
    l=[]
    start_time=time.time()
    l=[[1 for _ in range(n+1)] for _ in range(k)]
    end_time=time.time()

    start_time1=time.time()
    for i in range(k):
        l[i].pop()
    end_time1=time.time()
  
    return (end_time-start_time)*(end_time1-start_time1)
   

i=np.random.randint(2,50)
n=np.random.randint(10000,100000,i)

k_values=np.sort(n)


execution_times=[]

for i in k_values:
    execution_time=Perf_pop_Last(1,i)
    execution_times.append(execution_time)

print(execution_times)

    
plt.plot(k_values,execution_times,marker='o')
plt.xlabel('Number of Elements')
plt.ylabel('temps d\' execution (secondes)')
plt.title('Temps d\'execution de l\'operation pop en fonction du nombre d\'elements')
plt.grid(True)
plt.show()

    
    