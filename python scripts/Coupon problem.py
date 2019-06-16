# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 00:04:33 2019

@author: Andrew
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

## specify number of coupons, and the probability of getting a coupon
num_coupons=5
expected_number_of_trials = 0
for i in range(num_coupons, 0, -1):
    expected_number_of_trials = expected_number_of_trials + (1/(i/num_coupons))

iterations = 1000
df = pd.DataFrame()
df['iteration'] = range(1,iterations+1)
df['average_num_trials_required'] = None

for i in range(0, iterations):
    full_set = set(range(0,num_coupons))
    current_set = set([])
    total_number_of_coupons_collected = 0
    while(current_set != full_set):
        total_number_of_coupons_collected = total_number_of_coupons_collected+1
        random_coupon = np.asscalar(np.random.randint(low=0, high=num_coupons, size=1))
        update_set = list(current_set)
        update_set.append(random_coupon)
        current_set = set(update_set)
        del random_coupon, update_set
    
    if(i+1 == 1):
        df.loc[df['iteration']==i+1, 'average_num_trials_required'] = total_number_of_coupons_collected
    else:
        df.loc[df['iteration']==i+1, 'average_num_trials_required'] = float(((df.loc[df['iteration']==i, 'average_num_trials_required']*i) + total_number_of_coupons_collected)/(i+1))

plt.plot(df['iteration'], df['average_num_trials_required'])
plt.title('Coupon Problem') 
plt.xlabel('Iterative Step') 
plt.ylabel('average_num_trials_required') 