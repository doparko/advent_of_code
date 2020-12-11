# AOC 2020 Day 2
# Chris Oparko
#
# Goal is to count the number of valid passwords given different polices


import numpy as np
import re

filename = '2020_d2.txt'
datin = open(filename)
datinss = datin.readlines()

dimen = len(datinss)
mpass = [None]*dimen

for i in range(dimen):
    mpass[i] = datinss[i][:-1]
    
count1 = 0 # initiate count of valid passwords
count2 = 0
 
for j in mpass:
    hloc = j.find('-') #Hyphen location
    bloc = j.find(' ') #Blank location
    cloc = j.find(':') #Colon location
    
    pmin = int(j[:hloc])
    pmax = int(j[hloc+1:bloc])
    plet = j[bloc+1:cloc]
    
    # Using regex function to search for correct amount of letters
    ex = re.findall(plet,j[cloc+1:])
    amount = len(ex)
    if (amount >= pmin) and (amount <= pmax):
        count1 +=1
        
    npass = j[cloc+1:]
    if (plet == npass[pmin]) ^ (plet == npass[pmax]):
        count2 +=1
        
print('The amount of valid passwords for part 1 is: ',count1)
print('The amount of valid passwords for part 2 is: ',count2)