import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    #pass
    #print(type(x))
    arr =np.array(x)
    return np.where(arr>0, x, 0)
    