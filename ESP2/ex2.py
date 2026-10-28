a, n_bit = input("inserire un numero intero e il numero di bit cui apllicare le operazioni di shift. separati da uno spazio!").split()


n_bit = int(n_bit)
a = int(a)
print("il numero inserito in rappresentazione binaria è: ", bin(a))
print("il numero inserito in rappresentazione esadecimale è: ", hex(a))


a_plusb = (a << n_bit)
a_minusb = (a >> n_bit)
print('a   : {:>12}'.format( bin(a)))
print('a<<n: {:>12}'.format( bin(a_plusb)))
print('a>>n: {:>12}'.format( bin(a_minusb)))
print("-------------------")
print('a   : {:>12}'.format( hex(a)))
print('a<<n: {:>12}'.format( hex(a_plusb)))
print('a>>n: {:>12}'.format( hex(a_minusb)))


