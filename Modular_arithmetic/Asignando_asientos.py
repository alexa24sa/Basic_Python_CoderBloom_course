"""
PROBLEMA: Asignación de Asientos en un Auditorio

En un auditorio hay M filas y cada fila tiene N asientos.  
Los boletos están numerados consecutivamente empezando en 1, 
llenando primero toda la Fila 1 de izquierda a derecha (asientos 1 a N), 
luego la Fila 2, y así sucesivamente.

Dado:
- B → número de boleto de un asistente,
- M → número total de filas del auditorio,
- N → número de asientos por fila,

escribe un programa que determine en qué FILA (F) y en qué ASIENTO (A) 
debe sentarse dicho asistente.

SALIDA ESPERADA:
Dos números F A indicando:
F = número de fila donde se sienta el asistente
A = número de asiento dentro de la fila

EJEMPLO:
Entrada:
9
5 4

Salida:
3 1

Explicación:
En un auditorio de 5 filas y 4 asientos por fila, el boleto #9 
corresponde al primer asiento de la fila 3.
"""

def assinging_seat(b, M, N):
    # Recorremos asiento por asiento en orden creciente
    counter = 0  # Cuenta cuántos asientos se han pasado
    
    for rows in range(1, M + 1):       # Recorrer las filas
        for seats in range(1, N + 1):  # Recorrer los asientos dentro de cada fila
            counter += 1               # Avanzamos un asiento en la numeración global
            
            # Cuando el contador coincide con el boleto B, encontramos su asiento
            if counter == b:
                return (seats, rows)   # Retornamos asiento y fila (A, F)

# --- Entrada ---
b = int(input().strip())          # Número de boleto
M, N = map(int, input().split())  # M filas, N asientos por fila

# --- Procesamiento ---
c, f = assinging_seat(b, M, N)    # c = asiento, f = fila

# --- Salida ---
print(f"{f} {c}")                 # Imprimir como "Fila Asiento"
