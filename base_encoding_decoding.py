import base64

def base64_encode(plaintext):
    plaintext_bytes = plaintext.encode('utf-8')
    base64_encoded_bytes = base64.b64encode(plaintext_bytes)
    base64_text = base64_encoded_bytes.decode('utf-8')
    return base64_text

def base64_decode(encoded_text):
    encodedtext_bytes = encoded_text.encode('utf-8')
    plain_text_bytes = base64.b64decode(encodedtext_bytes)
    plain_text = plain_text_bytes.decode('utf-8')
    return plain_text

def base32_encode(plaintext):
    plaintext_bytes = plaintext.encode('utf-8')
    base64_encoded_bytes = base64.b32encode(plaintext_bytes)
    base64_text = base64_encoded_bytes.decode('utf-8')
    return base64_text

def base32_decode(encoded_text):
    encodedtext_bytes = encoded_text.encode('utf-8')
    plain_text_bytes = base64.b32decode(encodedtext_bytes)
    plain_text = plain_text_bytes.decode('utf-8')
    return plain_text
'''
def base_encoding_decoding(plaintext):
    b64_encode = base64_encode(plaintext)
    b64_decode = base64_decode(b64_encode)
    b32_encode = base32_encode(plaintext)
    b32_decode = base32_decode(b32_encode)

    print(f"Palintext: {plaintext}")
    print(f"Base64 Encoded: {b64_encode}")
    print(f"Base64 Decode: {b64_decode}")
    print(f"Base32 Encode {b32_encode}")
    print(f"Base32 Decode: {b32_decode}")

base_encoding_decoding('This is a big brown fox')
'''