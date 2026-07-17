import numpy as np
from collections import Counter 
def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    rec = Counter(y)
    entropy=0.0 ; classes = len(rec)
    for each in rec:
        if rec[each]!=0:
            p = rec[each]/len(y)
            entropy+= (-1*p * np.log2(p))
    return entropy 