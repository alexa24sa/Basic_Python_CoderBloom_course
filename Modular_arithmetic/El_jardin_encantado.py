#!/usr/bin/python3

"""
En un jardín encantado, vive un duende que cuida semillas mágicas. Cada vez que planta una semilla especial, esta se multiplica 7 veces por cada día que pasa.

Después de N días, la cantidad total de plantas mágicas sigue la regla:

total de plantas = 7^N (7 elevado a la N)

El duende ha notado algo curioso: el color de las flores que nacen de estas plantas sigue un patrón que depende del último dígito del número total de plantas. Por eso, no necesita contar todas las plantas, solo quiere conocer el último dígito para predecir el color de las flores mágicas.

Dado el número de días 
 que han pasado desde que el duende plantó la primera semilla, determina el último dígito de la cantidad total de plantas mágicas en el jardín.

Entrada
Un entero N que indica el número de días.

Salida
Un entero que indica el último dígito de 7^N (7 elevado a la N).

Ejemplo
Entrada	Salida	Descripción
4
1
El número total de plantas al pasar 4 días sería 7 
 (7 elevado a la 4) = 2,401 por lo que el último dígito es 1.

7
3
"""
def plantas_magic(N):
    
    cycle = [7,9,3,1]
    magic_plants = cycle[(N-1)%4]
    print(magic_plants)
    
N = int(input().strip())
plantas_magic(N)
