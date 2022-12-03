# Oparko
# Advent of Code 2022 Yay
#
# Day 2
#
# Goal rock paper scissors
# We are given a sheet of opponent hands and our hands. From there we
# should find out the score associated with the round
# Win = 6, Draw = 3, Lose = 0
# My hand also has value,
# Rock = 1 , Paper = 2, Scissors = 3

# # ##################################################################### # #
# A = rock, B = Paper, C = Scissors
# X = rock, Y = Paper, Z = Scissors

import matplotlib.pyplot as plt
import re
import numpy as np
import math


# input data

filename = 'day2_input.txt'

datin = open(filename)
datinss = datin.read()
datin.close()

datas = datinss.split('\n')


# Functions start here

# Part 1 functions

def mresults(apick):
    winmap = {'A':'Y', 'B':'Z', 'C':'X'}
    drawmap = {'A':'X', 'B':'Y', 'C':'Z'}
    losemap = {'A':'Z', 'B':'X', 'C':'Y'}
    winn = winmap[apick]
    losee = losemap[apick]
    draww = drawmap[apick]
    return winn, losee, draww

def matchstate(pick):
    opponent = pick[0]
    me = pick[-1]
    win, lose, draw = mresults(opponent)
    mypick = {'X':1,'Y':2,'Z':3}
    score = 0 
    score = mypick[me] + (me == win)*6 + (me == lose)*0 + (me == draw)*3
    print("win is ",win," , lose is ",lose," , draw is ",draw," my pick is ",me,", the score is ",score)
    return score

# Part 2 functions

def match2(pick):
    opponent = pick[0]
    condition = pick[-1]
    mine = myhand(opponent,condition)
    handscore = {'A':1,'B':2,'C':3}
    winscore = {'X':0,'Y':3,'Z':6}
    score = handscore[mine] + winscore[condition]
    return score
    

def myhand(they,cond):
    if cond == 'X':
        # Lose
        pmap = {'A':'C','B':'A','C':'B'}
    elif cond == 'Y':
        pmap = {'A':'A','B':'B','C':'C'}
    else:
        pmap = {'A':'B','B':'C','C':'A'}
    return pmap[they]
    
fullscore = 0

for e in datas:
    fullscore+=matchstate(e)
    
print("Part 1 answer for the full score is: ",fullscore)
    

# Part 2 
# X = Lose , Y = Draw , Z = Win
# Still need to find the score for our rounds and sum up


score2 = 0
for e in datas:
    score2 += match2(e)
    
print("Part 2 answer for the full score is: ",score2)