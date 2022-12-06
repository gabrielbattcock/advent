#day 1

import numpy as np

file = open("calories.txt")
cal = file.read().split('\n')


total = []
sub_tot = 0
for item in cal:
    if item != '':
        sub_tot += int(item)
    else:
        total.append(sub_tot)
        sub_tot = 0
        
print(max(total))

#part 2
total.sort(reverse=True)
print(total[0]+total[1]+total[2])