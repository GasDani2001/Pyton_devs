def rek_faktorialis(n):
    if n == 0:
        return 1
    else:
        return n * rek_faktorialis(n-1)
n = 5
print(rek_faktorialis(n))

def brute_force_faktorialis(n):
    ossz = 1
    for i in range(1, n+1):
        ossz *= i
    return ossz

print(brute_force_faktorialis(n))
def din_faktorialis(n):
    faktorialisok = [1]
    for i in range(1, n + 1):
        faktorialisok.append(i * faktorialisok[i - 1])
    return faktorialisok[n]

print(din_faktorialis(n))