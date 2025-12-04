"""
Descripción:
Bob Esponja necesita simplificar una fracción A/B usada en una receta.
Para mantener la misma proporción, debe dividir A y B entre su Máximo Común Divisor (MCD)
para obtener la fracción equivalente más simple.

Entrada:
Dos enteros positivos A y B:
- A = numerador
- B = denominador

Salida:
Dos enteros separados por un espacio: la fracción reducida A' B'

Ejemplo:
Entrada:
8 12
Salida:
2 3

Entrada:
25 5
Salida:
5 1
"""

import math

A, B = map(int, input().split())

mcd = math.gcd(A, B)

print(A // mcd, B // mcd)
