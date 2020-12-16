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
        print('start ',start,' end ',end)
        temp = np.linspace(start,end,end-start+1)
        totarray = np.append(totarray,temp)
    return totarray

ranges = []
ranges.extend(re.findall('\d+\-\d+',datas[0]))

okayvalues = valrange(ranges)
notvalid = []
checkthese = datas[2].split('\n')
for i in checkthese[1:]:
    group = [int(x) for x in i.split(',')]
    for m in group:
        if m not in okayvalues:
            notvalid.append(m)

answer1 = sum(notvalid)
print('Part 1 answer is: ',answer1)