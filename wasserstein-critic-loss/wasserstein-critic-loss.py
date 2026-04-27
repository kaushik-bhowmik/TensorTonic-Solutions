import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    rm = np.mean(real_scores)
    fm = np.mean(fake_scores)
    return fm - rm 