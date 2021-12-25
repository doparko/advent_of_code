# AOC 2021 Day 15
# Chris O
#
# Goal 
#Example
# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581

import matplotlib.pyplot as plt
import re
import numpy as np
import math
filename = 'day15_inputsample.txt'
#filename = 'day15_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')

# Clean data
grid = []
for e in datas:
    grid.append([int(x) for x in re.findall('\d',e)])

# If exceed this value you should just ignore the path, this considers strait down and over
hor = sum(grid[-1])
vert = 0
for k in grid:
    vert+= k[0]

maximum = vert + hor

paths = []

