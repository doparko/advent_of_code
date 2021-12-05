# AOC 2021 Day 4
# Chris O
#
# Goal use the tope input to have as bingo numbers called
# Mark off the board with called numbers in order and stop when a "bingo" is called
# only vertical or horizontal (no diagonal)
# on winning board sum all unmarked numbers and then multiply by the recent called number, that is solution


# example

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7


import numpy as np
import math
filename = 'day4_inputsample.txt'
#filename = 'day4_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = np.array(datinss.split('\n\n'))

# Bing location from indicie function
def bingopos(index):
    row = math.floor((index)/5)
    column = index%5
    return row,column

# Bingo calling numbers
binum = datas[0]
boards = [None]*(len(datas)-1)
# Bingo boards
# First indicie = bingo board
# Second        = indicie location
for i in range(len(datas)-1):
    boards[i] = datas[i+1].split('\n')

        