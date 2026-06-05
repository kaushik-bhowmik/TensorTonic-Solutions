import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    #pass
    v = np.array(v,dtype=float) ; w = np.array(w,dtype=float)
    dot = np.dot(v, w)
    mv = np.linalg.norm(v) ; mw = np.linalg.norm(w)
    if mv==0 or mw ==0:
        return np.nan 
    x = dot/(mv * mw)
    x = np.clip(x, -1, 1)
    theta=np.arccos(x)
    return theta