import numpy as np 
def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    X = np.asarray(X,dtype=float)
    hout = X.shape[0]//pool_size
    wout = X.shape[1]//pool_size
    xnew = X.reshape(hout, pool_size,wout,pool_size).max(axis=(1,3))
    lst = xnew.tolist()
    return lst 