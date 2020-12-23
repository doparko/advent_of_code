# AOC 2020 Day 17
# Chris O
#
# Goal is to 

import numpy as np
import re
import statistics as st
import copy
import math
from matplotlib import pyplot as plt

filename = 'test_d17.txt'
filename = '2020_d17.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

def neighbors1(cent):
    comma1 = cent.find(',')
    comma2 = cent.find(',',comma1+1)
    x = int(cent[:comma1])
    y = int(cent[comma1+1:comma2])
    z = int(cent[comma2+1:])
    friends = []
    for a in range(-1,2):
        for b in range(-1,2):
            for c in range(-1,2):
                if (a != 0) or (b != 0) or (c != 0):
                    entry = str(x+a)+','+str(y+b)+','+str(z+c)
                    friends.append(entry)
    return friends

def neighbors2(cent):
    comma1 = cent.find(',')
    comma2 = cent.find(',',comma1+1)
    comma3 = cent.find(',',comma2+1)
    print(cent)
    x = int(cent[:comma1])
    y = int(cent[comma1+1:comma2])
    z = int(cent[comma2+1:comma3])
    w = int(cent[comma3+1:])
    friends = []
    for a in range(-1,2):
        for b in range(-1,2):
            for c in range(-1,2):
                for d in range(-1,2):
                    if (a != 0) or (b != 0) or (c != 0) or (d != 0):
                        entry = str(x+a)+','+str(y+b)+','+str(z+c)+','+str(w+d)
                        friends.append(entry)
    return friends

def addneighbors(count,friends):
    for a in friends:
        if a not in count:
            count[a] = 1
        else:
            count[a]+=1
    return

def updatecell(state,count):
    newactive = {}
    for a in count:
        if a not in state:
            state[a] = 0
    for a in state:
        if a not in count:
            #print(a,' was not in count')
            count[a] = 0
    for b in state:
        if state[b] == 1:
            if (count[b] == 2) or (count[b] ==3):
                newactive[b] = 1
        else:
            if count[b] == 3:
                #print('turning on ',count[b])
                newactive[b] = 1
    return newactive
                
# def showgrid(states):
#     for a in states:
#         comma1 = a.find(',')
#         comma2 = a.find(',',comma1+1)
#         x = int(a[:comma1])
#         y = int(a[comma1+1:comma2])
#         z = int(a[comma2+1:])
                    

# initialize which are active
active = {}

for i in range(len(datas)):
    for j in range(len(datas[0])):
        if datas[i][j] == '#':
            active[str(i)+','+str(j)+',0'] = 1

active2 = {}

for i in range(len(datas)):
    for j in range(len(datas[0])):
        if datas[i][j] == '#':
            active2[str(i)+','+str(j)+',0,0'] = 1

# running through a while for 6 iteration cycles
itt = 0

while itt < 6:
    # dictionary for holding how many neighbors are active
    necount = {}
    for i in active:
        myneigh = neighbors1(i)
        addneighbors(necount,myneigh)
    active = updatecell(active,necount)
    #print(itt)
    itt+=1

answer1 = 0
for i in active:
    if active[i] == 1:
        #print(i)
        answer1+=1
        
print('Part 1 answer: ',answer1)

itt2 = 0
while itt2 < 6:
    # dictionary for holding how many neighbors are active
    necount = {}
    for i in active2:
        myneigh = neighbors2(i)
        addneighbors(necount,myneigh)
    active2 = updatecell(active2,necount)
    #print(itt)
    itt2 +=1
    
print('Part 2 answer: ',len(active2))