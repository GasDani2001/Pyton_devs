import math, statistics as stat, random # math, statistics, random modulok importálása

# Kör kerületének kiszámítása
sugar = 5
kerulet = 2 * math.pi * sugar # használjuk a pi beépített értéket a 3,14 helyett
print("A kör kerülete:", kerulet)
print("A kör kerülete:", math.sqrt(sugar)*math.pi)# írjuk ki és számítsuk ki a kör területét math modul sqrt() és pi elemeit használva

# Átlag (mean), szórás számítás
print("Mean: ",stat.mean([-11, 5.5, -3.4, 7.1, -9, 22]))
print("Standard deviation: ",stat.stdev([-11, 5.5, -3.4, 7.1, -9, 22]))

# Véletlen értékek
lista = ["auto", 2,3,4, "motor", True,False, 2.38,] # lista[] létrehozása tetszőleges típusú elemekkel
random.shuffle(lista) # véletlenszerű sorrendbe rendezi az elemeket
print(lista) #új lista kiírása
print(random.sample(lista, k=2)) # random.sample(honnan, mennyit)


