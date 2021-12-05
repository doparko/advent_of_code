# AOC 2021 Day 3
# Chris O
#
# Goal is to determine gamma and episolon rate
# Gamma rate is the most common of each bit in each spot (you will have 5 bits total for example and 12 for our input)
# Eipsilon is the inverse of the gamma bit

# example

# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010

import numpy as np
#filename = 'day3_inputsample.txt'
filename = 'day3_input.txt'
datin = open(filename)
datinss = datin.read()
datin.close()

datas = np.array(datinss.split('\n'))

data = [None]*len(datas)

for i in range(len(datas)):
    data[i] = int(datas[i])

#Part 1

#looping to find the max of the first digit and looping again to find of each digit

gamma= []

for i in range(len(datas[0])):
    bitcount = 0
    for j in range(len(datas)):
        bitcount+= int(datas[j][i])
    vpercent = round(bitcount/len(datas))
    gamma.append(str(vpercent))
        
#Flip the gamma for the epsilon
epsilon = []
for e in gamma:
    epsilon.append(str(int(not(int(e)))))
    
product = int(''.join(gamma),2)*int(''.join(epsilon),2)
    
print('Your prodcut of gamma and epsilon: ', product)

#Part 2

def airsplit(mlist,bitnum):
    onegroup =[]
    zerogroup =[]
    bitct = 0
    for m in range(len(mlist)):
        dig = int(mlist[m][bitnum])
        if dig == 1:
            onegroup.append(mlist[m])
        else:
            zerogroup.append(mlist[m])
        bitct +=dig
    print('length ',len(mlist),' bitct ',bitct)
    takegroup = bitct/len(mlist)
    return onegroup,zerogroup,takegroup
    
bitlen = len(datas[0])

# Looking for Oxygen generator scrubbing
otemp = datas
for k in range(bitlen):
    ones, zeros, ratio = airsplit(otemp,k)
    if ratio < 0.5:
        otemp = zeros
    else:
        otemp = ones
    if len(otemp) == 1:
        break

# Looking for carbon generator scrubbing
ctemp = datas
for k in range(bitlen):
    ones, zeros, ratio = airsplit(ctemp,k)
    if ratio < 0.5:
        ctemp = ones
    else:
        ctemp = zeros
    if len(ctemp) == 1:
        break

product_part2 = int(''.join(otemp),2)*int(''.join(ctemp),2)

print('Part 2 produc of oxy and co2 scrub is: ',product_part2)        
