import somme

n = input("inserire il numero fino a cui si vuole sommare e fattorizzare")
n = int(n)
somma, fattoriale = somme.somme_prod(n)


print("la somma dei primi n numeri naturali è: ", somma)
print("il prodotto dei primi n numeri naturali è: ", fattoriale)


somma2 = somme.somme_esp(n, 2)
print("La somma dei numeri con esponente variabile è: ", somma2)
