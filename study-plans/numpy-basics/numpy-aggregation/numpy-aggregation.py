import numpy as np

def summarize(data: list, axis: int) -> np.ndarray:
    """
    Returns float64 rows of mean, standard deviation, minimum, and maximum.
    """
    data = np.array(data,dtype=np.float64)
    mean_arr = data.mean(axis=axis)
    col_std = np.std(data,axis=axis)
    min_data = np.min(data,axis=axis)
    max_data = np.max(data,axis=axis)
    return np.stack([mean_arr,col_std,min_data,max_data])
