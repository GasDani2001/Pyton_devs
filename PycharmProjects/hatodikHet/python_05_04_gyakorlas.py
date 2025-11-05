# Legnagyobb közös osztó kiszámítása rekurzívan
def lnko(a, b):
    if b == 0:
        return a
    else:
        return lnko(b, a % b)

# Teszteljük a függvényt
eredmeny = lnko(84, 18)
print(eredmeny) # eredmény: 6



