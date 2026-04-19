import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    cosx1x2 = np.dot(x1,x2)/(np.linalg.norm(x1)*np.linalg.norm(x2))
    if label==1:
        L = 1- cosx1x2 
    else:
        L = max(0,cosx1x2-margin)
    return L 