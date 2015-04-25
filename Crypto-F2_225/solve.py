flag = [129, 60, 116, 104, 103, 54, 109, 101, 121, 111, 60, 98, 125, 57, 120, 112, 108, 131]

def b(a):
    return (a%3) + (a%5) + (a%7)

for i in range(1,19):
    flag[i-1] -= b(2**i)

print ''.join([chr(x) for x in flag])
