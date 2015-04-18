f = open("givemeflag.txt", "r")
data = f.read().split(" ")
f.close()

program = []
for char in data:
    program.append(char.decode("hex"))

f = open("givemeflag.class", "w")
f.write(''.join(program))
f.close()
