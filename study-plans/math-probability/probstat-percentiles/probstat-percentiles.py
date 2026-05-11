import numpy as np

def percentiles(x, q):
    """
    Returns: numpy array of percentile values.
    """
    x = np.array(x, dtype=float)
    return_array = np.percentile(x,q)
    return return_array
        
        