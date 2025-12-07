file = open("d5.txt", "r")

ingredient_divide = False
id_ranges = []
ingredient_ids = []
fresh_id_ranges = []
fresh_cntr_1 = 0
fresh_cntr_2 = 0



for line in file.readlines():
    if line.rstrip() == '':
        ingredient_divide = True
    elif not ingredient_divide:
        id_ranges.append(list(map(int, line.rstrip().split('-'))))
    elif ingredient_divide:
        ingredient_ids.append(int(line.rstrip()))

### part 1 ### 
for id in ingredient_ids:
    for id_range in id_ranges:
        if id >= id_range[0] and id <= id_range[1]:
            fresh_cntr_1 += 1
            break

### part 2 ###
for id in id_ranges: #TODO finnish 
    for compare_id in id_ranges:
        start = id[0]
        end = id[1]
        if start < compare_id[0] and start > compare_id[1]:
            start = id[0] - compare_id[0]
        if end < compare_id[1] and end > compare_id[0]:
            end = id[1] - compare_id[1]

    fresh_id_ranges.append(start - end)
        
print(fresh_id_ranges)

print("part 1: " + str(fresh_cntr_1))
print("part 2: " + str(fresh_cntr_2))

