def basic_probability(p_a: float, p_b: float, p_a_and_b: float) -> list:
    """
    Returns four rounded probability values in the required order.
    """
    return[round(float(p_a+p_b-p_a_and_b),4),round(float(1-p_a),4),round(float(1-p_b),4),round(float(p_a-p_a_and_b) ,4)]