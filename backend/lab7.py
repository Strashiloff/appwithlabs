import lab4

def encodeH(password):
  # password = 'testpassword'
  msg = "6A09E667BB67AE853CEEF372A54FF53A6A09E667BB67AE853CEEF372A54FF53A6A09E667BB67AE853CEEF372A54FF53A"
  msg = lab4.stringRightLength(msg)

  blocks = lab4.textIntoBlocks(password)
  key = lab4.stringToBinary(msg)
    
  for i in range(lab4.countRounds):
    for i in range(len(blocks)):
      blocks[i] = lab4.encodeRound(blocks[i], key)

  result = ''
  for block in blocks:
    i = 0
    while i < len(block):
      result += format(int(block[i:i+8], 2),'x')
      i+=8
      
  return result.upper()