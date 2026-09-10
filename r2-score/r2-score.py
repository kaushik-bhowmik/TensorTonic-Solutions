import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    # Write code here
    num = den=0
    mean = sum(y_true)/len(y_true)
    flag=False 
    #if len(set(y_true))==1:
    #    return 1.0
    for i in range(len(y_true)):
        num+=(y_true[i]-y_pred[i])**2
        den+=(y_true[i]-mean)**2
    if y_true == y_pred:
        return 1.0
    if den==0:
        return 0.0 
    r2 = 1- (num/den) 
    return r2 
        