import math, random, os, sys, utils

g, p = 0, 0 # public
a, b = 0, 0 # private
A, B = 0, 0
K1, K2 = 0, 0

def getDH():
  global g, p, a, b, A, B, K1, K2
  simpes = utils.getPrime(0)
  arr = utils.getIndex(simpes, 0)
  i = random.randint(1, len(arr) - 1)
  g = arr[i]
  arr.pop(i)
  p = arr[random.randint(1, len(arr) - 1)]

  simpes = utils.getPrime(4096)
  arr = utils.getIndex(simpes, 4096)
  index = random.randint(1, len(arr) - 1)
  a = arr[index]
  arr.pop(index)
  b = arr[random.randint(1, len(arr) - 1)]
  A = pow(g, a, p)
  B = pow(g, b, p)
  K1 = pow(B, a, p)
  K2 = pow(A, b, p)
  return g, p, a, b, A, B, K1, K2

def encrypt(text):
  global K1
  encrypt_text = ''
  key = K1
  for char in text:
    encrypt_text += chr(ord(char) + key) 

  return encrypt_text

def decrypt(text):
  global K2
  decrypt_text = ''
  key = K2
  for char in text:
    decrypt_text += chr(ord(char) - key)

  return decrypt_text