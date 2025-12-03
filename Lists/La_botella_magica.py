"""
Descripción:
El Rey Helado quiere elegir a un ayudante entre sus fieles pingüinos usando una botella encantada.
La botella primero apunta a un pingüino inicial y luego se mueve en círculo en sentido horario
un número determinado de posiciones.

Los pingüinos están organizados alrededor de un círculo en la siguiente secuencia:
["Gunter", "Kissy", "Waddles", "Chilly", "Gunter2", "Pep", "Snowball"]

El juego funciona así:
- Se da el nombre del pingüino inicial, desde donde empieza a contar la botella mágica.
- Se da un número entero K, que indica cuántas posiciones avanzará la botella.
- El pingüino señalado después del último movimiento será el elegido como ayudante del Rey Helado.

Entrada:
Una sola línea con el nombre del pingüino inicial seguido de un entero K separado por un espacio.

Salida:
El nombre del pingüino elegido tras mover la botella K posiciones en círculo.

Ejemplo:
Entrada:
Kissy 2
Salida:
Chilly
"""

penguins = ["Gunter", "Kissy", "Waddles", "Chilly", "Gunter2", "Pep", "Snowball"]

def penguins_searching(penguin_name, k):
    initial_position = penguins.index(penguin_name)
    final_pos = (initial_position + k) % len(penguins)
    print(penguins[final_pos])
    
penguin_name, k = map(str, input().split())
k = int(k)

penguins_searching(penguin_name, k)
