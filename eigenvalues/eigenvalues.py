import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    matrix=np.array(matrix,dtype=np.float64)
    eig_v=np.linalg.eigvals(matrix)
    eig_v = np.sort(eig_v)
    eig_v = np.real(eig_v)
    return eig_v