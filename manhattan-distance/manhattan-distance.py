import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x=np.array(x,dtype=np.float64)
    y=np.array(y,dtype=np.float64)
    return abs(np.sum(abs(x-y)))