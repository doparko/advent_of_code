# Oparko
# Advent of Code 2022 Yay
#
# Day 3
#
# Goal 

# Each sack contains two compartments, split the input into two sections
# find the common element in each sack and from there each item has a priority 
# number. Add the common item's priority number for each sack


# # ##################################################################### # #
# A = rock, B = Paper, C = Scissors
# X = rock, Y = Paper, Z = Scissors

import matplotlib.pyplot as plt
import re
import numpy as np
import math


# input data

filename = 'day3_input.txt'

datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

# Function area

def prior(sack):
    slength = len(sack)
    comp1 = sack[0:int(slength/2)]
    comp2 = sack[int(slength/2):]
    for i in comp1:
        if i in comp2:
            common = i
            break
    value = ord(common) -96
    if value < 0:
        value = value + 58
    return value

def prior2(sack1,sack2,sack3):
    for k in sack1:
        if (k in sack2) and (k in sack3):
            common = k
            break
    value = ord(common) -96
    if value < 0:
        value = value + 58
    return value
    
            

# Main code

prioritycount = 0

for e in datas:
    prioritycount += prior(e)

print("Sum of priority part 1 is ", prioritycount)

# Part 2 main code

groupcount = 0
enum = len(datas) # amount of elf bags
gnum = int(enum/3) # amount of groups of 3

for i in range(gnum):
    groupcount += prior2(datas[i*3],datas[i*3+1],datas[i*3+2])
    
print("Sum of priority part 2 with groups is: ", groupcount)
