import numpy as np 
def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    predictions= np.array(predictions, dtype=float)
    targets = np.array(targets)
    pt = np.where(targets==0, 1-predictions, predictions )
    #print(pt)
    fl = -alpha *np.log(pt)* (1-pt)**gamma 
    return np.mean(fl)