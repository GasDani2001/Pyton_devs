# Palindrom ellenőrzés rekurzívan, iteratívan és brute force elveket követve
# Palindrom (palindróma) az a szókapcsolat, ami visszafelé olvasva ugyanaz.
# (pl. Géza kék az ég. Indul a görög aludni.
def palindrom_rek(s):
    if len(s) <=1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom_rek(s[1: -1])

def palindrom_iterativ(s):
    bal, jobb = 0,len(s) -1
    while bal < jobb:
        if s[bal] != s[jobb]:
            return False
        bal+=1
        jobb-=1
    return True


def palindrom_bruteforce(s):
    # Kezdeti feltételezések
    n = len(s)

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


s = input("Kérek egy vizsgálandó kifejezést: ")
# Vegyük ki a stringből a szóközöket, pontot, és tegyük kisbetűssé!
s2 = s.replace(" ", "").lower()
print("A szóközök eltávolítása után, csupa kisbetűvel: ", s2)
print("Palindrom (iterativ):", palindrom_iterativ(s2))
print("Palindrom (rekurziv):", palindrom_rek(s2))
print("Palindrom (brute force):", palindrom_bruteforce(s2))
