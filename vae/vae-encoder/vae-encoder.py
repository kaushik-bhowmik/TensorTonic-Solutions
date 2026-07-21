import numpy as np

def vae_encoder(x: np.ndarray, W_mu: np.ndarray, b_mu: np.ndarray, W_logvar: np.ndarray, b_logvar: np.ndarray) -> dict:
    """
    Returns: dict with 'mu' and 'log_var' as np.ndarrays of shape (batch, latent_dim)
    """
    # Your implementation here
    #pass
    mu = x@W_mu+b_mu #, axis=0)
    lvar = x@W_logvar+b_logvar #)
    #lvar = np.var(var,axis=0)
    return {"mu":mu, "log_var":lvar}
