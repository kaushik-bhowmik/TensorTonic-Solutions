import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    """
    Perform one Nesterov Momentum update step.
    """
    # Write code here
    w = np.array(w, dtype=float)
    v = np.array(v, dtype=float)
    grad = np.array(grad, dtype=float)
    #print(type(w), type(v), type(grad))
    wlook = w- momentum *v 
    #v = momentum * v  + lr* grad * wlook
    v = momentum * v + lr * grad
    w = w- v
    return (w,v) 