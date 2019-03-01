"""A BUNCH OF RANDOM FUNCTIONS

    Author: Óscar García Hinde <oghinde@tsc.uc3m.es>
    Python Version: 3.6
"""

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

    return '{:.0f} hours, {:.0f} minutes {:.3f} seconds'.format(h, m, s)



