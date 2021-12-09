# AOC 2020 Day 10
# Chris O
# I'm attempting this the following year as I'm not sure why I got stuck

# Goal is to

import numpy as np
import re
import statistics as st

#filename = 'test_d10.txt'
filename = '2020_d10.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

mydat = [None]*len(datas)
mydat= [int(i) for i in datas[:-1]]
mydat.sort()

ones = 0
threes = 1
tmp = 0
difflist = []

for e in range(len(mydat)):
    diff = mydat[e] - tmp
    difflist.append(diff)
    if diff == 1:
        ones+=1
    elif diff == 3:
        threes+=1
    tmp = mydat[e]
print('Solution part1 is ', ones*threes)

# Attempting part 2
# If you go through the list of differences and if 2 side by side values
# If they add up to 3 or less you can remove that value
removecount = 0
for j in range(len(difflist)):
    if difflist[j] + difflist[j] <= 3:
        removecount+=1