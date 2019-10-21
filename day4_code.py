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
        dm = int(ent[ins[0]:ends[0]]+ent[ins[1]:ends[1]]+ent[ins[2]:ends[2]]+ent[ins[3]:ends[3]])
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
    count = 0
    while sett == 0:
        count += 1
        diff = int((end+beg)/2)
        #print("diff:",diff,"plist length:",len(plist),"begin:",beg,"end:",end)
        #checknum = int((plist[diff])[inns[0]:endds[0]]+(plist[diff])[inns[1]:endds[1]]+(plist[diff])[inns[2]:endds[2]]+(plist[diff])[inns[3]:endds[3]])
        if beg == end:
            sett = 1
            index = beg
        elif numb == int((plist[diff])[inns[0]:endds[0]]+(plist[diff])[inns[1]:endds[1]]+(plist[diff])[inns[2]:endds[2]]+(plist[diff])[inns[3]:endds[3]]):
            sett = 1
            index = diff
        elif beg == end:
            sett = 1
            index = beg
        elif numb > int((plist[diff])[inns[0]:endds[0]]+(plist[diff])[inns[1]:endds[1]]+(plist[diff])[inns[2]:endds[2]]+(plist[diff])[inns[3]:endds[3]]):
            beg = int(np.ceil((end+beg)/2))
        else:
            end = diff
    return index
starts = [6,9,12,15]
ending = [8,11,14,17]
ordmonth = mdorder(data,starts,ending)      # Orders the data month-day-hour-min

# Write-Overwrites 
file1 = open("myfile.txt","w")#write mode 
file1.write(''.join(ordmonth)) 
file1.close()

minsleep = {}

for ea in ordmonth:
    ident = ea.split(" ")
    if ident[2] == "Guard":
        onguard = ident[3]
    elif ident[2] == "falls":
        sleepstart = int(ea[15:17])
    elif ident[2] == "wakes":
        sleepend = int(ea[15:17]) - 1
        if onguard in minsleep:
            minsleep[onguard] = minsleep[onguard] + (sleepend - sleepstart)
        else:
            minsleep[onguard] = sleepend - sleepstart
slguard = max(minsleep))
print("guard that sleeps the most is:", max(minsleep))

for el in ordmonth:
    maing = (el.split(" "))[2]
    if maing == "guard":
        duty = (el.split(" "))[3]
        


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
