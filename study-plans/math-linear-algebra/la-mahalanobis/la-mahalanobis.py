import numpy as np

def mahalanobis_distance(x, mean, cov):
    """
    Returns: float, the Mahalanobis distance from x to the distribution.
    """
    x = np.array(x,dtype=float)
    mean = np.array(mean,dtype=float)
    cov = np.array(cov,dtype=float)
    change = x -  mean
    cov_inv = np.linalg.pinv(cov)
    dist = change.T @ cov_inv @ change
    dist = np.sqrt(dist)
    return dist