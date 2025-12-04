"""
Descripción:
Ash participa en la Liga Pokémon con varios entrenadores. Cada combate otorga puntos:
- victoria: +3 puntos
- empate: +1 punto
- derrota: +0 puntos

Cada combate se registra como:
Entrenador1 Resultado Entrenador2

Donde Resultado puede ser:
- victoria  -> el primer entrenador gana al segundo
- empate    -> ambos reciben +1
- derrota   -> el primer entrenador pierde ante el segundo

Se debe generar la tabla de clasificación final con:
- Los entrenadores ordenados por puntaje de mayor a menor
- En caso de empate en puntaje, ordenar alfabéticamente
- Imprimir: Nombre Puntaje

Entrada esperada:
N
Entrenador1 Resultado Entrenador2
...
(n líneas)

Salida esperada:
Lista ordenada de entrenadores con su puntaje final.
"""

N = int(input())

puntos = {}

def asegurar(nombre):
    if nombre not in puntos:
        puntos[nombre] = 0

for _ in range(N):
    e1, res, e2 = input().split()
    asegurar(e1)
    asegurar(e2)

    if res == "victoria":
        puntos[e1] += 3
    elif res == "empate":
        puntos[e1] += 1
        puntos[e2] += 1
    elif res == "derrota":
        puntos[e2] += 3

ranking = sorted(puntos.items(), key=lambda x: (-x[1], x[0]))

for nombre, puntaje in ranking:
    print(nombre, puntaje)
