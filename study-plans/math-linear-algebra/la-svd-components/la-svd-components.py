import numpy as np

def svd(A):
    """
    Returns: tuple (U, s, Vt) where A = U @ diag(s) @ Vt.
    """
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    return (U,s,Vt)