import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:
    """
    Forward pass through entire sequence.
    """
    # YOUR CODE HERE
    T = X.shape[1]
    ht =[]
    for t in range(0,T):
        this = np.tanh(X[:, t, :]@W_xh.T + h_0@W_hh.T + b_h)
        ht.append(this)
        h_0 = this 
    hidden_states = np.stack(ht, axis=1)
    h_final = hidden_states[:, -1, :]
    return (hidden_states, h_final)