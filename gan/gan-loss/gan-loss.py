import numpy as np

def discriminator_loss(real_probs, fake_probs):
    """Compute discriminator loss using binary cross-entropy.
    Returns: Loss value rounded to 4 decimals."""
    #pass
    real_probs = np.asarray(real_probs,dtype=float)
    fake_probs = np.asarray(fake_probs,dtype=float)
    eps = 1e-8
    rp = np.clip(real_probs, eps, 1-eps) ; fp = np.clip(fake_probs,eps,1-eps)
    term = np.log(rp) + np.log(1-fp)
    loss = -np.mean(term)
    return loss 
    

def generator_loss(fake_probs):
    """Compute non-saturating generator loss.
    Returns: Loss value rounded to 4 decimals."""
    eps = 1e-8
    fp = np.clip(fake_probs,eps,1-eps)
    term = np.log(fp)
    loss = -np.mean(term)
    return loss 