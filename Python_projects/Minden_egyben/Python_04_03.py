# Hozz létre egy listát a kedvenc gyümölcseiddel!

gyumolcsok = ["körte", "narancs", "paradicsom"]

# Kérj be egy gyümölcs nevét a felhasználótól, és ellenőrizd, hogy benne van-e a listában!
a = input("Írj be egy gyümölcsnevet: ")
benne_van = False
for i in gyumolcsok:
    if i == a:
        benne_van = True
print("Benne van." if benne_van else "Nincs benne.")

mas_gyumolcsok = gyumolcsok # Másold le a listát egy másik listába!
b = input("Írj be egy gyümölcsnevet: ")
print(mas_gyumolcsok)  # Adj hozzá egy elemet az új listához, amit a felhasználó ír be! Nézd meg, változott-e az eredeti lista!
for i in mas_gyumolcsok: # Hogy lehet elérni, hogy az eredeti lista változzon/ne változzon?
    if b == i:
        break
    else:
        mas_gyumolcsok.append(b)
# Rendezd a listát aszerint csökkenő sorrendbe, hogy hányszor szerepel benne az a betű!
from collections import Counter

def szamlal(gyumolcs):
    return Counter(gyumolcs)["a"]

gyumolcsok.sort(key = szamlal, reverse=True)
print(gyumolcsok)

# Készíts egy listát, ami tartalmazza a gyümölcs lista és az alábbi lista metszetét!
tobb_gyumolcs = ["szőlő", "barack", "alma", "banán", "cseresznye", "citrom", "ananász", "szilva"]
metszet = list(set(gyumolcsok) & set(tobb_gyumolcs))
print(metszet)
# Fűzd össze a két listát!
osszefuzott = gyumolcsok + tobb_gyumolcs
print("Összefűzött lista: " ,osszefuzott)
# Távolítsd el a listából a duplikált elemeket!
osszefuzott = list(set(osszefuzott))
# Rendezd a listát, majd fűzd össze egy sztringggé a következő elválasztóval.
osszefuzott.sort()
koz = " -- "
osszefuzott_string = koz.join(osszefuzott)
print(osszefuzott_string)
