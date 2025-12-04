"""
Descripción:
En un observatorio astronómico se estudian los ciclos orbitales de distintos planetas
alrededor de su estrella. Los astrónomos calculan que, después de N días, todos los
planetas estarán alineados únicamente si N es divisible por el período orbital de cada
uno de ellos.

Dado un número N de días y una lista de periodos orbitales, determina si los planetas
se alinearán en ese momento.

Entrada:
- Un entero N que representa la cantidad de días.
- Un entero K que representa la cantidad de periodos orbitales.
- Una lista de K enteros p1, p2, …, pK que representan cada período orbital.

Salida:
- Imprime "SI" si N es divisible por todos los periodos orbitales.
- Imprime "NO" en caso contrario.

Ejemplo:
Entrada:
84
3
2 3 7
Salida:
SI

Entrada:
97
2
7 13
Salida:
NO
"""

N = int(input())
K = int(input())
periodos = list(map(int, input().split()))

ok = True
for p in periodos:
    if N % p != 0:
        ok = False
        break

print("SI" if ok else "NO")

