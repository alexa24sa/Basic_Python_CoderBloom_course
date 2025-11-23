#!/usr/bin/python3

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
