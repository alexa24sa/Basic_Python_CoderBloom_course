"""
Descripción:
Finn ha encontrado un mapa mágico en la Mazmorra de Ooo. El mapa está representado 
como una matriz de N filas y M columnas, donde cada fila es un string de longitud M 
formado por los caracteres:
    T → tesoro
    E → enemigo
    . → sala vacía

El mapa está invertido horizontalmente, por lo que Finn necesita invertir cada fila 
para mostrar el mapa real.

Tu tarea es ayudar a Finn a corregir el mapa invirtiendo horizontalmente cada una 
de las N filas, sin cambiar el número de filas ni de columnas.

Entrada:
- La primera línea contiene dos enteros N y M (1 ≤ N, M ≤ 20).
- Las siguientes N líneas contienen cada fila del mapa, cada una como un string de M
  caracteres consecutivos sin espacios ("T", "E" o ".").

Salida:
- Imprimir la matriz resultante después de invertir horizontalmente cada fila, 
  manteniendo N filas y M columnas.

Ejemplo de entrada:
3 4
.T.E
E...
T.E.

Ejemplo de salida:
E.T.
...E
.E.T
"""


def mazmorra_two(N,M):
    maz= list()
    for _ in range (0, N):
        fila = str(input().strip())
        maz.append(fila)
    
    for i in range (0, N):
        fila_invertida = maz[i][::-1]
        print(fila_invertida)
    
        
N,M = map(int, input().split())
mazmorra_two(N,M)
