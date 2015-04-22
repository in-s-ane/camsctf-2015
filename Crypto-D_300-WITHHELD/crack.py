import itertools

def check_prime(n, primes):
    for p in primes:
        if not n % p:
            return False
    return True

def prime_sieve():
    primes = set()
    for n in itertools.count(2):
        if check_prime(n, primes):
            primes.add(n)
            yield n

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

def generate_key(e):
    n = p * q
    t = (p-1) * (q-1)
    try:
        d = modinv(e, t)
    except:
        d = "bad"
    return (n, e, d)

o = open("primes", "r")
primes = o.read().split(" ")[1:]
primes = [int(num) for num in primes]

def crack():
    g = prime_sieve()
    for i in g:
        #print i
        n, e, d = generate_key(i)
        if d != "bad":
            try:
                flag = pow(c, d, n)
                flag = hex(flag)[2:-1].decode("hex")
                if "{" in flag and "}" in flag:
                    print i, flag
            except:
                pass
crack()
