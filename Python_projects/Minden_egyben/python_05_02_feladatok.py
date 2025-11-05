gyumolcsok = {
    "papaya": 300,
    "kókuszdió": 250,
}
print("Gyümölcsök szótár:", gyumolcsok)

# Kérj be egy gyümölcs nevét a felhasználótól, majd írd ki az árát, ha benne van!
a = input("Kérek szépen egy gyümölcs nevet: ")
if a in gyumolcsok:
    print(f"A {a} ára: ", gyumolcsok.get(a))
else:
    print("Ez a gyümölcs nincs benne a szótárban.")

# Adj hozzá egy új elemet (név és ár) az új szótárhoz, amit a felhasználó ír be!
uj_gyumolcs = input("Írjon be egy új gyümölcsnevet: ")
uj_ar = input("Kérem a gyümölcs árát: ")
try:
    gyumolcsok[uj_gyumolcs] = int(uj_ar)
except ValueError:
    print("Az árnak számnak kell lennie.")

# Nézd meg a gyumolcsok szótár változását!
print("Gyümölcsök szótár (módosított): ", gyumolcsok)

# Rendezd a szótárt kulcsok szerint csökkenő sorrendbe!
rendezett_gyumolcsok = dict(sorted(gyumolcsok.items(), key=lambda x: x[0], reverse=True))
print("Rendezett gyümölcsök kulcs szerint csökkenő sorrendben:", rendezett_gyumolcsok)


tobb_gyumolcs = {
    "szőlő": 300,
    "barack": 250,
    "banán": 200,
    "citrom": 180,
    "ananász": 400,
}
# Két szótár egyesítése (tobb_gyumolcs és gyumolcs)
osszes_gyumolcs = gyumolcsok | tobb_gyumolcs
print("Összes gyümölcs:", osszes_gyumolcs)

# Rendezd a szótárat értékek szerint növekvő sorrendbe!
rendezett_ertek_szerint = dict(sorted(osszes_gyumolcs.items(), key=lambda item: item[1]))
print("Rendezett gyümölcsök ár szerint:", rendezett_ertek_szerint)

# Fűzd össze a kulcsokat egy sztringgé a következő elválasztóval (--)
elvalaszto = " -- "
gyumolcs_string = elvalaszto.join(rendezett_ertek_szerint)
print("Gyümölcsök összefűzve:", gyumolcs_string)
