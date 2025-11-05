# Legnagyobb közös osztó kiszámítása rekurzívan
def lnko(a, b):
    if b == 0:
        return a
    else:
        return lnko(b, a % b)

# Teszteljük a függvényt
eredmeny = lnko(84, 18)
print(eredmeny) # eredmény: 6

def lnko(a, b):
    if b == 0:
        return a
    return lnko(b, a % b)

def lkkt(a, b):
    return abs(a * b) // lnko(a, b)

# Példa használat
a = 84
b = 18
print(lkkt(a, b))



