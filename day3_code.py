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
                        
        

"""
for ii in range(datlen):
        xlength = maxx[ii] - minx[ii] + 1
        xd = np.linspace(minx[ii],maxx[ii],xlength)
        ylength = maxy[ii] - miny[ii] + 1
        yd = np.linspace(miny[ii],maxy[ii],ylength)
        xmat,ymat = np.meshgrid(xd,yd)
        comb = xmat%1000 + ymat*1000
        combflat = list(comb.flatten())
        timelist.append(time.time() - start_t)
        growlen.append(len(growlist))
        for e in combflat:
                if (str(growlist).find(" "+str(e)) != -1) or (str(growlist).find("["+str(e)) != -1):
                        sqcount = sqcount + 1
                else:
                        growlist.append(e)
"""                                               
print("The amount of overlapping fabric in sq inches is:",sqcount)


        

##for idim in range(datlen):
##        miinx = minx[idim] -1
##        maaxx = maxx[idim] -1
##        miiny = miny[idim] -1
##        maaxy = maxy[idim] -1
##        for x in range(1000):
##                for y in range(1000):
##                        if (x >= (miinx and x <= maaxx) and (y >= miiny and y <= maaxy):
##                                if fabric[x,y] == 0:
##                                        fabric[x,y] = 1
##                                elif fabric[x,y] == 1:
##                                        fabric[x,y] = 1000000
##print("You have the following amount of sq inch overlaps:",np.floor(fabric.sum()/1000000))
##        

# Will loop over the width and height
# leftin and topin are starting positions
# check cell, if 0 then place a 1, if 1 then place 'x', if x then nothing
# We then count up the amount of x's we have and that is solution

