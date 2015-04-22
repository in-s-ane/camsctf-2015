import bz2

'''
We notice that in the first few bytes of the output of loop are
\x00\x00\x68\x39\x31\x41\x59\x26\x53\x59 which is \x00\x00h91AY&SY.
This is very similar to the file header of a bz2 compressed file, except that
the beginning BZ is replaced with \x00\x00. Running this decompression 501
(it was supposed to only be 500, but whatever LOL) got us the flag
'''

with open("loop", "r") as f:
    data = f.read()
    for i in range(0, 501):
        data = "BZ" + data[2:]
        data = bz2.decompress(data)
        print i
    print data

# Flag: {many_many_many_decompressions_later.......}
