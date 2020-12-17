# AOC 2020 Day 16
# Chris O
#
# Goal is to 

import numpy as np
import re
import statistics as st
import copy
import math
from matplotlib import pyplot as plt

filename = 'test_d16.txt'
filename = '2020_d16.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n\n')

def valrange(codes):
    totarray = np.array([])
    for e in codes:
        bloc = e.find('-')
        start = int(e[0:bloc])
        end = int(e[bloc+1:])
        #print('start ',start,' end ',end)
        temp = np.linspace(start,end,end-start+1)
        totarray = np.append(totarray,temp)
    return totarray

ranges = []
ranges.extend(re.findall('\d+\-\d+',datas[0]))

okayvalues = valrange(ranges)
notvalid = []
valid = []
checkthese = datas[2].split('\n')
for i in checkthese[1:]:
    group = [int(x) for x in i.split(',')]
    for m in group:
        if m not in okayvalues:
            notvalid.append(m)
            break
        if m == group[-1]:
            valid.append(group)
        
valarray = np.array(valid)            

answer1 = sum(notvalid)
print('Part 1 answer is: ',answer1)

# We need to create a dictionary that has each set of valid values for a given field
# 
# Put the ticket data into a 2d array such that we can easily pull out an entire column
#
# Remove the rows that had an entry that didn't fit anywhere
#
# Find the field that all the values in column can fit and that will be the field that matches
# With it
#
# Trying to make a ? x n array for the possible value dictionary
fields = datas[0].split('\n')
fdict = {}

for t in fields:
    fieldvalues = re.findall('\d+\-\d+',t)
    fdict[re.findall('[\w ]*\w+:',t)[0][:-1]] = valrange(fieldvalues)

itt = 0
fieldcol = {}
while (len(fdict) != 0) and (itt < len(valarray[0])):
    for j in fdict:
        for k in valarray[:,itt]:
            if k not in fdict[j]:
                break
            if k == valarray[-1,itt]:
                fieldcol[j] = itt
                del fdict[j]
                break
        if j not in fdict:
            break
    itt+=1

# Making my ticket list
myticketall = datas[1].split('\n')
myticket = myticketall[1].split(',')
departkeys = []
answer2=1
for p in fieldcol:
    if 'departure' in p:
        print(p,fieldcol[p])
        answer2*=int(myticket[fieldcol[p]])

print('Part 2 answer is: ',answer2)


