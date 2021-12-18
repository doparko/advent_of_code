# AOC 2021 Day 11
# Chris O
#
# Goal

#Example

# 5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526

import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day11_inputsample.txt'
filename = 'day11_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

# Finding neighbors of given index and return in a list
def neighbor(index):
    groups = []
    size = 10
    for m in range(-1,2):
        for n in range(-1,2):
            if (m != 0 or n != 0) and (index[0]+m >= 0 and index[0]+m < 10) and (index[1]+n >=0 and index[1]+n< 10):
                groups.append((index[0]+m,index[1]+n))
    return groups
    

# Function for stepping through one step given dictionary map
def flashstep(mapp):
    newmap = {}
    # Adding 1 to each cell to begin with
    for t in mapp:
        mapp[t]+=1
        
    octocheck = [x for x in mapp if mapp[x] > 9]        #Selecting all the octos w/ energy > 9
    while len(octocheck) > 0:
        for e in octocheck:
            newmap[e] = mapp.pop(e)
            neighbors = neighbor(e)
            for m in neighbors:
                if m in mapp:
                    mapp[m] +=1
        octocheck = [x for x in mapp if mapp[x] > 9]        #Selecting all the octos w/ energy > 9
    flashes = len(newmap)
    newmap = dict.fromkeys(newmap,0)
    for k in mapp:
        newmap[k] = mapp[k]
    return newmap, flashes
            


columns = len(datas[0])
rows = len(datas)

dmap = {}
field = np.zeros((rows,columns),dtype=int)
for i in range(rows):
    for j in range(columns):
        field[i,j] = datas[i][j]
        dmap[(i,j)] = int(datas[i][j])

dmap2 = dmap.copy()
steps = 100
flashcount = 0

for i in range(steps):
    dmap, flashes = flashstep(dmap)
    flashcount += flashes

# For part 2 finding when all is synched together and flashes
allflash = 0
stepnum =0
while not(allflash):
    stepnum+=1
    dmap2, flashes = flashstep(dmap2)
    if flashes == 100:
        allflash = 1
        break
    
print('Part 1 number of flashes after 100 steps is: ',flashcount)
print('Part 2, step that all finally flash together is: ',stepnum)      