# AOC 2020 Day 10
# Chris O
#
# Goal is to

import numpy as np
import re
import statistics as st

filename = 'test_d10.txt'
#filename = '2020_d10.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

mydat= np.array([int(i) for i in datas])
mydat.sort()
mydat =np.append(np.array([0]),mydat)
#def recurnext(index):
#    mlist = []
#    count = 0
#    if index == len(mydat)-1:
#        return 1  
#    elif index >= len(mydat)-2:
#        for n in range(1,2):
#            if mydat[index+n]-mydat[index] < 4:
#                mlist.append(index+n)
#    elif index >= len(mydat)-3:
#        for n in range(1,3):
#            if mydat[index+n]-mydat[index] < 4:
#                mlist.append(index+n)
#    else: #if index == len(mydat)-4:
#        for n in range(1,4):
#            if mydat[index+n]-mydat[index] < 4:
#                mlist.append(index+n)
#    if len(mlist) == 0:
#        return 0
#    else:
#        for ii in mlist:
#            count += recurnext(ii)
#            #print(count)
#        return count
            
def mypath(index):
    mlist=[]
    if index == len(mydat)-1:
        return mlist  
    elif index >= len(mydat)-2:
        for n in range(1,2):
            if mydat[index+n]-mydat[index] < 4:
                mlist.append(mydat[index+n])
    elif index >= len(mydat)-3:
        for n in range(1,3):
            if mydat[index+n]-mydat[index] < 4:
                mlist.append(mydat[index+n])
    else: #if index == len(mydat)-4:
        for n in range(1,4):
            if mydat[index+n]-mydat[index] < 4:
                mlist.append(mydat[index+n])
    return mlist
              
    


dif1 = []
dif2 = []
dif3 = []
difmore = []

for j in range(len(mydat)):
    if j+1 == len(mydat):
        break
    if mydat[j+1] - mydat[j] == 1:
        dif1.append(mydat[j])
    elif mydat[j+1] - mydat[j] == 2:
        dif2.append(mydat[j])
    elif mydat[j+1] - mydat[j] == 3:
        dif3.append(mydat[j])
    elif mydat[j+1] - mydat[j] > 3:
        difmore.append(mydat[j])
      
#mycon = {}
#lengthcon =[]
#for jj in range(len(mydat)):
#    mycon[mydat[jj]] = mypath(jj)
#    lengthcon.append(len(mycon[mydat[jj]]))
    

    
answer2 = 0
barebones = []
itt = 0
while itt != len(mydat)-1:
    if itt >= len(mydat)-2:
        if mydat[itt+1]-mydat[itt] < 4:
            barebones.append(mydat[itt+1])
            itt +=1
        print('in block 1, itt = ',itt)   
    elif itt >= len(mydat)-3:
        for w in range(1,3):
            if mydat[itt+3-w] - mydat[itt] <4:
                barebones.append(mydat[itt+3-w])
                itt+=3-w
                break
        print('in block 2, itt = ',itt)
    else:
        for w in range(1,4):
            if mydat[itt+4-w] - mydat[itt] <4:
                #print('the difference is ',mydat[itt+4-w] - mydat[itt],'saving the ',mydat[itt+4-w],'was at ',mydat[itt])
                barebones.append(mydat[itt+4-w])
                itt+=4-w
                break
        print('in block 3, itt = ',itt)
    
remaining = len(mydat)-len(barebones)-1
for q in range(remaining+1):
    answer2+= (np.math.factorial(remaining))/(np.math.factorial(q)*(np.math.factorial(remaining-q)))
    #print(answer2)
    
print('part 2 answer: ',answer2)
#while itt < len(lengthcon):
#    if lengthcon[ii] >1:
#        multans.append(lengthcon[ii])
#    else:
#        answer2+=
#        
    
    
    
    
    
#print('your answer : ',(1+len(dif1))*(len(dif3)+1))


# Theron's practice problem set
#problem #1:    1,2,3,6,7,8,11,12,13
#problem #2:   1,2,3,4,5,8,9,10,13,14,15,16,17
#

