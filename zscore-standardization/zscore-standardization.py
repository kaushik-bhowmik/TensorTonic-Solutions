import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X)
    sum = np.sum(X,axis, keepdims=True)
    n = X.shape[0]
    mean = sum/n
    #eps = 1e-8
    var = np.var(X, axis, keepdims=True)
    return (X-mean)/(np.sqrt(var)+eps) 
    
    
    