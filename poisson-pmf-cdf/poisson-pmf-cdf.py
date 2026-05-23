import numpy as np
import math 
def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    #pass
    ki = np.arange(k+1)
    pmf = (((np.e)**-lam) *lam**k )/math.factorial(k)
    num = (np.e**-lam)*lam**ki
    den = np.array([math.factorial(x) for x in range(k+1)])
    return (pmf, np.sum(num/den))
    