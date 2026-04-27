import numpy as np

def hadamard_product(A, B):
    """
    Returns: ndarray, the element-wise product A * B.
    """
    A = np.array(A,dtype=float)
    B = np.array(B,dtype=float)
    return A * B
    