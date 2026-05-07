import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    mean = np.mean(x)
    median = np.median(x)
    mode = Counter(x)
    mode_final = 0
    max_mode = 0
    for i in mode:
        if mode[i] > max_mode:
            max_mode = mode[i]
            mode_final = i
    return {'mean':mean,'median':median,'mode':mode_final}