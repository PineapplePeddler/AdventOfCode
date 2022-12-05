"""
Advent Of Code 2022 Day 3
Author: PineapplePeddler
Date: 05/12/22
"""

def calc_priority(item):
    dec_val = ord(item)
    if dec_val > 96:
        return dec_val - 96 #lowercase letters
    else:
        return dec_val - 38 #uppercase



# Import data
with open("2022/Day3_Input.txt") as f:
   backpack_all = f.read().split("\n")

priority_sum = 0

#Task 1

for backpack in backpack_all:

    for i in range(0,int(len(backpack)/2)):
        if backpack[i] in backpack[int(len(backpack)/2):]:
            print(backpack[i])
            priority_sum += calc_priority(backpack[i])
            break

print(priority_sum)

#Task 2

priority_sum_2 = 0

print(backpack_all)
print(len(backpack_all))
for i in range(0,len(backpack_all)-2,3):
    print(i)
    for thing in backpack_all[i]:
        print(thing)
        if thing in (backpack_all[i+1]) and (thing in backpack_all[i+2]):
            print("Match: " + thing)
            priority_sum_2 += calc_priority(thing)
            break

print(priority_sum_2)



