# AOC 2020 Day 11
# Chris O
#
# Goal is to

import numpy as np
import re
import statistics as st
import copy

filename = 'test_d11.txt'
filename = '2020_d11.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

def countoccurs(row,col,mlist):
    # If we pad the array to start we don't need to worry about edge cases
    numrows, numcols = len(mlist), len(mlist[0])
    paddarray = np.pad(mlist,1,mode='constant')
    # Now look around the row we care about. Remember it will be +1 in the
    # padded array
    padrow, padcol= row+1,col+1
    staken= 0 #count if seat taken aka #
    sopen = 0 #count if seat is open/empty
    # Now time to run through the array to return the open/occupied seats
    for m in range(-1,2):
        for n in range(-1,2):
            if not((m == 0) and (n ==0)):
                if paddarray[padrow+m,padcol+n] == '#':
                    staken+=1
                elif paddarray[padrow+m,padcol+n] == 'L':
                    sopen+=1
    return staken,sopen

nrows = len(datas)
ncols = len(datas[0])

#datray = np.chararray((nrows,ncols))
datray = np.array([[None]*ncols]*nrows)

for i in range(nrows):
    for j in range(ncols):
        datray[i,j] = datas[i][j]


#print('%d taken seats and %d open seats' % (takenseat,openseat))

temparray = [[None]*ncols]*nrows
itt = 0
while not(np.array_equal(temparray,datray)):
    noccupied = 0
    temparray = copy.deepcopy(datray)
    for i in range(nrows):
        for j in range(ncols):
            takenseat, openseat= countoccurs(i,j,temparray)
            if temparray[i,j] == '#' and takenseat >+ 4:
                datray[i,j] = 'L'
            elif temparray[i,j] == 'L' and takenseat == 0:
                datray[i,j] = '#'
            if temparray[i,j] == '#':
                noccupied +=1
    itt+=1


print('There are %d taken seats' % noccupied)


