#!/usr/bin/python3
"""
Tanjiro y sus compañeros se enfrentan a una Luna Superior en una batalla decisiva. El demonio comienza con una vida inicial de 
. Para vencerlo, los cazadores lanzan espadas mágicas con diferentes poderes, cada una de un solo uso.

La pelea dura exactamente 
 turnos como máximo. En cada turno ocurre lo siguiente:

Se lanza una espada con cierto poder de ataque (un entero positivo).
El demonio pierde esa cantidad de vida.
Si el demonio sigue vivo, recupera 
 puntos de vida al final del turno.
Si la vida del demonio llega a 
 o menos en algún turno, el combate termina de inmediato en victoria.
Si después de los 
 turnos el demonio sigue con vida, los cazadores serán derrotados.

Entrada
Tres enteros V,R,K
 y 
:

 V → la vida inicial del demonio.
 R → la cantidad de vida que el demonio regenera al final de cada turno (si aún está vivo).
 K → la cantidad máxima de turnos de la pelea.
Luego K enteros positivos, cada uno representando el poder de una espada en cada turno.

Salida
Si el demonio muere dentro de los K turnos, imprime VICTORIA >:3

Caso contrario, imprimir DERROTA :'(
"""



def rondas(V,R,K):
    if V <= 0:
        print("VICTORIA >:3")

    for i in range (1,K+1):
        attack = int(input().strip())
        V = V-attack
        if  V <= 0:
            print("VICTORIA >:3")
            return 0
        else:
            V = V + R
    
    if  V > 0:
        print("DERROTA :'(")
        
        

V, R, K = map(int, input().split())

rondas(V,R,K)
