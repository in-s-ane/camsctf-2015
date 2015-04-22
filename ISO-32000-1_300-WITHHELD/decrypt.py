import zlib

with open("cipher", "r") as f:
    data = f.read()
    decompressed = zlib.decompress(data)
    print decompressed
