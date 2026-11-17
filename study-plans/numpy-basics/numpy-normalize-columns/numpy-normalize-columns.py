import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    data = np.array(data, dtype=np.float64)
    mean_data = data.mean(axis=0,keepdims=True)
    col_std = data.std(axis=0)
    col_std[col_std == 0] = 1.0
    return (data-mean_data)/col_std