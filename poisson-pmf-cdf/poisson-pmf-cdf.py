import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmf=0
    cdf_count = 0
    pmf=(np.exp(-lam)*lam**k)/math.factorial(k)
    for i in range(k+1):
        cdf_count+=(np.exp(-lam)*lam**i)/math.factorial(i)
        
    return {"pmf":float(pmf),"cdf":float(cdf_count)}