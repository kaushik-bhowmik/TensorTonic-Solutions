import numpy as np

def detect_mode_collapse(generated_samples, threshold=0.1):
    """
    Returns: dict with "diversity_score" (float) and "is_collapsed" (bool)
    """
    # Your implementation here
    std = np.std(generated_samples,axis=0)
    ds = np.mean(std)
    collapse = ds <threshold  
    return {"diversity_score":ds, "is_collapsed":collapse}