szamlalo = 0
osszeado = 0
atlag = 0
szamok = []

while True:
    beker_szam = input(f"Adja meg a(z) {szamlalo+1} egész számot: ") #szám bekérése
    try:
        beker_szam = int(beker_szam)  #megpróbál konvertálni

        if beker_szam == 0:  # ha a bekért szám 0, akkor kilép a ciklusból
            break

        szamlalo += 1
        osszeado += beker_szam
        szamok.append(beker_szam)

    except ValueError:     #a konvertálás sikertelen
        print("Rossz adattípus.")

if szamlalo == 0:
    print("Mivel 1. számként 0-át adott meg, ezért az átlag számítás nem lehetséges.")
else:
    atlag = osszeado / szamlalo      #azért nem használok például float(osszeado)-t, mert az output érték így is valós szám nálam (a rendszer termináljában is).
    print("\nAz összes bekért szám kiírva: ", szamok)
    print("A bekért számok átlaga: ", atlag)