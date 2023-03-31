#The binascii module is being imported so as to convert bytes to integers and vice versa
# The sys module  provides the name of the existing python modules which have been imported.
import binascii
import sys
import os.path
# The left circular shift funcyion cuts off a bunch of the most significant bytes and places them in the least significant bytes
# As we know that MD5 is nade to work on 32- bits integer . The left Circular Shift is a 32 bit integer 
# This thing is being used because the string 1000 circularly shifted to left as a four -bit integer is 001 but as a 32 bit integer it is 10000  
def leftCircularShift(k,bits):
    bits = bits%32
    k = k%(2**32)
    upper = (k<<bits)%(2**32)
    result = upper | (k>>(32-(bits)))
    return(result)

# we know that the padded message is a 512 bit block, but in actaual we divide this 512 -bit blocks further into 16 blocks
# each of a size of 32 bits. 

def blockDivide(block, chunks):
    result = []
    size = len(block)//chunks
    for i in range(0, chunks):
        # Here we are using the int.from_bytes to take a sequence of bits and convert the following to an integer.
        # We had used byteorder="little" because this is a specification of MD5 algoritm
        result.append( int.from_bytes( block[i*size:(i+1)*size],byteorder="little" ))
    return(result)

#  F,G, H and I are the different logical functions 
def F(X,Y,Z):
    return( (X&Y)|((~X)&Z) )

def G(X,Y,Z):
    return( (X&Z) | (Y&(~Z)))

def H(X,Y,Z):
    return( X^Y^Z )

def I(X,Y,Z):
    return( Y^(X|(~Z)))

 # Functions FF,GG,HH,II are the functions that will mix up the data of the message with the previous output of the hash in iterations over blocks.
 # Here a,b,c,d will be the previous outputs of the compression function and M will be one 32- bit piece of a 512- bit block
def FF(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+F(b,c,d)+M+t), s)
    return(result)

def GG(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+G(b,c,d)+M+t), s)
    return(result)

def HH(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+H(b,c,d)+M+t), s)
    return(result)

def II(a,b,c,d,M,s,t):
    result = b + leftCircularShift( (a+I(b,c,d)+M+t), s)
    return(result)


# From the specifications of MD5 algoritm we know that we need to format a number as a hexadecimal value with the smallest bytes first
# The fmt 8 performs the same operation
def fmt8(num):
    bighex = "{0:08x}".format(num)
    binver = binascii.unhexlify(bighex)
    result = "{0:08x}".format(int.from_bytes(binver,byteorder='little'))
    return(result)
# The bitlen function is used to return the length of the bits
def bitlen( bitstring ):
    return(len(bitstring)*8)
