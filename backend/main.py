import os, rsa, glob, DH, lab4, lab6_huffman, lab6_lzw
from lab7 import encodeH
from lab5 import check
from lab8 import encryptGamma, decryptGamma
from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS

UPLOAD_FOLDER = os.path.abspath('') + '/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app, expose_headers=["x-suggested-filename"])

# rsa
d = 0
e = 0
n = 0
f = 0
mainfile = ''
encryptfile = ''
decryptfile = ''
# rsa

# DH
string = ''
# DH

def saveFile ():
  path = app.config['UPLOAD_FOLDER']
  if not os.path.isdir(path):
    os.makedirs(path)
  filelist = glob.glob(os.path.join(path, "*"))
  for f in filelist:
    os.remove(f)
  file = request.files["file"]
  file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
  return file.filename

@app.route('/', methods=['GET', 'POST'])
def index ():
  global mainfile, e, n, d, f
  mainfile = saveFile()
  d, e, n, f = rsa.getRSA()
  return jsonify(private = d, public = e, n = n)

@app.route('/encrypt', methods=['POST'])
def getFileEncrypt():
  global mainfile, d, e, n, encryptfile, decryptfile
  encryptfile = rsa.encryptFile(mainfile, e, n, d)
  decryptfile = rsa.decryptFile(encryptfile, d, n, f)
  response = send_file(os.path.join(app.config['UPLOAD_FOLDER'], encryptfile), as_attachment = True)
  response.headers['x-suggested-filename'] = encryptfile
  return response

@app.route('/decrypt', methods=['POST'])
def getFileDecrypt():
  global decryptfile
  response = send_file(os.path.join(app.config['UPLOAD_FOLDER'], decryptfile), as_attachment = True)
  response.headers['x-suggested-filename'] = decryptfile
  return response

@app.route('/getdh', methods=['POST'])
def getdh():
  g, p, a, b, A, B, K1, K2 = DH.getDH()
  return jsonify(g = g, p = p, a = a, b = b, A = A, B = B, K1 = K1, K2 = K2)

@app.route('/encryptdh', methods=['POST'])
def encryptdh():
  string = DH.encrypt(request.json['text'])
  sr = DH.decrypt(string)
  return jsonify(encrypt = string, decrypt = sr)

@app.route('/feistel', methods=['POST'])
def feistel():
  key = request.json['key']
  # key = '1C'
  # text = '䱌Это пример текста для шифрования с помощью блочного алгоритма'
  res = lab4.networkFeistelEncode(request.json['text'], key)
  r = lab4.networkFeistelDecode(res, key)
  return jsonify( encode = res, decode = r, key = key)

@app.route('/lab5', methods=['POST'])
def lab5():
  st = request.json['text']
  bits, blocks, G, P, R, P1_1, P1, mas_s, index_error, fix_code, first_code = check(st)
  return jsonify(bits = bits, blocks = blocks, G = G.tolist(), P = P.tolist(), R = R, P1 = P1_1, P1_error = P1, mas_s = mas_s, index_error = index_error, fix_code = fix_code, first_code = first_code)

@app.route('/lab6', methods=['POST'])
def lab6():
  # st = 'Hello world! Hello world! Hello world!'
  st = request.json['text']
  size = lab6_lzw.utf8len(request.json['text'])
  encodedLzw, encodeSize = lab6_lzw.compress(st)
  encodeSize = lab6_lzw.utf8len(encodedLzw)
  encodedHuff, code = lab6_huffman.huffman_encode(encodedLzw)
  decoceHuff = lab6_huffman.huffman_decode(encodedHuff, code)
  decoceLzw = lab6_lzw.decompress(decoceHuff)
  return jsonify(encodedLzw = encodedLzw, size = size, encodeSize = encodeSize, encodedHuff = encodedHuff, codes = code, decoceHuff = decoceHuff, decoceLzw = decoceLzw)

@app.route('/lab7', methods=['POST'])
def lab7():
  pas = request.json['text']
  hashPass = encodeH(pas)
  return jsonify(hashPass = hashPass)
  
@app.route('/lab8', methods=['POST'])
def lab8():
  st = request.json['text']
  mes, gamm = encryptGamma(st)
  res = decryptGamma(mes, gamm)
  return jsonify( encrypt = mes, gamma = gamm, decrypt = res)
