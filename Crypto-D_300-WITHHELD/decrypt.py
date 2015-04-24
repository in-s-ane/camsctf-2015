semi_prime = 5402781180552782668953973941046317096919389759822397332691011281833142607685445546514933124263094226119

# Credits to msieve for being awesome at factoring although it took 32 hours... LOL
p = 2387138776635375741923867468329379132354280601643
q = 2263287427372737185431258623661229697823729862967653333

print "Properly factored?", semi_prime == p * q

with open("crypto_d", "r") as f:
    c = int(f.read().encode("hex"), 16)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def generate_key():
    n = p * q
    t = (p-1) * (q-1)
    e = 0x10001 #65537
    d = modinv(e, t)
    return (n, e, d)

def decrypt():
    n, e, d = generate_key()
    flag = pow(c, d, n)
    flag = "0" + str(hex(flag)[2:-1]) # Add padding to the front of RSA decryption
    print repr(flag.decode("hex"))
    
decrypt()

'''
We initially thought that we would have to guess the public exponent, so we did a
brute force algorithm that tried every exponent up to ~800000000
Then we consulted the mods and they released a hint that it was the most common
exponent used for RSA. Using 65537 would still not work.
Afterwards we played with the padding and realized that python truncated the '0'
in the front of the decrypted hex. Adding this padding revealed the flag.

\x02i%\r\r\x03 \x03\xd0\xebK5\xa3\x1e\xb0Fr\x99?\x04L\x80\x1c\xac\x00Is it {4ll_0v3r}?
'''
