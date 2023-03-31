def rotate_string(plaintext, rotation):
    """
    Rotates the characters in a string by a given amount.
    """
    rotated = ''
    for char in plaintext:
        if char.isalpha():
            # Determine the ASCII value of the first letter in the alphabet (uppercase or lowercase)
            first_letter = 'A' if char.isupper() else 'a'
            # Determine the number of positions to rotate based on the given amount
            positions = (ord(char) - ord(first_letter) + rotation) % 26
            # Convert the rotated ASCII value back to a character and add it to the output
            rotated += chr(ord(first_letter) + positions)
        elif char.isdigit():
            # Determine the number of positions to rotate based on the given amount
            positions = (int(char) + rotation) % 10
            # Convert the rotated number back to a character and add it to the output
            rotated += str(positions)
        else:
            # Non-alphabetic and non-nuhttp://web.whatsapp.com/meric characters are not rotated
            rotated += char
    return rotated

def rotate_encode(plaintext, key):
    return rotate_string(plaintext, key)
def rotate_decode(ciphertext, key):
    return rotate_string(ciphertext, -key)

def rotation_cipher(plaintext, key):
    encoded_text = rotate_encode(plaintext, key)
    decoded_text = rotate_decode(encoded_text, key)
    #print(encode_text)
    #print(decoded_text)
    return (encoded_text, decoded_text)

#rotation_cipher('Suranjan', 47)