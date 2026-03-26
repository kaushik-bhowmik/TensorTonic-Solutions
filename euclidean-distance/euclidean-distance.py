import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    pass
    print(type(x), type(y))
    x= np.array(x)
    y = np.array(y)
    res = x-y
    res = res *res
    print(res)
    return np.sqrt(np.sum(res))