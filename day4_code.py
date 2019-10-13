# day 4 problem

import numpy as np

filename = 'day4_input.txt'
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
            ind = 0
        else:
            ind = biplace(ordlist,dm,ins,ends)
        ordlist.insert(ind,ent)
    return ordlist

def biplace(plist,numb,inns,endds):
    beg = 0
    end = len(plist)
    sett = 0
    while sett == 0:
        diff = int((end+beg)/2)
        if beg == end:
            sett = 1
            index = beg
        elif numb == int((plist[diff])[inns:endds]):
            sett = 1
            index = diff
        elif beg == end:
            sett = 1
            index = beg
        elif numb > int((plist[diff])[inns:endds]):
            beg = int(np.ceil((end+beg)/2))
        else:
            end = diff
    return index

ordmonth = mdorder(data,6,8)      # Orders months
ordday = mdorder(ordmonth,9,11)   # Orders to the day
ordhour = mdorder(ordday,12,14)   # Orders to the hour
ordfinal = mdorder(ordhour,15,17) # Final ordering to the final minute

# Write-Overwrites 
file1 = open("myfile.txt","w")#write mode 
file1.write(''.join(ordmonth)) 
file1.close()


##
##ins = 6
##ends = 8
##ordlist = []

##for ent in data:
##    dm = int(ent[ins:ends])
##    if len(ordlist) == 0:
##        index = 0
##    else:
##        beg = 0
##        end = len(ordlist)
##        sett = 0
##        while sett == 0:
##            diff = int((end+beg)/2)
##            if beg == end:
##                sett = 1
##                index = beg
##                break
##            elif dm == int((ordlist[diff])[ins:ends]):
##                sett = 1
##                index = diff
##                break
##            elif dm > int((ordlist[diff])[ins:ends]):
##                beg = int(np.ceil((end+beg)/2))
##            else:
##                end = diff
##    ordlist.insert(index,ent)
