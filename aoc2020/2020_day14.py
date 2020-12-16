# AOC 2020 Day 14
# Chris O
#
# Goal is to 

import numpy as np
import re
import statistics as st
import copy
import math

def bi32(initial):
    a = bin(initial).replace("0b","")
    padlen = 36 - len(a)
    return '0'*padlen+a

def storemem(mask,myvalue):
    masklist = list(mask)
    mylist = list(myvalue)
    temp = ''
    for i in range(len(masklist)):
        if masklist[i] != 'X':
            mylist[i] = masklist[i]
    return (temp.join(mylist))

def addsplit(codeadd):
    num = len(re.findall('X',codeadd))
    addresslist = list(codeadd)
    blank = ''
    temp1 = copy.deepcopy(addresslist)
    temp2 = copy.deepcopy(addresslist)
    thelist = []
    #print('initial code was ',codeadd)
    if num == 0:
        return codeadd
    elif num == 1:
        #print('only 1 left')
        for e in range(len(addresslist)):
            if addresslist[e] == 'X':
                temp1[e] = '1'
                temp2[e] = '0'
                break
        t1 = blank.join(temp1)
        t2 = blank.join(temp2)
        thelist.append(t1)
        thelist.append(t2)
        return thelist
    else:
        #print('In the else')
        for e in range(len(addresslist)):
            if addresslist[e] == 'X':
                temp1[e] = '1'
                temp2[e] = '0'
                break
        t1 = blank.join(temp1)
        t2 = blank.join(temp2)
        thelist.extend(addsplit(t1))
        thelist.extend(addsplit(t2))
        return thelist
        
     
             
def memorylocations(loc,mask):
    biloc = list(bi32(loc))
    masklist = list(mask)
    temp = ''
    for i in range(len(masklist)):
        if masklist[i] != '0':
            biloc[i] = masklist[i]
    addressmix = temp.join(biloc)
    alladd = addsplit(addressmix)
    return alladd

filename = 'test_d14.txt'
filename = '2020_d14.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

#Part 1
#
#memlist = {}
#itt = 0
#
#while itt<len(datas):
#    if 'mem' in datas[itt]:
#        stloc = int(re.findall('\[\d+\]',datas[itt])[0][1:-1])
#        value = int(re.findall('\s\d+',datas[itt])[0][1:])
#        bivalue = bi32(value)
#        memlist[stloc] = storemem(currentmask,bivalue)
#    else:
#        # masking template
#        currentmask = re.findall('[X10]+',datas[itt])[0]
#    itt +=1
#
#answer1 = 0
#for e in memlist:
#    answer1+=int(memlist[e],2)
#    
#print('Part 1 answer is: ',answer1)

itt2 = 0
memlist2 = {}
while itt2 < len(datas):
    ttemp = []
    if 'mem' in datas[itt2]:
        stloc = int(re.findall('\[\d+\]',datas[itt2])[0][1:-1])
        value = int(re.findall('\s\d+',datas[itt2])[0][1:])
        memloc = memorylocations(stloc,currentmask)
        for j in memloc:
            memlist2[int(j,2)] = value
    else:
        # masking template
        currentmask = re.findall('[X10]+',datas[itt2])[0]
    itt2 +=1

answer2= 0 
for m in memlist2:
    answer2+=memlist2[m]

print('Part 2 answer is: ',answer2)
    
    
    
    
    
    
    
    
    