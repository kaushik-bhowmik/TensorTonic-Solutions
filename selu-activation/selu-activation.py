import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    pass
    x = np.array(x)
    x = np.where(x > 0, lam*x, lam*alpha*(-1+np.exp(x)))
    return x 
