# AOC 2020 Day 3
# Chris Oparko
#
# Goal is to find the amount of trees encountered in the path while taking
# a right 3 down 1 path to reach the end. 

import numpy as np

filename = '2020_d3.txt'
datin = open(filename)
datinss = datin.readlines()

vertlen = len(datinss)
horlen = len(datinss[0][:-1])

# the amount of iterations sliding and counting trees
#treecount = 0 
#iterations = 0 # was neccessary for part 1

moveright = np.array([1,3,5,7,1])
movedown = np.array([1,1,1,1,2])
treehit = np.zeros(5)

for j in range(len(moveright)):
    iterations = 0
    while iterations*movedown[j] < vertlen:
        row = movedown[j]*iterations
        col = (moveright[j]*iterations)%horlen
        if datinss[row][col] == '#':
            treehit[j] +=1
#            treecount +=1
        iterations +=1
    
#print("You have collided with ",treecount," trees, oh my...")
print("You have collided with this amount of trees on your path with the different methods:",treehit)
print("Your product of all trees hit is: ",np.prod(treehit))
