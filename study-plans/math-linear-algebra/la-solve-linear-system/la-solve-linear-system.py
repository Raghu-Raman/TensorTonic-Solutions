import numpy as np

def solve_linear_system(A, b):
    """
    Returns: float64 array, the solution x to A @ x = b.
    """
    A = np.array(A,dtype = float)
    b = np.array(b,dtype = float)
    
    if A.shape[0] == A.shape[1]:
        x = np.linalg.solve(A,b)
    else:
        x, residual, rank, sv = np.linalg.lstsq(A,b, rcond=None)
    return x
