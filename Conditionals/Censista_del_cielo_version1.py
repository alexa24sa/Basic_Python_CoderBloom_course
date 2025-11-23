#!/usr/bin/python3
"""
Dada la temperatura de una estrella, ayuda a determinar la clase que le corresponde de acuerdo al sistema de clasificación de Harvard.

Entrada
Un entero 
 que indica la temperatura en grados Kelvin (K) de una estrella.

Salida
Una letra que indica la clase de estrella de acuerdo al sistema de clasificación de Harvard.

Ejemplo
Entrada	Salida	Descripción
5778
G
El sol es una estrella con una temperatura de 5,772 °K por lo que es considerado una estrella clase G.

"""



def temp_estrellas(T):
  if T >= 33000:
    print("O")
  elif T in range (10000, 33000):
    print('B')
  elif T in range (7500, 10000):
    print('A')
  elif T in range (6000, 7500):
    print('F')
  elif T in range (5200, 6000):
    print('G')
  elif T in range (3700, 5200):
    print('K')
  elif T in range (2500, 3700):
    print('M')
    
T = int(input().strip())
temp_estrellas(T)
