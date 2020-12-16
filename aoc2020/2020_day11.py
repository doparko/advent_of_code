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

def padwith(vector, pad_width, iaxis, kwargs):
	vector[:pad_width[0]] = 'p'
	vector[-pad_width[1]:] = 'p'
	return vector

def countsee(row,col,thedata):
    stake = 0
    sopen = 0
    #print('row %d col %d' %(row,col))
    mappad = np.pad(np.array(thedata),100,padwith)
    uu,dd,ll,rr,ul,ur,dl,dr =[],[],[],[],[],[],[],[]
    num = 0
    prow=row+100
    pcol=col+100
    kk = 1
    while num <8:
    	#print('new code value ',mappad[prow-kk,pcol],'old code value ',thedata[row-kk][col])
    	#print(uu,ll,dd,rr,ul,ur,dl,dr)
    	if (mappad[prow-kk,pcol] == '#' or mappad[prow- kk,pcol] == 'L' or mappad[prow-kk,pcol] == 'p') and (len(uu) == 0):
    		uu.append(mappad[prow-kk,pcol])
    	if (mappad[prow+kk,pcol] == '#' or mappad[prow+kk,pcol] == 'L' or mappad[prow+kk,pcol] == 'p') and (len(dd) == 0):
    		dd.append(mappad[prow+kk,pcol]) 
    	if (mappad[prow,pcol-kk] == '#' or mappad[prow,pcol-kk] == 'L' or mappad[prow,pcol-kk] == 'p') and (len(ll) == 0):
    		ll.append(mappad[prow,pcol-kk]) 
    	if (mappad[prow,pcol+kk] == '#' or mappad[prow,pcol+kk] == 'L' or mappad[prow,pcol+kk] == 'p') and (len(rr) == 0):
    		rr.append(mappad[prow,pcol+kk])
    	if (mappad[prow-kk,pcol-kk] == '#' or mappad[prow-kk,pcol-kk] == 'L' or mappad[prow-kk,pcol-kk] == 'p') and (len(ul) == 0):
    		ul.append(mappad[prow-kk,pcol-kk])
    	if (mappad[prow-kk,pcol+kk] == '#' or mappad[prow-kk,pcol+kk] == 'L' or mappad[prow-kk,pcol+kk] == 'p') and (len(ur) == 0):
    		ur.append(mappad[prow-kk,pcol+kk])
    	if (mappad[prow+kk,pcol+kk] == '#' or mappad[prow+kk,pcol+kk] == 'L' or mappad[prow+kk,pcol+kk] == 'p') and (len(dr) == 0):
    		dr.append(mappad[prow+kk,pcol+kk])
    	if (mappad[prow+kk,pcol-kk] == '#' or mappad[prow+kk,pcol-kk] == 'L' or mappad[prow+kk,pcol-kk] == 'p') and (len(dl) == 0):
    		dl.append(mappad[prow+kk,pcol-kk])
    	kk+=1
    	num = len(dd+uu+ll+rr+ul+ur+dl+dr)
    print('iteration ',itt,' all closest',uu,ll,dd,rr,ul,ur,dl,dr)
    if uu[0]=='#':
    	stake+=1 
    if ul[0]=='#':
    	stake+=1 
    if ur[0]=='#':
    	stake+=1 
    if dd[0]=='#':
    	stake+=1 
    if dl[0]=='#':
    	stake+=1 
    if dr[0]=='#':
    	stake+=1 
    if ll[0]=='#':
    	stake+=1 
    if rr[0]=='#':
    	stake+=1
    #print(uu[0],'and',stake)
    return stake,sopen

    
# Rules
# Seat is empty (L) and there are no surrounding seats, becomes filled
# Seat is taken (#) and there are at least 4 surrounding that are full, becomes empty


mydat = []
skdat = []
for j in range(len(datas)):
    mydat.append(list(datas[j]))
    skdat.append(list(datas[j]))
    for x in range(len(datas[0])):
        if skdat[j][x] == 'L':
            skdat[j][x] = '#'
    
temp1 = skdat[:]
temp2 = copy.deepcopy(temp1)

temp1[0][0] = 'L'

itt = 0
while temp1 != temp2:
    temptemp = copy.deepcopy(temp1)
    temp1 = copy.deepcopy(temp2)
    takenseats = 0
    for ii in range(len(temp2)):
        for jj in range(len(temp2[0])):
            taken, empty = countsee(ii,jj,temp1)
            if temp1[ii][jj] == 'L' and taken == 0:
                temp2[ii][jj] = '#'
            elif temp1[ii][jj] == '#' and taken >= 5:
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
        

# This took 82 iterations to get to the answer below. took sooooo long.
#iteration  82  all closest ['L'] ['L'] ['p'] ['p'] ['L'] ['p'] ['p'] ['p']
#Open . seats  1447 
# Taken # seats  1897 
# Open L seats  4846 
# counted total seats 8190




                