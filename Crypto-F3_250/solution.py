f = open("cryptof3_trans", "r").read().split("\n")[:-1]

a = []

for i in f:
    a.append(int(i, 16))

result = a[0]
a = a[1:]

for i in range(len(a)):
    result = result ^ a[i]
    print ("%x" % result)

output = "%x" % (result)

print output

print ("0" + output).decode("hex")
