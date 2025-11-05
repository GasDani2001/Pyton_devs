import Python_02_07_modul as sajatmodul # modul átnevezése, elemek elérés . után
from Python_02_07_modul import összeadas

eredmény = sajatmodul.összeadas(3, 5) # összeadás metódus hívása
print("Összeadás: ",eredmény)

# osztas metódus hívása 3,5 értékekkel, eredmeny kiírása
eredmény = sajatmodul.osztás(3,5)
print("osztás: ",eredmény)

from Python_02_07_modul import * # modul minden elemét előtag nélkül használhatjuk

eredmény = kivonas(3,5)
print("kivonás: ",eredmény)
# szorzas metódus hívása 3,5 értékekkel, eredmény kiírása
eredmény = sajatmodul.szorzás(3,5)
print("szorzás: ", eredmény)