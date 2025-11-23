#!/usr/bin/python3
"""
Zenitsu está practicando sus cálculos durante el entrenamiento con Tanjiro. Para mejorar su concentración, anota una lista de números que representan la energía de sus golpes.

Sin embargo, hay un valor específico X que representa un número prohibido: cada vez que aparece, debe ignorar ese número y continuar con los demás.

Tu tarea es ayudar a Zenitsu a calcular el promedio de los números válidos (es decir, ignorando los valores prohibidos).

Entrada
La primera línea contiene dos enteros 
N y X la cantidad de números en la lista y el valor prohibido que debe ignorarse
Luego siguen N líneas con un entero en cada una, que represenentan las energías anotadas por Zenitsu
Salida
Un número entero que representa la parte entera del promedio de las energías válidas
En caso todos los números hayan sido números prohibidos, imprimir 
Ejemplo
Entrada	Salida	Descripción
5 7
4
7
3
7
10
5
Los números válidos son 4, 3 y 10, y su suma es 17, entonces el promedio es 17/3 = 5.67, pero se pide la parte entera, entonces la respuesta es 5

1 5
5
0
El único número anotado es 5, el cual está prohibido, por lo que imprimimos 0
"""



def entrenamiento(N, X):
    promedio = 0
    counter = 0
    if N > 100 or X > 100 or N <= 0 or X <= 0:
        return 0 
    
    
    for x in range (1, N+1):
        entrance = int (input().strip())
        if entrance != X:
            promedio = promedio + entrance
            counter +=1
    
    if promedio == 0:
        print('0')
    else :
        promedio = int(promedio / counter)
        print (promedio)

N, X = map(int, input().split())
entrenamiento(N, X)
    
    
        
        
