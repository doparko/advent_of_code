# AOC 2021 Day 
# Chris O
#
# Goal use coordinates to create line segments that are vertical or horizontal
# find number of locations that overlap at least once

# example

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2

import re
import numpy as np
import math
#filename = 'day5_inputsample.txt'
filename = 'day5_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

#cleaning up data a bit
linend = datinss.split('\n')

def begend(text):
    points = text.split(' -> ')
    begin = points[0].split(',')
    endin = points[1].split(',')
    return (int(begin[0]),int(begin[1])) , (int(endin[0]),int(endin[1]))

def popmat(p1,p2,mat):
    #p1 and p2 are end points 
    #mat is the matrix being populate by points
    if p1[0] == p2[0]:
        # x values are the same thus a vertical line
        startpoint = min(p1[1],p2[1])
        endpoint = max(p1[1],p2[1])
        for m in range(endpoint-startpoint+1):
            mat[p1[0],startpoint+m]+=1
    elif p1[1] == p2[1]:
        # y values must be same thus a horizontal line
        startpoint = min(p1[0],p2[0])
        endpoint = max(p1[0],p2[0])
        for m in range(endpoint-startpoint+1):
            #print(startpoint+m,' , ',p1[1])        # Debug statement
            mat[startpoint+m,p1[1]]+=1
    return mat

# Determing the dimensions of the matrix
allnumbers = re.findall('\d{1,10}',datinss)

allint = [None]*len(allnumbers)

for i in range(len(allnumbers)):
    allint[i] = int(allnumbers[i])
    
maxdim = max(allint)+1

# Now we want to make a matrix with each line all zeros except the locations of the string so it is now a 1

empt = np.zeros((maxdim,maxdim))
tmp = empt
for e in linend:
    start,finish = begend(e)
    tmp = popmat(start,finish,tmp)
    
countoverlap = 0

flattmp = tmp.flatten()
for j in flattmp:
    if j > 1:
        countoverlap +=1
    
print('Your amount of at least one overlap is: ', countoverlap)