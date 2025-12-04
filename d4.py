import numpy as np
file = open("d4.txt", "r")
cntr_1 = 0
cntr_2 = 0
floor = []

for line in file.readlines():
    floor.append(list(line.rstrip()))

def count_adjacent(x,y):
    l = []
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            if len(floor) > x+i >= 0 and len(floor[x]) > y+j >= 0:
                l.append(floor[x+i][y+j])
    return l.count('@')

### part 1 ### 
for x in range(len(floor)):
    for y in range(len(floor[x])):
        if floor[x][y] == '@':
            if count_adjacent(x,y) < 5:
                cntr_1 += 1

### part 2 ###
possible_moves_to_be_made = True
while(possible_moves_to_be_made):
    possible_moves_to_be_made = False
    for x in range(len(floor)):
        for y in range(len(floor[x])):
            if floor[x][y] == '@':
                if count_adjacent(x,y) < 5:
                    floor[x][y] = 'X'
                    cntr_2 += 1
                    possible_moves_to_be_made = True

print("part 1: " + str(cntr_1))
print("part 2: " + str(cntr_2))