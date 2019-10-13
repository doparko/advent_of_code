# day 4 problem

import numpy as np

filename = 'day4_short_input.txt'
datas = open(filename)
data = datas.readlines()
datas.close()

# for month ins = 6 ends = 8
# for day   ins = 9 ends = 11

def mdorder(datin,ins,ends):
    ordlist = []
    for ent in datin:
        dm = int(ent[ins:ends])
        if len(ordlist) == 0:
            ordlist.append(ent)
        else:
            ind = biplace(ordlist,dm,ins,ends)
            ordlist.insert(ind,ent)
    return ordlist

def biplace(plist,numb,inns,endds):
    beg = 0
    end = len(plist)
    sett = 0
    while sett == 0:
        diff = int((end-beg)/2)
        if numb == int((plist[diff])[inns:endds]):
            sett = 1
            index = diff
        elif numb > int((plist[diff])[inns:endds]):
            beg = diff
        else:
            end = diff
    return index

ordmonth = mdorder(data,6,8)
ordday = mdorder(data,9,11)

