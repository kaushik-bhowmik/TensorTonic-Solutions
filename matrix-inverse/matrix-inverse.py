import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    pass
    if len(A)!=len(A) or np.linalg.det(A)==0:
        return None 
    res = np.linalg.inv(A)
    return res 
