# -*- coding: utf-8 -*-
"""
Created on Tue May 28 00:12:13 2019

@author: Andrew
"""

######################
## import libraries ##
######################
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt 

plt.plot([1,2], [1,1], color='blue'), 
plt.plot([1,2], [1.1,1.1], color='blue')
plt.plot([1,1], [1,1.1], color='blue')
plt.plot([2,2], [1,1.1], color='blue')
plt.plot([1.2,1.2], [1,1.1], color='blue')
plt.plot([1.6,1.6], [1,1.1], color='blue')
plt.ylim([0,2])
plt.plot([1.01,1.01], [1.15,1.2], color='black')
plt.plot([1.99,1.99], [1.15,1.2], color='black')
plt.plot([1.01,1.99], [1.2,1.2], color='black')
plt.plot([1.5,1.5], [1.2,1.25], color='black')
plt.text(1.5, 1.3, 'unit length 1', fontsize=10, horizontalalignment='center')
plt.plot([1.01,1.01], [0.95,0.9], color='black')
plt.plot([1.19,1.19], [0.95,0.9], color='black')
plt.plot([1.01,1.19], [0.9,0.9], color='black')
plt.plot([1.1,1.1], [0.9,0.85], color='black')
plt.text(1.1, 0.75, 'a', fontsize=10, horizontalalignment='center')
plt.plot([1.21,1.21], [0.95,0.9], color='black')
plt.plot([1.59,1.59], [0.95,0.9], color='black')
plt.plot([1.21,1.59], [0.9,0.9], color='black')
plt.plot([1.4,1.4], [0.9,0.85], color='black')
plt.text(1.4, 0.75, 'b', fontsize=10, horizontalalignment='center')
plt.plot([1.61,1.61], [0.95,0.9], color='black')
plt.plot([1.99,1.99], [0.95,0.9], color='black')
plt.plot([1.61,1.99], [0.9,0.9], color='black')
plt.plot([1.8,1.8], [0.9,0.85], color='black')
plt.text(1.8, 0.75, '1-a-b', fontsize=10, horizontalalignment='center')
plt.axis('off')


plt.plot([0,1], [1,0], color='blue', label = "total probability space")
plt.plot([0,0], [1,0], color='blue')
plt.plot([0,1], [0,0], color='blue')
plt.plot([0.5,0.5], [0.5,0], color='red', linestyle='dashed', label = "probability space that can form triangle")
plt.plot([0,0.5], [0.5,0.5], color='red', linestyle='dashed')
plt.plot([0,0.5], [0.5,0], color='red', linestyle='dashed')
plt.xlabel('a') 
plt.ylabel('b') 
plt.legend() 

## number of iterations 
iterations = 1000000
results = pd.DataFrame()
results['iteration'] = list(range(1,iterations+1))
percentage = iterations*[None]

np.random.seed(10815657)
count = 0
for i in range(0, iterations):
    print(i)
    random_draws = np.random.uniform(low=0, high=1, size=2)
    a = min(random_draws)
    b = abs(random_draws[0] - random_draws[1])

    if((a<0.5) and (b<0.5) and (0.5 < a+b)):
        count=count+1
        
    percentage[i] = count / (i+1)

results['percentage'] = percentage

######################
## Plot the results ##
######################
from ggplot import *
del chopsticks, diamonds, meat, movies, mpg, mtcars, pageviews, pigeons, salmon
print(ggplot(results, aes(x='iteration', y='percentage', group='1')) + geom_point() + geom_line(color="red"))








