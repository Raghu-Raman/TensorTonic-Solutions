import numpy as np

def pca_project(X, n_components):
    """
    Returns: ndarray of shape (n_samples, n_components), the projected data.
    """
    X = np.array(X,dtype=float)
    mean =X.mean(axis=0)
    centered_X = X - mean
    cov = (centered_X.T @ centered_X)/(X.shape[0]-1)
    eigen_values, eigen_vectors = np.linalg.eigh(cov)
    idx = np.argsort(eigen_values)[::-1]
    eigen_vectors = eigen_vectors[:,idx]
    eigen_vectors =eigen_vectors[:,:n_components]
    return centered_X @ eigen_vectors
    