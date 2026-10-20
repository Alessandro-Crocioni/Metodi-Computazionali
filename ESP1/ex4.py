from datetime import datetime, timedelta

datenow = datetime.now()

data_nascita = input("inserire la propria data di nascita nel seguente formato: g-m-a o:m:s")

mydatehr = datetime.strptime(data_nascita, "%d-%m-%Y %H:%M:%S")


timediff = datenow - mydatehr
print(timediff)
tots = timediff.total_seconds()
totm = tots / 60
toth = totm/60

l1 = ["differenza secondi", "differenza minuti", "differenza ore"]
l2 = [tots, totm, toth]

for k, v in zip(l1, l2):
    print('{:<25} : {:10.2f}'.format(k, v))

