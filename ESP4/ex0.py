import somme

num = input("inserire il numero naturale fino a cui sommare")
num = int(num)
out1 = somme.somme(num)
out2 = somme.somme_rad(num)
print("la somma risulta: ", out1)
print("la somma delle radici risulta: ", out2)