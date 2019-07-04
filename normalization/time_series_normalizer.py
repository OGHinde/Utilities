"""
    Author: Óscar García Hinde <oghinde@tsc.uc3m.es>
    Python Version: 3.6
"""

import numpy as np

def check_shapes(X, y):
    """Check correct data formating.

    Specifically, check that X and y have the same number of samples.
    """
    n_X, d = X.shape
    n_y, _ = y.shape
    
    if n_X != n_y:
        raise ValueError('Number of samples in X and y do not match.')
    n = n_X

    return n, d

class TimeSeriesNormalizer():
    """Time series specific normalization.

    A class containing a bunch of different time series specific 
    normalization strategies.
    """
    def __init__(self, mode='min_max', new_min=0, new_max=1, 
                 perc_low=0, perc_high=100):
        if mode == 'min_max':
            self.mode = mode
            self.new_min = new_min
            self.new_max = new_max
            self.perc_low = perc_low
            self.perc_high = perc_high
        elif mode == 'mean_var':
            self.mode = mode
        else:
            raise ValueError('{} is not a valid normalization mode.'.format(mode))

    def normalize(self, X, y):
        """Normalize a set of input samples and their corresponding 
        targets according to the specified normalization mode.
        """
        if self.mode == 'min_max':
            X_norm, y_norm = self._min_max_norm(X, y)
        else:
            X_norm, y_norm = self._mean_var_norm(X, y)

        return X_norm, y_norm

    def denormalize(self, X):
        """Denormalize a set of predicted targets according to the mode 
        that was used in the normalization stage.
        """
        if self.mode == 'min_max':
            return self._min_max_denorm(X)
        else:
            return self._mean_var_denorm(X)

    def _min_max_norm(self, X, y):
        """Min-max normalization.

        Transform values so that they lie between new_min and new_max.
        """
        n, d = check_shapes(X, y)
        
        old_max = np.percentile(X, axis=1, q=self.perc_high)[:, np.newaxis]
        old_min = np.percentile(X, axis=1, q=self.perc_low)[:, np.newaxis]
        new_max = self.new_max
        new_min = self.new_min

        X_norm = (X - old_min) * (new_max - new_min) / (old_max - old_min) + new_min
        y_norm = (y - old_min) * (new_max - new_min) / (old_max - old_min) + new_min

        self.old_max_ = old_max
        self.old_min_ = old_min

        return X_norm, y_norm

    def _min_max_denorm(self, X):
        """Undo min-max normalization on a vector or matrix.
        """
        numerator = (X - self.new_min)*(self.old_max_ - self.old_min_)
        return self.old_min_ + numerator/(self.new_max - self.new_min)
    
    def _mean_var_norm(self, X, y):
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

    def _mean_var_denorm(self, X):
        """Undo mean-variance normalization on a vector or matrix.
        """
        return X*self.std_ + self.mean_