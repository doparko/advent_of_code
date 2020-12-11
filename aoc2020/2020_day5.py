# AOC 2020 Day 5
# Chris O
#
# Goal is to find the higher seat id given binary search binary search parameters
# F means front
# B means back
# L means lower (left ish)
# R means upper (right ish)

import numpy as np
import re
import statistics as st

filename = '2020_d5.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

scodes = datas[:-1]
numrows = 128
numcol = 8

def frontback(code, beg, end,low, up):
    if code == 'F':
        end = int(st.mean([beg,end]))
    elif code == 'B':
        beg = int(st.mean([beg,end]))+1
    elif code == 'L':
        up = int(st.mean([low,up]))
    elif code == 'R':
        low = int(st.mean([low,up]))+1
    return beg,end, low, up
    

highid = 0
sids = np.zeros(len(scodes))
itt = 0      
for e in scodes:
    srow = 0
    erow = 127
    scol = 0
    ecol = 7
    for i in e:
        srow,erow,scol,ecol = frontback(i,srow,erow,scol,ecol)
#        print('Code using: ',i,' you get the following for row start / row end / col start / col end:',beg,end, low, up)
    answer = srow*8 + scol
    sids[itt] = answer
    itt +=1
#    print(answer)
    if (answer) > highid:
        highid = answer


# part 2 must find my specific seat id
# It is missing from the list but there is an id that is +1 and one that is -1 from mine
sids.sort() # This orders the list
myseatid = 0
for j in range(len(sids)):
    if sids[j] + 1 != sids[j+1]:
        myseatid = sids[j] + 1
        break
    
print('Your seat id is :',myseatid)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    