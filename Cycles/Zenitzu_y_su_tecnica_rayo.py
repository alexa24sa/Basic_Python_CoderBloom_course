#!/usr/bin/python3
"""
El número de golpes aumenta de manera progresiva:

En el primer trueno hace 1 golpe.
En el segundo trueno hace 2 golpes.
En el tercero hace 3 golpes.
Y así sucesivamente.
Se pide mostrar el entrenamiento de Zenitsu en forma de un patrón de asteriscos (*), donde cada fila representa un trueno y la cantidad de asteriscos en esa fila corresponde al número de golpes realizados.

Entrada
Un número entero N
, que indica la cantidad de truenos que Zenitsu escuchó.

Salida
Un patrón de i
 filas. La fila i
 debe contener exactamente 
 asteriscos, sin espacios entre ellos.

Ejemplo
Entrada	Salida
4
*
**
***
****
"""



def golpes(N):
    if N>20 or N<1:
        return 0 
    
    for i in range (1, N+1):
        print("*"*i)
        

N = int(input().strip())
golpes(N)
