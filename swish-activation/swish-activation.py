import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    pass
    x = np.array(x)
    ans = x/(1+np.exp(-x))
    return ans 