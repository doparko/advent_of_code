# Running code for day 3

import numpy as np

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

print(topin[2],leftin[2],width[2],height[2])

minx = width
maxx = width + leftin
miny = height
maxy = height + topin

# Will loop over the width and height
# leftin and topin are starting positions
# check cell, if 0 then place a 1, if 1 then place 'x', if x then nothing
# We then count up the amount of x's we have and that is solution

