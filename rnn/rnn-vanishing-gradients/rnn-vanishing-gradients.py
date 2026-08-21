import numpy as np

def compute_gradient_norm_decay(T: int, W_hh: np.ndarray) -> list:
    """
    Simulate gradient norm decay over T time steps.
    Returns list of gradient norms.
    """
    # YOUR CODE HERE
    res= [1]
    norm_Whh = np.linalg.norm(W_hh, 2)
    for i in range(1,T):
        res.append(norm_Whh**i)
        #gradient_norms = [norm_Whh ** t for t in range(1, T + 1)]
    return res