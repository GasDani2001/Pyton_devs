def reszhalmazok(lista):
    # Alapeset: üres lista esetén az egyetlen részhalmaz az üres halmaz
    if len(lista) == 0: # if üres listavizsgálat:
        return  [[]] # üres listával tér vissza
    else:
        # A lista első elemét kiválasztjuk
        elso = lista[0] # elso = ?
        # A maradék lista összes részhalmaza
        maradek_reszhalmazok = reszhalmazok(lista[1:]) # maradek_reszhalmazok = ? rekurziv hívás
        # Létrehozzuk az összes lehetséges részhalmazt
        kombinaciok = []
        for halmaz in maradek_reszhalmazok:
            kombinaciok.append(halmaz)
            kombinaciok.append([elso] + halmaz)
        return sorted(kombinaciok, key=len) # részhalmaz hossza alapján rendez

# Példa meghívás:
print(reszhalmazok([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
