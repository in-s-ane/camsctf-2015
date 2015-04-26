f = open("usb_data.txt", "r")
data = f.readlines()

binary = []

for d in data:
    movement = d.strip().split(":")
    all_zeros = True
    for i in movement:
        if int(i, 16) != 0:
            all_zeros = False
    if all_zeros:
        continue
    if movement[0] == "01":
        binary.append("0")
    elif movement[0] == "02":
        binary.append("1")

binary_string = ''.join(binary)
n = int(binary_string, 2)
flag = ("%x" % n).decode("hex")
print flag

# Flag: {cl1ck_c1ick}
