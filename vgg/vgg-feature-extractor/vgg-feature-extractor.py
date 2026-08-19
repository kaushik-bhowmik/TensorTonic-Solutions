import numpy as np

def maxpool_2x2(x):
    B, H, W, C = x.shape
    return x.reshape(B, H//2, 2, W//2, 2, C).max(axis=(2, 4))

def vgg_features(x: np.ndarray, config: list, conv_weights: list, conv_biases: list) -> np.ndarray:
    """
    Returns: np.ndarray feature tensor after applying conv layers and max pooling
    """
    # Your implementation here
    index=0
    for i, each in enumerate(config):
        if config[i]!="M":
            out = np.maximum(0,x@conv_weights[index] + conv_biases[index])
            index+=1
        else:
            out = maxpool_2x2(x)
        x = out 
    return x 