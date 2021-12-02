# AOC 2021 Day 2
# Chris O
#
# Goal is to determine the final depth and forward location
# operations are:
# forward - horizontal position increase
# up - decreases depth (sounds funny but thats it)
# down - increase depth

# example

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2

import numpy as np

filename = 'day2_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()
datas = np.array(datinss.split('\n'))

# Function to take location and operation and yields new location
def substep1(loc,operation):
    direction = operation[0]
    amt = int(operation[-2:])
    if direction == 'f':
        loc[0] = loc[0] + amt
    elif direction == 'u':
        loc[1] = loc[1] - amt
    else:
        loc[1] = loc[1] + amt
    return loc

def substep2(loc,operation):
    direction = operation[0]
    amt = int(operation[-2:])
    if direction == 'f':
        loc[0] = loc[0] + amt
        loc[1] = loc[1] + amt*loc[2]
    elif direction == 'u':
        loc[2] = loc[2] - amt
    else:
        loc[2] = loc[2] + amt
    return loc

#Part 1
location1 = [0,0]  # Start location

for e in datas:
    location1 = substep1(location1,e)
    
print('Part 1 location is:',location1,' And your product of final location is: ',location1[0]*location1[1])

#Part 2 now we track aim in addition to our dept and horizontal position
# forward adds X to horizontal position AND increase depth by aim*X
# down increases your aim
# up decreases your aim

location2 = [0,0,0]

for e in datas:
    location2 = substep2(location2,e)
    
print('Part 2 location is:',location2,' and your product between horizontal and depth is: ',location2[0]*location2[1])
    
