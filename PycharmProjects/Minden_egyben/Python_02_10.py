ossz = 0
i = 0

while True:
    beker = input(f"Kérem szépen a(z) {i+1} számot: ")
    if beker.lower() == "q":
        break
    try:
        szam = float(beker)
        i += 1
        ossz += szam

    except ValueError:
        print("Érvénytelen bemenet, kérem számot adjon meg!")
        continue

if i > 0:
    atlag = ossz / i
    print(f"\nA(z) {i} szám átlaga: {atlag}")
else:
    print("Nem adott meg egyetlen számot sem, így nincs átlag.")