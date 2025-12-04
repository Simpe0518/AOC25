file = open("d1.txt", "r")
dial = 50
cntr = 0
cntr_2 = 0
instructions = []

### part 1 ### 
for line in file.readlines():
    instructions = instructions + line.split()

for line in instructions:
    if line[0] == 'R':
        dial += int(line[1:])
    elif line[0] == 'L':
        dial -= int(line[1:])
    else:
        raise Exception("Bad input")
    
    if dial % 100 == 0:
        cntr += 1

### part 2 ###
dial = 50 
for line in instructions: 
    tick = (1 if line[0] == 'R' else -1)
    for i in range(int(line[1:])):
        dial += tick
        if dial % 100 == 0:
            cntr_2 += 1

print("part 1: " + str(cntr))
print("part 2: " + str(cntr_2))
