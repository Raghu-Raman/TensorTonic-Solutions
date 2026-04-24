import numpy as np

def projection_matrix(A):
    """
    Returns: ndarray, the projection matrix onto the column space of A.
    """
    A = np.array(A, dtype=float)
    return A @ np.linalg.pinv(A.T @ A) @ A.T