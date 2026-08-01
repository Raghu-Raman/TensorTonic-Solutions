import numpy as np
def softmax_2d(x, axis=-1):
    # Shift x along the specified axis
    x_max = np.max(x, axis=axis, keepdims=True)
    exp_x = np.exp(x - x_max)
    # Sum along the same axis
    return exp_x / np.sum(exp_x, axis=axis, keepdims=True)

def scaled_dot_product_attention(Q, K, V):
    """
    Returns: ndarray, the attention output softmax(Q @ K.T / sqrt(d_k)) @ V.
    """
    Q = np.array(Q, dtype=float)
    K = np.array(K, dtype=float)
    V = np.array(V, dtype=float)

    attention = softmax_2d( Q @ K.T/np.sqrt(Q.shape[1])) @ V
    return attention
    
    