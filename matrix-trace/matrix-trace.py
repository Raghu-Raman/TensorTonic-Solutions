import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    A = np.array(A, dtype=np.float64)
    trace=0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if i == j:
                trace +=A[i][j]
    return trace