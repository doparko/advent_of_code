# AOC 2020 Day 12
# Chris O
#
# Goal is to take direction instructions that tell us a direction to move and how much (N,E,S,W #)
# Direction to turn L or R and degrees (R# or L#)
# how much to move forward (F#)

import numpy as np
import re
import statistics as st
import copy

#filename = 'test_d12.txt'
filename = '2020_d12.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss.split('\n')

def newface(lor,amt,initial):
    codedirection = {'R':'NESW','L':'NWSE'}
    #print('start facing',initial,' and after turning ',lor,amt,' times we now face ',codedirection[lor][(codedirection[lor].find(initial)+amt)%4])
    return codedirection[lor][(codedirection[lor].find(initial)+amt)%4]

def moveforward(start,move,faceing):
    final = np.array([start[0],start[1]])
    if faceing =='N':
        final[1] = final[1]+move
    elif faceing =='S':
        final[1] = final[1]-move
    elif faceing =='E':
        final[0] = final[0]+move
    else:
        final[0] = final[0]-move
    #print('We are moving ',faceing,move,',start ',start, ' and end ',final)
    return final
        
def newpos(loc,fc,instruct):
    doo = instruct[0]
    go = int(instruct[1:])
    if (doo == 'L') or (doo == 'R'):
        num = int(go/90)
        fc = newface(doo,num,fc)
    elif doo == 'F':
        loc = moveforward(loc,go,fc)
    else:
        loc = moveforward(loc,go,doo)
    return loc,fc
 
def newrot(lor,amt,way):
    left = np.array([[0,-1],[1,0]])
    right = np.array([[0,1],[-1,0]])
    for j in range(amt):
        if lor == 'L':
            way = np.matmul(left,way)
        else:
            way = np.matmul(right,way)
    return way

def moveway(start,wp,amt):
    #final = np.array([0,0])
    #print('in moveway',start[0],'waypoint',wp[0])
    for j in range(amt):
        start[0] = start[0] + wp[0]
        start[1] = start[1] + wp[1]
    return start
    
    
def newplace(loc,wloc,inst):
    doo = inst[0]
    go = int(inst[1:])
    if (doo == 'L') or (doo == 'R'):
        num = int(go/90)
        wloc = newrot(doo,num,wloc)
    elif doo == 'F':
        loc = moveway(loc,wloc,go)
    else:
        wloc = moveforward(wloc,go,doo)
    return loc,wloc
      
pos1 = np.zeros(2)
pos2 = np.zeros(2)
wypoint = np.array([10,1])
face = 'E'

# part 2
#
# Running through the data list to have each instruction read
#for e in datas:
#	pos1,face = newpos(pos1,face,e)

#print('Your manhattan distance is',abs(pos1[0])+abs(pos1[1]),' and you are at position',pos1)    
print('start values',pos2,'wp',wypoint)
for x in datas:
    pos2,wypoint = newplace(pos2,wypoint,x)
    
print('Your manhattan distance is',abs(pos2[0])+abs(pos2[1]),' and you are at position',pos2)
