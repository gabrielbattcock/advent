#day 8

import numpy as np
import matplotlib.pyplot as plt

file = open("forest.txt")
forest = file.read().split('\n')

test = [[int(3),int(0),int(3),int(7),int(3)],[int(2),int(5),int(5),int(1),int(2)],[(6),(5),(3),(3),(2)],[3,3,5,4,9],[3,5,3,9,0]]

count = 0
for i in range(1, len(test)-1):
    for j in range(1, len(test)-1):
        if test[i,j] > max(test[:i,j]) or test[i,j] > max(test[i:,j]) or test[i,j] > max(test[i,:j]) or test[i,j] > max(test[i,j:]):
            count +=1
        else:
            continue
print(count)


# matrix = np.empty([len(forest[0]), len(forest)], dtype = int)
# i = 0
# j = 0 
# for item in forest:
#     print(item)
#     for j in range(len(item)):
#         matrix[i,j] = int(item[j])
#     i += 1    

# print(matrix)
# count = 0
# for i in range(0, len(matrix)):
#     for j in range(0, len(matrix)):
#         if matrix[i,j] <= max(matrix[:i,j]) and matrix[i,j] <= max(matrix[i:,j]) and matrix[i,j] <= max(matrix[i,:j]) and matrix[i,j] <= max(matrix[i,j:]):
#             continue
#         else:
#             count +=1
            
# print(count)


# plt.imshow(matrix)
# plt.show()