#from Crypto.Cipher import AES

with open("crypto_9.txt", "r") as f:
    data = f.read()
    decoded = data.decode("base64")
    print decoded

    c = open("aes.bin", "w")
    c.write(decoded[12:])
