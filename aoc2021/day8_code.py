# AOC 2021 Day 8
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
filename = 'day8_inputsample.txt'
filename = 'day8_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

def decode(alpha,code):
    nummap = nummatch(alpha)
    code = re.findall(r'\b[a-z]{2,7}\b',code)
    #print(code)
    answer = []
    #print('our number map is: ',nummap)
    for m in code:
        for n in range(len(nummap)):
            if sorted(m) == sorted(nummap[n]):
                answer.append(n)
        #answer.append(nummap.index(m))
    return answer

def combmatch(strings,common,amt):
    #print('String is: ',strings)
    for a in strings:
        count = 0
        for b in a:
            try:
                common.index(b)
                count+=1
            except:
                pass
        #print('for matching ',a,'to ',common,' the count is: ',count,' and amount to match is: ',amt)
        if count == amt:
            answer = a
            break
    return answer
    

def nummatch(letters):
    onegroup = re.findall(r'\b[a-z]{2}\b',letters)[0]
    sevengroup = re.findall(r'\b[a-z]{3}\b',letters)[0]
    fourgroup = re.findall(r'\b[a-z]{4}\b',letters)[0]
    eightgroup = re.findall(r'\b[a-z]{7}\b',letters)[0]
    mix5 = re.findall(r'\b[a-z]{5}\b',letters)
    mix6 = re.findall(r'\b[a-z]{6}\b',letters)
    twogroup = combmatch(mix5,fourgroup,2)
    threegroup = combmatch(mix5,sevengroup,3)
    mix5.remove(twogroup)
    mix5.remove(threegroup)
    fivegroup = mix5[0]
    sixgroup = combmatch(mix6,sevengroup,2)
    mix6.remove(sixgroup)
    ninegroup = combmatch(mix6,fivegroup,5)
    mix6.remove(ninegroup)
    zerogroup = mix6[0]
    return [zerogroup,onegroup,twogroup,threegroup,fourgroup,fivegroup,sixgroup,sevengroup,eightgroup,ninegroup]
    
allnumbers = []
value = 0

for e in datas:
    key , message = e.split('|')
    numbers = decode(key,message)
    allnumbers = allnumbers+numbers
    value+= numbers[0]*1000 + numbers[1]*100 + numbers[2]*10 + numbers[3]
    
count1= 0

for t in allnumbers:
    if (t == 1) or (t == 4) or (t ==7) or (t == 8):
        count1+=1
        
print('Part 1 counting 1,4,7, and 8 is: ',count1)
print('Part 2 summing all outputs is: ',value)