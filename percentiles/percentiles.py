import numpy as np
from math import floor, ceil 
def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    q= np.asarray(q)
    r = q*(len(x)-1)/100
    l = np.floor(r).astype(int)
    u = np.ceil(r).astype(int); w = r-l 
    x.sort()
    p = (1 - w) * np.asarray(x)[l] + w * np.asarray(x)[u]
    #p = np.asarray(p)
    return p 
