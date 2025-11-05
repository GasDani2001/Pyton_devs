#megtett_ut = complex
#eltelt_ido = complex

#while True:
#    megtett_ut = input("Kérem a megtett utat: ")
#    if megtett_ut.isdigit() and megtett_ut != "0":
#        megtett_ut = float(megtett_ut)
#        break

#A fenti while ciklust teljesen magamtól csináltam, de sajnos csak természetes számokat kezel.
# Az eltelt_ido-höz is csináltam egy ugyanilyen while cikulust, csak azt töröltem.

#A try - except megoldást ugyan segítséggel oldottam meg, de ennek csak annyi az oka, hogy eddig nem tudtam, hogy pythonban ez a legésszerűbb megoldás
# a típus konverzió ellenőrzésére. Egyébként a lenti kódra ránézve a tudás ismeretében, (ami nem volt meg) valósztínűleg meg tudtam volna így is oldani.


while True:
    megtett_ut = input(f"Kérem a megtett utat km-ben: ")
    # Ellenőrizze, hogy a bemenet érvényes szám-e
    try:
        megtett_ut = float(megtett_ut)  # Próbálja meg konvertálni float típusra
        if megtett_ut > 0:
            break
        else:
            print("0-val nem lehet osztani, hátrafelé meg nem szokott az ember sokat menni.")
    except ValueError:
        print("Rossz adattípus.")


while True:
    eltelt_ido = input(f"Kérem adja meg, hogy óraában mennyi idő alatt teljesítette: ")
    try:
        eltelt_ido = float(eltelt_ido)
        if eltelt_ido > 0:
            break
        else:
            print("0-val nem lehet osztani, hátrafelé meg nem szokott az ember sokat menni.")
    except ValueError:
        print("Rossz adattípus.")

atlag_sebesseg = megtett_ut/eltelt_ido
print("Átlagsebessége: ", atlag_sebesseg ," km/h\n")

if atlag_sebesseg < 80:
    print("Nem megfelelő az átlagsebessége.")
elif atlag_sebesseg == 80:
    print("Tökéletes az átlagsebessége.")
else:
    print("Megfelelő az átlagsebessége.")