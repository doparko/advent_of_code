# AOC 2021 Day 1
# Chris O
#
# Goal is to determine how many times the depth increases 

# example

# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
# 200 (decreased)
# 207 (increased)
# 240 (increased)
# 269 (increased)
# 260 (decreased)
# 263 (increased)

import numpy as np

filename = 'day1_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()
datas = np.array(datinss.split('\n'))

data = [None]*len(datas)

for i in range(len(datas)):
    data[i] = int(datas[i])

#Part 1
startval = data[0]
increase_count = 0

for i in range(len(data)):
    if i == len(data) - 1:
        break
    if startval < data[i+1]:
        increase_count +=1
    startval = data[i+1]
    
print('Part 1 ______ Amount of times increased is: ',increase_count)

#Part 2
# Now need to figure out increase for a window of 3 instead of each one
# Example:

# 199  A      
# 200  A B    
# 208  A B C  
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G  
# 269    F G H
# 260      G H
# 263        H

# Amount of 3 window would be the length minus 2
it3len = len(data) - 2

inc3_count = 0
startval = data[0] + data[1] + data[2]

for j in range(it3len):
    if j == it3len - 1:
        break
    temp = data[j+1] + data[j+2] + data[j+3]
    if startval < temp:
        inc3_count +=1
    startval = temp
    
print('Part 2 ______ Amount of times 3 window increased is: ',inc3_count)









