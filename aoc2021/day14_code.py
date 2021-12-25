# AOC 2021 Day 14
# Chris O
#
# Goal from given starting point you will need to look at first two pairs
# decide if there is a rule that applies and carry it out placing new letter between
# this will increase list length as you go so keep that in mind
# After running through the list once you have completed 1 step
# do this X number of times and solution is the highest frequency minus lowest frequency letter

#Example
# NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C


import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day14_inputsample.txt'
filename = 'day14_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

start, datas = datinss.split('\n\n')
datas = datas.split('\n')

# Functions
def synth(string,mapp):
    i = 0
    while i < len(string)-1:
        tmp = string[i]+string[i+1]
        #print('Checking: ',tmp,' in the list' )
        if tmp in mapp:
            string.insert(i+1,mapp[tmp])
            i+=2
        else:
            i+=1
        #print('i is: ',i,' and the length of string is: ', len(string))
    return string

def synth2(string,mapp):
    length = len(string)
    newlength = 2*length - 1
    newstring = np.array([None]*newlength)
    # Our iterators for the original and new letters
    i_old = 2*np.linspace(0,length-1,length,dtype=int)
    i_new = 2*np.linspace(0,length-2,length-1,dtype=int)+1
    # Easy to do our originals as we just copy them into new places
    newstring[i_old] = string[:]
    # Our new values are a bit harder as we have to pair up the letters
    # and from there use our dictionary map to get the values we need
    # You need to do a np.char.add(x1,x2) in order to and strings from arrays
    pfirst = np.linspace(0,length-2,length-1,dtype=int)
    psecond = np.linspace(1,length-1,length-1,dtype=int)
    #print('pfirst is: ', pfirst,'psecond is: ',psecond)
    #print('first string is: ',string[psecond])
    pletters = np.char.add(string[pfirst],string[psecond])
    #print('pletters: ',pletters)
    newstring[i_new] = np.array([mapp[element] for element in pletters])
    return newstring
    

def countoccur(string):
    count = {}
    for i in string:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

# Cleaning up my map data
polymer = np.array(list(start))
lettermap = {}

for e in datas:
    codes = re.findall('\w+',e)
    lettermap[codes[0]] = codes[1]
    
steps = 40
for e in range(steps):
    polymer = synth2(polymer,lettermap)
    polymer = polymer.astype(str)

lettervalues = list(countoccur(polymer).values())
maximum = max(lettervalues)
minimum = min(lettervalues)

print('Part 1, the max minus min is: ',maximum-minimum)
