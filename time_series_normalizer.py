"""
    Author: Óscar García Hinde <oghinde@tsc.uc3m.es>
    Python Version: 3.6
"""

import numpy as np

class TimeSeriesNormalizer():
    """Time series specific normalization.

    A class containing a bunch of different time-series specific 
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
            print("""{} is not a valid mode. Please specify either 
                  'min_max' or 'mean_var'.""")
            return

    def normalize(self, X, y):
        if self.mode == 'min_max'
            X_norm, y_norm = self._min_max(X, y)
        else:
            X_norm, y_norm = self._mean_var(X, y)

        return X_norm, y_norm

    def denormalize(self, X_norm, y_norm):
        if self.mode == 'min_max'
            X, y = self._min_max_denorm(X_norm, y_norm)
        else:
            X, y = self._mean_var_denorm(X_norm, y_norm)

        return X, y

    def _min_max(self, X, y):
        n_X, d = X.shape
        x_y, _ = y.shape
        
        if n_X != n_y:
            print('Data shapes do not match.')
            return
        n = n_X

        ref_min = np.percentile(X.min(axis=1), q=perc_low)
        ref_max = np.percentile(X.max(axis=1), q=perc_high)
        
        X_norm = self.new_min + (X - ref_min)*(self.new_max - self.new_min)/(ref_max - ref_min)
        y_norm = self.new_min + (y - ref_min)*(self.new_max - self.new_min)/(ref_max - ref_min)
        
        return X_norm, y_norm
    
    def _mean_var(self, X, y):
        n, d = X.shape
        m = X.mean(axis=0)
        m_ = np.tile(m, (n, 1))
        std = X.std(axis=0)
        std_ = np.tile(std, (n, 1))
        m_y = y.mean()
        std_y = y.std()
        X_norm = np.divide(X - m_, std_)
        y_norm = np.divide(y - m_y, std_y)
        
        return X_norm, y_norm, m, std, m_y, std_y

    def normalize_transform(self, X, y, m, std, m_y, std_y):
        n, d = X.shape
        m_ = np.tile(m, (n, 1))
        std_ = np.tile(std, (n, 1))
        X_norm = np.divide(X - m_, std_)
        y_norm = np.divide(y - m_y, std_y)
    
        return X_norm, y_norm