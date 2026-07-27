import numpy as np

def discriminator(x, W):
    """
    Returns: np.ndarray of shape (batch, 1) with probabilities rounded to 4 decimals
    """
    x= np.asarray(x, dtype=float) ; W= np.asarray(W, dtype=float)
    temp = x@W 
    out = 1 / (1 + np.exp(-temp))
    return out 