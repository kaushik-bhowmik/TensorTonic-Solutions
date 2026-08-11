import numpy as np

def candidate_hidden(h_prev: np.ndarray, x_t: np.ndarray, r_t: np.ndarray,
                     W_h: np.ndarray, b_h: np.ndarray) -> np.ndarray:
    """
    Compute candidate: h_tilde = tanh(W_h @ [r*h, x] + b_h)
    """
    # YOUR CODE HERE
    temp = r_t * h_prev 
    concat = np.concatenate([temp, x_t],axis=-1)
    this = concat @W_h.T +b_h 
    htilde = np.tanh(this)
    return htilde 