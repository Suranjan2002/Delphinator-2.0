#The binascii module is being imported so as to convert bytes to integers and vice versa
# The sys module  provides the name of the existing python modules which have been imported.
import binascii
import sys
import os.path
import md5sum2 as md
import md5sum3 as md1
#This are the constants required for MD5 Hash Calculation
# This ith element of the array  is  calculated by the following formula 2**32*abs(math.sin(i+1)) , in other words the first 32 bits of sin(i) variies from i=1,2.....65.
# This number are random numbers that will be mashed with the actual maessage in various ways in the compression function

SV = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 
        0x4787c62a, 0xa8304613, 0xfd469501, 0x698098d8, 0x8b44f7af,
        0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 
        0x49b40821, 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 
        0xd62f105d, 0x2441453, 0xd8a1e681, 0xe7d3fbc8, 0x21e1cde6, 
        0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 
        0x676f02d9, 0x8d2a4c8a, 0xfffa3942, 0x8771f681, 0x6d9d6122, 
        0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70, 
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x4881d05, 0xd9d4d039,
        0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 0xf4292244, 0x432aff97,
        0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 
        0x85845dd1, 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]


def md5sum(msg):
    #First, we pad the message
    msgLen = md.bitlen(msg)%(2**64)
    # Initial message function calling
    k1=md1.initialmessagelen(msgLen)
    msg = msg + b'\x80'
    zeroPad = (448 - (msgLen+8)%512)%512
    zeroPad //= 8
    msg = msg + b'\x00'*zeroPad + msgLen.to_bytes(8,byteorder='little')
    # The padded message len
    k2=md1.messagepad(msg)
    msgLen = md.bitlen(msg)
     # Final length of the message
    k3=md1.finalmessagepad(msgLen)
    iterations = msgLen//512
    #chaining variables
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476
    #main loop
    for i in range(0,iterations):
        a = A
        b = B
        c = C
        d = D
        block = msg[i*64:(i+1)*64]
        M = md.blockDivide(block,16)
        #Rounds
        a = md.FF( a,b,c,d, M[0], 7, SV[0] )
        d = md.FF( d,a,b,c, M[1], 12, SV[1] )
        c = md.FF( c,d,a,b, M[2], 17, SV[2] )
        b = md.FF( b,c,d,a, M[3], 22, SV[3] )
        a = md.FF( a,b,c,d, M[4], 7, SV[4] )
        d = md.FF( d,a,b,c, M[5], 12, SV[5] )
        c = md.FF( c,d,a,b, M[6], 17, SV[6] )
        b = md.FF( b,c,d,a, M[7], 22, SV[7] )
        a = md.FF( a,b,c,d, M[8], 7, SV[8] )
        d = md.FF( d,a,b,c, M[9], 12, SV[9] )
        c = md.FF( c,d,a,b, M[10], 17, SV[10] )
        b = md.FF( b,c,d,a, M[11], 22, SV[11] )
        a = md.FF( a,b,c,d, M[12], 7, SV[12] )
        d = md.FF( d,a,b,c, M[13], 12, SV[13] )
        c = md.FF( c,d,a,b, M[14], 17, SV[14] )
        b = md.FF( b,c,d,a, M[15], 22, SV[15] )
        a = md.GG( a,b,c,d, M[1], 5, SV[16] )
        d = md.GG( d,a,b,c, M[6], 9, SV[17] )
        c = md.GG( c,d,a,b, M[11], 14, SV[18] )
        b = md.GG( b,c,d,a, M[0], 20, SV[19] )
        a = md.GG( a,b,c,d, M[5], 5, SV[20] )
        d = md.GG( d,a,b,c, M[10], 9, SV[21] )
        c = md.GG( c,d,a,b, M[15], 14, SV[22] )
        b = md.GG( b,c,d,a, M[4], 20, SV[23] )
        a = md.GG( a,b,c,d, M[9], 5, SV[24] )
        d = md.GG( d,a,b,c, M[14], 9, SV[25] )
        c = md.GG( c,d,a,b, M[3], 14, SV[26] )
        b = md.GG( b,c,d,a, M[8], 20, SV[27] )
        a = md.GG( a,b,c,d, M[13], 5, SV[28] )
        d = md.GG( d,a,b,c, M[2], 9, SV[29] )
        c = md.GG( c,d,a,b, M[7], 14, SV[30] )
        b = md.GG( b,c,d,a, M[12], 20, SV[31] )
        a = md.HH( a,b,c,d, M[5], 4, SV[32] )
        d = md.HH( d,a,b,c, M[8], 11, SV[33] )
        c = md.HH( c,d,a,b, M[11], 16, SV[34] )
        b = md.HH( b,c,d,a, M[14], 23, SV[35] )
        a = md.HH( a,b,c,d, M[1], 4, SV[36] )
        d = md.HH( d,a,b,c, M[4], 11, SV[37] )
        c = md.HH( c,d,a,b, M[7], 16, SV[38] )
        b = md.HH( b,c,d,a, M[10], 23, SV[39] )
        a = md.HH( a,b,c,d, M[13], 4, SV[40] )
        d = md.HH( d,a,b,c, M[0], 11, SV[41] )
        c = md.HH( c,d,a,b, M[3], 16, SV[42] )
        b = md.HH( b,c,d,a, M[6], 23, SV[43] )
        a = md.HH( a,b,c,d, M[9], 4, SV[44] )
        d = md.HH( d,a,b,c, M[12], 11, SV[45] )
        c = md.HH( c,d,a,b, M[15], 16, SV[46] )
        b = md.HH( b,c,d,a, M[2], 23, SV[47] )
        a = md.II( a,b,c,d, M[0], 6, SV[48] )
        d = md.II( d,a,b,c, M[7], 10, SV[49] )
        c = md.II( c,d,a,b, M[14], 15, SV[50] )
        b = md.II( b,c,d,a, M[5], 21, SV[51] )
        a = md.II( a,b,c,d, M[12], 6, SV[52] )
        d = md.II( d,a,b,c, M[3], 10, SV[53] )
        c = md.II( c,d,a,b, M[10], 15, SV[54] )
        b = md.II( b,c,d,a, M[1], 21, SV[55] )
        a = md.II( a,b,c,d, M[8], 6, SV[56] )
        d = md.II( d,a,b,c, M[15], 10, SV[57] )
        c = md.II( c,d,a,b, M[6], 15, SV[58] )
        b = md.II( b,c,d,a, M[13], 21, SV[59] )
        a = md.II( a,b,c,d, M[4], 6, SV[60] )
        d = md.II( d,a,b,c, M[11], 10, SV[61] )
        c = md.II( c,d,a,b, M[2], 15, SV[62] )
        b = md.II( b,c,d,a, M[9], 21, SV[63] )
        A = (A + a)%(2**32)
        B = (B + b)%(2**32)
        C = (C + c)%(2**32)
        D = (D + d)%(2**32)
        k4=md1.abuffer(A)
        k5=md1.bbuffer(B)
        k6=md1.cbuffer(C)
        k7=md1.dbuffer(D)
    result = md.fmt8(A)+md.fmt8(B)+md.fmt8(C)+md.fmt8(D)
    return(k1,k2,k3,k4,k5,k6,k7,result)