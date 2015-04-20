f = open("crypto_2.txt", "r")
data = f.read()

c = data.split(" ")[:-1]
plain = [chr(int(ch, 16)) for ch in c]

print ''.join(plain)

'''
Going through some of our emails, I have found some suspicious documents that hint that we, Meterus 381, are {b31ng_$h4d0w3d}. Remember: [b3_s3cUrE_aNd_s7aY_s4f3]
Black Out.
'''
