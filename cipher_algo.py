#====================================================================================================================
#                                               CAESAR LAYER
#====================================================================================================================
#A python program to illustrate Caesar Cipher Technique
def CAESAR_ENCRYPT(plaintext,key):
    result = ""
    #Traversing and proccessing every character in the text
    #From Left to Right
    for i in range(len(plaintext)):
        char = plaintext[i]
 
        #To Encrypt the UPPERCASE characters
        #If the user has entered Uppercase characters in the supplied string
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        #To acknowledge the space entered in the user supplied string
        elif char == ' ':
            result += ' '
        #To Encrypt the lowercase characters
        #If the user has entered Lowercase chaaracters in the supplied string
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
 
    return(result)
# Function to decode the caesar cipher
def CAESAR_DECODE(encrypted, key):
    result = ""
    for i in range(len(encrypted)):
        char = encrypted[i]
        if (char.isupper()):
            result += chr((ord(char) - key-65) % 26 + 65)
        #To acknowledge the space entered in the user supplied string
        elif char == ' ':
            result += ' '
        #To Decrypt the lowercase characters
        #If the user has entered Lowercase chaaracters in the supplied string
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return (result)
#For step testing purpose, call the function by -------------> CAESAR(plaintext,key)

#======================================================================================================================
#                                               VIGENERE LAYER
#======================================================================================================================
"""
The CT function remits the 
encrypted text generated with the
help of the key generated.
"""
def VIGENERE_ENCRYPT(plaintext, key):
    """
    Encrypts plaintext using the Vigenere cipher with the given key.
    """
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext
def VIGENERE_DECRYPT(ciphertext, key):
    """
    Decrypts ciphertext using the Vigenere cipher with the given key.
    """
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                plaintext += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            else:
                plaintext += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

#cipherText(plaintext,KEYGEN(plaintext,vkey))

#====================================================================================================================
#                                               RAIL FENCE LAYER
#====================================================================================================================
def RAIL(text,key):
    rail = [['\n' for i in range(len(text))]
                for j in range(key)]
     
    # to find the direction
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
         
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
         
        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1
         
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher
    # using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
def RAILFENCE_DECRYPT(cipher, key):
 
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
     
    # to find the direction
    dir_down = None
    row, col = 0, 0
     
    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        # place the marker
        rail[row][col] = '*'
        col += 1
         
        # find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
             
    # now we can construct the fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    # now read the matrix in zig-zag manner to construct  the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
#====================================================================================================================
#                                                     DRIVER
#====================================================================================================================
def call(plaintext, CRkey):
    CC = CAESAR_ENCRYPT(plaintext,CRkey)
    vkeyword = CC.split()
    vkey = str(CRkey)
    VC = VIGENERE_ENCRYPT(CC, vkey)
    RFC = RAIL(VC,CRkey)
    print(CC)
    print(VC)
    print(RFC)
    return(CC,VC,RFC)
def decrypt_text(encrypted, CRkey):
    railFence_Decode = RAILFENCE_DECRYPT(encrypted, CRkey)
    vignere_decode = VIGENERE_DECRYPT(railFence_Decode, str(CRkey))
    caesar_decode = CAESAR_DECODE(vignere_decode, CRkey)
    print(caesar_decode)
    return(railFence_Decode, vignere_decode, caesar_decode)
#print(RAIL())
#call('Suranjan Saha is a good boy',12)
#decrypt_text('Itlf hesrxed paqq ej yI rrx',12)