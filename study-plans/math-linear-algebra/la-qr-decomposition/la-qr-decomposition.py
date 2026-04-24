import numpy as np

def qr_decompose(A):
    """
    Returns: tuple (Q, R) where A = Q @ R.
    """
    A = np.array(A,dtype=float)
    m,n = A.shape
    Q = np.zeros((m,n))
    R = np.zeros((n,n))
    for k in range(n):
        v = A[:,k].copy()
        for j in range(k):
            R[j,k] = Q[:,j] @ A[:,k]
            v -= R[j,k] * Q[:, j]
        R[k,k] = np.linalg.norm(v)
        Q[:,k] = v/R[k,k]
    for k in range(n):
        if R[k,k] < 0:
            R[k, :] *= -1
            Q[:, k] *= -1
    return Q,R