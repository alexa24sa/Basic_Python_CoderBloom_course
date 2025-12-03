"""
Los caballeros encuentran un cofre con gemas mágicas y deben repartirlas equitativamente entre C caballeros. 
Si sobran gemas, deben regresarse al cofre para evitar años de mala suerte. 
El programa determina cuántas gemas recibe cada caballero y cuántas deben volver al cofre.

Entrada:
Una línea con dos enteros G y C, que representan las gemas iniciales en el cofre y el número de caballeros.

Salida:
Una línea con dos enteros: las gemas que recibe cada caballero y las gemas que deben regresarse al cofre.

Ejemplo:
Entrada:
56 3
Salida:
18 2

Entrada:
450 15
Salida:
30 0
"""

def part_gems(g,c):
    mod = 0
    if g%c != 0:
        chest = g%c
        partition = int(g/c)
        print(f"{partition} {chest}")
    else:
        chest = 0
        partition = int(g/c)
        print(f"{partition} {chest}")
    
    
g, c = map(int, input().split())
part_gems(g,c)
