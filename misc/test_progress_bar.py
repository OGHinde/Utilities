#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:04:18 2019

@author: oghinde
"""

# Add CWLM and Utilities modules to PATH
from pathlib import Path
import sys
home = str(Path.home())
sys.path.append(home + '/Git/Clusterwise_Linear_Model/')
sys.path.append(home + '/Git/Utilities/')

import time
import numpy as np
import misc.utils as utils

K_range = np.arange(2, 18)
eta_range = np.linspace(0.1, 15, 35)
areas = ['Area 1', 'Area 2']

for area in areas:
    print('\nComputing for ' + area + '.')

    count=0
    for i in K_range:
        for j in eta_range:
            utils.printProgressBar(iteration=count, 
                                   total=len(K_range)*len(eta_range), 
                                   prefix='Progress:', 
                                   suffix='completed.')
            time.sleep(0.05)
            count += 1
    utils.printProgressBar(iteration=count, 
                           total=len(K_range)*len(eta_range), 
                           prefix='Progress:', 
                           suffix='completed.')