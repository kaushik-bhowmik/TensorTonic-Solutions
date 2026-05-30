import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    y_true = np.array(y_true,dtype=float) ; y_pred = np.array(y_pred, dtype=float)
    ph = np.clip(y_pred, eps, 1-eps)
    L = -1*(y_true*np.log(ph)+(1-y_true)*np.log(1-ph))
    #print(L)
    return L.tolist() 