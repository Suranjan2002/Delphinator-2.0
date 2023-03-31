MORSE_CODE_DICT = { 
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 
    'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 
    'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 
    'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', 
    '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
      '7':'--...', '8':'---..', '9':'----.', '0':'-----',',':'--..--','?':'..--..',
      '.':'.-.-.-',':':'---...', '/':'-..-.','-':'-....-','(':'-.--.',')':'-.--.-'}

def encrypt_morse(plaintext):
    cipher_text =''
    for letter in plaintext:
        if letter != ' ':
            cipher_text += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher_text += ' '
    return cipher_text


def decrypt_morse(cipher_text):
    cipher_text += ' '
    plain_text = ''
    decipher = ''
    citext = ''
    for letter in cipher_text:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher
'''
# Example usage
message = "HELLO WORLD"
encrypted_message = encrypt_morse(message)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt_morse(encrypted_message)
print("Decrypted message:", decrypted_message)
'''
