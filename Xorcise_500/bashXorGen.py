from itertools import product

s = "b *0x080488f2\n"
addition = "r %s-%s-%s-%s-%s\nx/s $eax\nc\n"

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for i in product(ALPHABET, repeat=5):
    a = "".join(i)
    s = s + addition % (a,a,a,a,a)

s = s + "quit"

print "DONE GENERATIOn -- WRITING"

fout = open('xorBash', "w")
fout.write(s)
