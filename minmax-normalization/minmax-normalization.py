import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    #pass
    X = np.array(X) #dtype=np.float32)
    mini = np.min(X, axis, keepdims=True)
    #maxi = np.maximum(X , eps) 
    maxi = np.max(X, axis, keepdims=True)
    denom = np.maximum(maxi - mini, eps)
    res = (X-mini)/(denom)
    return res 
    
    
    