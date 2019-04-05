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

import misc.utils as utils
import time
  
A_range = range(10)
B_range = range(5)
count=0
print('\nPROGRESS BAR DEMO\n')
for i in A_range:
    for j in B_range:
        utils.print_progress_bar(iteration=count, 
                                 total=len(A_range)*len(B_range), 
                                 prefix='Progress:', 
                                 suffix='completed.')
        time.sleep(0.05)
        count += 1
  
# Finish the bar
utils.print_progress_bar(iteration=count, 
                         total=len(A_range)*len(B_range), 
                         prefix='Progress:', 
                         suffix='completed.')