"""
Created on Sat Oct  5 15:48:19 2019

@author: dopar
"""
# Advent of Code
# Day 2

import os
import numpy as np
 
filename = "day2_input.txt"

datain = open(filename,'r')

text = datain.readlines()

dubs = 0
trips = 0
i = 0

xsort = [None] * len(text)

for x in text:
    xsort[i] = sorted(x)
    
    checkdub = 0
    checktrip = 0
    
    for j in xsort[i]:
        if xsort[i].count(j) == 2 and checkdub == 0:
            dubs = dubs + 1
            checkdub = 1
        elif xsort[i].count(j) == 3 and checktrip == 0:
            trips = trips + 1
            checktrip = 1
            
    i = i + 1

checksum = dubs * trips

print(checksum)

datain.close()