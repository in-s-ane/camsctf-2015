# It would appear that the asciis between values 3F and 7D are flipped
# around the center

# 94 is the middle

STRING = "AY[L[ZPW]MV]SNVPSYHSNU?"
OUTPUT = ""

for i in list(STRING):
# note that everything within the STRING has ascii value less than 94
    OUTPUT = OUTPUT + chr(125 - (ord(i) - 63))

print OUTPUT
