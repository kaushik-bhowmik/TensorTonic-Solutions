import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    pass
    size= len(A)
    tot=0
    for i in range(size):
        tot+=A[i][i]
    return tot
