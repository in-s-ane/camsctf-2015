from PIL import Image

WHITE = (255, 255, 255, 255)
OFF_WHITE = (255, 255, 254, 255)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 255)
def read(img):
    image = Image.open(img)
    pixels = image.load()
    for c in range(1000):
        for r in range(1000):
            if pixels[c,r] != WHITE:
                if pixels[c,r] == OFF_WHITE:
                    pixels[c,r] = BLACK
                else:
                    pixels[c,r] = RED
    image.save('out.png')

read('crypto_c.png')
