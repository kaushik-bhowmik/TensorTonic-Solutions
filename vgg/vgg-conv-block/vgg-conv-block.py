import numpy as np

def vgg_conv_block(x: np.ndarray, weights: list, biases: list) -> np.ndarray:
    """
    Returns: np.ndarray of shape (B, H, W, C_out) after sequential linear transforms with ReLU
    """
    # Your implementation here
    layer = len(biases)
    #weights = np.asarray(weights,dtype=float)
    biases = np.array(biases,dtype=float)
    for i in range(layer):
        out = np.maximum(0,x@np.asarray(weights[i],dtype=float) +np.asarray(biases[i],dtype=float))
        x= out 
    return out 