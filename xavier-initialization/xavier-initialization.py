import numpy as np 
def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    W = np.array(W)
    L = np.sqrt(6/(fan_in + fan_out))
    Wout = W *2*L - L 
    return Wout 