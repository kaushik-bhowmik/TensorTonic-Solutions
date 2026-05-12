import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X= np.array(X) ; y = np.array(y)
    f = np.linalg.inv(X.T@X)
    s = X.T@y 
    w = f@s
    return w 
    