import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#FUNZIONE GENERICA
def func(x):
    y = (3/1000)*(x**2)
    return y

arrx = np.arange(0, 10, 0.01)
arry = func(arrx)




#METODO HIT OR MISS
randx = np.random.uniform(low=0, high=10, size=1000000)
randy = np.random.uniform(low=0, high=0.30, size=1000000)
mask = randy <= func(randx)
plt.figure()
plt.scatter(randx[mask], randy[mask], marker=".", color="red")
plt.plot(arrx, arry)
plt.title("HIT OR MISS")
plt.savefig(fname = "METODO HIT OR MISS")
plt.show()




#METODO DELL CUMULATIVA
def cumulativa(x):
    c = (1/1000)*(x**3)
    return c

def cumulativa_inv(x):
    c = (1000*x)**(1/3)
    return c

randx2 = np.random.random(1000000)
randy2 = cumulativa_inv(randx2)
plt.figure()
plt.hist(randy2, bins=100, density=True, alpha=0.6, color='green', label='Simulazione (Cumulativa)')
plt.plot(arrx, arry)
plt.title("METODO CUMULATIVA")
plt.savefig(fname = "METODO CUMULATIVA")
plt.show()


    


