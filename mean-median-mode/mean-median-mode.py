from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """Return the mean, median, and smallest mode."""
    # Write code here
    x.sort()
    mean = sum(x)/len(x)
    if len(x)%2==0:
        median = (x[len(x)//2] + x[-1+ len(x)//2])/2
    else:
        median = float(x[len(x)//2])
    rec = Counter(x)
    maxi = max(rec.values())
    mode = float("inf")
    for each in rec:
        if rec[each]==maxi:
            mode = float(min(mode,each))
    return {"mean":mean,"mode":mode,"median":median}
    