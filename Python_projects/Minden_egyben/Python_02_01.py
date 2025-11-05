# függvény létrehozása, hívása
def sajat_fuggveny():
    print("Ez az első metódus, mely kiír Engem...")
    print("Nincs visszatérési értékem és nem kaptam paramétert sem...")

print("\n-------------Függvény létrehozása, hívása--------------")
sajat_fuggveny()

# paraméterátadással függvényhívás, létrehozás
def sajat_fuggveny2(parameter, parameter2):
    print("Egy újabb metódus... már kap paramétert, melyet kiír...csupa nagybetűvel!")
    print(parameter.upper(), parameter2)

print("\n-----Paraméterátadással függvényhívás, létrehozás-------")
sajat_fuggveny2(parameter="igen", parameter2="nem")

