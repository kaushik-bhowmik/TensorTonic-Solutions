import numpy as np
import math
from scipy.special import erf

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    #pass
    x = np.array(x)
    #g = 0.5 * x*(1+np.tanh(np.sqrt(2/np.pi)* (x+0.044715*x**3)))
    return 0.5 * x * (1 + erf(x / np.sqrt(2))) 
