# Halmaz létrehozása hárommal osztható számok halmaza 21-ig.
harommal_oszthato = { x for x in range(0,22) if x % 3 == 0}
print("Hárommal osztható számok halmaza: ", harommal_oszthato)
harommal_oszthato.add(21)
print("Hárommal osztható számok halmaza: ", harommal_oszthato)

# Néggyel osztható számok halmazának létrehozása
neggyel_oszthato = { x for x in range(0,22) if x % 4 == 0}

print("Néggyel osztható számok halmaza: ", neggyel_oszthato)

# Hozz létre egy halmazt, ami tartalmazza a páros számokat 0-tól 20-ig!
paros_hamaz = { x for x in range(0,22) if x % 4 == 0}
print("Páros számok halmaza 20-ig: ", paros_hamaz)

# Add hozzá a páros számokat tartalmazó halmazhoz a 22 számot is!
paros_hamaz.add(22)
print("Páros számok halmaza 22-ig: ", paros_hamaz)

# Ellenőrizd, hogy részhalmaza-e a néggyel osztható számok halmaza a páros számok halmazának!
print("A néggyel osztható halmaz részhalmaza a páros számoknak? ", paros_hamaz <= neggyel_oszthato)

# Készíts egy hattal osztható halmazt, majd tedd bele az annak megfelelő számokat!

# Tipp: páros és hárommal osztható számok metszete.
hattal_oszthato = paros_hamaz & harommal_oszthato
print("Hattal osztható számok halmaza: ", hattal_oszthato)

# Írd ki a hárommal és néggyel osztható számok unióját!
unio = harommal_oszthato | neggyel_oszthato
print("Hárommal vagy néggyel osztható számok uniója:", unio)
