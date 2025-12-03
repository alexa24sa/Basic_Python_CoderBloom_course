"""
En un reino lejano, la reina posee un cofre lleno de cristales mágicos. Cada cristal tiene un número que indica su poder.
La reina descubrió que al combinar los cristales, se activa un hechizo especial solo si la suma de todos los dígitos
del número inscrito en el cristal es divisible por 9.

Tu tarea es determinar si el hechizo se activa para un cristal gigante que puede contener hasta 100,000 dígitos.

Entrada:
Un número N inscrito en el cristal.

Salida:
Imprime "SI" si la suma de los dígitos de N es divisible por 9; de lo contrario imprime "NO".

Ejemplo:
Entrada:
123456
Salida:
NO
"""

def crystal_aura(n):
    sum_1 = 0
    for element in n:
        sum_1 += int(element) 
    if sum_1 % 9 == 0:
        print("SI")
    else:
        print("NO")
    
    
n = str(input().strip())
crystal_aura(n)
