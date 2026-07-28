import numpy as np

def qr_decompose(A):
    """
    Returns: tuple (Q, R) where A = Q @ R.
    """
    A =  np.array(A, dtype=float)
    At = A.T
    return_array = []
    temp = None
    for i in range(len(At)):
        temp = At[i].copy()
        for j in return_array:
           proj = np.dot(At[i], j) / np.dot(j, j) * j
           temp = temp - proj
        temp = temp/np.linalg.norm(temp)
        return_array.append(temp)
    Q = np.array(return_array).T
    Qt = Q.T
    R = np.matmul(Qt,A)
    return (Q,R)
                      