#day 4

import numpy as np

file = open("cleanup.txt")
clean = file.read().split('\n')

#function to split string into two pairs of ints and return T or F whetehr they overlap
def full_overlap(line):
    def int_range(ranges):
        a,b = ranges.split('-')
        a,b = int(a), int(b)
        return a,b
    ran1, ran2 = line.split(',')
    ran1 = int_range(ran1)
    ran2 = int_range(ran2)
    if (ran1[0] <= ran2[0] and ran1[1] >= ran2[1]) or (ran2[0] <= ran1[0] and ran2[1] >= ran1[1]) :
        return True
    else:
        return False
    
count = 0   
for i in range(len(clean)):
    if full_overlap(clean[i]) == True:
        count += 1
    else:
        count = count
print(count)

#part 2

def partial_overlap(line):
    def int_range(ranges):
        a,b = ranges.split('-')
        a,b = int(a), int(b)
        return a,b
    ran1, ran2 = line.split(',')
    ran1 = int_range(ran1)
    ran2 = int_range(ran2)
    if (ran1[0] <= ran2[0] <= ran1[1]) or  (ran1[0] <= ran2[1] <= ran1[1]) :
        return True
    else:
        return False

count = 0   
for i in range(len(clean)):
    if partial_overlap(clean[i]) == True or full_overlap(clean[i]) == True:
        count += 1
    else:
        count = count
print(count)
