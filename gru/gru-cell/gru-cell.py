import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def gru_cell(x_t: np.ndarray, h_prev: np.ndarray,
             W_r: np.ndarray, W_z: np.ndarray, W_h: np.ndarray,
             b_r: np.ndarray, b_z: np.ndarray, b_h: np.ndarray) -> np.ndarray:
    """
    Complete GRU cell forward pass.
    """
    # YOUR CODE HERE
    ###rt
    concat = np.concatenate([h_prev,x_t],axis=-1)
    this = concat @W_r.T + b_r 
    rt =sigmoid(this)
    ##zt
    concat = np.concatenate([h_prev,x_t],axis=-1)
    this = concat @W_z.T + b_z 
    z_t = sigmoid(this)
    ## htilde
    temp = rt * h_prev 
    concat = np.concatenate([temp, x_t],axis=-1)
    this = concat @W_h.T +b_h 
    htilde = np.tanh(this)
    ##
    h_t = z_t * h_prev + (1-z_t)*htilde 
    return h_t 
