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
filename = 'day12_inputsample.txt'
#filename = 'day12_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

def possiblepath(mapp):
    mystep = mapp['start']
    for e in mystep:
                

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
            
# paths = possiblepath(cavemap)
    
