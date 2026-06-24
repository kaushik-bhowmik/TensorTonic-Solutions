import numpy as np

def dropout(x: np.ndarray, p: float = 0.5, training: bool = True, mask: np.ndarray = None) -> np.ndarray:
    """
    Apply inverted dropout. If mask is provided, use it; otherwise generate one.
    """
    # YOUR CODE HERE
    if mask is None:
        mask = np.ones_like(x)
    if training==True:
        out = x* mask* (1-p)**-1
    else:
        out = x 
    return out 
        