# AOC 2021 Day 10
# Chris O
#
# Goal is to find corrupted lines in the string, get score for those specific types of
# corruptions. Part 2 has you complete this lines and again find score with that.

#Example


import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day10_inputsample.txt'
filename = 'day10_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')


# Writing a function to deal with a string
# If there is a legal open close bracket, it removes both
# If there is a corruption it will stop and return False (for corrupt) and the corrupt bracket
# If no corruption at all it returns True and random word for non corrupt
def checkcorrupt(string):
    bracket = {')':'(', '}':'{', ']':'[', '>':'<'}
    string = list(string)
    # Goal here is to remove the acceptable brackets from the string until we see it
    # is all okay or finding one corruption
    i = 0
    while i < len(string)-1:
        left = string[i]                  # For comparing 2 characters, this is left/first one
        right = string[i+1]               # This is right/second character
        if (right in bracket) and (left not in bracket):    # Checking if right character is close and left is open
            if bracket[right] == left:                      # If a good open and close remove those two and start over
                string.pop(i)
                string.pop(i)
                i = -1
            else:                                           # This is a corruption detected
                return True, right
        i+=1                                                
    return False, ''.join(string)

# Function to return the missing pieces to the string
def completeline(string):
    bracket = {'(':')' , '{':'}' , '[':']' , '<':'>'}
    string = string[::-1]
    newstring = ''
    for i in string:
        newstring = newstring + bracket[i]
    return newstring
    
# Function to score the completing string characters
def completescore(string):
    comscore = {')':1, '}':3, ']':2, '>':4}
    score = 0
    for i in string:
        score*= 5
        score+= comscore[i]
    return score
                
       
# Counting the amount of different types of brackets found as corruption
brackcount = {')':0, '}':0, ']':0, '>':0}
brackscore = {')':3, '}':1197, ']':57, '>':25137}

# Collecting the incomplete and not corrupted strings
incomplete = []

for e in datas:
    corrval = checkcorrupt(e)
    if corrval[0]:
        brackcount[corrval[1]] +=1
    else:
        incomplete.append(corrval[1])

# Part one value
count1 = 0
for m in brackcount:
    count1+= brackcount[m]*brackscore[m]

# Part two scoring and sorting of values
scores = []
for m in incomplete:
    finstring = completeline(m)
    scores.append(completescore(finstring))

sortscore = sorted(scores)
ans2 = sortscore[int(np.floor(len(sortscore)/2))]
    
print('Part 1 all scores together are: ',count1)
print('Part 2 middle score of the now completed list is: ', ans2)