# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 12:05:02 2019

@author: Andrew
"""

import numpy as np

################################
## Classic Monty Hall Problem ##
################################
np.random.seed(123456)
iterations = 100000
win = 0

for i in range(0, iterations):
    doors1_list = list(range(0,3))
    car = doors1_list[np.asscalar(np.random.randint(low=0, high=len(doors1_list), size=1))]
    first_choice = doors1_list[np.asscalar(np.random.randint(low=0, high=len(doors1_list), size=1))]
    doors2_list = doors1_list.copy()
    doors2_list.remove(first_choice)
    
    if(first_choice == car):
        reveal = doors2_list[np.asscalar(np.random.randint(low=0, high=len(doors2_list), size=1))]
        doors2_list.remove(reveal)
        final_choice = doors2_list[0]
    else:
        doors2_list.remove(car)
        reveal = doors2_list[0]
        final_choice = car
    
    if(final_choice == car):
        win = win+1
        
    del doors1_list, car, first_choice, doors2_list, reveal, final_choice

print("The percentage of times you will win if you switch is approximately " + str(win/iterations))



###################################################
## If the host is also blind to where the car is ##
###################################################
import numpy as np
np.random.seed(123456)
iterations = 100000
win = 0
denominator = 0

for i in range(0, iterations):
    doors1_list = list(range(0,3))
    car = doors1_list[np.asscalar(np.random.randint(low=0, high=len(doors1_list), size=1))]
    first_choice = doors1_list[np.asscalar(np.random.randint(low=0, high=len(doors1_list), size=1))]
    doors2_list = doors1_list.copy()
    doors2_list.remove(first_choice)
    
    reveal = doors2_list[np.asscalar(np.random.randint(low=0, high=len(doors2_list), size=1))]
    
    if(reveal != car):
        denominator = denominator+1
        doors2_list.remove(reveal)
        final_choice = doors2_list[0]
        if(final_choice == car):
            win = win+1
        del final_choice
    
    del doors1_list, car, first_choice, doors2_list, reveal

print("In the case where the host is also blind to where the car is, but the revealed door is a goat, the percentage of times you will win if you switch is approximately " + str(win/denominator))

            





    
    
    