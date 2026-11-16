import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random_walk

N = 1000
passo = 0.5
num_walkers = 5
x_walkers = []
y_walkers = []
dist_quad_walkers = []

for i in range(num_walkers):
    x, y = random_walk.walk(passo, N)
    x_walkers.append(x)
    y_walkers.append(y)
    dist_quad = x**2 + y**2
    dist_quad_walkers.append(dist_quad)


#PUNTO A
plt.figure(figsize=(8, 8))
for i in range(num_walkers):
    plt.plot(x_walkers[i], y_walkers[i], label=f'Walker {i+1}')
    # Segna il punto di partenza (0,0)
    plt.scatter(x_walkers[i][0], y_walkers[i][0], color='black', zorder=5) 

plt.title("Punto A: Traiettorie 2D di 5 Random Walker (con cicli for)")
plt.xlabel("Asse X")
plt.ylabel("Asse Y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()




#PUNTO B
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Primo pannello: Stesso grafico del punto A
for i in range(num_walkers):
    ax1.plot(x_walkers[i], y_walkers[i], label=f'Walker {i+1}')
ax1.set_title("Traiettorie 2D dei Walker")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.grid(True)
ax1.axis('equal')
ax1.legend()

# Secondo pannello: Quadrato della distanza in funzione dei passi per i 5 walker
passi = np.arange(N + 1) # Da 0 a N passi
for i in range(num_walkers):
    ax2.plot(passi, dist_quad_walkers[i], label=f'Walker {i+1}')
ax2.set_title("Quadrato della Distanza ($x^2 + y^2$)")
ax2.set_xlabel("Numero di Passi")
ax2.set_ylabel("Distanza al quadrato")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig("5Walkers e Distanza")
plt.show()
