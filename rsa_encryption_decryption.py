import rsa

def generate_the_key():
    (public_key,private_key) = rsa.newkeys(1024)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(public_key.save_pkcs1('PEM'))
    with open('keys/privateKey.pem','wb') as p:
        p.write(private_key.save_pkcs1('PEM'))
    
def load_keys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey

def encrypt_message(message,key):
    return rsa.encrypt(message.encode('ascii'),key)

def decrypt_message(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign(message,key):
    return rsa.sign(message.encode('ascii'),key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

def rsa_encryption(plaintext):
    generate_the_key()
    private_key, public_key = load_keys()
    ciphertext = encrypt_message(plaintext, public_key)
    signature = sign(plaintext, private_key)
    text = decrypt_message(ciphertext, private_key)
    if text:
        return (ciphertext,signature,text)
    else:
        text = 'Cant be decrypted '
        return (ciphertext,signature,text)

'''   
generate_the_key()
privateKey, publicKey =load_keys()
message = input('Write your message here:')
ciphertext = encrypt_message(message, publicKey)
signature = sign(message, privateKey)
text = decrypt_message(ciphertext, privateKey)
print(f'Cipher text: {ciphertext}')
print(f'Signature: {signature}')
if text:
    print(f'Message text: {text}')
else:
    print(f'Unable to decrypt the message.')

if verify(text, signature, publicKey):
    print('Successfully verified signature')
else:
    print('The message signature could not be verified')
'''