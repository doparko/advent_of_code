# AOC 2020 Day 15
# Chris O
#
# Goal is to 

import numpy as np
import re
import statistics as st
import copy
import math
from matplotlib import pyplot as plt

#filename = 'test_d15.txt'
#filename = '2020_d15.txt'
#datin = open(filename)
#datinss = datin.read()
#datas = datinss.split('\n')

datas =[0,3,6]            # test data
datas = [13,16,0,12,15,1] # my actual data

gamedict1 = {}
gamedict2 = {}

for e in range(len(datas)):
    gamedict1[datas[e]] = e

for t in range(len(datas)-1):
    gamedict2[datas[t]] = t

itt = len(datas)
last = datas[-1]
ex = [13,16,0,12,15,1]
while itt <30000000:
    if last not in gamedict2:
        gamedict2[last] = itt-1
        last = 0
    else:
        age = itt - gamedict2[last] -1
        gamedict2[last] = itt-1
        last = age
    #print(last)
    ex.append(last)
    itt+=1