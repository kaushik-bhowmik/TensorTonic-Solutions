import numpy as np

def gradient_descent_step(values, gradients, learning_rate):
    """
    Returns: updated values and the predicted first-order objective change
    """
    nval = []
    for i in range(len(values)):
        nval.append(values[i]-learning_rate*gradients[i])
    Lpred = 0 
    for i in range(len(values)):
        Lpred+=gradients[i]* (nval[i]-values[i])
    return (nval,Lpred)