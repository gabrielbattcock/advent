#day 10 advent of code

import numpy as np
import pandas as pd

file = open("day10.txt")
data = file.read().split('\n')


x = 1
counter = 1
total = {}
for line in data:
    instruct = line.split(' ')[0]
    if instruct == 'addx':
        num =  int(line.split(' ')[1])
        total.update({counter: x})
        counter += 1
        total.update({counter: x})
        counter += 1
        x += num
        total.update({counter: x})
    else:
        x += 0
        total.update({counter: x})
        counter += 1
    

sum = 20*total[20] + 60*total[60] + 100*total[100] + 140*total[140] + 180*total[180] + 220*total[220]
print(sum)



output = []

for k, v in total.items():
    sprite = '...........................................'
    position = v
    new_char = '#'
    temp = list(sprite)
    temp[v] = new_char
    temp[v+1] = new_char
    temp[v+2] = new_char
    sprite = ''.join(temp)
    if k < 41: 
        output.append(sprite[k])
    if k >= 40 and k <80:
        output.append(sprite[k-40])
    if k >= 80 and k <120:
        output.append(sprite[k-80])
    if k >= 120 and k <160:
        output.append(sprite[k-120])
    if k >= 160 and k <200:
        output.append(sprite[k-160])
    if k >= 200 and k <240:
        output.append(sprite[k-200])

line1 = ''.join(output[:40])
line2 = ''.join(output[40:80])
line3 = ''.join(output[80:120])
line4 = ''.join(output[120:160])
line5 = ''.join(output[160:200])
line6 = ''.join(output[200:240])

print(line1, '\n',line2, '\n',line3, '\n',line4, '\n',line5, '\n',line6, '\n',)