import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k = np.array(k)
    ans = np.empty_like(k)
    ans = p * (1 - p) ** (k - 1)
    mean = 1/p 
    return (ans, mean)
