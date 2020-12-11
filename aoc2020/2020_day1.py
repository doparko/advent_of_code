# AOC 2020 Day 1
# Chris Oparko
#
# Goal is to take a list input and find the two numbers (num1, num2)
# that add up to 2020 and when those are found your answer
# is num1*num2

import numpy as np
import re

filename = '2020_d1.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

# Turning our data into a list of just integers
ml = np.zeros(len(datas)-1)

for j in range(len(datas)-1):
    ml[j] = int(datas[j])
    
# Now actually running through the data to answer the question
# Setting up meshgrid to avoid havig to do many for loops
xv, yv = np.meshgrid(ml,ml)
addmat = xv + yv
flatadd = addmat.flatten() # Makes one long array rather than 2d array
dimen = len(ml)

for i in range(len(flatadd)):
    if flatadd[i] == 2020:
        col = i%(dimen)
        row = int(np.floor(i/(dimen)))
        
        #check if just using same number twice
        if row != col:
            break
        
num1 = xv[row,col]
num2 = yv[row,col]

ans = num1*num2

print('Your answer to part 1 is:',ans)

# For part 2 now
xn,yn,zn = np.meshgrid(ml,ml,ml)
add3 = xn + yn + zn
flat3 = add3.flatten()

for i in range(len(flat3)):
    if flat3[i] == 2020:
        ex = int(np.floor(i/(dimen**2)))
        i2d = i - ex*(dimen**2)
        ey = int(np.floor(i2d/(dimen)))
        ez = i2d%(dimen)
                
        #check if just using same number twice
        if (ex != ey) and (ey != ez):
            break

an1 = xn[ex,ey,ez]
an2 = yn[ex,ey,ez]
an3 = zn[ex,ey,ez]

print('Your answer to part 2 is:', an1*an2*an3)


# Here we try to use a more simple concise way to solve
# using a regex function   

