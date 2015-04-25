import binascii

mmm_string = "mMMMMmMMmmMMMMmmmMMmmMmmmMMmMmmMmMMMmMMmmmMMMMMmmMMMMmmmmMMmMmMMmMMmmmMMmm" # Extracted line from MmMmMm and tested to find one that decoded correctly

binary_string = mmm_string.replace("m", "0").replace("M", "1")
print binary_string

flag = []
for i in range(len(binary_string)/8):
    n = int(binary_string[i*8:i*8+8], 2)
    flag.append(binascii.unhexlify('%02x' % n))

print ''.join(flag) + "d4lyfe</span>]" # This second part is taken for when the image looks like a QR code
