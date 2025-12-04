def is_prime(N):
    # Caso especial: 0, 1, negativos → NO primos
    if N <= 1:
        print("Rechazado")
        return
    
    # Probar divisores desde 2 hasta sqrt(N)
    limite = int(N ** 0.5) + 1
    for n in range(2, limite):
        if N % n == 0:
            print("Rechazado")
            return
    
    # Si no encontramos divisor, es primo
    print("Aprobado")


N = int(input().strip())
is_prime(N)
