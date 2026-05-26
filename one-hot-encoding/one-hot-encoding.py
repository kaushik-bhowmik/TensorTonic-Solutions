import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    y= np.array(y)
    res=[]
    if num_classes is not None:
        this =num_classes
    else:
        this = max(y)+1
    print(this)
    for i in range(len(y)):
        res.append([0]*this)
        res[i][y[i]]=1
    return res 
        