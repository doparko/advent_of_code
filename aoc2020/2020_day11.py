# AOC 2020 Day 11
# Chris O
#
# Goal is to

import numpy as np
import re
import statistics as st
import copy

#filename = 'test_d11.txt'
filename = '2020_d11.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')


def countocc(row,col,thedata):
    stake = 0
    sopen = 0
    for m in range(-1,2):
        for n in range(-1,2):
            if not((m == 0) and (n == 0)):
                if not(( m+row < 0 or m+row > len(thedata)-1) or ( n+col < 0 or n+col > len(thedata[0])-1)):
                    #print('row',m+row,' col ',n+col)
                    if thedata[row+m][col+n] == '#':
                        stake +=1
                    elif thedata[row+m][col+n] == 'L':
                        sopen +=1
    return stake,sopen

def countsee(row,col,thedata):
    stake = 0
    sopen = 0
    
    
# Rules
# Seat is empty (L) and there are no surrounding seats, becomes filled
# Seat is taken (#) and there are at least 4 surrounding that are full, becomes empty


mydat = []
for j in range(len(datas)):
    mydat.append(list(datas[j]))
    
temp1 = mydat[:]
temp2 = copy.deepcopy(temp1)

temp1[0][0] = '#'

itt = 0

while temp1 != temp2:
    temptemp = copy.deepcopy(temp1)
    temp1 = copy.deepcopy(temp2)
    takenseats = 0
    for ii in range(len(temp2)):
        for jj in range(len(temp2[0])):
            taken, empty = countocc(ii,jj,temp1)
            if temp1[ii][jj] == 'L' and taken == 0:
                temp2[ii][jj] = '#'
            elif temp1[ii][jj] == '#' and taken >= 4:
                temp2[ii][jj] = 'L'
            if temp1[ii][jj] == '#':
                takenseats+=1
    itt +=1
countL = 0
countper = 0
counttake = 0
for p in range(len(temp1)):
    countper += len(re.findall('\.',str(temp1[p])))
    counttake += len(re.findall('#',str(temp1[p])))
    countL += len(re.findall('L',str(temp1[p])))

print('Open . seats ',countper,'\n Taken # seats ',counttake,
      '\n Open L seats ',countL,'\n counted total seats',countper+countL+counttake)
        






                