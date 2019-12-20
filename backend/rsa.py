import main, math, random, os, sys, sympy
from sympy import mod_inverse

def getPrime():
  endLim = 1048576 + 5000
  a = []
  for i in range(endLim + 1):
    a.append(i)

  a[1] = 0

  i = 2
  while i <= endLim:
    if a[i] != 0:
      j = i + i
      while j <= endLim:
        a[j] = 0
        j = j + i
    i += 1

  a = set(a)
  a.remove(0)
  return list(a)

def gcd (a, b):
  if b != 0:
	  return gcd (b, a % b)
	
  return a

def getIndex (array):
  arr = []
  for index, i in enumerate(array):
    if i >= 1048576:
      arr.append(i)
  return arr

def getRSA ():
  simples = getPrime()
  arr = getIndex(simples)
  p = arr[random.randint(1, len(arr) - 1)]
  q = arr[random.randint(1, len(arr) - 1)]
  n = p * q
  predF = (p - 1) * (q - 1)
  d = 0
  while d == 0:
    e = random.randint(1, predF)
    try:
      d = mod_inverse(e, predF)
    except:
      d = 0

  d = int(d)
  return d, e, n, predF


def encryptFile(filename, e, n, f):
  path = main.app.config['UPLOAD_FOLDER']
  mainfileRead = open(os.path.join(path, filename), 'r')
  encryptFile = open(os.path.join(path, filename.replace('.txt', '_encrypt.txt')), 'w')
  for line in mainfileRead:
    for char in line:
      m = ord(char)
      c = pow(m, e, n)
      encryptFile.write(str(c) + ' ')

  mainfileRead.close()
  encryptFile.close()
  return filename.replace('.txt', '_encrypt.txt')

def decryptFile(filename, d, n, f):
  path = main.app.config['UPLOAD_FOLDER']
  mainfileRead = open(os.path.join(path, filename), 'r')
  encryptFile = open(os.path.join(path, filename.replace('_encrypt.txt', '_decrypt.txt')), 'w')
  for line in mainfileRead:
    chars = line.split(' ')
    chars.pop(len(chars) - 1)
    for char in chars:
      c = pow(int(char), d, n)
      encryptFile.write(str(chr(c)))

  encryptFile.write('\nDecrypt file')
  mainfileRead.close()
  encryptFile.close()
  return filename.replace('_encrypt.txt', '_decrypt.txt')

"""
# Попытки сделать свои методы
"""

# def IsPrime(n):
#   d = 2
#   while n % d != 0:
#     d += 1
  
#   return d == n

# def SelectPrivateD(fn, e):
#   if math.gcd(e, fn) == 1:
#     for i in range(int(fn/3), fn):
#       if ((i*fn)+1) % e == 0:
#         print("\nK = "+str(i)+"\n")
#         d = ((i*fn)+1)/e
#         return d

#   return 0

# def pow (p, e, n):
#   binar = bin(e)
#   k = len(bin(e)) - 2
#   res = 1
#   i = 0
#   j = k - 1
#   while i < k:
#     res = res * ((p ** (2 ** i)) ** int(binar[j + 2]))
#     i+=1
#     j-=1
#   s = res % n
#   return s

# x1 = 0
# for x in range(1, predF):
#   d = (1 + x * predF) / e
#   if d.is_integer():
#     print(d)
#     x1 = x
#     break