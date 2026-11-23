import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x = np.array(x, dtype=np.float64)
    x_cent = x-np.mean(x)
    sample_std = np.sqrt((x_cent.T@x_cent)/(x.shape[0]-1))
    t = (np.mean(x)-mu0)/(sample_std/np.sqrt(x.shape[0]))
    return float(t)