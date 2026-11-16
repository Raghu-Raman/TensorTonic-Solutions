import numpy as np

def filter_and_extract(data: list, row_start: int, row_stop: int, threshold: float) -> np.ndarray:
    """
    Returns matching values in row-major order as a 1D float64 array.
    """
    data = np.array(data, dtype=np.float64)
    data = data[row_start:row_stop]
    mask = data > threshold
    data = mask * data
    data = data[data!=0]
    return data
    
