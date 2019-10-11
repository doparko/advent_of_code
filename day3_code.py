# Running code for day 3

import numpy as np
import time

filename = "day3_input.txt"
datafile = open(filename)
data = datafile.readlines()
datafile.close()

# initiate an array of zeros  where each entry is one sq inch
fabric = np.zeros((1000,1000))

datlen = len(data)
empt = [None] * datlen
num =[''] * datlen
crap =[''] * datlen
loc = [''] * datlen
dimensions =[''] * datlen
leftin = [''] * datlen
tophold = [''] * datlen
lefthold = [''] * datlen
topin= [''] * datlen
width = [''] * datlen
height = [''] * datlen
widthhold = [''] * datlen
heighthold = [''] * datlen

itt = 0
# Running for loop to gather data in groups by their type
for e in data:
	num[itt], crap[itt], loc[itt], dimensions[itt] = e.split()
	lefthold[itt], tophold[itt] = loc[itt].split(',')
	topin[itt] = int(tophold[itt].replace(':',''))
	leftin[itt] = int(lefthold[itt])
	widthhold[itt], heighthold[itt] = dimensions[itt].split('x')
	width[itt] = int(widthhold[itt])
	height[itt] = int(heighthold[itt])
	itt = itt + 1

#print(topin[2],leftin[2],width[2],height[2])

miny = np.array(leftin)
maxy = np.array(height) + np.array(leftin)
minx = np.array(topin)
maxx = np.array(width) + np.array(topin)
timelist =[]
growlen = []
growlist = []
sqcount = 0
start_t = time.time()

for ii in range(datlen):
        r = topin[ii]
        c = leftin[ii]
        xlength = maxx[ii] - minx[ii]
        xd = np.linspace(1,1,xlength)
        ylength = maxy[ii] - miny[ii]
        yd = np.linspace(1,1,ylength)
        xmat,ymat = np.meshgrid(xd,yd)
        fabric[r:r+xmat.shape[0],c:c+xmat.shape[1]] += xmat
        

for xx in range(1000):
        for yy in range(1000):
                if fabric[xx,yy] > 1:
                        sqcount += 1


# Part 2
# Would look for an area that had no overlap and return the id of that one

exfab = ['']*datlen

for ii in range(datlen):
        r = topin[ii]
        c= leftin[ii]
        xlength = maxx[ii] - minx[ii]
        xd = np.linspace(1,1,xlength)
        ylength = maxy[ii] - miny[ii]
        yd = np.linspace(1,1,ylength)
        xmat,ymat = np.meshgrid(xd,yd)
        exfab[ii] = fabric[r:r+xmat.shape[0],c:c+xmat.shape[1]]
        if exfab[ii].sum() == width[ii]*height[ii]:
                ans = num[ii]
                break



                                              
print("The amount of overlapping fabric in sq inches is:",sqcount)
print("The pattern that has no overlap is:#",ans)
