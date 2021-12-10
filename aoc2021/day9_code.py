# AOC 2021 Day 9
# Chris O
#
# Goal to find the minimum spots in the entire field of numbers
# If there is an adjacent (left,right,up,down) then check if that has another 
# minimum near it. Collect all the mins and consider those for part 1

#Example

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# In the above example, there are four low points, all highlighted: two are in 
# the first row (a 1 and a 0), one is in the third row (a 5), and one is in the 
# bottom row (also a 5). All other locations on the heightmap have some lower 
# adjacent location, and so are not low points

import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day9_inputsample.txt'
filename = 'day9_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

def myindex(shape,x,y):
    groups = []
    # The following statements check if we are on edges because there would
    # be less adjacent values to consider
    if x < shape[0]-1:
        groups.append((x+1,y))
    if x > 0:
        groups.append((x-1,y))
    if y < shape[1]-1:
        groups.append((x,y+1))
    if y > 0:
        groups.append((x,y-1))
    return groups
        
def minindex(valmap,x,y):
    indicies = myindex(np.shape(valmap),x,y)
    #indicies = indicies + [(x,y)]
    minvalue = valmap[x,y]
    minind = (x,y)
    for m in indicies:
        if minvalue > valmap[m]:
            minvalue = valmap[m]
            minind = m
    #print('Minvalue is: ',minvalue,' , min index is: ',minind)
    if minvalue == valmap[x,y]:
        return minind
    else:
        return minindex(valmap,minind[0],minind[1])

columns = len(datas[0])
rows = len(datas)

field = np.zeros((rows,columns),dtype=int)
for i in range(rows):
    for j in range(columns):
        field[i,j] = datas[i][j]
        
# list with the indicies of the miniumns, do be careful not to include duplicates
minpoints = []

for a in range(rows):
    for b in range(columns):
        temp = minindex(field,a,b)
        if temp not in minpoints:
            minpoints.append(temp)
count1 = 0
for k in minpoints:
    count1+= 1 + field[k]
    
print('Part 1 , sum of all low points plus one for each is: ',count1)