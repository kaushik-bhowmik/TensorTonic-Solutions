import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X =np.array(X)
    if X.ndim != 2:
        return None
    if X.shape[0] <= 1:
        return None
    mean = np.mean(X, axis=0)
    Xc = X -mean 
    cov = np.transpose(Xc, axes=None) @ Xc 
    return cov / (Xc.shape[0]-1)