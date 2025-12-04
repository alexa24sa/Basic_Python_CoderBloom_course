# Problema: Para cada entrenador contar cuántos tipos distintos de Pokémon tiene
# y luego listar los tipos que TODOS los entrenadores tienen en común.
# Entrada:
#   T                      -> número de entrenadores
#   Para cada entrenador:
#       N_i                -> cantidad de Pokémon
#       N_i cadenas        -> tipos de esos Pokémon
# Salida:
#   T líneas con la cantidad de tipos diferentes de cada entrenador
#   1 línea final con los tipos en común ordenados alfabéticamente o "Ninguno"

T = int(input())

comunes = None
diferentes_por_entrenador = []

for _ in range(T):
    N = int(input())
    tipos = input().split()
    conjunto_tipos = set(tipos)
    diferentes_por_entrenador.append(len(conjunto_tipos))
    if comunes is None:
        comunes = conjunto_tipos
    else:
        comunes &= conjunto_tipos

for c in diferentes_por_entrenador:
    print(c)

if comunes:
    print(" ".join(sorted(comunes)))
else:
    print("Ninguno")
