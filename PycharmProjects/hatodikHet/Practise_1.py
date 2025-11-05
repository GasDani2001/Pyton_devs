"""def faktorial_rek(n):
    if n == 1:
        return True
    else:
        return  (n * faktorial_rek(n-1))


n = 5
print(faktorial_rek(n))"""
"""
def ismetles_rek(n):
    print(n)

    if n == 1:
        return 1
    else:
        ismetles_rek(n-1)

n = 20
ismetles_rek(n)
"""

"""
def fibonacci_rek(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        secvence = fibonacci_rek(n-1)
        secvence.append(secvence[-1] + secvence[-2])
        return secvence

n = 10
print(fibonacci_rek(n))
"""
"""
def hatvanyozas_rek(n):
    szam = 5
    if n == 0:
        return True
    else:
        return szam * hatvanyozas_rek(n-1)

n = 3
print(hatvanyozas_rek(n))"""

def paros_rek(n):
    if n < 0:
        return
    else:
        if n % 2 == 1:
            print(n)
        paros_rek(n - 1)

n = -10
paros_rek(n)