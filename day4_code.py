# day 3 problem

import numpy as np

filename = 'day3_input.txt'
datas = open(filename)
data = datas.readlines()
datas.close()


def mdorder(datin,ins,ends):
    ordlist = []
    for ent in datin:
        dm = int(ent[6:8])
        if len(ordlist) == 0:
            ordlist.append(ent)
        else:
            n = len(ordlist)
            
