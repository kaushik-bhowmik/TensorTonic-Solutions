import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    if len(x.shape)==1:
        maxi = np.max(x, axis=0,keepdims=True) 
    else:
        maxi = np.max(x, axis=1,keepdims=True) 
    x_max  = x-maxi
    ex_max = np.exp(x_max)
    if len(x.shape)==1:
        tot = np.sum(ex_max , axis = 0)
    else:
        tot = np.sum(ex_max , axis = 1,keepdims=True)
    ans = ex_max / tot 
    return ans 