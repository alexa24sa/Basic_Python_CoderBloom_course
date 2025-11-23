#!/usr/bin/python3
"""
Tanjiro debe cortar una roca con su espada. Cada día, Tanjiro duplica la cantidad de cortes que hace respecto al día anterior. El primer día hace exactamente 1 corte, el segundo día 2 cortes, el tercero 4 cortes, y así sucesivamente.

Se pide mostrar cuántos cortes hizo en total después de 
 días de entrenamiento.

Entrada
Un entero N
 que representa el número de días

Salida
El número de cortes que hizo Tanjiro en total después de 
N días de entrenamiento

Ejemplos
Entrada	Salida	Descripción
1
1
El primer día solo hace 1 corte

2
3
1 corte en el primer día y 2 cortes en el segundo día, 3 cortes en total
"""


def cortes(N):
    if N > 10:
        return 0 
    
    N = 2 **(N) -1
    
    return N 
    
N = int(input().strip())
print(cortes(N))
