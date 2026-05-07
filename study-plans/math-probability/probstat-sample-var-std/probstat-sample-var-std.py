import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    mean = np.mean(x)
    variance = 0
    for i in range(len(x)):
        variance += (x[i]-mean)**2
    variance = (1/(len(x)-1)) * variance
    std = np.sqrt(variance)
    return {"variance":variance, "std_dev":std}