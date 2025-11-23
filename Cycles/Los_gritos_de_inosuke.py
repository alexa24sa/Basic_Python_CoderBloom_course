#!/usr/bin/python3
"""
Inosuke está entrenando su voz. Cada vez que grita AH, lo hace con más fuerza, lo cual se puede representar como si se agregara una H extra.

Dado un número entero N, que representa la cantidad de gritos que dará, se pide imprimir cómo suenan esos gritos.

En el primer grito, imprime: AH
En el segundo grito, imprime: AHH
En el tercero grito, imprime: AHHH
Y así sucesivamente hasta el grito N
Entrada
Un entero N que indica el número de gritos.

Salida
N líneas con el grito de cada línea
"""
def gritos(N):
    if N > 100:
        return 0 
    
    for i in range (1, N+1):
        print('A' + 'H'*i)
        

N = int(input().strip())
gritos(N)
