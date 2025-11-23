#!/usr/bin/python3
"""
Descripción
Alicia tiene un reloj de 12 horas. Ella mira la hora actual y quiere saber qué hora marcará el reloj después de que pasen h horas.

Entrada
Una línea con dos enteros t y h, que representan t la hora actual y h las horas que pasarían.

Salida
La hora del reloj después de h horas.

Ejemplo
Entrada	Salida	Descripción
10 5
3
La hora actual son las 10, al pasar 5 horas serán las 3.

12 25
1

"""
def horas(t, h):
    t = t + h 
    hora = t % 12
    
    print(hora)
    
t, h = map(int, input().split())
horas(t, h)
    
