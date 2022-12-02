"""
Advent Of Code 2022 Day 1
Author: PineapplePeddler
Date: 01/12/22
"""
def calc_results(p1,p2):
    game_score = 0
    if p2 == 'X':
        # Points for playing shape
        game_score += 1

        # Points for winning or drawing/
        if p1 == 'A':
            game_score += 3
        elif p1 == 'C':
            game_score += 6

    elif p2 =='Y':
        # Points for playing shape
        game_score += 2

        # Points for winning or drawing/
        if p1 == 'B':
            game_score += 3
        elif p1 == 'A':
            game_score += 6

    elif p2 == 'Z':
        # Points for playing shape
        game_score += 3

        # Points for winning or drawing/
        if p1 == 'C':
            game_score += 3
        elif p1 == 'B':
            game_score += 6
    
    return game_score
     
def calc_play(p1,strat):
    if strat == "X": #lose
        if p1 == "A":
            return "Z"
        elif p1 == "B":
            return "X"
        elif p1 == "C":
            return  "Y"
    
    elif strat == "Y": #Draw
        if p1 == "A":
            return "X"
        elif p1 == "B":
            return "Y"
        elif p1 == "C":
            return "Z"
    
    elif strat == "Z": #Win
        if p1 == "A":
            return "Y"
        elif p1 == "B":
            return "Z"
        elif p1 == "C":
            return "X"


# Import data
with open("2022/Day2_Input.txt") as f:
   guide = f.read().split("\n")

# Task 1
total_score_1 = 0

for game in guide:
    total_score_1 += calc_results(game[0],game[2])

print(total_score_1)

# Task 2
total_score_2 = 0

for game in guide:
    total_score_2 += calc_results(game[0],calc_play(game[0],game[2]))

print(total_score_2)