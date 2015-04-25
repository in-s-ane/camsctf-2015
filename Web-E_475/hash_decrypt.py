binary = "01101101111110011110111110110011011000001000000110000000000000000000000000000000000001111111111111111111111111111111111"
binary = binary[::-1]

data = [""] * 17
for i in range(0, len(binary)):
    data[i%17] += binary[i]

data = [chr(int(ch, 2)) for ch in data]
#print data

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

hashed[0] = "b" # This has to be modified so that it follows the hint given that the first is a-f. b is the correct one

index = 0
for ch in "9" + "333" + "272670" + str(1026989203 + ord(hashed[0])) + "00483" + "59712329280582551573":
    while hashed[index] != "":
        index += 1
    hashed[index] = ch

print ''.join(hashed)

# b9d333c272670a1026989301ffa00483acc59a7c12fc32c9280582ba55c1f573 is the correct hash
# http://md5hashing.net/hash/sha256/b9d333c272670a1026989301ffa00483acc59a7c12fc32c9280582ba55c1f573?is_search=true 
# We get the decoded value of bitwize123
# Inputting that on the server:
# Flag: {srsly?_dis?_DIS_OBFUSCATED_PAIN?}
