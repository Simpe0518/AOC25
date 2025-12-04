file = open("d2.txt", "r")
sum_1 = 0
sum_2 = 0 

for line in file.readlines():
    product_ids = line.rstrip().split(',')

def is_repeating_once(s):
    return s[:len(s)//2] == s[len(s)//2:]

def is_repeating_multiple(s):
    return s in (s + s)[1:-1]

for id in product_ids:
    split_id = id.split('-')
    for i in range(int(split_id[0]), int(split_id[1])):
        ### part 1 ### 
        if is_repeating_once(str(i)):
            sum_1 += i
        ### part 2 ### 
        if is_repeating_multiple(str(i)):
            sum_2 += i

print("part 1: " + str(sum_1))
print("part 2: " + str(sum_2))