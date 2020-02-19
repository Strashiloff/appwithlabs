sizeCharUnicode = 16
sizeKey = 32
sizeBlock = 64
countRounds = 8

def stringRightLength(text):
  global sizeCharUnicode, sizeBlock
  while (len(text) * sizeCharUnicode) % sizeBlock != 0:
    text += '~'
  
  return text

def stringToBinary(text):
  binstr = ''
  
  for char in text:
    binchar = format(ord(char), 'b')
    while len(binchar) < sizeCharUnicode:
      binchar = '0' + binchar
    binstr += binchar
  
  return binstr

def textIntoBlocks(text):
  global sizeBlock
  blocks = []
  
  text = stringToBinary(text)
  i = 0
  length = len(text)
  while i < length:
    blocks.append(text[i : i + sizeBlock])
    i += sizeBlock
  
  return blocks

def encodeRound(block, key):
  global sizeBlock
  c = int(len(block)/2)
  left = block[0:c]
  right = block[c:c*2]

  return right + XOR(left, func(right, key))

def decodeRound(block, key):
  global sizeBlock
  c = int(sizeBlock/2)
  left = block[0:c]
  right = block[c:sizeBlock]
  return XOR(func(left, key), right) + left
  
def XOR(s1, s2):
  result = ''
  length = len(s1)
  for i in range(length):
    a = bool(int(s1[i]))
    b = bool(int(s2[i]))
    if a ^ b:
      result += '1'
    else:
      result += '0'
      
  return result

def func(s1, s2):
  return XOR(s1, s2)  

def networkFeistelEncode(text, key):
  global countRounds
  text = stringRightLength(text)
  key = stringToBinary(key)
  blocks = textIntoBlocks(text)
  
  for i in range(countRounds):
    for i in range(len(blocks)):
      blocks[i] = encodeRound(blocks[i], key)

  result = ''
  for block in blocks:
    result += chr(int(block[0:16], 2)) + chr(int(block[16:32], 2)) + chr(int(block[32:48], 2)) + chr(int(block[48:64], 2))
  
  return result

def networkFeistelDecode(text, key):
  global countRounds
  text = stringRightLength(text)
  key = stringToBinary(key)
  blocks = textIntoBlocks(text)
  
  for i in range(countRounds):
    for i in range(len(blocks)):
      blocks[i] = decodeRound(blocks[i], key)

  result = ''
  for block in blocks:
    result += chr(int(block[0:16], 2)) + chr(int(block[16:32], 2)) + chr(int(block[32:48], 2)) + chr(int(block[48:64], 2))
  
  return result.replace('~', '')
