"""
Descripción:
BMO está componiendo una nueva canción y quiere practicar las notas musicales básicas.
Tiene una lista fija con las siguientes notas:
["do", "re", "mi", "fa", "sol", "la", "si"]

BMO pedirá un número entero N, que representa la cantidad de notas musicales
que quiere usar al inicio de su canción.

El programa debe imprimir, en orden, las primeras N notas de la lista,
separadas por un espacio.

Entrada:
Un entero N, que representa la cantidad de notas musicales que se deben mostrar.

Salida:
Las primeras N notas de la lista, separadas por un espacio.

Ejemplos:
Entrada:
3
Salida:
do re mi

Entrada:
5
Salida:
do re mi fa sol
"""


notas = ["do", "re", "mi", "fa", "sol", "la", "si"]


def select_notas(N):
    if N > 7:
        return 0
    
    for element in range(0,N):
        print(notas[element])
        

N = int(input().strip())
select_notas(N)
