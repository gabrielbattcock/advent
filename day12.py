#day 12 of advent of code

import numpy as np
import pandas as pd

file = open("day12.txt")
data = file.read().split('\n')

count = 0 
for letter in data[0]:
    
    count += 1
        
print(count)

matrix = np.empty([count, len(data)])

j = 0
i = 0 
for j in range(len(data)):
    for i in range(count): 
        matrix[i,j] = data[]
        
    i += 1

