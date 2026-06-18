import numpy as np

def conv_block(x, W1, W2, Ws):
    """
    Returns: np.ndarray with sum of main path output and projected shortcut
    """
    # YOUR CODE HERE
    x= np.array(x, dtype=float); W1= np.array(W1, dtype=float); W2= np.array(W2, dtype=float); Ws= np.array(Ws, dtype=float)
    h = np.maximum(0, x @ W1)
    #z = np.maximum(0, h @ W2)
    z= h @ W2
    # shortcut path (projection)
    s = x@Ws 

    # residual addition
    y = z + s
    return np.maximum(0, y) 