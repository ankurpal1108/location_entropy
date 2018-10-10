# Authors: Ankur Paliwal <ankurpal1108@gmail.com>

import pandas as pd
import numpy as np
from math import log

def cal_location_entropy(data_series, remove_missing = True):
    """ Computes entropy of a data series. 
    
    The function takes in a data series in the form of list or pandas series or numpy 1d array and computes the entropy.
    All values are treated as categorical, even if they are continous numericals.
    
    entropy = sum (-p(i)*log2(p(i))) for all i
    where, p(i) is the probability of the value i or count of i / length of data series
    
    Parameters
    ----------
    data_series: list or numpy 1d array or pandas series
        The main data series
        
    remove_missing: bool, optional default=True
        If True, removes all the missing values from data and proceeds to computing entropy
        If False, treats missing values (nan) as a separate class and computes entropy
        If not boolean, defaults to True
        
    Returns
    -------
        Entropy of the data series
    """
    
    if type(remove_missing) != bool:
        remove_missing = True
    
    # If remove_missing is True, update data_series by removing missing values
    # If remove_missing is False, get the length of data series and count missing values and then update the data_series by removing missing values
    if remove_missing:
        data_series = (pd.Series(data_series)).dropna()
        n_data_series = len(data_series)
    else:
        data_series = pd.Series(data_series)
        missing_count = data_series.isna().sum()
        n_data_series = len(data_series)
        data_series = data_series.dropna()

    # if length of data_series is less than or equal to 1 entropy is 0
    if n_data_series <= 1:
        return 0

    value,counts = np.unique(data_series, return_counts=True) # get unique values and their respective counts
    probs = counts / n_data_series # calculate probabilities, divide counts by length of data_series
    if not remove_missing:
        np.append(probs, missing_count / n_data_series) # if remove_missing is False, append the probability of missing value to probs
    
    # n_classes is the total number of classes, if 0 or 1, entropy is 0
    n_classes = np.count_nonzero(probs)
    if n_classes <= 1:
        return 0
    
    # initialize entropy
    entropy = 0.
    
    # calculate entropy
    for i in probs:
        entropy -= i * log(i, 2)

    return entropy
