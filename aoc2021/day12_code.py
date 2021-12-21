# AOC 2021 Day 12
# Chris O
#
# Goal find all paths that only visit small caves (lower case) at most once
# but can go into large caves as many times as you'd like

#Example

# fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW


import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day12_inputsample2.txt'
filename = 'day12_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

def countlower(clist):
    # Counting occurences of letter in clist
    if len(clist) < 2:
        return 0,{clist[0]:1}
    count = {}
    for e in clist:
        if e == e.lower():
            if e in count:
                count[e]+=1
            else:
                count[e]=1
    themax = max(list(count.values()))
    return themax,count
    
def morepath(current,mapp):
    ourpaths = []
    forks = mapp[current[-1]]
    #print('Started here: ' ,current[-1],' and possible paths are: ', forks)
    for e in forks:
        #print('focus on fork: ', e)
        if e == 'end':
            #place holder
            tmp = current.copy()
            #print('Path has reached end: ',tmp)
            ourpaths.append(tmp)
        else:
            if not(e in current and (e == e.lower())):
                tmp = current.copy()
                tmp.append(e)
                #print('ended with this path: ', tmp)
                ourpaths+= morepath(tmp,mapp)
            #else:
                #print('Cannot take this path with: ', e,' because small cave again')
                #print('Path: ', current, ' with: ', e,' after is illegal')
    #print('our paths are: ',ourpaths,'\n\n')
    return ourpaths

def morepath2(current,mapp):
    # For part 2, can visit small cavves at most twice
    ourpaths = []
    forks = mapp[current[-1]]
    #print('Started here: ' ,current[-1],' and possible paths are: ', forks)
    for e in forks:
        #print('focus on fork: ', e)
        if e == 'end':
            #place holder
            tmp = current.copy()
            #print('Path has reached end: ',tmp)
            ourpaths.append(tmp)
        else:
            maxim,lvalues = countlower(current)
            if e == e.upper() or maxim < 2:
                tmp = current.copy()
                tmp.append(e)
                #print('ended with this path: ', tmp)
                ourpaths+= morepath2(tmp,mapp)
            elif e not in lvalues:
                tmp = current.copy()
                tmp.append(e)
                #print('ended with this path: ', tmp)
                ourpaths+= morepath2(tmp,mapp)
            #else:
                #print('Cannot take this path with: ', e,' because small cave again')
                #print('Path: ', current, ' with: ', e,' after is illegal')
    #print('our paths are: ',ourpaths,'\n\n')
    return ourpaths

def allpaths(mapp):
    starting = mapp['start']
    apath = []
    for e in starting:
        thispath = [e]
        #print('Start: ', thispath)
        apath += morepath(thispath,mapp)
    return apath
        
def allpaths2(mapp):
    # For part 2, can visit small caves at most twice
    starting = mapp['start']
    apath = []
    for e in starting:
        thispath = [e]
        #print('Start: ', thispath)
        apath += morepath2(thispath,mapp)
    return apath             

cavemap = {}

for a in datas:
    first, second = a.split('-')
    if first != 'end' and second != 'start':
        if first not in cavemap:
            cavemap[first] = [second]
        else:
            cavemap[first].append(second)
    if second != 'end' and first != 'start':
        if second not in cavemap:
            cavemap[second] = [first]
        else:
            cavemap[second].append(first)
            
paths = allpaths(cavemap)
paths2 = allpaths2(cavemap)
    
print('Part 1 number paths is: ',len(paths))
print('Part 2 number paths is: ',len(paths2))