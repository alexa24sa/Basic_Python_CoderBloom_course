# Problema: Para cada región contar cuántas especies únicas capturó Ash
# y luego listar las especies capturadas exclusivamente en la primera región.

R = int(input())

regiones = []
unicos_por_region = []

for _ in range(R):
    N = int(input())
    especies = input().split()
    conjunto = set(especies)
    regiones.append(conjunto)
    unicos_por_region.append(len(conjunto))

for c in unicos_por_region:
    print(c)

otros = set()
for i in range(1, R):
    otros |= regiones[i]

exclusivas_primera = regiones[0] - otros

if exclusivas_primera:
    print(" ".join(sorted(exclusivas_primera)))
else:
    print("Ninguno")
