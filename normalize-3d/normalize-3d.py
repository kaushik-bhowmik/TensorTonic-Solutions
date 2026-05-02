import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v)
    print(len(v.shape))
    if len(v.shape)==1:
        mag = np.sqrt(np.sum(v**2)) 
    else:
        mag =   np.sqrt(np.sum(v**2, axis=1, keepdims=True))
    mag = np.where(mag==0, 1, mag) #np.repeat(x, 2)
    print(v.shape, mag.shape)
    v  = v/mag# np.repeat(mag, v.shape[1]).reshape(v.shape[0],v.shape[1])
    return v 