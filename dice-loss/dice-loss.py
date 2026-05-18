import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.array(p, dtype=float)
    y = np.array(y,dtype=float)
    t1 = np.sum(p*y)
    n = 2*t1 +eps 
    d = np.sum(p) +np.sum(y) + eps 
    return 1-(n/d) 
    