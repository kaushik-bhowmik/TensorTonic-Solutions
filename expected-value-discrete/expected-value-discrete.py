import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x) ; p = np.array(p)
    if not abs(np.sum(p) - 1) <=1e-5:
        raise ValueError("Probabilities must sum to 1 within tolerance 1e-6")
    this = np.sum(x*p)
    return this 
