import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    pass
    x= np.array(x)
    y = np.array(y)
    res = np.abs(x-y)
    print(type(np.sum(res)))
    return float(np.sum(res))
    