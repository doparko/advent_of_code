# AOC 2021 Day 6
# Chris O
#
# Goal determine amount of fish left after 80 days
# fish timer reach 0 and change to 6 reproduce
# new fish doesn't count down day born but starts next journey at 8 instead

# example

# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  8 days: 2,3,2,0,1,2,3,4,4,5
# After  9 days: 1,2,1,6,0,1,2,3,3,4,8
# After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
# After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
# After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
# After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
# After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
# After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
# After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
# After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
# After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8

import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day6_inputsample.txt'
#filename = 'day6_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

blahdata = datinss.split(',')
data = [None]*len(blahdata)
for x in range(len(blahdata)):
    data[x] = int(blahdata[x])

def fishloop(flist):
    tmp = []
    for e in flist:
        if e == 0:
            tmp.append(6)
            tmp.append(8)
        else:
            tmp.append(e-1)
    return tmp
        
# # run loop to iterate 80 days
# for i in range(80):
#     data = fishloop(data)
    
# numfish = len(data)
# print('Part 1, after 80 days there are ',numfish,' fish')

#Part 2
days =[]
fishnum = []
for j in range(8):
    temp = data
    for i in range((j+1)*10):
        temp = fishloop(temp)
    days.append((j+1)*10)
    fishnum.append(len(temp))

plt.plot(days,fishnum)