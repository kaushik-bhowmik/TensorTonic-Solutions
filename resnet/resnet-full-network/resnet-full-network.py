import numpy as np

def resnet_forward(x, conv1, W1_b1, W2_b1, W1_b2, W2_b2, Ws_b2, fc):
    """
    Returns the network logits as a nested list.
    """
    x = np.asarray(x)
    conv1= np.asarray(conv1)
    W1_b1= np.asarray(W1_b1)
    W2_b1= np.asarray(W2_b1)
    W2_b2 = np.asarray(W2_b2)
    Ws_b2= np.asarray(Ws_b2)
    fc = np.asarray(fc)
    ini = np.maximum(0,x@conv1)
    b1 = np.maximum(0,ini@W1_b1)@W2_b1 
    this = ini +b1 
    this = np.maximum(0, ini + b1)
    ini2 = np.maximum(0,this@W1_b2)
    b2 = ini2@W2_b2 + this @Ws_b2 
    #o1 = np.maximum(0,b2)
    out = np.maximum(0, b2)
    logits = out @fc 
    ll = logits.tolist()
    return ll 
    