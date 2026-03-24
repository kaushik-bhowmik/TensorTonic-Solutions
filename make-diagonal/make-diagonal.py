import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    pass
    size = len(v)
    arr1 = np.zeros((size,size))
    for i in range(size):
        arr1[i][i]=v[i]
    return arr1
    
