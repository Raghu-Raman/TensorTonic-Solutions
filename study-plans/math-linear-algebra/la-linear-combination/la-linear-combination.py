import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """
    vectors = np.array(vectors, dtype=float)
    coefficients = np.array(coefficients, dtype=float)
    
    return  coefficients @ vectors