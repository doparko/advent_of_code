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

import re
import numpy as np
import math
#filename = 'day4_inputsample.txt'
filename = 'day4_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = np.array(datinss.split('\n\n'))

# Bing location from indicie function
def bingopos(index):
    row = math.floor((index)/5)
    column = index%5
    return row,column

# Function to plot on bingo card
def bingoplot(card,number):
    try:
        card[card.index(number)] = "X"
    except:
        pass
    return card

# Check bingo function
def checkbingo(card):
    # Checking horizontals
    # Horizontals index 0 - 4, 5 - 9, and so on till 20 - 24
    shift = 5
    for a in range(5):
        if card[0+a*shift] == card[1+a*shift] == card[2+a*shift] == card[3+a*shift] == card[4+a*shift] == 'X':
            return True
    # Checking Verticals
    # Verticals index [0,5,10,15,20] , [1,6,11,16,21] .... [4,9,14,19,24]
    for b in range(5):
        if card[0+b] == card[5+b] == card[10+b] == card[15+b] == card[20+b] == 'X':
            return True
    return False

# Removes blotted values and sums the remaining
def sumremain(card):
    count = 0
    for e in card:
        if e != 'X':
            count+= int(e)
    return count

# Bingo numbers being called
callnum = re.findall('\d{1,2}',datas[0])

# Bingo cards
numcards = len(datas) - 1
bincards = [None]*numcards


# Getting all the cards their on index in this list and making them one dimension flat
# Can get the actual position by running bingopos function to get row/column
for i in range(len(bincards)):
    bincards[i] = re.findall('\d{1,2}',datas[i+1])   # The first element in datas are the numbers called so we skip ahead

bingo = 0
for m in callnum:
    for n in range(len(bincards)):
        bincards[n] = bingoplot(bincards[n],m)
        if checkbingo(bincards[n]):
            bingo = True
            break
    if bingo:
        break

# Now that we left on the winning bingo card and number, lets comput sum of remaining numbers
# and multiply by the last called number

# Sum of remining not blotted values
sumbingo = sumremain(bincards[n])

# Product of last number and sum
product1 = int(m)*sumbingo

print('The answer to part 1 is: ',product1)

# Part 2 we want to take the card that wins last
# Approach, do the same thing but instead we remove a card once it gets a bingo unless it is the last one

bingo2 = 0
number_of_bingos = 0
already_bingo = []
for m in callnum:
    for n in range(len(bincards)):
        try:
            already_bingo.index(str(n))
            wall = False
        except:
            wall = True
        if wall:   
            bincards[n] = bingoplot(bincards[n],m)
            if checkbingo(bincards[n]):
                number_of_bingos +=1
                already_bingo.append(str(n))
                if number_of_bingos == len(bincards):
                    bingo2 = True
                    break
    if bingo2:
        break

# Sum of remining not blotted values
sumbingo2 = sumremain(bincards[n])

# Product of last number and sum
product2 = int(m)*sumbingo2

print('The answer to part 2 is: ',product2)


        
