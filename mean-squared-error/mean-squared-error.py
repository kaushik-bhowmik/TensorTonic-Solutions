import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    samples = y_pred.shape[0]
    this = y_pred - y_true
    MSE = (this*this)/samples 
    #print(MSE)
    return MSE.sum()
