import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    # Write code here
    C = np.asarray(C, dtype=float)
    E = np.zeros_like(C, dtype=float) #np.zeros_like(C) 
    rt = np.sum(C,axis=1)
    ct = np.sum(C,axis=0)
    gt = np.sum(C)
    for row in range(len(rt)):
        for col in range(len(ct)):
            E[row][col] = rt[row] * ct[col]/gt 
    chi = float(np.sum((C - E)**2 / E))
    #chi = np.sum((C-E)**2 /E)
    return {"chi2":chi, "expected":E}
    