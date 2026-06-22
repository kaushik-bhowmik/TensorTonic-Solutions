import numpy as np

def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """
    AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation).
    """
    # YOUR CODE HERE
    ans = (image.shape[0],55,55,96)
    #print(ans)
    arr = np.zeros(ans)
    return arr 
    #pass