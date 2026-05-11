import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    tpr = np.array(tpr,dtype=float) ; fpr = np.array(fpr,dtype=float)
    tpr2 = tpr[:len(tpr)-1] + tpr[1:]
    fpr2 = fpr[1:] - fpr[:len(fpr)-1] 
    auc = np.sum(tpr2*fpr2)*0.5
    return auc 