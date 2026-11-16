import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    data = np.array(data, dtype=np.float64)
    mask_data = data > threshold
    any_data = np.any(data>threshold,axis=1,keepdims=True)
    all_data = np.all(data>threshold,axis=1,keepdims=True)
    any_data = np.repeat(any_data, data.shape[1], axis=1) 
    all_data = np.repeat(all_data, data.shape[1], axis=1) 
    mask_data= np.where(mask_data, 1, 0)
    any_data= np.where(any_data, 1, 0) * data
    all_data= np.where(all_data, 1, 0)  * data
    stacked_array =np.stack([mask_data,any_data,all_data])
    return stacked_array
