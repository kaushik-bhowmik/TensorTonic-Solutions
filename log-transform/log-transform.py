import numpy as np
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    lv = np.log(1+ np.array(values))
    return lv 
    