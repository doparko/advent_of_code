# animation attempt 
# Chris Oparko

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

filename = '2020_d8.txt'
datin = open(filename)
datinss = datin.read()
datas = datinss[:-1].split('\n')

# Code functions for running through the given data
def gamecode(clist,pos):
    code = clist[pos][:3]
    numb = int(clist[pos][4:])
    if code == 'acc':
        return numb, pos + 1
    elif code == 'jmp':
        return 0, pos + numb
    else:
        return 0, pos + 1
    
def rungame(dataloop):
    point = 0
    accumulator = 0
    dupcheck = []
    fstore = np.zeros((0,2))
    while point not in dupcheck:
        # ploting business here
        tempstart= point
        dupcheck.append(point)
        temp, point =  gamecode(dataloop,point)
        accumulator += temp
        fstore = np.append(fstore,jumpmoveland(tempstart,point),axis=0)
        #print('fstore length: ',jumpmoveland(tempstart,point))
        # This is where you copy in the graphing pieces
        # Right here
        # Do it
        if point == len(dataloop):
            # Now have person run off screen to darkness
            break
    return fstore #fstore


# Want to create an animation that causes the person to duck down 2 frames
# then up 3 frames
# Then 1 frame per step
# then 3 frames to land

def jumpmoveland(start,end):
    num = int(abs(end-start)/10)
    am = np.zeros((7+num,2))
    am[:5,0]= start
    am[-2:,0]= end
    am[5:-2,1] = 1.5
    am[5:-2,0] = np.linspace(start,end,num)
    for k in range(1,3):
        am[k-1,1] = k*(-0.25)
        am[1+k,1] = -1 + k*0.5
        am[-3+k,1] = 1.5 - k*0.75
    am[4,1] = 1
    #print('am length: ',)
    return am
    

#animation function
def animation(i):
    #center = aniframes[i,0]
    #plt.xlim(center-2,center+2)
    body = plt.plot(aniframes[i,0],aniframes[i,1]+0.5,"b",marker='$'+markers[1]+'$',markersize=20)
    #head = plt.plot(aniframes[i,0],aniframes[i,1]+1.5,"b",marker='$'+markers[2]+'$',markersize=6)
    return body

def init():
    return []
    
#Here I'm running my start of animation part
aniframes = np.append(np.zeros((3,2)),rungame(datas),axis=0)

testdata = datas

markers=['\\bowtie','\\times','\sigma']
#body = plt.plot(aniframes[0,0],aniframes[0,1]+0.5,"b",marker='$'+markers[1]+'$',markersize=60)
#head = plt.plot(aniframes[0,0],aniframes[0,1]+1.5,"b",marker='$'+markers[2]+'$',markersize=60) 

persontrail = np.array([[0,0],[0,0],[0,0]])

#persontrail[0,0],persontrail[0,1]=
#persontrail[1,0],persontrail[1,1]=
#persontrail[2,0],persontrail[2,1]=

#persontrail[0,0],persontrail[0,1]=xtime,ytime
#persontrail[1,0],persontrail[1,1]=persontrail[0,0],persontrail[0,1]
#persontrail[2,0],persontrail[2,1]=persontrail[1,0],persontrail[1,1]


#plt.plot(xtime,ytime,"b",marker='$'+markers[1]+'$',markersize=60)
#plt.plot(xcirc,ycirc,"b",marker='$'+markers[2]+'$',markersize=60)
#plt.plot(np.linspace(-2,640,2),np.array([0,0]))

fig = plt.figure(figsize=(20,10))
plt.xticks(np.arange(0,len(testdata)-1,step=1),testdata,rotation=-90)
plt.xlim(0,640)
plt.ylim(-0.5,4)

#fig,ax=plt.subplots(figsize=(20,10))
#ax.set_xlim([0,640])
#ax.set_ylim([-0.5,4])
grnd = plt.plot(np.linspace(-2,640,2),np.array([0,0]))
# Animator function
anim= FuncAnimation(fig,animation,frames=2641,interval=10,init_func=init,blit=True,repeat=1)
plt.show()
#anim.save('jump.gif', writer='imagemagick')

