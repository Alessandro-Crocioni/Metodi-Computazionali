
#PRIMO PUNTO
l1 = ["lunedì","martedì","mercoledì","giovedì","venerdì","sabato","domenica"]
print("i giorni della settimana sono: ", l1)

#SECONDO PUNTO
l2 = ["giovedì","venerdì","sabato","domenica"]
l3 = ["lunedì","martedì","mercoledì","giovedì","venerdì","sabato"]
l4 = l2 + 3*l1 + l3
print("i giorni del mese di ottobre sono: ", l4)

#TERZO E QUARTO PUNTO
n = 31
ln = [0]*31
for i in range(0, 31):
    ln[i] = i + 1



oct = dict(zip(ln, l4))
print ("perciò risulterà: ",oct)





                 
 