import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.array(a,dtype = float)
    b = np.array(b,dtype = float)
    if (np.linalg.norm(a,2)==0)or (np.linalg.norm(b,2)==0):
        cosine_sim = 0    
    else:
        cosine_sim = np.dot(a,b)/(np.linalg.norm(a,2) * np.linalg.norm(b,2))
    cosine_sim = float(cosine_sim)
    return cosine_sim