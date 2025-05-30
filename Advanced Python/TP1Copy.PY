import time
import numpy as np
import matplotlib.pyplot as plt

def Perf_copy(n, K):
    L = [1] * n
    start_time = time.time()
    LL = [L[:] for _ in range(K)]
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Liste de différentes valeurs de n
n_values = [100, 500, 1000, 5000, 10000]
K = 100  # Valeur fixe de K

# Mesurer le temps d'exécution pour chaque valeur de n
execution_times = []
for n in n_values:
    execution_time = Perf_copy(n, K)
    execution_times.append(execution_time)
print(execution_times)

# Tracer la courbe d'exécution en fonction de n
plt.plot(n_values, execution_times, marker='o')
plt.xlabel('Valeur de n')
plt.ylabel('Temps d\'exécution (secondes)')
plt.title('Courbe d\'exécution en fonction de n')
plt.grid(True)
plt.show()


