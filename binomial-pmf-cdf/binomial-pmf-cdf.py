import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    first_term = math.comb(n,k)
    second_term = p**k
    third_term = (1-p)**(n-k)
    cdf = 0
    for i in range(k+1):
        first_term_c = math.comb(n,i)
        second_term_c = p**i
        thrid_term_c = (1-p)**(n-i)
        cdf += first_term_c*second_term_c*thrid_term_c
    return {"pmf":float(first_term*second_term*third_term), "cdf":float(cdf)}
        