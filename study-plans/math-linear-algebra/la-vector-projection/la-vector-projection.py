import numpy as np

def vector_projection(u, v):
    """
    Returns: float64 array, the projection of u onto v.
    """
    u = np.asarray(u)
    v = np.asarray(v)
    num = np.dot(v,u)
    den = np.dot(v,v)
    res = num/den * v
    return res