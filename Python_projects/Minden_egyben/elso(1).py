print("Hello Python!")

#Python_01_02
# deklarációs rész, kezdőértékadással
a = 10  # a egy int típusú változó, értéke 10
# típusok ellenőrzése, kiírása
print("Az a változó típusa: ", type(a))  # int típus - szám(egész)

# b egy str (string) típusú változó, értéke "szöveg"
b = "valami"

print("A b változó típusa: ", type(b))
# akármikor megváltoztatható a típus!!!

a = "most pedig szöveg"
print("Az a változó típusa: ", type(a))


#Python_01_03
x, y, z = 10, "alma", 23.12  # egyszerre több változó inicializálása

print("Az x értéke: ", x)
print("Az y értéke: " + y)  # stringet stringhez + jellel is hozzáfűzhetünk
print("A  z értéke: " + str(z))

# többszörös értékadás (x,y,z egységesen legyen banán)
x = y = z = "banán"  # többszörösértékadás
print("\nAz x értéke: ", x) # legyen előtte egy sortörés
print("Az y értéke: ", y)
print("A z értéke: ", z)


#Python_01_04
x = 1 # int - egész
y = 2.8 # float - lebegőpontos
z = 1j # complex - komplex

y = int(y)
print(y)
print("x értéke: ",x,  "típusa -->", type(x))
print("y értéke: ",y, "típusa -->", type(y))
print("z értéke: ",z, "típusa -->", type(z))


#Python_01_05
a = '''Természetesen megadható
akár hosszabb szöveg is,
a python még ezt is szereti.
Dupla idézőjellel is működik és még sortöréseket is megtartja!'''

print(a)
print("18. karakter: ", a[17])  # 18. karakter kiírás
print("String részlet: ", a [3:7])  # írjuk ki az első sorból a mész stringrészletet
print("String részlet: ", a[-7:-3])  # negatív index, mi az eredmény?


#Python_01_06
x = "string, függvények, tesztelése"
print("String hossza: ", len(x)) # írjuk ki a string hosszát
print("Nagybetűs kiírás: ", x.upper()) # legyen csupa nagybetűs
print("Darabol: ", x.split(",")) # daraboljuk fel
print("Keresett érték(f) indexe: ", x.index("f"))

y = "123"
print("Számjegyek? (x) ", x.isdigit())
print("Számjegyek? (y) ", y.isdigit())
print(x + " " + y)  # minden változás csak megjelenítésben változtat

elso, masodik = 2,30
z = "Szeretnék {0} almát és {1} körtét."
print(z.format(elso, masodik))


#Python_01_07
jatekok = ["autó", "baba", "kocka", "lego", "kisvasút"]

print("Kiírás: ", jatekok)  # teljes lista kiírása
print("Részlista: ", jatekok[2:4])  #részlista megjelenítése kocka, lego

jatekok[1] = "motor" # baba elem --> motor változtatás/átírás
# újabb elem hozzáadása append fügvénnyel (tank)
jatekok.append("tank")
print("Új lista: ", jatekok)


#Python_01_08
szinek = ("piros", "sárga", "kék", "zöld", "rózsaszín") # tuple típus
print("A színek kiírása:", szinek) # elemek kiírása
print("Kiírás (3.elem): ", szinek[2]) # 3. elem kiírása
# módosítsuk a "kék" elem értékét "kékeszöldre"
del szinek  # az egész tuple törölhető


#Python_01_09



#Python_01_10
