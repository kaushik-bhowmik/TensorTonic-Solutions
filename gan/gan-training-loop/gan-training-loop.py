import numpy as np

def train_gan_step(real_data, fake_data, D_W):
    """
    Returns: dict with "d_loss" and "g_loss" as float values
    """
    # Your implementation here
    real_data = np.asarray(real_data,dtype="float") ; fake_data = np.asarray(fake_data,dtype="float")
    D_W = np.asarray(D_W, dtype="float")
    ep = 10**-8
    pr = 1/(1+np.exp(-real_data@D_W))
    pf = 1/(1+np.exp(-fake_data@D_W))
    pr = np.clip(pr, ep, 1-ep)
    pf = np.clip(pf, ep, 1-ep)
    d_loss = -np.mean(np.log(pr) + np.log(1-pf))
    g_loss = -np.mean(np.log(pf))
    return {"d_loss":d_loss, "g_loss":g_loss}