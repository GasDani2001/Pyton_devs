halmaz1 = {1, 2, 3, 4, 5}
halmaz2 = {3, 4, 5, 6}
halmaz2.add(3) # nem fut hibára, de nem is kerül be újra a halmazba
print("Halmaz 1 elemei: ", halmaz1)
print("Halmaz 2 elemei: ", halmaz2)
unio = halmaz1 | halmaz2 # Unió (összevonás)
print("A két halmaz uniója : ", unio)
metszet = halmaz1 & halmaz2 # Metszet (közös elemek)
print("A két halmaz metszete: ", metszet)
kulonbseg = halmaz1 - halmaz2# Különbség (az első halmazban lévő elemek, amelyek nincsenek a másodikban)
print("A két halmaz különbsége: ", kulonbseg)