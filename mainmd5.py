# MD5 is a popular HAshing algoritm and is used for checking the integrity of data
     # The algoritm is as follows
     # The algoritm first pads the message with a '1' bit then a bunch of Zeros until the padded message length in bits is congruent to 448 modulo 512 that is(448%512).
     # Then finally a 64 bit representation of the length of the original message modulo 2^64 is appended to the message in the byteorder="little"( that is the last byte of binary representation of the multibyte data-type is stored first).
     #  The message is then flushed in various intricate ways , one 512-bit block at a time. 
     #  Then the message passes through the various transformation (here the transformation functions is FF, GG, HH and II) is called a round. There are in total 64 of them.
     # The result of these 64 rounds are added to a tally modulo 2^32, and the final result of the four makes the hash


import md5algo as md2
def main(message):
     t=[]
     t=md2.md5sum(message.encode('utf-8'))
     return(t)
