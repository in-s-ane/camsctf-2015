from PIL import Image
import hashlib

files = [ "PIL/pixels0.png"
        , "PIL/pixels1.png"
        , "PIL/pixels2.png"
        , "PIL/pixels3.png"
        , "PIL/pixels4.png"
        , "PIL/pixels5.png"
        , "PIL/pixels6.png"
        , "PIL/pixels7.png"
        , "PIL/pixels8.png"
        , "PIL/pixels9.png"
        ]

def pixhash(img):
    image = Image.open(img)
    pixels = image.load()
    r_sum = 0
    g_sum = 0
    b_sum = 0
    for c in range(300):
        for r in range(300):
            r_sum += pixels[r,c][0]
            g_sum += pixels[r,c][1]
            b_sum += pixels[r,c][2]
    r_hash = hashlib.md5()
    r_hash.update(str(r_sum))
    r_hash = r_hash.hexdigest()
    g_hash = hashlib.md5()
    g_hash.update(str(g_sum))
    g_hash = g_hash.hexdigest()
    b_hash = hashlib.md5()
    b_hash.update(str(b_sum))
    b_hash = b_hash.hexdigest()
    hash_str = hashlib.md5()
    hash_str.update(r_hash+g_hash+b_hash)
    hash_str = hash_str.hexdigest()
    return hash_str

hashes = ''.join([pixhash(f) for f in files])
total_hash = hashlib.md5()
total_hash.update(hashes)
total_hash = total_hash.hexdigest()
print total_hash
