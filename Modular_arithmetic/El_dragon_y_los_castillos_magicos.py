"""
En un reino mágico, un dragón recorre un circuito circular de C castillos numerados del 1 al C.
Con cada gran aleteo avanza exactamente un castillo. Tras A aleteos, se desea saber en cuál
castillo terminará, pues ahí dejará su tesoro.

Entrada:
Una línea con dos enteros A y C, que representan los aleteos del dragón y el número de castillos.

Salida:
El número del castillo en el que dejará su tesoro.

Ejemplos:
Entrada:
14 5
Salida:
4

Entrada:
23 10
Salida:
3
"""

def dragon_circuit(a,c):
    circuit = a % c
    if circuit == 0:
        print(c)
        return 0
    else:
        print(circuit)
        return 0
    

a,c = map(int, input().split())
dragon_circuit(a,c)
    
