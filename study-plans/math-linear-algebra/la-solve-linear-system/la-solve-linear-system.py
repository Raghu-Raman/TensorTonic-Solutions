import numpy as np

def solve_linear_system(A, b):
    """
    Returns: float64 array, the solution x to A @ x = b.
    """
    return np.linalg.solve(np.array(A, dtype=float), np.array(b, dtype=float))

