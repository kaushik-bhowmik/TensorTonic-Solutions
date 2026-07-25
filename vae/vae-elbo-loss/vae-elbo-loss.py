import numpy as np

def vae_loss(x: np.ndarray, x_recon: np.ndarray, mu: np.ndarray, log_var: np.ndarray) -> dict:
    """
    Returns: dict with "total", "recon", and "kl" loss values as floats
    """
    # Your implementation here
    ### Reconstruction 
    recons = np.mean(np.sum((x - x_recon) ** 2, axis=1), axis=0)
    ## KL Divergence
    t1 = 1+log_var - mu*mu -np.exp(log_var)
    kl_r = -0.5 * np.mean(np.sum(t1, axis=1), axis=0)
    vae_loss = recons + kl_r  
    return {"total":vae_loss, "recon":recons, "kl":kl_r}
    ###
