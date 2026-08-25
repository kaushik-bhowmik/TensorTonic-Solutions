import numpy as np

def finite_difference_derivative(coefficients, x, h):
    """
    Returns: the polynomial value at x, the value at x plus h, and the forward-difference slope
    """
    f=fh=0
    for i in range(len(coefficients)):
        f+=coefficients[i]*x**i
        fh+=coefficients[i]*(x+h)**i
    slope = (fh-f)/h
    return (f,fh, slope)