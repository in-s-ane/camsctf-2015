#/usr/bin/python
# -*- coding: utf-8 -*-

import bz2

with open("flag.zip", "r") as f:
    data = f.read()
    data = data.replace("PK", "BZ")
    print bz2.decompress(data)

'''
Right after solving loop, I realized that this might be compress with bz2. Turns
out it was! Since this started with PKh91AY&SY, which corresponds to zip, I
thought that it was a zip for a long while since the filezilla transferred a
flag.zip file.
So I modified this to match the header for a bz2 file, by replacing Pk with BZ,
which would then successfully decompress to the flag.
Flag: {let's_FTP_w/_filezilla!!}
'''
