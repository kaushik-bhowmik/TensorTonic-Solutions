import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    size = len(y_true)
    y_true = np.array(y_true) ; y_score =np.array(y_score); 
    ltemp = margin - y_true * y_score
    res =np.where(ltemp > 0, ltemp, 0)
    res = res.sum()
    if reduction=="mean":
        res = res/size 
    return res 