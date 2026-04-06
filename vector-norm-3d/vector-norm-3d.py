import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    pass
    v = np.array(v)
    v= v**2
    tot = v.sum(axis=-1)
    tot = tot**0.5
    return tot 
        