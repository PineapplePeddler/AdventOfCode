"""
Advent Of Code 2022 Day 1
Author: PineapplePeddler
Date: 01/12/22
"""

# Import data
with open("2022/Day1_Input.txt") as f:
   elf_data_raw = f.read().split("\n\n")

elves_meals = []
elves_total_cals = []

for elf in elf_data_raw:
    elf_meals = list(map(int, elf.split("\n")))
    elves_meals.append(elf_meals)
    elves_total_cals.append(sum(elf_meals))

# Task 1: print cals carried by elf carrying highest total cals

loaded_elf = elves_total_cals.index(max(elves_total_cals))
print(loaded_elf)
print(elves_total_cals[loaded_elf])
print(elves_total_cals[25])
print(elves_total_cals[26])

#  Task 2: 3 loaded elves

loaded_elves = []
temp = elves_total_cals[:]

for i in range(3):
    max_cals = max(temp)
    loaded_elves.append(elves_total_cals.index(max_cals))
    temp.remove(max_cals)

del temp

print(loaded_elves)
print([elves_total_cals[i] for i in loaded_elves])
print(sum([elves_total_cals[i] for i in loaded_elves]))
