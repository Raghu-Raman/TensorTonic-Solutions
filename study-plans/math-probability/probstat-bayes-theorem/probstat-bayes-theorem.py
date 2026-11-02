def bayes_theorem(p_a: float, p_b_given_a: float, p_b_given_not_a: float) -> float:
    """
    Returns the posterior probability rounded to four decimals.
    """
    p_not_a = 1-p_a
    p_b = p_b_given_a*p_a + p_b_given_not_a * p_not_a
    p_a_given_b = (p_b_given_a*p_a)/p_b
    p_a_given_b = round(p_a_given_b, 4)
    return p_a_given_b