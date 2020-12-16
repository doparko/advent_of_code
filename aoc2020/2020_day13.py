# AOC 2020 Day 13
# Chris O
#
# Goal is to 

import numpy as np
import re
import statistics as st
import copy
import math

def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

filename = 'test_d13.txt'
filename = '2020_d13.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')


#datas = ['982','1789,37,47,1889']
mytime = int(datas[0])
offset = {}
busids = datas[1].split(',')
busid = re.findall('\d+',datas[1])
minid = 1000
mindis = 1000
primes = []
end = 1
for e in busid:
    num = int(e)
    dif = num - (mytime % num)
    if dif < mindis:
       minid = num
       mindis = dif
    if isprime(num):
        primes.append(num)
    end *= num

#get a starting point from multiplying all primes
# End point multiplying all numbers
start = np.prod(np.array(primes))


print('id: ',minid,' distance: ',mindis,'answer: ',minid*mindis)

for j in range(len(busids)):
    if busids[j] != 'x':
        offset[int(busids[j])] = j
 
primes.sort(reverse=True)      
foundg = []
itt = 0
itby = 1
which = 0
while len(foundg) < len(offset):
    print('your itby ',itby,' + your itt ',itt,' = ',itby+itt,'looking for ',primes[which])
    #print('itby',itby,'itt:',itt,'integer which:',which,'checking: ',primes[which])
    if (itt + offset[primes[which]]) % primes[which] == 0:
        foundg.append(primes[which])
        mul = 1
        for x in foundg:
            mul *=x
        itby = mul
        which +=1
    itt +=itby
    #print('itby',itby,'itt:',itt,'checking: ',primes[which])
    
print('Part 2 answer: ',itt-itby)