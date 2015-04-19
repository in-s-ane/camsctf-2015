import struct
carve = """89 50 4e 47
0d 0a 1a 0a 00 00 00 0d 49 48 44 52 00 00 00 10
00 00 00 10 08 06 00 00 00 1f f3 ff 61 00 00 00
06 62 4b 47 44 00 ff 00 ff 00 ff a0 bd a7 93 00
00 00 09 70 48 59 73 00 00 0b 13 00 00 0b 13 01
00 9a 9c 18 00 00 00 07 74 49 4d 45 07 de 03 01
11 21 29 c8 35 8e 82 00 00 01 05 49 44 41 54 38
cb c5 93 21 4b 43 61 14 86 9f 73 bc e8 e6 e4 3a
1c 2c 18 0c ee 46 83 60 11 2c 22 b2 20 86 81 ec
8f 18 c6 60 a2 0b 06 19 38 30 18 fc 01 26 19 96
61 18 d3 62 50 d0 64 76 86 05 07 4b 0a 22 d7 85
1d 7f 80 9f f7 ca 0c 3b f1 7b ce f7 f2 86 e7 c0
b8 47 ee e7 52 c9 de d0 4a c0 3a b0 0c a4 63 fe
bc 03 4f 02 b7 85 b7 cf 8a 5c a6 a7 0f 80 ea 88
05 aa 0a e4 5d 64 f5 f4 8c f9 5c 2e 2e 20 af 40
e0 44 1b 9b 2c 34 5b 2c ee 14 a3 02 02 05 fc a8
8d ec e1 11 4b c7 27 bf 61 5f 81 44 5c cf 99 ad
6d 82 5a dd 85 12 6a 66 61 5c c0 c7 55 93 e7 d2
ee 8f 77 33 0b 3d e0 2b aa 45 7f af cc 4b e3 c2
ed 80 48 e8 01 03 27 bd 69 d3 ad d7 78 ed 74 a2
ca 0d a4 e1 27 1f 55 65 65 14 09 cc ec 4e 0d 6b
ff c3 e4 d6 c4 da a4 77 9d 12 66 55 24 34 b3 8c
88 4c fd 41 e5 07 81 f3 ee d0 f6 c7 7e 8c 7c 03
65 67 44 65 27 f1 32 55 00 00 00 00 49 45 4e 44
ae 42 60 82"""
out = open('carved.png', 'wb')
h = ''
for byte in carve.replace('\n', ' ').split(' '):
    h+=struct.pack('!B', int(byte, 16))
out.write(h)
out.close()
