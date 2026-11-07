import numpy as np

def linear_beta_schedule(num_steps: int, beta_start: float, beta_end: float) -> dict:
    """
    Returns a dict with float64 arrays "betas", "alphas" and "alpha_bars", each of shape (num_steps,).
    """
    if num_steps==1:
        return {
            "betas": np.array([beta_start], dtype=np.float64),
            "alphas": np.array([1 - beta_start], dtype=np.float64),
            "alpha_bars": np.array([1 - beta_start], dtype=np.float64)
            }
    else:
        size = (beta_end-beta_start)/(num_steps-1)
    betas =[beta_start]
    for i in range(1,num_steps):
        betas.append(beta_start + i* size)
    betas = np.asarray(betas)
    alpha = 1-betas 
    alpha_bars =[alpha[0]]
    for i in range(1,len(betas)):
        alpha_bars.append(alpha[i]*alpha_bars[-1])
    alpha_bars = np.asarray(alpha_bars)
    return {"betas": betas, "alphas": alpha, "alpha_bars":alpha_bars}
