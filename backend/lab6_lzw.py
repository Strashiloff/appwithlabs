from io import StringIO

def utf8len(s):
  return len(s.encode('utf-8'))

# Алгоритм Лемпеля Зива Велча

def compress(uncompressed):
    dict_size = 1104
    dictionary = {chr(i): i for i in range(dict_size)}
    w = ''
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    
    stri = ''
    for i in result:
      stri += chr(i)
    return stri, utf8len(stri)
 
 
def decompress(compresseds):
    compressed = []
    for c in compresseds:
        compressed.append(ord(c))
        
    # Создаем словарь
    dict_size = 1104
    dictionary = {i: chr(i) for i in range(dict_size)}
    # print('dic', dictionary)
 
    # use StringIO, otherwise this becomes O(N^2)
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()
