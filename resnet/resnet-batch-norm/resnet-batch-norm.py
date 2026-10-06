import numpy as np

def batch_norm_block(x, W1, W2, gamma1, beta1, gamma2, beta2, mode):
    """
    Returns the normalized residual-block result and selected mode in a dictionary.
    """
    x = np.asarray(x) ; W1 = np.asarray(W1) ; W2 = np.asarray(W2) ; gamma1 = np.asarray(gamma1)
    gamma2 = np.asarray(gamma2) ; beta1 = np.asarray(beta1) ; beta2 = np.asarray(beta2)
    def batchnorm(inp, g,b):
        mean = np.mean(inp,axis=0,keepdims=True)
        var = np.var(inp,axis=0, keepdims=True)
        xhat = (inp-mean)/ (np.sqrt(var+0.00001))
        return g * xhat + b 
    if mode=="post":
        p1 = x@W1 ; p2 = batchnorm(p1,gamma1,beta1) ; p3 = np.maximum(0,p2)
        p4 = p3@W2 ; path = batchnorm(p4,gamma2,beta2) 
        out = np.maximum(0,path +x) # np.maximum(0, x)
    else:
        p1 = batchnorm(x,gamma1,beta1) ; p2 = np.maximum(0,p1) ; p3 = p2@W1 
        p4 = batchnorm(p3,gamma2,beta2) ; p5 = np.maximum(0,p4) ; path = p5@W2  
        out = path+ x
    return {"output":out, "mode":mode} 