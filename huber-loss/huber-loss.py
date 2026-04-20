import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    error = np.abs(y_true - y_pred) 
    ans = np.where(error<=delta, 0.5*error*error, delta *(np.abs(error)-0.5*delta))
    return ans.mean()
    