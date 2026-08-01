import numpy as np
import math

def rbf_kernel_matrix(X, gamma):
    """
    Returns: ndarray of shape (n, n), the RBF kernel matrix.
    """
    X = np.array(X,dtype=float)
    result = np.ndarray((X.shape[0],X.shape[0]),dtype=float )
    for i in range(len(result)):
        for j in range(len(result)):
            result[i][j] = math.exp(-gamma * (np.linalg.norm(X[i]-X[j])**2))
    return result