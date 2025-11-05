# Brutális erő algoritmus a hátizsákproblémára (n:targyak szama)
def hatizsak_bruteforce(sulyok, ertekek, kapacitas, n):
    # Alapeset: ha nincs több tárgy vagy a kapacitás elérte a 0-t
    if n == 0 or kapacitas == 0:
        return 0, []
    # Ha a tárgy súlya nagyobb, mint a fennmaradó kapacitás, nem vehetjük fel
    if sulyok[n - 1] > kapacitas:
        return hatizsak_bruteforce(sulyok, ertekek, kapacitas, n - 1)
    else:
        # Két esetet hasonlítunk össze: a tárgyat felvesszük vagy nem
        val1, elemek1 = hatizsak_bruteforce(sulyok, ertekek, kapacitas - sulyok[n - 1], n - 1)
        val2, elemek2 = hatizsak_bruteforce(sulyok, ertekek, kapacitas, n - 1)
        # Mindkét rekurzív hívás eredményét tároljuk, és a nagyobb értéket választjuk
        if val1 + ertekek[n-1] > val2:
            # Ha a tárgyat felvesszük, akkor az indexét hozzáadjuk a listához
            elemek1.append(n-1)
            return val1 + ertekek[n-1], elemek1
        else:
            return val2, elemek2

# Fő program, ahol megadjuk a bemeneti adatokat
ertekek = [20, 50, 30, 200, 60, 100] # adjunk meg értékeket [] zárójelben tetszőleges számban
sulyok = [2, 1, 3, 5, 10, 4] # ugyanannyi súlyt állítsunk be, minden értékhz tartozzon egy súly []
kapacitas = 15 # definiáljuk a kapacitas értékét
n = len(ertekek)
max_ertek, kivasztott_elemek = hatizsak_bruteforce(sulyok, ertekek, kapacitas, n)
print("Az elérhető legnagyobb érték: ",max_ertek) # írjuk ki az elérhető legnagyobb érték
print("iválasztott elemek indexe: ",kivasztott_elemek) # írjuk ki a  kiválasztott elemek indexeit:


