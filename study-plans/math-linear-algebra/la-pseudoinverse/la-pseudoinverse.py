import numpy as np

def pseudoinverse(A):
    """
    Returns: ndarray, the Moore-Penrose pseudoinverse of A.
    """
    A = np.array(A, dtype=float)
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    tol = 1e-10
    s_inv = np.array([1.0 / si if si > tol else 0.0 for si in s])
    return Vt.T @ np.diag(s_inv) @ U.T