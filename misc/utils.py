# -*- coding: utf-8 -*-

"""A BUNCH OF RANDOM FUNCTIONS

    Author: Óscar García Hinde <oghinde@tsc.uc3m.es>
    Python Version: 3.6
"""

import sys
import numpy as np

def mean_absolute_percentage_error(y_true, y_pred, multitarget=None):
    """Mean absolute precentage error regression loss.
    TODO: multi target.
    
    Parameters
    ----------
    y_true : array-like, shape = (n_samples) or (n_samples, n_targets)
        Ground truth (correct) target values.
    y_pred : array-like, shape = (n_samples) or (n_samples, n_targets)
        Estimated target values.

    Returns
    -------
    loss : float or ndarray of floats
        A non-negative floating point value (the best value is 0.0), or an
        array of floating point values, one for each individual target.
    """

    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def time_disp(seconds):
    """Display a time given in seconds in a more pleasing manner.
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    return """{:.0f} days, {:.0f} hours, 
              {:.0f} minutes {:.3f} seconds.""".format(d, h, m, s)

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        bar_length  - Optional  : character length of bar (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    
    try:
        bar = u"\u2588" * filled_length + '-' * (bar_length - filled_length)
    except:
        bar = '*' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()