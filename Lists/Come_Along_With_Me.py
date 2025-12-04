"""
Descripción:
La Dulce Princesa está enseñando a su última creación a organizar listas de invitados
para una fiesta en el Dulce Reino. Ella entrega una lista de nombres de personajes de Ooo
y luego indica si deben ordenarse alfabéticamente en orden normal o en orden inverso.

Tu misión es ordenar correctamente la lista según la instrucción final.

Entrada:
- Una lista de nombres de personajes separados por espacios, en una sola línea.
- Una segunda línea con la palabra "normal" o "inverso", indicando el orden de salida.

Salida:
Imprime la lista de nombres ordenados alfabéticamente según la instrucción dada.

Ejemplos:

Entrada:
Finn Jake Marceline BMO
normal
Salida:
BMO Finn Jake Marceline

Entrada:
Finn Jake Marceline BMO
inverso
Salida:
Marceline Jake Finn BMO
"""

def reverse_list(personajes, mode):
    personajes = sorted(personajes)
    if mode == 'inverso':
       print(*personajes[::-1])
    elif mode == 'normal':
        print(*personajes)
    else:
        return 0

personajes = list(map(str, input().split()))
mode = str(input().strip())
reverse_list(personajes, mode)
