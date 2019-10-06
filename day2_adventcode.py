"""
Created on Sat Oct  5 15:48:19 2019

@author: dopar
"""
# Advent of Code
# Day 2

# Apparently not used but I have it  here anyway
# import os
# import numpy as np
 
# Using to import my data from text file
filename = "day2_input.txt"

# Opens and reads file by lines, allows to split line into items of list
datain = open(filename,'r')
text = datain.readlines()
datain.close()

part_select = input("Enter the part that you want to do:")

# part 1
if part_select == "1":
    # Some constants that will iterate and count the exact doubles/triples
    dubs = 0
    trips = 0
    i = 0
    
    # Was necessary to make empty list to have sorted, but wasn't neccesary to sort
    xsort = [None] * len(text)
    
    for x in text:
        xsort[i] = sorted(x) #left this in to remind of sort but not needed
        
        checkdub = 0 #sets constant for checking if a double was found already or not within that item
        checktrip = 0 # same as check dub but for the triples
        
        for j in xsort[i]:
            if xsort[i].count(j) == 2 and checkdub == 0: # Works if found exactly 2 matching and there hasn't been one found yet
                dubs = dubs + 1
                checkdub = 1
            elif xsort[i].count(j) == 3 and checktrip == 0: # same as above but for triples
                trips = trips + 1
                checktrip = 1
                
        i = i + 1
    
    checksum = dubs * trips # product which is requsted for answer
    
    print("\nchecksum:" + str(checksum))
# part 2
elif part_select == "2":
    #setting up variable for split up pieces
    sptext = [None] * len(text)
    j = 0
    ans = [None]
    for spec in text:
        sptext[j] = list(spec)
        j = j + 1

    n = len(sptext[0])
    print(len(sptext))
    en = len(sptext) - 1
    print(en)
    for ii in range(n):
        temp = sptext
        for jj in range(n):
            temp[jj].pop(ii)
        # en = len(temp) - 1
        for kk in range(en):
            print(kk)
            newtemp = temp
            trial = newtemp.pop(kk)
            for e in newtemp:
                if trial == e:
                    ans = trial
                    break
    print(ans)
    
else:
    print("bad input buddy")
    

