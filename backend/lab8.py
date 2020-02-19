import random, sys

def add_padding(message: bytearray):
  message.append(0x7e)
  while (len(message) * 8 + 8) % 32 != 0:
    message.append(0x00)
  message.append(0x7e)
  return message

def cut_into_blocks(message: bytearray):
  blocks = [message[i:i + 6] for i in range(0, len(message), 6)]
  return blocks

def get_gamma_block():
    return bytearray(random.getrandbits(8) for _ in range(6))

def get_gamma(blocks_count: int):
  return [get_gamma_block() for _ in range(blocks_count)]

def xor(a, b):
  return int.from_bytes(a, 'big') ^ int.from_bytes(b, 'big')

def encrypt(message_blocks, gamma_blocks):
  cypher = [xor(block[1], block[0]).to_bytes(6, 'big') for block in zip(message_blocks, gamma_blocks)]
  return cypher

def decrypt(cypher_blocks, gamma_blocks):
  message_blocks = [xor(block[0], block[1]).to_bytes(6, 'big') for block in zip(cypher_blocks, gamma_blocks)]
  return message_blocks
  
def encryptGamma(message = 'Hello world'):
  message = bytearray(message, 'utf-8')
  message = add_padding(message)
  
  message_blocks = cut_into_blocks(message)
  
  gamma_blocks = get_gamma(len(message_blocks))
  cypher_blocks = encrypt(message_blocks, gamma_blocks)
  
  gamma = (b''.join(x for x in gamma_blocks)).hex()
  encrypt_message = (b''.join(x for x in cypher_blocks)).hex()
  
  return encrypt_message, gamma

def decryptGamma(message, gamma):
  cypher_blocks = cut_into_blocks(bytearray.fromhex(message))
  gamma_blocks = cut_into_blocks(bytearray.fromhex(gamma))
  
  decrypt_blocks = decrypt(cypher_blocks, gamma_blocks)
  
  raw_message = bytearray(b''.join(x for x in decrypt_blocks))
  text = raw_message[:raw_message.find(b'\x7e')]
  text = text[:raw_message.find(b'\x00')]
  # print(sys.getdefaultencoding())
  return text.decode()
