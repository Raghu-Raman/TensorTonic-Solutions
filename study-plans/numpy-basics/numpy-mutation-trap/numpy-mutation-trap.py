import numpy as np

def original_and_clipped(data: list, row_idx: int, lo: float, hi: float) -> np.ndarray:
    """
    Returns a (2, n) float64 array: original row, then clipped row.
    """
    data = np.array(data,dtype=np.float64)
    return np.stack([data[row_idx],np.clip(data[row_idx],lo,hi)])
