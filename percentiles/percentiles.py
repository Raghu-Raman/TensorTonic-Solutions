import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    x = np.array(x,dtype=np.float64)
    return_array=np.zeros(len(q))
    x=np.sort(x)
    for i in range(len(q)):
        temp= (q[i]/100) * (x.shape[0]-1)
        if temp.is_integer():
            return_array[i] = x[int(temp)]
        else:
            fraction = temp- np.floor(temp)
            return_array[i] =x[int(np.floor(temp))] + fraction * (x[int(np.floor(temp))+1]-x[int(np.floor(temp))])
    return return_array