# Problema: Semáforos sincronizados
# Dado un semáforo central que cambia cada M segundos y una lista de N semáforos laterales,
# un semáforo lateral está correctamente sincronizado si:
#   - Su tiempo t_i es divisor de M  (M % t_i == 0)
#   - O si M es divisor de t_i      (t_i % M == 0)
# Se debe contar cuántos semáforos laterales cumplen alguna condición.
#
# Input:
#   N M
#   t1 t2 ... tN
#
# Output:
#   Número total de semáforos sincronizados.

N, M = map(int, input().split())
tiempos = list(map(int, input().split()))

contador = 0
for t in tiempos:
    if M % t == 0 or t % M == 0:
        contador += 1

print(contador)
