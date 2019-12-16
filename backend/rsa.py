import main, math, random, os, sympy

def getPrime():
  endLim = 100
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

def IsPrime(n):
  d = 2
  while n % d != 0:
    d += 1
  
  return d == n

def getRSA ():
  simples = getPrime()
  p = simples[random.randint(0, len(simples) - 1)]
  q = simples[random.randint(0, len(simples) - 1)]
  n = p * q
  predF = (p - 1) * (q - 1)
  gcdr = 0
  while gcdr != 1:
    e = random.randint(1, predF)
    if sympy.isprime(e):
      gcdr = gcd(e, predF)

  d = 0.1
  for x in range(1, predF):
    v = (1 + x * predF) / e
    if v.is_integer():
      d = int(v)
      break
  return d, e, n, predF

def pow (p, e, n):
  binar = bin(e)
  k = len(bin(e)) - 2
  res = 1
  i = 0
  j = k - 1
  while i < k:
    res = res * ((p ** (2 ** i)) ** int(binar[j + 2]))
    i+=1
    j-=1
  s = res % n
  return s

def encryptFile(filename, e, n, f):
  path = main.app.config['UPLOAD_FOLDER']
  mainfileRead = open(os.path.join(path, filename), 'r')
  encryptFile = open(os.path.join(path, filename.replace('.txt', '_encrypt.txt')), 'w')
  for line in mainfileRead:
    for char in line:
      m = ord(char)
      c = pow(m, e, n)
      encryptFile.write(str(chr(c)))

  mainfileRead.close()
  encryptFile.close()
  return filename.replace('.txt', '_encrypt.txt')

def decryptFile(filename, d, n, f):
  path = main.app.config['UPLOAD_FOLDER']
  mainfileRead = open(os.path.join(path, filename), 'r')
  encryptFile = open(os.path.join(path, filename.replace('_encrypt.txt', '_decrypt.txt')), 'w')
  for line in mainfileRead:
    for char in line:
      m = ord(char)
      c = pow(m, d, n)
      encryptFile.write(str(chr(c)))
  encryptFile.write('\nDecrypt file')
  mainfileRead.close()
  encryptFile.close()
  return filename.replace('_encrypt.txt', '_decrypt.txt')