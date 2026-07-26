import numpy as np

def generator(z, W, b):
    """
    Returns: np.ndarray of shape (batch, output_dim) with tanh-activated values rounded to 4 decimals
    """
    z= np.asarray(z, dtype=float) ; W= np.asarray(W, dtype=float) ; b= np.asarray(b, dtype=float)
    return np.tanh(z@W+b)