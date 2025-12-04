file = open("d3.txt", "r")
sum_1 = 0
sum_2 = 0
batteries = []

for line in file.readlines():
    batteries.append(list(map(int,line.rstrip())))

### part 1 ###
for line in batteries:
    first = max(line[:len(line)-1])
    second = max(line[line.index(first)+1:])
    sum_1 += int(str(first) + str(second))


### part 2 ###
for line in batteries:
    battery = ""
    for i in range(11,-1,-1):
        battery = battery + str(max(line[:len(line)-i]))
        line = line[line.index(int(battery[-1]))+1:]
    print(battery)
    sum_2 += int(battery)

print("part 1: " + str(sum_1))
print("part 2: " + str(sum_2))


