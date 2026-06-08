import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    #pass
    z1 = np.array(Z1,dtype=float)
    z2 = np.array(Z2,dtype=float)
    S = z1 @z2.T /temperature 
    #print(S.shape)
    index = np.arange(z1.shape[0])
    #print(index)
    term = S - np.max(S,axis=-1,keepdims=True)
    #num = np.exp(S[index, index])
    #den = np.sum(np.exp(S[index]), axis=1, keepdims=True)
    num = np.exp(term[index,index])
    den = np.sum(np.exp(term), axis=1, keepdims=True)
    print(num.shape)
    print(den.shape)
    this = np.log(num.reshape(z1.shape[0], -1)/den)
    l = -np.mean(this)
    return l