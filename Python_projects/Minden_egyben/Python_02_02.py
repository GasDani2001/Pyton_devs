# Argumentumok - alapértelmezett értékek megadása
# Ha a függvényt argumentum nélkül hívjuk meg, akkor az alapértelmezett értéket használja
def sajat_fuggveny3(a = 3, b = 6):
    for x in range(1, a+1):
        for y in range(1, b+1):
            print(x*y, end="\t")
        print("\n")

print("\n-----Argumentumok - alapértelmezett értékek megadása: üres")
sajat_fuggveny3()
print("\n-----Argumentumok - alapértelmezett értékek megadása: 2")
sajat_fuggveny3(a=2)
print("\n-----Argumentumok - alapértelmezett értékek megadása: 4,4")
sajat_fuggveny3(a=4, b=4)


