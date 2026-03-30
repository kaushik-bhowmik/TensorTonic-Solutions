import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    arr = np.array(x)
    return np.where(arr>=0, arr, alpha*arr) #np.max(x,alpha*x)