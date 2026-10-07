import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    output_dict ={"pmf":[], "mean": 0, "variance":0}
    for num in x:
        if num:
            output_dict["pmf"].append(p)
        else:
            output_dict["pmf"].append(1-p)
    output_dict['pmf'] =np.array(output_dict['pmf'])
    output_dict['mean']=float(p)
    output_dict['variance']=float(p*(1-p))

    return output_dict
            