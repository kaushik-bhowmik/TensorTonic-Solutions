import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    n = len(x)
    x= np.asarray(x)
    mean = np.mean(x)
    this = x-mean
    this = this * this 
    s = np.sqrt(np.sum(this)/(n-1))
    t= (mean -mu0)/(s/np.sqrt(n))
    if s==0:
        if mean==mu0:
            return 0.0
        else:
            return float("inf")
    return float(t)  