# AOC 2021 Day 22
# Chris O
#
# Goal from the input you want to turn on or off the cubes in range given
# solution is the number of cubes on at the end

#Example


import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day22_inputsample.txt'
filename = 'day22_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

p1data = datas[:20]
length = len(p1data)

# Cleaning up data
state = [None]*length
xranges = [None]*length
yranges = [None]*length
zranges = [None]*length

for e in range(length):
    state[e], tmp = p1data[e].split(' ')
    xrange,yrange,zrange = tmp.split(',')
    # Offset by 50 so we don't have to deal with negative index
    xranges[e] = [int(p)+50 for p in xrange[2:].split('..')]
    yranges[e] = [int(p)+50 for p in yrange[2:].split('..')]
    zranges[e] = [int(p)+50 for p in zrange[2:].split('..')]

# Functions
def changestate(onoff,xes,yes,zes,cube):
    xc,yc,zc = generatecoord(xes,yes,zes)   # This will generate flat list of coordinates for all ranges
    if onoff =='on':
        cube[xc,yc,zc] = 1
    else:
        cube[xc,yc,zc] = 0
    return cube

def generatecoord(ex,ey,ez):
    coor = []
    x = np.linspace(ex[0],ex[1],ex[1]-ex[0]+1,dtype=int)
    y = np.linspace(ey[0],ey[1],ey[1]-ey[0]+1,dtype=int)
    z = np.linspace(ez[0],ez[1],ez[1]-ez[0]+1,dtype=int)
    xm,ym,zm = np.meshgrid(x,y,z)
    return xm.flatten(),ym.flatten(),zm.flatten()

oncubes = np.zeros((101,101,101),dtype=int)
for i in range(length):
    xr = xranges[i]
    yr = yranges[i]
    zr = zranges[i]
    oncubes = changestate(state[i],xr,yr,zr,oncubes)

print('Part 1 solution of on cubes is: ',sum(oncubes.flatten()))

