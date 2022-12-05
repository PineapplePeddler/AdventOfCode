"""
Advent Of Code 2022 Day 5
Author: PineapplePeddler
Date: 05/12/22
"""

# Import move data
with open("2022/Day5_Input_B.txt") as f:
   moves = f.read().split("\n")

# format moves
for i in range(0,len(moves)):
    move = moves[i].split(" ")
    moves[i] = list(map(int,[move[1],move[3],move[5]]))

#Input initial state
stock  = [
          ['F','T','C','L','R','P','G','Q'],
          ['N','Q','H','W','R','F','S','J'],
          ['F','B','H','W','P','M','Q'],
          ['V','S','T','D','F'],
          ['Q','L','D','W','V','F','Z'],
          ['Z','C','L','S'],
          ['Z','B','M','V','D','F'],
          ['T','J','B'],
          ['Q','N','B','G','L','S','P','H'],]

# Task 1 - Execute moves, individual crates
for move in moves:
    for i in range(0,move[0]):
        stock[move[2]-1].append(stock[move[1]-1][-1])
        del stock[move[1]-1][-1]

# Output string of top of stacks.
output_1 = ''
for stack in stock:
    output_1 += stack[-1]

print(output_1)

#reset stock initial state
stock  = [
          ['F','T','C','L','R','P','G','Q'],
          ['N','Q','H','W','R','F','S','J'],
          ['F','B','H','W','P','M','Q'],
          ['V','S','T','D','F'],
          ['Q','L','D','W','V','F','Z'],
          ['Z','C','L','S'],
          ['Z','B','M','V','D','F'],
          ['T','J','B'],
          ['Q','N','B','G','L','S','P','H'],]

# Task 1 - Execute moves, multicrate
for move in moves:
    stock[move[2]-1] = stock[move[2]-1] + stock[move[1]-1][-move[0]:]
    del stock[move[1]-1][-move[0]:]


# Output string of top of stacks.
output_2 = ''
for stack in stock:
    output_2 += stack[-1]

print(output_2)
