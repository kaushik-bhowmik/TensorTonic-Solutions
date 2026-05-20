import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    #maxi = max(set(y_true))
    #print(maxi)
    y_true = np.array(y_true) ; y_pred = np.array(y_pred,dtype=float)
    #print(y_pred.shape[0])
    index = np.arange(y_pred.shape[0])
    #print(index)
    if y_true.shape[0] !=y_pred.shape[0]:
        return False 
    loss = -np.mean(np.log(y_pred[index,y_true]))
    return loss 
    
        