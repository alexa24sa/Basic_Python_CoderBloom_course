#!/usr/bin/python3
"""
Tanjiro está practicando sus técnicas y necesita aprender todas las multiplicaciones de un rango de números.

El programa debe leer dos enteros A y B (con A<=B). Luego, para cada número desde 
A hasta B, se debe mostrar su tabla de multiplicar del A al B.

Entrada
Dos enteros A y B, en una sola línea, separados por espacio.

Salida
Las tablas de multiplicar desde 
A hasta B
. Cada tabla debe mostrar en líneas separadas las multiplicaciones del número correspondiente por 
. Entre cada tabla debe haber una línea en blanco. Ver el ejemplo para mayor detalle.

Entrada	Salida
2 4
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
"""
def tablas_mult(A,B):
    i = 0
    if A > 10 or A <= 0 or B >10 or B <=0:
        return 0
    elif A>B:
        return 0
    
    for x in range(A, B+1):
        while i<10:
            print(f'{x} x {i+1} = {x*(i+1)}')
            i +=1
        print('\n')
        i = 0
    
A,B = map(int, input().split())
tablas_mult(A,B)
