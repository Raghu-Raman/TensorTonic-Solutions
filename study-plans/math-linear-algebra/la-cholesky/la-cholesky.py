import numpy as np

def cholesky_decompose(A):
    """
    Returns: lower triangular L where A = L @ L.T, or None if not positive definite.
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]
    L = np.zeros((n, n))
    for j in range(n):
        val = A[j, j] - np.sum(L[j, :j] ** 2)
        if val <= 0:
            return None
        L[j, j] = np.sqrt(val)
        for i in range(j + 1, n):
            L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    return L