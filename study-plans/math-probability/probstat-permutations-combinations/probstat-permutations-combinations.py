def perms_and_combs(n: int, r: int) -> list:
    """
    Returns permutations, combinations, and n factorial as integers.
    """
    def factorial( n):
        if n<=1:
            return 1
        return n * factorial(n-1)
    n_ = factorial(n)
    r_ = factorial(r)
    n_r = factorial(n-r)
    perm = n_//n_r
    comb = n_//(r_*n_r)
    return [perm, comb, n_]
    
    