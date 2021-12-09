# AOC 2020 Day 16
# Giving this a second attempt
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
#filename = '2020_d16.txt'
datin = open(filename)
datinss = datin.read()
datin.close()
datas = datinss.split('\n')

# First three sections (or more if harder input) are the rules
rules = datas[:3]
posvalue = []
fieldtype = []
for e in rules:
    temp = re.findall('\d{1,4}[-]\d{1,4}',e) # Found rule intervals
    fieldtype.append(re.findall('[a-z]{1,10}:',e)[0])
    for i in temp:
        posvalue.append(i)
    
allowed = []
for m in posvalue:
    begin, end = m.split('-')
    for n in range(int(begin),int(end)+1):
        allowed.append(n)

badcount = 0
test = []
for e in datas[8:]:
    for k in e:
        try:
            allowed.index(int(k))
        except:
            if k != ',':
                print(k)
                badcount+=int(k)
                test.append(int(k))
            else:
                print(k)
            
        