# AOC 2020 Day 8
# Chris O
#
# Goal is to

import numpy as np
import re
import statistics as st


filename = '2020_d8.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss[:-1].split('\n')

def gamecode(clist,pos):
    code = clist[pos][:3]
    numb = int(clist[pos][4:])
    if code == 'acc':
        return numb, pos + 1
    elif code == 'jmp':
        return 0, pos + numb
    else:
        return 0, pos + 1
    
def rungame(dataloop):
    point = 0
    accumulator = 0
    dupcheck = []
    while point not in dupcheck:
        dupcheck.append(point)
        temp, point =  gamecode(dataloop,point)
        accumulator += temp
        if point == len(dataloop):
            break
    return point in dupcheck, accumulator

myanswer = 0

for e in range(len(datas)):
    tempdata = datas[:]
    cod = tempdata[e][:3]
    if cod == 'jmp':
        tempdata[e] = 'nop'+tempdata[e][3:]
        check, pnumber = rungame(tempdata)
        if check == False:
            myanswer = pnumber
    elif cod == 'nop':
        tempdata[e] = 'jmp'+tempdata[e][3:]
        check, pnumber = rungame(tempdata)
        if check == False:
            myanswer = pnumber

print('The value for accumulator with the edit is ',myanswer)
        
 
# Part 1
#        
#point = 0
#accumulator = 0
#dupcheck = []
#
#while point not in dupcheck:
#    dupcheck.append(point)
#    temp, point =  gamecode(datas,point)
#    accumulator += temp
#    
#print('The value we get from code before repeats is ',)
