import numpy as np
### Implement AdaDelta Update Step
def adadelta_step(w, grad, E_grad_sq, E_update_sq, rho=0.9, eps=1e-6):
    """
    Perform one AdaDelta update step.
    """
    # Write code here
    w = np.array(w,dtype=float) ; grad = np.array(grad,dtype=float)
    E_grad_sq = np.array(E_grad_sq,dtype=float) 
    E_update_sq = np.array(E_update_sq,dtype=float)
    egt = rho * E_grad_sq +(1-rho)*grad**2 
    num = np.sqrt(E_update_sq + eps)
    den = np.sqrt(egt +eps)
    d_w = grad *num/den 
    edw = rho * E_update_sq +(1-rho)* (d_w)**2
    wnew = w - d_w 
    return (wnew , egt, edw)