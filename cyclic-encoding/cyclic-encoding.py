from collections import defaultdict
import numpy as np 
def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    rec = defaultdict(int) ; res =[]
    #rec[0] = 0 ; rec[6] = np.pi /2 ; rec[12] = np.pi ; rec[18] = np.pi *3/4
    for v in values:
        each = 2* np.pi *v/period 
        this = [np.sin(each).item(), np.cos(each).item()]
        res.append(this)
    return res 