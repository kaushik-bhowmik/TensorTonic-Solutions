import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x= np.asarray(x,dtype="float")
    gamma = np.asarray(gamma,dtype="float")
    beta = np.asarray(beta,dtype="float")
    if len(x.shape)==2:
        axis=0
    else:
        axis = (0,2,3)
        gamma = gamma.reshape(1, -1, 1, 1)
        beta  = beta.reshape(1, -1, 1, 1)
    #print(x.shape, axis)
    mean = np.mean(x,axis,keepdims=True)
    var = np.var(x,axis,keepdims=True)
    den = np.sqrt(var+eps)
    xhat = (x-mean)/den 
    yi = gamma*xhat +beta 
    return yi 