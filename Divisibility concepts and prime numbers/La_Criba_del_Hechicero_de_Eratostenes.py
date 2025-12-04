N = int(input())

criba = [True] * (N + 1)
criba[0] = criba[1] = False

p = 2
while p * p <= N:
    if criba[p]:
        for i in range(p * p, N + 1, p):
            criba[i] = False
    p += 1

print(sum(criba))
