# AOC 2020 Day 7
# Chris O
#
# Goal is to find how many bags a shiny gold bag can fit in
# Part 2 finds how many bags inside a shiny gold bag

import numpy as np
import re
import statistics as st

#filename = 'test_d72.txt'
filename = '2020_d7.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss[:-1].split('\n')

def countbags(bagcolor,inthis):
    bags = []
    if bagcolor not in inthis:
        return []
    else:
        for i in inthis[bagcolor]:
            #print(i)
            bags.extend([i])
            newbag = countbags(i,inthis)
            #print(newbag)
            bags.extend(newbag)
        return bags

def insidebags(bagcolor,baginside):
    if baginside[bagcolor][0] == 'no other bag':
        return 1
    else:
        count = 0
        for i in baginside[bagcolor]:
            print(i)
            poo = int(i[0]) if baginside[i[2:]][0] != 'no other bag' else 0
            count += int(i[0])*insidebags(i[2:],baginside) + poo
            print(count)
        return count
    
#def countbags(bagcolor,inthis):
#    count = 0
#    if bagcolor not in inthis:
#        print('adding 0 form',bagcolor)
#        return 0
#    else:
#        for i in inthis[bagcolor]:
#            notbags.extend(inthis[i])
#            print('adding 1 from ',i)
#            count += (1 + countbags(i,inthis))
#        return count
            
    

rules = {}
inbag = {}

for e in datas:
    tempin =  re.findall('\d\D+bag|no other bag',e)
    bigbag = e.split('contain')[0][:-2]
    rules[bigbag] = tempin
    for n in tempin:
        litbag = n[2:] if n[0] != 'n' else n
        if litbag not in inbag:
            inbag[litbag] = [bigbag]
        else:
            inbag[litbag].append(bigbag)

numgold = countbags('shiny gold bag',inbag)
numbags = len(set(numgold).intersection(numgold))
print('Shiny gold bag is in ',numbags,' bags')

thebag = 'shiny gold bag'
ingold = insidebags(thebag,rules)
print('There are ',ingold,' bags in the ', thebag)
   
