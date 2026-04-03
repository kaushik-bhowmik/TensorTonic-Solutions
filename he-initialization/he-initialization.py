def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    L = np.sqrt(6/fan_in)
    W = np.array(W)
    W = W*2*L
    W = W - L
    return W