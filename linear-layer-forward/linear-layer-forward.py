import numpy as np 
def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code her
    X = np.array(X)
    W = np.array(W)
    b = np.array(b)
    y =X@W+b
    print(y)
    return y.tolist()