import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.array(X, dtype=np.float64)
    mean_X = X.mean(axis=0)
    X_cent = X-mean_X
    cov = (X_cent.T @ X)/(X.shape[0]-1)
    std_row = np.sqrt(np.diag(cov)) 
    std_Col = np.sqrt(np.diag(cov)) 
    
    return cov/np.outer(std_row,std_Col)
    