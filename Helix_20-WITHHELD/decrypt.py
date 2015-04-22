import zlib

with open("flag.zlib", "r") as f:
    print zlib.decompress(f.read())
