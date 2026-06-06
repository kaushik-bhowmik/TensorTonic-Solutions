import numpy as np 
def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    predictions = np.array(predictions,dtype=float)
    #print(predictions.shape[0])
    K= predictions.shape[0]
    tsoft = (1-epsilon) + epsilon/K
    qi = np.full((K,),epsilon/K)
    qi[target] = tsoft
    #arr = np.full((3, 4), 7)
    loss = -np.sum(qi*np.log(predictions))
    return loss
    