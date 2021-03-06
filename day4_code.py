# day 4 problem

import numpy as np
import operator

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
slguard = max(minsleep.items(), key =operator.itemgetter(1))[0]
print("guard that sleeps the most is:", slguard)

amtguard = len(minsleep)

begtime = []
endtime = []
for el in ordmonth:
    indat = el.split(" ")
    maing = indat[2]
    if maing == "Guard":
        duty = indat[3]
    elif duty == slguard:
        if maing == "falls":
            btime = int(el[15:17])
        elif maing == "wakes":
            etime = int(el[15:17]) - 1
            begtime.append(btime)
            endtime.append(etime)

freqtime = np.zeros(60)

for tt in range(len(freqtime)):
    for ii in range(len(begtime)):
        if tt >= begtime[ii] and tt <= endtime[ii]:
            freqtime[tt] += 1

comtime = np.argmax(freqtime)
print("your solution guard number * most commone minute sleept =",comtime*int(slguard[1:]))

#Part 2
guardminutes = {}
for ent in minsleep:
    guardminutes[ent] = []

for tt in ordmonth:
    spinfo = tt.split(" ")
    hed = spinfo[2]
    if hed == "Guard":
        duty = spinfo[3]
    if hed == "falls":
        stime = int(tt[15:17])
    elif hed == "wakes":
        wtime = int(tt[15:17]) - 1
        guardminutes[duty].extend(list(np.linspace(stime,wtime,wtime-stime+1,dtype=int)))
        
def mode(arr):
    if arr==[]:
        return None
    else:
        return max(set(arr), key=arr.count)

print("most common for guard #1217",mode(guardminutes['#1217']),"it should be:",comtime)

#now to count up the modes to see which one is really the most common
guardmodes = {}
for ente in guardminutes:
    clist = guardminutes[ente]
    mcom = mode(clist)
    counting = 0
    for ii in clist:
        if ii == mcom:
            counting += 1
    guardmodes[ente] = counting

#find the speicific guard with most value
guardmost = max(guardmodes.items(), key=operator.itemgetter(1))[0]
print(guardmost)
print("The amount for common minute times the guard:",mode(guardminutes[guardmost])*int(guardmost[1:]))

#print("guard that sleeps same minute most:",np.argmax(guardmodes)," The minute is:",mode(guardminutes[np.argmax(guardmodes)]))
#print("product of these is:",(np.argmax(guardmodes))[1:]*mode(guardminutes[np.argmax(guardmodes)]))
        

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
