def hatizsakdinamikus(sulyok, ertekek, kapacitas):
    n = len(ertekek)  # Elemek száma lekérdezése
    dp = [0] * (kapacitas + 1)  # Dinamikus programozást elősegítő tömb
    item_selected = [[False] * (kapacitas + 1) for _ in range(n + 1)]  #2 dimenziós tömb hogy le tudjuk követni az elmeket indexét

    #Áthaladunk az értékeinken
    for i in range(n):
        # Visszafelé ellenörizzük a kapacitáshoz képest az elemek értékeit és elmentjük őket
        for w in range(kapacitas, sulyok[i] - 1, -1):
            # Ha az újonnan hozzáadott elem értéke nagyobb, mint a korábbi maximális érték
            if dp[w] < dp[w - sulyok[i]] + ertekek[i]:
                dp[w] = dp[w - sulyok[i]] + ertekek[i]  # Frissítjük a maximális értékét
                item_selected[i][w] = True  # Elmentjük hogy az i edik elemet választottuk

    # Vissza téritjuk az elemeket
    kivasztott_elemek = []  # Kiválasztott elemek
    w = kapacitas  # Teljes kapacítás
    for i in range(n - 1, -1, -1):  # Visszafelé haladunk az elemek listájában
        # Ha az egy kiválasztott elem akkor hozzá adjuk a listához majd a maximális kapacításból levonjuk
        if item_selected[i][w]:
            kivasztott_elemek.append(i)
            w -= sulyok[i]

    return dp[kapacitas], kivasztott_elemek[::-1]  # Visszatérünk a maximális értékkel és a kiválasztott elemek indexeivel


ertekek = [100, 50, 30, 200, 300, 100]
sulyok = [2, 1, 3, 5, 17, 6]
kapacitas = 15

#függvény meghívása
max_ertek, kivasztott_elemek = hatizsakdinamikus(sulyok, ertekek, kapacitas)
print("A legnagyobb érték: ", max_ertek)  # Kiírjuk a maximális értéket
print("Ki választott elemek indexei: ", kivasztott_elemek)  # Kiírjuk a kiválasztott elemek indexeit

# Ez a kód nem a sajátom, mivel a dinamikus programozást még most sem értem igazán.
# A jelenlegi kódot is csak nagyon nehezem tudom értelmezni és szorgalmazom, hogy nézzük még át a dinamikuis programozást