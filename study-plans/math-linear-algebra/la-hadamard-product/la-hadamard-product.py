import numpy as np

def hadamard_product(A, B):
    """
    Returns: ndarray, the element-wise product A * B.
    """
    
    return_array = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            return_array[i][j] = A[i][j] * B[i][j]
    return_array = np.asarray(return_array,dtype=float)
    return return_array