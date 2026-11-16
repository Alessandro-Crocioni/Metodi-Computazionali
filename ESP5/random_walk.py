import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def walk(step, N):
    varphi = np.random.uniform(0, 2 * np.pi, N)
    x = [0.0]
    y = [0.0]
    curr_x = 0.0
    curr_y = 0.0
    for i in range(N):
        dx = step * np.cos(varphi[i])
        dy = step * np.sin(varphi[i])
        curr_x = curr_x + dx
        curr_y = curr_y + dy
        x.append(curr_x)
        y.append(curr_y)
        
    # Convertiamo le liste in array NumPy alla fine
    return np.array(x), np.array(y)


  
    


    
    





    



    
           
