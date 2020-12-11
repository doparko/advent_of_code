# AOC 2020 Day 5
# Chris O
#
# Goal is to 

import numpy as np
import re
import statistics as st

filename = '2020_d6.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss[:-1].split('\n\n')

# Make a set full of alphabet
alpha = np.linspace(97,122,122-97+1).astype(int)
alpha = [chr(i) for i in alpha]

count1 = 0
count2 = 0
for e in datas:
    tempone = set(alpha).intersection(e)
    count1 += len(tempone)
    temptwo = e.split('\n')
    numlen = len(temptwo)
    for j in tempone:
        if e.count(j) == numlen:
            count2 +=1

    
    
print('You have ',count1,' total yes answers from groups or someting idk')
print('Part two has all people in group agreeing to ',count2,' questions')