import math
import random
import numpy as np

def to_bits(stroka):
  result = []
  for c in stroka:
    b = bin(ord(c))[2:]
    b = '00000000'[len(b):] + b
    result.extend([int(bits) for bits in b])
  return result

def xor(x: int, y: int):
  if x != y:
    return 1
  else:
    return 0

def check(s):
  bits = to_bits(s)

  blocks = [bits[d:d + 4] for d in range(0, len(bits), 4)]

  # Порождающая матрица (первая часть единичная матрица + вторая часть по схеме уменьшения двоичного числа)
  G = np.array([[1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0], [0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0, 1, 1]])

  # Матрица проверки четности
  P = np.array([[1, 1, 1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 0], [1, 1, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0, 0, 1]])

  R = []
  for i in range(4):
    if blocks[2][i] == 1:
      T = []
      for j in range(8):
        T.append(G[i][j])
      R.append(T)
      
  # Суммирование строк для построения блочного кода
  RT = []
  for i in range(len(R)):
    RT.append([])
    for j in range(len(R[i])):
      RT[i].append(int(R[i][j]))
  
  P1 = []
  for i in range(8):
    PT = 0
    for j in range(len(R)):
      PT += int(R[j][i])
    P1.append(PT)

  for i in range(4,8):
    if P1[i] % 2 == 0:
      P1[i] = 0
    if not(P1[i] % 2 == 0):
      P1[i] = 1

  #Линейный блочный код
  P1_2 = []
  for i in range(len(P1)):
    P1_2.append(P1[i])

  # Генерация ошибки
  P1[2] = 0

  P1_1 = list(P1)

  # Проверки на четность
  # Для того, чтобы определить, в каком конкретно разряде произошла ошибка, нам необходимо узнать «синдром ошибки».
  # Синдром ошибки вычисляется методом проверок по ненулевым позициям проверочной матрицы на чётность.
  S1 = P1[0] + P1[1] + P1[2] + P1[3] + P1[4]
  S2 = P1[0] + P1[1] + P1[2] + P1[5]
  S3 = P1[0] + P1[1] + P1[3] + P1[6]
  S4 = P1[0] + P1[2] + P1[3] + P1[7]

  if S1 % 2 == 0:
    S1 = 0
  else:
    S1 = 1

  if S2 % 2 == 0:
    S2 = 0
  else:
    S2 = 1

  if S3 % 2 == 0:
    S3 = 0
  else:
    S3 = 1

  if S4 % 2 == 0:
    S4 = 0
  else:
    S4 = 1

  # Синдром ошибки
  mas_s = [S1, S2, S3, S4]
  index_j = 0
  for i in range(8):
    if (P[0][i] == mas_s[0]) and (P[1][i] == mas_s[1]) and (P[2][i] == mas_s[2]) and (P[3][i] == mas_s[3]):
      index_j = i

  # Разряд ошибки
  index_error = index_j+1
  if P1[index_j] == 0:
    P1[index_j] = 1
  else:
    P1[index_j] = 0

  # Исправленный код
  fix_code = []
  for i in range(len(P1)):
    fix_code.append(P1[i])
 
  first_code = []
  # Исходный блок кода
  for i in range(4):
    first_code.append(P1[i])

  return bits, blocks, G, P, RT, P1_2, P1_1, mas_s, index_error, fix_code, first_code
