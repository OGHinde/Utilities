"""
    Author: Óscar García Hinde <oghinde@tsc.uc3m.es>
    Python Version: 3.6
"""

import sys
import numpy as np

def check_shapes(X, y):
    """Check correct data formating.

    Specifically, check that X and y have the same number of samples.
    """
    n_X, d = X.shape
    x_y, _ = y.shape
    
    if n_X != n_y:
        raise ValueError('Number of samples in X and y do not match.')
    n = n_X

    return n, d

class TimeSeriesNormalizer():
    """Time series specific normalization.

    A class containing a bunch of different time series specific 
    normalization strategies.
    """

    def __init__(self, mode='min_max', new_min=0, new_max=1, perc_low=0, perc_high=100):
        if mode == 'min_max':
            self.mode = mode
            self.new_min = new_min
            self.new_max = new_max
            self.perc_low = perc_low
            self.perc_high = perc_high
        elif mode == 'mean_var':
            self.mode = mode
        else    
            raise ValueError(mode, 'is not a valid normalization mode.')

    def normalize(self, X, y):
        if self.mode == 'min_max'
            X_norm, y_norm = self._min_max_norm(X, y)
        else:
            X_norm, y_norm = self._mean_var_norm(X, y)

        return X_norm, y_norm

    def denormalize(self, X_norm, y_norm):
        if self.mode == 'min_max'
            X, y = self._min_max_denorm(X_norm, y_norm)
        else:
            X, y = self._mean_var_denorm(X_norm, y_norm)

        return X, y

    def _min_max_norm(self, X, y):
        """Min-max normalization.

        Transform values so that they lie between new_min and new_max.
        """
        n, d = check_shapes(X, y)

        ref_min = np.percentile(X.min(axis=1), q=perc_low)
        ref_max = np.percentile(X.max(axis=1), q=perc_high)
        
        X_norm = self.new_min + (X - ref_min)*(self.new_max - self.new_min)/(ref_max - ref_min)
        y_norm = self.new_min + (y - ref_min)*(self.new_max - self.new_min)/(ref_max - ref_min)
        
        self.ref_min_ = ref_min
        self.ref_max_ = ref_max

        return X_norm, y_norm

    def _min_max_denorm(self, X_norm, y_norm):
        """Undo min-max normalization.
        """
        X = self.ref_min_ + (X_norm - self.new_min)*(self.ref_max_ - self.ref_min_)/(self.new_max - self.new_min)
        y = self.ref_min_ + (y_norm - self.new_min)*(self.ref_max_ - self.ref_min_)/(self.new_max - self.new_min)

        return X, y
    
    def _mean_var(self, X, y):
        """Mean-variance normalization.

        Transform values so that they have zero mean and unit variance 
        in the temporal axis.
        """
        n, d = check_shapes(X, y)

        m = X.mean(axis=1)[:, np.newaxis]
        std = X.std(axis=1)[:, np.newaxis]
        X_norm = (X - m)/std
        y_norm = (y - m)/std
        
        self.mean_ = m
        self.std_ = std
        
        return X_norm, y_norm, 

    def _mean_var_denorm(self, X_norm, y_norm):
        """Undo mean-variance normalization.
        """
        X = X_norm*self.std_ + self.mean_
        y = y_norm*self.std_ + self.mean_

        return X, y