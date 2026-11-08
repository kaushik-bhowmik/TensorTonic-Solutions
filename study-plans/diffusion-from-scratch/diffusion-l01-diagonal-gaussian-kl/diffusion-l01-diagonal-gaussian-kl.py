import numpy as np

def diagonal_gaussian_kl(mean_p: np.ndarray, log_var_p: np.ndarray, mean_q: np.ndarray, log_var_q: np.ndarray) -> np.ndarray:
    """
    Returns KL(p || q) summed over the last axis, as a float64 array with the leading shape of the inputs.
    """
    var_p = np.exp(log_var_p)
    var_q = np.exp(log_var_q)
    f = np.log(var_q/var_p) 
    s = (var_p + (mean_p-mean_q)**2)/(var_q)
    term = f +s -1 
    kl = 0.5 * np.sum(term, axis=-1)
    return kl 
    
    
