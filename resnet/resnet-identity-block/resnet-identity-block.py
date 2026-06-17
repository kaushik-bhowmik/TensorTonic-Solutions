import numpy as np

def identity_block(x, W1, W2):
    """
    Returns: np.ndarray of shape (batch, channels) with identity residual block output
    """
    # YOUR CODE HERE
    x = np.array(x,dtype = float); W1 = np.array(W1,dtype = float); W2 = np.array(W2,dtype = float)
    h = np.maximum(0, x@W1.T)
    y = relu = np.maximum(0, h@W2.T +x)
    return y 
    ## np.maximum(0, x)
