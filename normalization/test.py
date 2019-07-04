#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:26:57 2019

@author: oghinde
"""

import sys
home = str(Path.home())
sys.path.append(home + '/Git/Clusterwise_Linear_Model/')
sys.path.append(home + '/Git/Utilities/')
import numpy as np
from normalization.time_series_normalizer import TimeSeriesNormalizer
import matplotlib
import matplotlib.pyplot as plt

N = 5
L = 100

new_min = 0
new_max = 1
perc_low = 5
perc_high = 90

amps = 100*np.random.rand(N, 1)
means = 100*np.random.randn(N, 1)
noise = 20*np.random.randn(N, L)

X = np.sin(np.linspace(-10, 10, L))[np.newaxis, :]
X_tr = np.dot(amps, X) + means + noise 
y_tr = np.random.randn(5, 1)

tr_normalizer = TimeSeriesNormalizer(new_min=new_min,
                                     new_max=new_max, 
                                     perc_low=perc_low, 
                                     perc_high=perc_high)

X_norm, y_norm = tr_normalizer.normalize(X_tr, y_tr)
X_denorm = tr_normalizer.denormalize(X_norm)

plt.plot(X_tr.T)
plt.title('Original')
plt.show()

plt.plot(X_norm.T)
plt.title('Normalized')
plt.show()

plt.plot(X_denorm.T)
plt.title('Denormalized')
plt.show()

