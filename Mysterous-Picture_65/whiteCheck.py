from PIL import Image

WHITE = (255, 255, 255, 255)
NOT_WHITE = (254, 254, 254)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)

def read(img):
    image = Image.open(img)
    pixels = image.load()
    for c in range(100):
        for r in range(100):
            if pixels[c,r] != WHITE:
                if pixels[c,r] == NOT_WHITE:
                    pixels[c,r] = BLACK
                else:
                    print c
                    print r
                    print pixels[c,r]
                    pixels[c,r] = RED
    #image.save('out.png')

#read('mysterious_picture.png')

s = ""
image = Image.open('mysterious_picture.png')
pixels = image.load()
for c in range(43):
    for i in range(3):
        s = s + str(pixels[c,42][i] - 254)

print s
