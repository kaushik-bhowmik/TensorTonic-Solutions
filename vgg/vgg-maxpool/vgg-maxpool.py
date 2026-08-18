import numpy as np

def vgg_maxpool(x: np.ndarray) -> np.ndarray:
    """
    Implement VGG-style max pooling (2x2, stride 2).
    """
    # Your implementation here
    B= x.shape[0] ; H = x.shape[1] ; W = x.shape[2] ; C= x.shape[3]
    x = x.reshape(B, H//2, 2, W//2,2,C).max(axis=(2,4))
    #x = x.reshape(B,H//2,W//2,C)
    return x 