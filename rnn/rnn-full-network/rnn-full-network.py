import numpy as np

def vanilla_rnn(X: np.ndarray, h_0: np.ndarray, W_xh: np.ndarray,
                W_hh: np.ndarray, W_hy: np.ndarray, b_h: np.ndarray,
                b_y: np.ndarray) -> dict:
    """
    Returns outputs and final_hidden_state as float64 arrays.
    """
    rec={}
    def rnn(W_xh, W_hh,ht_1, b_h,W_hy,b_y,h_0):
        ht = np.tanh(X[:, i, :] @ W_xh.T + ht_1 @ W_hh.T + b_h)
        #ht = np.tanh(W_xh @ X[:, i] + W_hh @ ht_1 + b_h)
        #yt = W_hy @ht + b_y
        yt = ht @ W_hy.T + b_y
        return ht,yt 
    T = X.shape[1] ; outputs = [] ; fhs =[] ;  ht_1 = h_0
    for i in range(T):
        ht, yt = rnn(
            W_xh, W_hh, ht_1,
            b_h, W_hy, b_y,
            X[:, i, :]   
        )
        outputs.append(yt)
        ht_1 = ht
        #fhs.append(ht)
        fhs = ht 
    outputs = np.stack(outputs, axis=1)
    #fhs = np.stack(fhs,axis=1)
    rec["outputs"] = outputs
    rec["final_hidden_state"] = fhs
    return rec