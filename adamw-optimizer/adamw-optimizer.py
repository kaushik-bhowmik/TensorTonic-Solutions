import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    """
    Perform one AdamW update step.
    """
    # Write code here
    #pass
    mt_1 = np.array(m,dtype=float)
    vt_1 = np.array(v, dtype=float)
    wt_1 = np.array(w, dtype=float)
    grad = np.array(grad, dtype=float)
    mt  = beta1 *mt_1 + (1-beta1)*grad
    vt = beta2 * vt_1 + (1-beta2)*grad*grad
    wt = wt_1 - lr*(weight_decay*wt_1) - lr* (mt/(np.sqrt(vt)+eps))
    return (wt, mt, vt)