# Problema: N es aceptado si es primo y la suma de sus dígitos también es primo.
# Input:
#   L R
# Output:
#   Cantidad de números en [L, R] que cumplen la regla.

L, R = map(int, input().split())

lim = 1_000_000
criba = [True] * (lim + 1)
criba[0] = criba[1] = False

p = 2
while p * p <= lim:
    if criba[p]:
        for i in range(p * p, lim + 1, p):
            criba[i] = False
    p += 1

def suma_digitos(n):
    return sum(map(int, str(n)))

contador = 0

for n in range(L, R + 1):
    if criba[n] and criba[suma_digitos(n)]:
        contador += 1

print(contador)
