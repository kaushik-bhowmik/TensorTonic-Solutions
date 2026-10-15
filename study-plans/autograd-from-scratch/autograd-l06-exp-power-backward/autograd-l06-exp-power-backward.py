import numpy as np

def exp_power_backward(x: float, exponent: float, upstream_gradient: float) -> tuple:
    """
    Returns a tuple of exp output, exp gradient, power output, and power gradient.
    """
    if exponent == 0:
        po = np.float64(1.0)
        pg = np.float64(0.0)
    else:
        po = np.float64(x**exponent)
        pg = np.float64(upstream_gradient* exponent* x**(exponent-1))
    eo = np.exp(x)
    eg = np.float64(upstream_gradient*np.exp(x))
    return (eo,eg,po,pg)
