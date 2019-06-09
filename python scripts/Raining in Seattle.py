# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:21:39 2019

@author: Andrew
"""

import numpy as np

np.random.seed(123456)
R_prob = 0.25
iterations = 10000000
it_rained = 0
denominator_count = 0

for i in range(0, iterations):
    R=0
    y1=0
    y2=0
    y3=0
    
    if(np.random.uniform(low=0, high=1, size=1)<=R_prob):
        R = 1
        
    if(R==1):
        y_prob = 2/3
        if(np.random.uniform(low=0, high=1, size=1)<=y_prob):
            y1=1
        if(np.random.uniform(low=0, high=1, size=1)<=y_prob):
            y2=1
        if(np.random.uniform(low=0, high=1, size=1)<=y_prob):
            y3=1
        if(y1==1 and y2==1 and y3==1):
            it_rained = it_rained+1
            denominator_count = denominator_count+1
    else:
        y_prob = 1/3
        if(np.random.uniform(low=0, high=1, size=1)<=y_prob):
            y1=1
        if(np.random.uniform(low=0, high=1, size=1)<=y_prob):
            y2=1
        if(np.random.uniform(low=0, high=1, size=1)<=y_prob):
            y3=1
        if(y1==1 and y2==1 and y3==1):
            denominator_count = denominator_count+1
        


print(it_rained/denominator_count)
print(8/11)



    
