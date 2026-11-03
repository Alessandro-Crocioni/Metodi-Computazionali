import numpy as np
import matplotlib.pyplot as plt


def somme (n):
    sum = 0
    for i in range (n+1):
        sum = sum + i
    return sum

def somme_rad (n):
    sum_rad = 0
    for i in range (n+1):
        sum_rad = sum_rad + np.sqrt(i)
    return sum_rad


def somme_prod (n):
    sum = 0
    pr = 1
    for i in range (1, n+1):
        sum = sum + i
        pr = pr * i
    return sum, pr



def somme_esp (n, a=1):
    sum = 0
    for i in range (n+1):
        sum = sum + i**a
    return sum

    


