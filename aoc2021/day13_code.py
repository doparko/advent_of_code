# AOC 2021 Day 13
# Chris O
#
# Goal fold the paper the amount of times requested
# after each fold sometimes the points will overlap. How many points remain
# after the folds (an overlap counts as one)

#Example



import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day13_inputsample.txt'
filename = 'day13_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas,folds = datinss.split('\n\n')
datas = datas.split('\n')
folds = folds.split('\n')

# Functions
def foldline(direction,number,matrix):
    newmat= []
    if direction == 'x':
        # folding on a vertical line
        for i in matrix:
            ex = i[0]               # x value will the the one changing
            ey = i[1]
            newex = ex
            if ex > number:
                diff = ex - number
                newex = number - diff
            if (newex,ey) not in newmat:
                newmat.append((newex,ey))
    else:
        # folding on a horizontal line
        for i in matrix:
            ex = i[0]               # y value will the the one changing
            ey = i[1]
            newey= ey
            if ey > number:
                diff = ey - number
                newey = number - diff
            if (ex,newey) not in newmat:
                newmat.append((ex,newey))
    return newmat

allfolds = []
# First fold
for e in folds:
    fold = re.findall('[xy]=\d+',e)
    direct,num = fold[0].split('=')
    allfolds.append([direct,int(num)])

# Clean input
dots = []
for e in datas:
    tmp = re.findall('\d+',e)
    tmp[0] = int(tmp[0])
    tmp[1] = int(tmp[1])
    dots.append((tmp[0],tmp[1]))
    
answer1 = foldline(allfolds[0][0],allfolds[0][1],dots)

print('Part 1, number of dots: ', len(answer1))

for e in allfolds:
    dots = foldline(e[0],e[1],dots)

for x in dots:
    plt.plot(x[0],-x[1],'rs',markersize=20)
plt.show()