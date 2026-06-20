import numpy as np
def relu(z):
    return np.maximum(0, z)

def bottleneck_block(x, W1, W2, W3, Ws):
    x = np.array(x, dtype=np.float64)
    W1 = np.array(W1, dtype=np.float64)
    W2 = np.array(W2, dtype=np.float64)
    W3 = np.array(W3, dtype=np.float64)
    shortcut = x if Ws is None else x @ np.asarray(Ws, dtype=np.float64)
    h1 = relu(x @ W1)
    h2 = relu(h1 @ W2)
    h3 = h2 @ W3            # no ReLU here
    return relu(h3 + shortcut)   # ReLU on the full sum