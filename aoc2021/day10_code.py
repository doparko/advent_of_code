# AOC 2021 Day 10
# Chris O
#
# Goal 

#Example


import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day10_inputsample.txt'
#filename = 'day10_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

# function going through and check each line for corruption
# Corrupt if open and ending on wrong type of bracket
def corrupt(string):
    bracket = {')':'(', '}':'{', ']':'[', '>':'<'}
    left = string[0]
    for i in range(len(string)-1):
        if string[i+1] in bracket:              # Checks if an end bracket
            if left != bracket[string[i+1]]:    # Checks if brackets don't match
                return string[i+1]              # Return the corrupt bracket
        left = string[i+1]                      # redefines the previous value in string
    return 'a'
        
# Counting the amount of different types of brackets found as corruption
brackcount = {')':0, '}':0, ']':0, '>':0}

for e in datas:
    corrval = corrupt(e)
    if corrval in brackcount:
        brackcount[corrval] +=1
        