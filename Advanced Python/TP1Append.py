import time 
import numpy as np 
import matplotlib.pyplot as plt

def Perf_append(n):
    L=[]
    L.append(1)
    start_time=time.time()
    for i in range (n):
        L.append(1)
    end_time=time.time()
    execution_time=end_time-start_time
    return execution_time

i=np.random.randint(2,50)
print(i)
n= np.random.randint(10000,100000,i)
n_values= np.sort(n)

print(n_values)

execution_times=[]

for i in n_values:
    execution_time=Perf_append(i)
    execution_times.append(execution_time)

print(execution_times)

plt.plot(n_values,execution_times,marker='o')
plt.xlabel('Number of Elements')
plt.ylabel('temps d\' execution (secondes)')
plt.title('Temps d\'execution de l\'operation append en fonction du nombre d\'elements')
plt.show()

