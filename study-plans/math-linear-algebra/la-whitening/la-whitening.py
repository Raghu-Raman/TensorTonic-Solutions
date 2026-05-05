import numpy as np

def whiten(X):
    """
    Returns: ndarray, the whitened data with identity covariance.
    """
    X = np.array(X, dtype=float)
    mean = X.mean(axis=0)
    X_centered = X - mean
    n = X.shape[0]
    cov = (X_centered.T @ X_centered) / (n - 1)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    # Handle near-zero eigenvalues
    tol = 1e-10
    d_inv_sqrt = np.array([1.0 / np.sqrt(lam) if lam > tol else 0.0 for lam in eigenvalues])
    return X_centered @ eigenvectors @ np.diag(d_inv_sqrt)