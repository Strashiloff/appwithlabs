def getPrime(num):
  endLim = num + 5000
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

def getIndex (array, num):
  arr = []
  for index, i in enumerate(array):
    if i >= num:
      arr.append(i)
  return arr
