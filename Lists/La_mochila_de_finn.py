"""
Descripción:
Finn y Jake se preparan para luchar contra un dragón mágico. Finn lleva una mochila con varios objetos,
y Jake quiere saber si tienen el objeto correcto para la batalla.

El programa debe leer una lista de objetos que Finn guarda en su mochila (todos en una sola línea,
separados por espacios). Luego, se leerá el nombre de un objeto que Jake pregunta.

Si Finn tiene ese objeto, se debe imprimir:
¡Genial! Sí tengo <OBJETO>, estamos listos para derrotar al dragón.

En caso contrario, se debe imprimir:
Oh no... no tengo <OBJETO>, tendremos que improvisar.

Entrada:
- Una línea con varios objetos separados por espacios, que representan la mochila de Finn.
- Una segunda línea con una cadena S, el objeto que Jake pregunta.

Salida:
Un mensaje de Finn indicando si tiene o no el objeto.

Ejemplos:
Entrada:
espada escudo manzana poción oro
espada
Salida:
¡Genial! Sí tengo espada, estamos listos para derrotar al dragón.

Entrada:
guante flor caramelo diamante slime
anillo
Salida:
Oh no... no tengo anillo, tendremos que improvisar.
"""


def object_searching(mochila, objeto):
    for element in mochila:
        if element == objeto:
            print(f"¡Genial! Sí tengo {objeto}, estamos listos para derrotar al dragón.")
            return 0
    print(f"Oh no... no tengo {objeto}, tendremos que improvisar")
    
mochila = input().split()
objeto = input().strip()
object_searching(mochila, objeto)
