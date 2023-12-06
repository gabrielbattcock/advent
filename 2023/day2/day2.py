#day 2 advent 2023

import numpy as np
import re

file = open("2023/day2/day2.txt")
test = file.read().split('\n')


point = 0
def get_game_number(line):
   #get the number of the game IF it passes the test
    win = True
    game_number = line.split(':')[0]
    game = line.split(':')[1]
    game_hand = game.split(";")

    for hand in game_hand:
        if ([float(s) for s in re.findall(r"(\d+) blue", hand)] != [] and [float(s) for s in re.findall(r"(\d+) blue", hand)][0] > 14.0):
            win = False
        elif([float(s) for s in re.findall(r"(\d+) red", hand)] != []and[float(s) for s in re.findall(r"(\d+) red", hand)][0] >12.0):
            win = False
        elif([float(s) for s in re.findall(r"(\d+) green", hand)] != [] and [float(s) for s in re.findall(r"(\d+) green", hand)][0] >13.0):
            win = False    
            
    
    if win == True:
        x = [int(s) for s in re.findall(r"(\d+)", game_number)][0]
        # print(x)
    else:
        x = 0
    return x
    #returns whether we 'win the game
    

# point = 0
# # apply for every line in the game
for line in test:
    point += get_game_number(line)
    get_game_number(line)
    print(point)



### Part 2 #####


def lowest_number_cubes(line):
   

    game_number = line.split(':')[0]
    game = line.split(':')[1]
    game_hand = game.split(";")

    blue = []
    red = []
    green = []
  
    for hand in game_hand:
        print(hand)
        if ([float(s) for s in re.findall(r"(\d+) blue", hand)] != []):
            blue.append([float(s) for s in re.findall(r"(\d+) blue", hand)][0])

            
        if([float(s) for s in re.findall(r"(\d+) green", hand)] != []):
            green.append([float(s) for s in re.findall(r"(\d+) green", hand)][0])

        if([float(s) for s in re.findall(r"(\d+) re", hand)] != []):
            red.append([float(s) for s in re.findall(r"(\d+) re", hand)][0]) 

            
    # print(max(red))
    # print(blue)
    # print(green)
    cubes = max(red)*max(blue)*max(green)
    return cubes

points2 = 0
for line in test:

    points2 += lowest_number_cubes(line)
    print(points2)