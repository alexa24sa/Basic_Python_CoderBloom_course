"""
Descripción:
Ash tiene una lista completa de todas las especies de Pokémon que existen en la Pokédex
y otra lista con los Pokémon que ha capturado (donde puede haber repeticiones).
Debe determinar qué especies aún no ha capturado.

Entrada:
- Un entero N: cantidad total de especies en la Pokédex.
- N líneas, cada una con el nombre de una especie distinta.
- Un entero M: cantidad de capturas registradas.
- M líneas, cada una con el nombre de un Pokémon capturado (puede repetirse).

Salida:
- Los nombres de las especies que Ash NO ha capturado, uno por línea,
  en orden alfabético.
- Si no falta ninguna especie por capturar, imprimir exactamente:
  ¡Pokédex completa!
"""

N = int(input())
todas = [input().strip() for _ in range(N)]

M = int(input())
capturadas = {input().strip() for _ in range(M)}

faltantes = sorted(set(todas) - capturadas)

if faltantes:
    for nombre in faltantes:
        print(nombre)
else:
    print("¡Pokédex completa!")
