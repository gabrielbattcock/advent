#advent day 2

#Rock paper scissors game. the opponant will play either A, B or C (rock, paper, scissors respetively)
#I have been given the cheat sheet with a winning move X, Y, Z (rock, paper, scissors respetively) to win
# I have to calculate my score based on the hand I play and if I win, draw or lose for each scenario.


import numpy as np 
import requests


#open file and read it in as matrix
file = open("strategy.txt")

strategy = [line.replace('\n','').split(' ') for line in file.readlines()]

#define dictionaries to calculat the scores
win = {
    "A":"Y",
    "B":"Z",
    "C":"X"
}

draw = {
    "A":"X",
    "B":"Y",
    "C":"Z"
}

loss = {
    "A":"Z",
    "B":"X",
    "C":"Y"
}
#define hierarchies between the hands

#puzzle 1
score = 0
    
def calculate_round(round):
    if round[1]=="X":
        choice = 1
    elif round[1] =="Y":
        choice = 2
    else:
        choice = 3
        
    if round[1] == win[round[0]]:
        compet = 6
    elif round[1] == draw[round[0]]:
        compet = 3
    else:
        compet = 0
    temp = choice + compet
    return temp


for round in strategy:
    score += calculate_round(round)
print(score)


#puzzle 2
#X means i need to lose, Y draw, Z win

score = 0 

new_strat = {
    "X": loss,
    "Y": draw,
    "Z": win
}


def new_score(round):
    if round[1]=="X":
        temp  = calculate_round([round[0],loss[round[0]]])
    elif round[1] =="Y":
        temp  = calculate_round([round[0],draw[round[0]]])
    elif round [1] == "Z":
        temp  = calculate_round([round[0],win[round[0]]])
    return temp

for round in strategy:
    score += new_score(round)
print(score)