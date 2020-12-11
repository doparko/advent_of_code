# AOC 2020 Day 9
# Chris O
#
# Goal is to

import numpy as np
import re
import statistics as st


filename = '2020_d9.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss[:-1].split('\n')

numlen = len(datas)
testdata = np.zeros(numlen)
for i in range(numlen):
    testdata[i] = int(datas[i])
    
def group25(index):
    if index < 25:
        return[]
    xv,yv = np.meshgrid(testdata[index-25:index],testdata[index-25:index])
    mymat = xv+yv
    return mymat

answer = []
iindex = []
for e in range(len(testdata)):
    if e >= 25:
        if testdata[e] not in group25(e):
            answer.append(testdata[e])
            iindex.append(e)
            
#print('first not in: ',answer[0])
            
newend = iindex[0]
grouping = 2
itt = 0

answer2 = []
while len(answer2) == 0:
    for k in range(newend-grouping):
        value = sum(testdata[k:k+grouping])
        if value == answer[0]:
            answer2.append([k,k+grouping])
    grouping +=1
    
    
realanswer = max(testdata[answer2[0][0]:answer2[0][1]]) + min(testdata[answer2[0][0]:answer2[0][1]])
print('Your answer to the sum of big and large grouping: ',max(testdata[answer2[0][0]:answer2[0][1]]),min(testdata[answer2[0][0]:answer2[0][1]]))
print('your real answer is: ',realanswer)