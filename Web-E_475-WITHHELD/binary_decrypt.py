binary = "01101101111110011110111110110011011000001000000110000000000000000000000000000000000001111111111111111111111111111111111"
binary = binary[::-1]

data = [""] * 17
for i in range(0, len(binary)):
    data[i%17] += binary[i]

data = [chr(int(ch, 2)) for ch in data]
print data

hashed = [""] * 64
hashed[6] = data[0]
hashed[13] = data[1]
hashed[24] = data[2]
hashed[25] = data[3]
hashed[26] = data[4]
hashed[32] = data[5]
hashed[33] = data[6]
hashed[34] = data[7]
hashed[37] = data[8]
hashed[39] = data[9]
hashed[42] = data[10]
hashed[43] = data[11]
hashed[46] = data[12]
hashed[54] = data[13]
hashed[55] = data[14]
hashed[58] = data[15]
hashed[60] = data[16]
hashed[2] = "d"

index = 0
for ch in "9" + "333" + "272670" + "1026989260" + "00483" + "59712329280582550000":
    while hashed[index] != "":
        index += 1
    hashed[index] = ch

print hashed

# 0_________1_________2_________3_________4_________5_________6___
# 93d332c726701a0269892600ffa04835acc97a1c23fc29c2805825ba55c0f000
