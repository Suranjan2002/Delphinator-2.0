#IMPORT LIBRARIES
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import cipher_algo as calgo
import mainmd5 as mmd
from datetime import datetime
import rotation_cipher as rot
import rsa_encryption_decryption as rs
import morse_code as morse
import base_encoding_decoding as bs

app = Flask(__name__)

#DEFAULT ROUTE
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

'''------------------------------ COMBINATIONAL CIPHER ------------------------------'''
#COMBINATIONAL CIPHER ROUTE
@app.route("/combo_cipher", methods=['GET', 'POST'])
def cipher():
    return render_template('combo_cipher.html')

#COMBINATIONAL CIPHER ENCRYPTION ROUTE
@app.route("/combo_cipher_encrypt", methods=['GET', 'POST'])
def cipher_encrypt():
    if (request.method=='POST'):
        plaintext=request.form.get('cptext')
        crkey=request.form.get('ckey')
        crkey=int(crkey)
        ls=[]
        ls=calgo.call(plaintext,crkey)
        return render_template('combo_cipher_encrypt.html', ptext=plaintext, key=crkey, cresult=ls)
    return render_template('combo_cipher.html')

#COMBINATIONAL CIPHER DECRYPTION ROUTE
@app.route("/combo_cipher_decrypt", methods=['GET', 'POST'])
def cipher_decrypt():
    if (request.method=='POST'):
        ciphertext=request.form.get('cptext')
        crkey=request.form.get('ckey')
        crkey=int(crkey)
        ls=[]
        ls=calgo.decrypt_text(ciphertext,crkey)
        return render_template('combo_cipher_decrypt.html', ptext=ciphertext, key=crkey, cresult=ls)
    return render_template('combo_cipher.html')


'''------------------------------ MD5 HASH ------------------------------'''
#MD5 HASH ROUTE
@app.route("/md5hash", methods=['GET', 'POST'])
def hash():
    if request.method=="POST":
        plaintext=request.form.get('plaintext')
        ls2=[]
        ls2=mmd.main(plaintext)
        return render_template('md5hash_display.html', ptext=plaintext, hresult=ls2)
    return render_template('md5hash.html')


'''------------------------------ ROT13 CIPHER ------------------------------'''
#ROT13 CIPHER ROUTE
@app.route("/rot13", methods=['GET', 'POST'])
def rot_cipher():
    return render_template('rot13.html')

#ROT13 CIPHER ENCRYPTION ROUTE
@app.route("/rot13_encrypt", methods=['GET', 'POST'])
def rotation_cipher_encrypt():
    if request.method == "POST":
        plaintext = request.form.get('rptext')
        rot_key = request.form.get('rotkey')
        rot_key = int(rot_key)
        ls3 = rot.rotate_encode(plaintext, rot_key)
        return render_template('rot13_encrypt.html',ptext=plaintext, key=rot_key, rotresult=ls3)
    return render_template('rot13.html')

#ROT13 CIPHER DECRYPTION ROUTE
@app.route("/rot13_decrypt", methods=['GET', 'POST'])
def rotation_cipher_decrypt():
    if request.method == "POST":
        plaintext = request.form.get('rptext')
        rot_key = request.form.get('rotkey')
        rot_key = int(rot_key)
        ls3 = rot.rotate_decode(plaintext, rot_key)
        return render_template('rot13_decrypt.html',ptext=plaintext, key=rot_key, rotresult=ls3)
    return render_template('rot13.html')


'''------------------------------ RSA CIPHER ------------------------------'''
#RSA CIPHER ROUTE
@app.route("/rsa", methods=['GET', 'POST'])
def rsa_encryption():
    if request.method == "POST":
        plaintext = request.form.get('rsa_text')
        ls4 = []
        ls4 = rs.rsa_encryption(plaintext)
        return render_template('rsa_display.html', ptext=plaintext, rsaresult=ls4)
    return render_template('rsa.html')


'''------------------------------ MORSE CODE ------------------------------'''
#MORSE CODE ROUTE
@app.route("/morse_code", methods=['GET','POST'])
def morse_page():
    return render_template('morse.html')

#MORSE CODE ENCRYPTION ROUTE
@app.route("/morse_encrypt", methods=['GET','POST'])
def morse_encode():
    if request.method == "POST":
        plaintext = request.form.get('morse_text')
        ls5 = morse.encrypt_morse(plaintext)
        print(ls5)
        return render_template('morse_encrypt.html', ptext=plaintext, mencoderes=ls5)
    return render_template('morse.html')

#MORSE CODE DECRYPTION ROUTE
@app.route("/morse_decrypt", methods=['GET','POST'])
def morse_decode():
    if request.method == "POST":
        morse_text = request.form.get('morse_text')
        ls6 = morse.decrypt_morse(morse_text)
        return render_template('morse_decrypt.html', ptext=morse_text, mdecoderes=ls6)
    return render_template('morse.html')

'''------------------------------ BASE CIPHER ------------------------------'''
#BASE CIPHER ROUTE
@app.route("/base", methods=['GET', 'POST'])
def base_encrption():
    return render_template('base.html')

#BASE64 ENCRYPTION ROUTE
@app.route("/base64_encrypt", methods=['GET', 'POST'])
def base64_encoder():
    if request.method == "POST":
        plain_text = request.form.get('base_text')
        ls7 = bs.base64_encode(plain_text)
        return render_template('base64_encrypt.html', ptext=plain_text, basencoder=ls7)
    return render_template('base.html')

#BASE32 ENCRYPTION ROUTE
@app.route("/base32_encrypt", methods=['GET', 'POST'])
def base32_encoder():
    if request.method == "POST":
        plain_text = request.form.get('base_text')
        ls8 = bs.base32_encode(plain_text)
        return render_template('base32_encrypt.html', ptext=plain_text, basencoder=ls8)
    return render_template('base.html')

#BASE64 DECRYPTION ROUTE
@app.route("/base64_decrypt", methods=['GET', 'POST'])
def base64_decoder():
    if request.method == "POST":
        base64_text = request.form.get('base_text')
        ls9 = bs.base64_decode(base64_text)
        return render_template('base64_decrypt.html', ptext=base64_text, basedecoder=ls9)
    return('base.html')

#BASE32 DECRYPTION ROUTE
@app.route("/base32_decrypt", methods=['GET', 'POST'])
def base32_decoder():
    if request.method == "POST":
        base32_text = request.form.get('base_text')
        ls10 = bs.base32_decode(base32_text)
        return render_template('base32_decrypt.html', ptext=base32_text, basedecoder=ls10)
    return('base.html')

#MAIN METHOD
if __name__=='__main__':
    app.run(debug=True)