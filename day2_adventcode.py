# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:48:19 2019

@author: dopar
"""
# Advent of Code
# Day 2

import os
import numpy as np
 
filename = "day2_input.txt"
folder = "C:/Users/dopar/Documents/advent_of_code/"

datain = open(folder + filename,'r')

text = datain.readlines() 
print(text[0])
print(text[1])

datain.close()