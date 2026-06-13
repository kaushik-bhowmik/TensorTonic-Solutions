import numpy as np
##Gradient Clipping (Global Norm)
def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    #pass
    g = np.array(g, dtype=float)
    norm = np.linalg.norm(g)
    print(norm)
    print(max_norm)
    if max_norm<=0:
        return g 
    if norm<=max_norm:
        return g #np.array([norm])
    return g *max_norm /norm
    
    """
    if max_norm == 0 or max_norm<0 or gmag==0:
        return np.zeros_like(g)
    if gmag <max_norm:
        return g
    else:
        return g* max_norm/ gmag """