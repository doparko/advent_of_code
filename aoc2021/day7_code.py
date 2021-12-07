# AOC 2021 Day 7
# Chris O
#
# Goal to find the location that would minimize crab movement in horizontal direction
# You are then to find fuel used during that move
# example

# 16,1,2,0,4,2,7,1,2,14

# solution position 2 and fuel 37


import matplotlib.pyplot as plt
import re
import numpy as np
import math
#filename = 'day7_inputsample.txt'
filename = 'day7_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datinss = datinss.split(',')
data = [int(x) for x in datinss]

# Function that determines the amount of fuel taken by each crab to get to a position desired
def crabfuel(pos,crabs):
    fuelcount=0
    for i in crabs:
        fuelcount += abs(i-pos)
    return fuelcount

# Same function above, however for part 2 each step requires an additional amount of fuel to the previous move
def crabfuel2(pos,crabs):
    fuelcount=0
    for i in crabs:
        n = abs(i-pos)
        fuelcount+= (n*(n+1))/2
    return fuelcount

end, begin = max(data), min(data)

fuel1 = []
fuel2 = []

for i in range(begin,end+1):
    fuel1.append(crabfuel(i,data))
    fuel2.append(crabfuel2(i,data))
    
print('Part 1, min fuel needed:',min(fuel1))
print('Part 2, min fuel needed:',min(fuel2))    