import numpy as np

def vae_forward(x: np.ndarray, epsilon: np.ndarray,
                W_mu: np.ndarray, b_mu: np.ndarray,
                W_logvar: np.ndarray, b_logvar: np.ndarray,
                W_dec: np.ndarray, b_dec: np.ndarray) -> dict:
    """
    Returns reconstruction, mu, log_var, and z as float64 arrays.
    """
    mu = x@W_mu + b_mu 
    logv2 = x@W_logvar +b_logvar 
    Z = mu + np.exp(logv2/2) * epsilon 
    this = Z@W_dec + b_dec  
    Xhat = 1 / (1 + np.exp(-this))
    return {"reconstruction": Xhat , "mu":mu , "log_var": logv2, "z":Z }