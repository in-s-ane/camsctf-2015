f = open("crypto_1.txt", "r")
data = f.read()

c = data.split(" ")
plain = [chr(int(ch, 2)) for ch in c]

print ''.join(plain)

'''
I think I'm being watched. For now, Mr. Browning, let us communicate in {7h1s_1np3n37r3bl3_c0d3}. 
Ninteenus Out. 
'''
