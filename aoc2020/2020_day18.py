# AOC 2020 Day 18
# Chris O
#
# Goal is to 

import numpy as np
import re
import statistics as st
import copy
import math
from matplotlib import pyplot as plt

filename = 'test_d18.txt'
#filename = '2020_d18.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

def operate(line):
    value = 0
    a = 0
    while a < len(line):
        if line[a] == '(':
            # Start parentheses
            print('going into parentheses ',line[a+1:])
            try:
                value = str(eval(value+operation+operate(line[a+1:])))
                print(value+operation,'value operation parentheses')
            except:
                value = str(operate(line[a+1:]))
                print('starting with parentheses')
            startnew = line.find(')',a)
            print('was at index ',a,' now at ',startnew)
            a = startnew
        elif line[a] == ')':
            # End parentheses
            print('returning from parentheses with value',value)
            return str(value)
        elif line[a] == '*' or line[a] == '+':
            # sets operation to use
            operation = line[a]
            print('collecting this operation ',operation)
        elif len(re.findall('\d',line[a])) >0:
            # Evaluate the expression
            try:
                value = str(eval(value+operation+line[a]))
                print('did the operation and got ',value)
            except:
                value = line[a]
                print('new value ',value)
        a+=1
    return str(value)
        
        
# answer for part 1 starts off at zero and adds each line up
answer1 = 0

# running through the loop of each entry
for i in datas:
    temp = int(operate(i))
    print('finished a line, it is ',temp)
    answer1+= temp
    
print('Part 1 answer is: ',answer1)
