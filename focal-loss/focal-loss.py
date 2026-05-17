import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    p = np.array(p) ; y = np.array(y)
    f = np.log(p)*y*(1-p)**gamma
    s = np.log(1-p)*(1-y)*p**gamma
    fl  = -f  -s 
    return np.mean(fl)