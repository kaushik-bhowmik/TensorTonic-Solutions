import numpy as np
def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    rc = np.array(reference_counts,dtype=float)
    pc = np.array(production_counts,dtype=float)
    src = np.sum(rc)
    spc = np.sum(pc)
    rc = rc /src 
    pc = pc / spc 
    temp = np.sum(np.abs(pc-rc))
    tvd = 0.5*temp
    flag=False 
    if tvd> threshold:
        flag=True 
    else:
        flag = False 
    return {"score": tvd, "drift_detected": flag}