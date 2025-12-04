"""
Descripción:
Bob Esponja y Patricio recuerdan solo el MCD (g) y el MCM (m) de dos números secretos (a, b).
Se desea reconstruir un par válido (a, b) tal que:

    MCD(a, b) = g
    MCM(a, b) = m

Recordando que:
    a * b = g * m

Si NO existe un par de números que cumpla esto, se debe imprimir -1.

Entrada:
Dos enteros positivos g y m:
- g = MCD original
- m = MCM original

Salida:
- Dos enteros a y b tales que MCD(a,b)=g y MCM(a,b)=m
- Si no existe solución, imprimir -1

Ejemplo:
Entrada:
3 60
Salida:
12 15

Entrada:
6 20
Salida:
-1
"""

import math

g, m = map(int, input().split())

# Si m no es múltiplo de g, es imposible que existan a y b
if m % g != 0:
    print(-1)
else:
    # El par (g, m) siempre cumple gcd = g y lcm = m
    a = g
    b = m
    # (opcional) comprobación de seguridad:
    # assert math.gcd(a, b) == g and (a * b) // math.gcd(a, b) == m
    print(a, b)
