"""
Descripción:
Ember está aprendiendo a programar y escribió todo su código ¡en una sola línea!,
pero no sabe si colocó bien los paréntesis. Tu tarea es ayudarla revisando
cuáles paréntesis le faltan.

Entrada:
Una sola línea que contiene el código de Ember.

Salida:
- Si los paréntesis están balanceados, imprimir:   Todo bien :3
- Si faltan paréntesis de apertura '(' (es decir, aparece un ')' sin su '('),
  debes reportar un '(' por cada uno en el orden en que se detecten.
- Si faltan paréntesis de cierre ')' (quedan '(' sin pareja al final),
  debes reportar un ')' por cada uno, al final.
- Los paréntesis faltantes se imprimen todos juntos, en una sola línea,
  en el orden en que se fueron detectando.

Ejemplos:

Entrada:
for()(()(
Salida:
))

Entrada:
int emberseestaenojando()
Salida:
Todo bien :3
"""

linea = input()

pila = []
faltantes = []

for ch in linea:
    if ch == '(':
        pila.append('(')
    elif ch == ')':
        if pila:
            pila.pop()
        else:
            # Falta un paréntesis de apertura antes de este ')'
            faltantes.append('(')

# Por cada '(' que quedó sin cerrar, falta un ')'
for _ in range(len(pila)):
    faltantes.append(')')

if faltantes:
    print("".join(faltantes))
else:
    print("Todo bien :3")
