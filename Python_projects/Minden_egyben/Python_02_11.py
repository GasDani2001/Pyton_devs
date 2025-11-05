import random

kitalalt_szam = random.randint(1, 100)

while True:
    beker = input("Kérek szépen egy egész számot 1 és 100 között: ")
    try:
        szam = int(beker)

        if not (1 <= szam <= 100):
            print("\nKérem, hogy 1 és 100 között adjon meg számokat!\n")
            continue

        if szam == kitalalt_szam:
            print("\nEltalálta!")
            break

        elif szam < kitalalt_szam:
            print("A kitalált szám nagyobb.\n")

        else:
            print("A kitalált szám kisebb.\n")

    except ValueError:
        print("Érvénytelen bemenet, kérem számot adjon meg!\n")
