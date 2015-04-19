
import struct
carve = """47 49 46 38 39 61 01
00 01 00 80 01 00 00 00 00 ff ff ff 21 f9 04 01
00 00 01 00 2c 00 00 00 00 01 00 01 00 00 02 02
4c 01 00 3b"""
out = open('carved3.gif', 'wb')
h = ''
for byte in carve.replace('\n', ' ').split(' '):
    h+=struct.pack('!B', int(byte, 16))
out.write(h)
out.close()
