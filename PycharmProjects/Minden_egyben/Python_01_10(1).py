while True:
    a = input("Kérem az 1. szám értékét: ")  # 'a' szám beolvasása a billentyűzetről
    if a.isdigit():
        a = int(a)
        break

while True:
    b = input("Kérem a 2. szám értékét: ")  # 'b' szám beolvasása a billentyűzetről
    if b.isdigit():
        b = int(b)
        break
# Kis hibakezelést is belevittem a programba, igaz ez esetben elesünk a negatív számok bevitelétől

if b > a:
  print("Az összhasonlítás eredménye: ",b," nagyobb, mint ",a,)
elif b == a:
    print("Az összhasonlítás eredménye: ",a," és ",b," értéke ugyanannyi.")
else:
  print("Az összhasonlítás eredménye: ",a," nagyobb, mint ",b)

# rövid kiírás
print(a," nagyobb, mint ",b) if a > b else print("egyenlőek") if a == b else print(b," nagyobb, mint ",a)