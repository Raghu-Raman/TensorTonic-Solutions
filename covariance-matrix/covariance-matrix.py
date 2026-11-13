import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X,dtype = float)
    X_m = X.mean(axis=0)
    X_c = X-X_m
    sigma = np.matmul(X_c.T,X_c)/(X.shape[0]-1)
    return sigma
    