"""
Advent Of Code 2022 Day 4
Author: PineapplePeddler
Date: 05/12/22
"""
# Func for task 1
def check_containment(elf_A,elf_B):
    # Check if assignment A is entirely contained within B.
    if elf_A[0] >= elf_B[0] and elf_A[1] <= elf_B[1]:
        return True
    # Check if assignment B is entirely contained within A.
    if elf_B[0] >= elf_A[0] and elf_B[1] <= elf_A[1]: 
        return True
    else:
        return False

#Func for task 2
def check_overlap(elf_A,elf_B):
    # Check which is the lower range
    if elf_A[0] > elf_B[0]:
        if elf_A[0] > elf_B[1]:
            return False
    elif elf_B[0] > elf_A[0]:
        if elf_B[0] > elf_A[1]:
            return False
    
    return True

# Import data
with open("2022/Day4_Input.txt") as f:
   assignments_all = f.read().split("\n")

# reformat into nested lists of integers
for i in range(0,len(assignments_all)):
    assignment = assignments_all[i].split(",")
    assignment[0] = list(map(int, assignment[0].split("-")))
    assignment[1] = list(map(int, assignment[1].split("-")))
    assignments_all[i] = assignment

contained_pairs = 0

for assignment in assignments_all:
    if check_containment(assignment[0],assignment[1]):
        contained_pairs += 1

print(contained_pairs)

# Task 2

overlap_pairs = 0

for assignment in assignments_all:
    if check_overlap(assignment[0],assignment[1]):
        overlap_pairs += 1

print(overlap_pairs)



