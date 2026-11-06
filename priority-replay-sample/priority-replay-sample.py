import numpy as np  
def priority_replay_sample(priorities: list, alpha: float, beta: float) -> list:
    """
    Returns sampling probabilities and normalized importance weights.
    """
    # Write code here
    N = len(priorities)
    priorities = np.asarray(priorities)
    p_alpha = priorities** alpha
    pi = p_alpha / sum(p_alpha)
    wi = (N*pi)**(-beta)
    wnorm = wi / max(wi)
    return [pi.tolist(), wnorm.tolist()]
    