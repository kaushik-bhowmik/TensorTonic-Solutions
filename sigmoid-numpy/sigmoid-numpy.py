import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    pass
    #print(type(x))
    x = np.array(x)
    val = 1/(1+np.e**-x)
    return val