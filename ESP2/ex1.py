import sys
import math
import numpy as np


a = input("inserire il primo intero")
b = input("inserire il secondo intero")
a = int(a)
b = int(b)
print( "a binario: ",bin (a))
print( "b binario: ",bin (b))
print("a esadecimale: ", hex(a))
print("b esadecimale: ", hex(b))


ab_or = (a|b)
ab_and = (a & b)
print('----------------------')
print(' a  : {:08b}'.format(a))
print(' b  : {:08b}'.format(b))
print('----------------------')
print('c|d : {:08b}'.format( ab_or ))
print('c&d : {:08b}'.format( ab_and))