import numpy as np
##Implement Nadam (Nesterov + Adam)
def nadam_step(w, m, v, grad, lr=0.002, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Perform one Nadam update step.
    """
    # Write code here
    w = np.array(w,dtype=float); m= np.array(m,dtype=float)
    v= np.array(v,dtype=float) ; grad= np.array(grad,dtype=float)
    mt = beta1* m +(1-beta1)*grad 
    vt = beta2* v + (1-beta2) * grad**2
    wt = w -lr*(beta1*mt+(1-beta1)*grad)/(np.sqrt(vt)+eps)
    return (wt,mt,vt)