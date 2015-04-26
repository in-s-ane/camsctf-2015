dependencies_loaded = False
try:
    from PIL import Image
    import zbar
    '''
    If the above segfaults, which it will most likely do on OSX, install python zbar like this:
    > pip install git+https://github.com/npinchot/zbar.git --upgrade
    Credeits to http://stackoverflow.com/questions/21612908/zbar-python-crashes-on-import-osx-10-9-1
    '''
    dependencies_loaded = True
except:
    dependencies_loaded = False

data = ""
with open("crypto_f4", "r") as f:
    data = f.read()
data = [ch for ch in data]

startbyte = 0
endbyte = 0

headers = [0,0,0,0]
i = 0
for ch in data:
    headers[i%4] = ord(ch)
    if 0x89 in headers and 0x50 in headers and 0x4e in headers and 0x47 in headers:
        startbyte = i-3
        break
    i += 1

trailers = [0,0,0,0]
i = 0
for ch in data:
    trailers[i%4] = ord(ch)
    if 0x49 in trailers and 0x45 in trailers and 0x4e in trailers and 0x44 in trailers:
        endbyte = i+4
        break
    i += 1

# This is data found from multiple trials, after which we realized from the header
# and trailer that all the data in the png is swapped in every set of 4 bytes.
extracted_png = data[startbyte:endbyte+1]
for i in range(0, len(extracted_png)-1, 2):
    extracted_png[i], extracted_png[i+1] = extracted_png[i+1], extracted_png[i]

with open("crypto_f4-fixed.png", "w") as f:
    png = ''.join(extracted_png)
    f.write(png)

if dependencies_loaded:
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')
    image = Image.open("crypto_f4-fixed.png").convert('L')
    width, height = image.size
    raw = image.tostring()
    barcode = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(barcode)
    for symbol in barcode:
        print 'Decoded', symbol.type, 'symbol:', '"%s"' % symbol.data
    del(image)
