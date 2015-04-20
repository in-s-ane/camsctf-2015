from PIL import Image

def reveal(input_image_file):
	img = Image.open(input_image_file)
	width, height = img.size
	buff, count = 0, 0
	bitab = []
	limit = None
	for row in range(height):
		for col in range(width):

			for color in img.getpixel((col, row)):
				buff += (color&1)<<(7-count)
				count += 1
				if count == 8:
					bitab.append(chr(buff))
					buff, count = 0, 0
					if bitab[-1] == ":" and limit == None:
						try:
							limit = int("".join(bitab[:-1]))
						except:
							pass

			if len(bitab)-len(str(limit))-1 == limit :
				return "".join(bitab)[len(str(limit))+1:]
	return ""

if __name__ == "__main__":
	print(reveal('steg1.png'))
