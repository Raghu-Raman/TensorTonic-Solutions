import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    data=np.array(data,dtype=np.float64)
    if operation =="flatten":
        data = data.reshape(-1)
    elif operation =="transpose":
        data = data.T
    else:
        data =  np.expand_dims(data, axis=0)
    return data