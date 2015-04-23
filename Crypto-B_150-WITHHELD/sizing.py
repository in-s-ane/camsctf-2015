import sys
from PIL import Image

RESIZED_WIDTH = 800
RESIZED_HEIGHT = 1618

def read(img):
    image = Image.open(img)
    pixels = image.load()
    width, height = image.size
    resized_image = Image.new('RGB', (RESIZED_WIDTH, RESIZED_HEIGHT), (255, 255, 255))
    resized_pixels = resized_image.load()
    for r in range(RESIZED_HEIGHT):
        row_adjusted = r * RESIZED_WIDTH
        for c in range(RESIZED_WIDTH):
            resized_pixels[c, r] = pixels[((row_adjusted + c) % width), ((row_adjusted + c) // width)]
    resized_image.save("out-%sx%s.png" % (RESIZED_WIDTH, RESIZED_HEIGHT))

if len(sys.argv) > 1:
    read(sys.argv[1])
else:
    print "Please specify a picture to read!\npython sizing.py [FILE]"
