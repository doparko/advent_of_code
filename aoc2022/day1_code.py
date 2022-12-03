# Oparko
# Advent of Code 2022 Yay
#
# Day **
#
# Goal
#
#


import matplotlib.pyplot as plt
import re
import numpy as np
import math


# input data

filename = 'day1_input.txt'

datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n\n')

nume = len(datas)
cal = [None]*nume
# running through to get calories for each elf

elfnum = 0
for e in datas:
    incalorie = e.split('\n')
    mysum=0
    for i in incalorie:
        mysum = mysum + int(i)
    cal[elfnum] = mysum
    elfnum +=1
    
cal.sort()

print("the answer part 2: ",cal[-1] + cal[-2] + cal[-3])

