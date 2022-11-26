"""
Advent Of Code 2021 Day 1
Auther: PineapplePeddler
Date: 26/11/22
"""

# Import data
with open("2021/Day1_Input.txt") as f:
   depth_data = f.read().split()

# Comvert to integers
depth_data = list(map(int, depth_data))

# Puzzle 1 - Count number of times depth reading increases compared to previous reading.

increase_count = 0

for i in range(1,len(depth_data)):
    if depth_data[i] > depth_data[i-1]:
        increase_count += 1

print(increase_count)

increase_count_window = 0

# Puzzle 2 - compare a sliding window of 3 values. 

for i in range(3,len(depth_data)):
    print(depth_data[i-3:i])
    print(depth_data[i-2:i+1])
    if sum(depth_data[i-2:i+1]) > sum(depth_data[i-3:i]):
        increase_count_window += 1

print(increase_count_window)
