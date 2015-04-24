from PIL import Image, ImageDraw

CONSTANT = 100

f = open("usb_data.txt", "r")
data = f.readlines()
g = open ("usb_time_deltas.txt", "r")
times = g.readlines()

scratchpad = Image.new('RGB', (1000,1000), (255,255,255))
canvas = scratchpad.load()
draw = ImageDraw.Draw(scratchpad)

mouse_x = 500
mouse_y = 500
mouse_dx = 0
mouse_dy = 0

for d, t in zip(data, times):
    raw_movement = d.strip().split(":")
    movement = raw_movement[:]
    all_zeros = True
    for i in movement:
        if int(i, 16) != 0:
            all_zeros = False
    if all_zeros:
        movement = ["%.6f"%delta] + movement
        #print movement
        continue

    '''
    delta = float(t[6:14])
    movement = ["%8d"%int(m, 16) for m in movement]
    if "1" in movement[0]:
        movement[0] = "%8s" % "leftcl"
    elif "2" in movement[0]:
        movement[0] = "%8s" % "rightcl"
    if movement[2].strip() != "0":
        if "255" in movement[3]:
            movement[3] = "%8s" % "left"
        elif "0" in movement[3]:
            movement[3] = "%8s" % "right"
    if movement[4].strip() != "0":
        if "255" in movement[5]:
            movement[5] = "%8s" % "up"
        elif "0" in movement[5]:
            movement[5] = "%8s" % "down"
    movement = ["%.6f"%delta] + movement
    #print movement
    '''
    delta = float(t[6:14])
    old_mouse_x = mouse_x
    old_mouse_y = mouse_y
    mouse_x += mouse_dx * delta * CONSTANT
    mouse_y += mouse_dy * delta * CONSTANT
    draw.line((old_mouse_x, old_mouse_y, mouse_x, mouse_y), fill=128)

    movement = [int(m, 16) for m in raw_movement]
    if movement[2] != 0:
        if movement[3] == 255:
            mouse_dx = - (256-movement[2])
        elif movement[3] == 0:
            mouse_dx = movement[2]
    else:
        mouse_dx = 0
    if movement[4] != 0:
        if movement[5] == 255:
            mouse_dy = - (256-movement[4])
        elif movement[5] == 0:
            mouse_dy = movement[4]
    else:
        mouse_dy = 0

scratchpad.save("mouse.png")
