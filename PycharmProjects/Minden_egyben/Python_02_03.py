def osszeg(*szamok):
    ossz = 0
    for szám in szamok:
        ossz += szám # összegezzük a szamok értékeit az ossz változóba
    return ossz

print("A számok összege:", osszeg(1, 2, 3, 4)) # keressük meg a szintaktikai hibát

def osszefuz(*szinek, sep="/"):
    print("A *színek típusa: ", type(szinek))# írjuk ki a szinek változó típusát
    return sep.join(szinek)

print("Színek :",osszefuz("lila","kek","zold"))
print("Színek(,) :",osszefuz("lila","kek","zold",sep=","))

def szemely_adatok(**adatok):
    print("A **adatok típusa:", type(adatok))# írjuk ki az adatok változó típusát
    for kulcs, ertek in adatok.items():
        print(f"{kulcs}: {ertek}")

szemely_adatok(név="Péter", életkor= 30, varos="Budapest", szin="lila") # szemely_adatok feltöltése értékekkel

