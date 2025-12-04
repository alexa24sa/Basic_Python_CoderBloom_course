"""
Descripción:
Finn y Jake han entrado en una misteriosa mazmorra de Ooo. La mazmorra está formada por salas,
y cada sala contiene uno de los siguientes valores:
0 → una sala vacía
1 → un enemigo
2 → un tesoro

La mazmorra se representa como una matriz de enteros.

El programa debe realizar:
1. Recorrer toda la mazmorra y contar cuántos enemigos (1) y cuántos tesoros (2) hay en total.
2. Leer dos enteros F y C (fila y columna) que representan la sala que Finn y Jake quieren explorar.
   - Si la sala contiene un 1, imprimir: "¡Finn se enfrenta a un enemigo!"
   - Si contiene un 2, imprimir: "¡Jake encontró un tesoro!"
   - Si contiene un 0, imprimir: "La sala está vacía..."

Entrada:
- Dos enteros N y M: número de filas y columnas.
- N líneas, cada una con M enteros que representan la matriz de la mazmorra.
- Finalmente, dos enteros F y C indicando la posición a explorar (índices desde 0).

Salida:
- Una línea con dos enteros: total de enemigos y total de tesoros.
- Una segunda línea con el mensaje correspondiente a la sala en la posición (F, C).

Ejemplo:
Entrada:
3 3
0 1 2
2 0 1
0 0 2
1 2

Salida:
2 3
Jake encontró un tesoro!
"""


# 1) Leer N y M (filas y columnas)
N, M = map(int, input().split())

# 2) Leer la matriz de la mazmorra
mazmorra = []
for _ in range(N):
    fila = list(map(int, input().split()))  # cada fila tiene M enteros
    mazmorra.append(fila)

# 3) Contar enemigos (1) y tesoros (2)
enemigos = 0
tesoros = 0

for i in range(N):
    for j in range(M):
        if mazmorra[i][j] == 1:
            enemigos += 1
        elif mazmorra[i][j] == 2:
            tesoros += 1
            
        # TODO: si la celda es 1, aumenta enemigos
        # TODO: si la celda es 2, aumenta tesoros
        pass

# 4) Imprimir primera línea: total de enemigos y total de tesoros
print(f"{enemigos} {tesoros}")
# TODO: imprime enemigos y tesoros en una sola línea separados por espacio


# 5) Leer F y C (posición que Finn y Jake quieren revisar)
F, C = map(int, input().split())

# 6) Revisar el contenido de esa sala y mostrar el mensaje correcto
valor = mazmorra[F][C]

if valor == 1:
    # TODO: imprimir exactamente "¡Finn se enfrenta a un enemigo!"
    print("¡Finn se enfrenta a un enemigo!")
    pass
elif valor == 2:
    # TODO: imprimir exactamente "¡Jake encontró un tesoro!"
    print("¡Jake encontró un tesoro!")
    pass
else:
    # TODO: imprimir exactamente "La sala está vacía..."
    print("La sala está vacía...")
    pass
