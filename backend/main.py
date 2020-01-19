import os, rsa, glob, DH
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

# @app.route('/decryptdh', methods=['POST'])
# def decryptdh():
#   global string
  
#   return jsonify(message = sr)